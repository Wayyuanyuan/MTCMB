# -*- coding: utf-8 -*-
"""build_tcm_ft_enriched_deepseek.py 共用：JSONL、提示词、API、解析与校验。"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from openai import OpenAI

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROTECTED = {
    (PROJECT_ROOT / "data" / "3.TCM_FT.jsonl").resolve(),
}


@dataclass(frozen=True)
class PromptConfig:
    system_prompt: str
    user_template: str


def load_prompts(yaml_path: Path) -> PromptConfig:
    if yaml is None:
        raise RuntimeError("未安装 PyYAML: pip install pyyaml")
    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    system = data.get("system_prompt")
    user_tpl = data.get("user_template")
    if not system or not user_tpl:
        raise ValueError(f"{yaml_path} 须含 system_prompt 与 user_template")
    return PromptConfig(
        system_prompt=str(system).strip(),
        user_template=str(user_tpl).strip(),
    )


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    q = str(record.get("question", ""))
    a = str(record.get("answer", ""))
    rid = record.get("id")
    if rid == 93 and "是什么?" in q and "肾气不固，多因" in q:
        parts = q.split("是什么?", 1)
        if len(parts) == 2 and parts[1].strip():
            q = parts[0].strip() + "是什么?"
            a = parts[1].strip() + a
    return {"id": int(rid), "question": q.strip(), "answer": a.strip()}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{line_no} JSON 失败: {e}") from e
    return records


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def assert_safe_output(path: Path) -> None:
    if path.resolve() in PROTECTED:
        raise ValueError(f"拒绝覆盖原数据集: {path}")


def normalize_points_text(text: str) -> str:
    bullets: list[str] = []
    for raw in text.strip().splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("- "):
            bullets.append(line)
        elif line.startswith("-"):
            bullets.append("- " + line[1:].strip())
        elif re.match(r"^\d+[\.\)、]\s*", line):
            bullets.append("- " + re.sub(r"^\d+[\.\)、]\s*", "", line).strip())
        else:
            bullets.append("- " + line)
    if not bullets:
        raise ValueError("points 为空")
    return "\n".join(bullets)


def extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    if not text:
        raise ValueError("模型返回为空")
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
    if fence:
        text = fence.group(1).strip()
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        raise ValueError(f"未找到 JSON: {text[:200]}...")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError(f"JSON 未闭合: {text[:200]}...")


def parse_combined_output(text: str) -> tuple[str, str]:
    obj = extract_json_object(text)
    q_rw = str(obj.get("question_rewritten", "")).strip()
    pts_raw = obj.get("points", "")
    if isinstance(pts_raw, list):
        pts_raw = "\n".join(
            f"- {str(p).lstrip('- ').strip()}" for p in pts_raw if str(p).strip()
        )
    pts = normalize_points_text(str(pts_raw))
    if not q_rw:
        raise ValueError("question_rewritten 为空")
    return q_rw, pts


def validate_row(original: dict[str, Any], row: dict[str, Any]) -> None:
    norm = normalize_record(original)
    oid = int(norm["id"])
    if int(row["id"]) != oid:
        raise ValueError(f"id 不一致: {oid} vs {row['id']}")
    if row["question"] != norm["question"]:
        raise ValueError(f"id={oid} question 被改动")
    if row["answer"] != norm["answer"]:
        raise ValueError(f"id={oid} answer 被改动")
    q_rw = str(row["question_rewritten"]).strip()
    if not q_rw or q_rw == norm["question"]:
        raise ValueError(f"id={oid} question_rewritten 无效")
    normalize_points_text(str(row["points"]))


def merge_row(
    original: dict[str, Any],
    question_rewritten: str,
    points: str,
) -> dict[str, Any]:
    norm = normalize_record(original)
    row = {
        "id": norm["id"],
        "question": norm["question"],
        "answer": norm["answer"],
        "question_rewritten": question_rewritten.strip(),
        "points": normalize_points_text(points),
    }
    validate_row(norm, row)
    return row


def chat_completion(
    client: OpenAI,
    prompts: PromptConfig,
    variables: dict[str, str],
    *,
    model: str,
    temperature: float,
) -> str:
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompts.system_prompt},
            {"role": "user", "content": prompts.user_template.format(**variables)},
        ],
    }
    if "reasoner" not in model.lower():
        kwargs["temperature"] = temperature
    response = client.chat.completions.create(**kwargs)
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("API 返回 content 为空")
    return content
