#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TCM-FT enriched：改写 question + 从原 answer 提炼 points。
每次运行覆盖写入 3.TCM_FT_enriched.jsonl。

--provider deepseek    OpenAI SDK → DeepSeek（默认）
--provider openrouter  requests → OpenRouter（Key 见下方 OPENROUTER_*）
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests
from openai import OpenAI
from tqdm import tqdm

from mtcmb_datasets import CANONICAL_DATA_ROOT, Purpose, Shot, load_records

from tcm_ft_llm_utils import (
    PromptConfig,
    assert_safe_output,
    chat_completion,
    load_jsonl,
    load_prompts,
    merge_row,
    normalize_record,
    parse_combined_output,
    write_jsonl,
)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from mtcmb_env import load_dotenv

load_dotenv()

DEFAULT_ORIGINAL = CANONICAL_DATA_ROOT / "3.TCM_FT.jsonl"
DEFAULT_OUTPUT = CANONICAL_DATA_ROOT / "3.TCM_FT_enriched.jsonl"
PROMPT_YAML = SCRIPT_DIR / "prompts" / "tcm_qa_points_output.yaml"

# ---------- DeepSeek（OpenAI SDK）----------
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip()
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").strip()
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-reasoner").strip()

# ---------- OpenRouter（requests.post，仅本脚本）----------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o").strip()
OPENROUTER_HTTP_REFERER = os.getenv("OPENROUTER_HTTP_REFERER", "https://github.com/MTCMB").strip()
OPENROUTER_SITE_TITLE = os.getenv("OPENROUTER_SITE_TITLE", "MTCMB").strip()

MAX_RETRIES = 3
RETRY_DELAY = 2.0
REQUEST_SLEEP = 0.5
TEMPERATURE = 0.3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def chat_completion_openrouter(
    prompts: PromptConfig,
    variables: dict[str, str],
    *,
    model: str,
    temperature: float = TEMPERATURE,
) -> str:
    """OpenRouter：requests.post + json.dumps（与官方示例一致）。"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_HTTP_REFERER,
        "X-OpenRouter-Title": OPENROUTER_SITE_TITLE,
    }
    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompts.system_prompt},
            {"role": "user", "content": prompts.user_template.format(**variables)},
        ],
    }
    if "reasoner" not in model.lower():
        payload["temperature"] = temperature

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        data=json.dumps(payload),
        timeout=180,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        raise RuntimeError(f"OpenRouter HTTP {response.status_code}: {response.text[:500]}") from e

    data = response.json()
    if data.get("error"):
        raise RuntimeError(f"OpenRouter 错误: {data['error']}")
    content = data["choices"][0]["message"]["content"]
    if not content:
        raise ValueError("OpenRouter 返回 content 为空")
    return str(content)


def call_api(
    provider: str,
    client: OpenAI | None,
    prompts: PromptConfig,
    question: str,
    answer: str,
    model: str,
) -> tuple[str, str]:
    variables = {"question": question, "answer": answer}
    if provider == "openrouter":
        raw = chat_completion_openrouter(prompts, variables, model=model)
    else:
        assert client is not None
        raw = chat_completion(
            client, prompts, variables, model=model, temperature=TEMPERATURE,
        )
    return parse_combined_output(raw)


def process_one(
    provider: str,
    client: OpenAI | None,
    prompts: PromptConfig,
    original: dict[str, Any],
    model: str,
) -> dict[str, Any]:
    norm = normalize_record(original)
    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            q_rw, pts = call_api(
                provider, client, prompts, norm["question"], norm["answer"], model,
            )
            return merge_row(norm, q_rw, pts)
        except Exception as e:
            last_err = e
            logger.warning("id=%s 第 %s/%s 次失败: %s", norm["id"], attempt, MAX_RETRIES, e)
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)
    assert last_err is not None
    raise last_err


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="改写问句 + 提炼要点，每次覆盖生成 enriched JSONL")
    p.add_argument("--original", type=Path, default=DEFAULT_ORIGINAL)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    p.add_argument("--limit", type=int, default=None)
    p.add_argument(
        "--provider",
        choices=("deepseek", "openrouter"),
        default="deepseek",
        help="deepseek=OpenAI SDK；openrouter=requests",
    )
    p.add_argument("--model", type=str, default=None)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    provider = args.provider
    model = (args.model or "").strip() or (
        OPENROUTER_MODEL if provider == "openrouter" else DEEPSEEK_MODEL
    )

    orig_path = args.original.resolve()
    out_path = args.output.resolve()
    assert_safe_output(out_path)

    if not orig_path.exists():
        logger.error("原数据集不存在: %s", orig_path)
        sys.exit(1)

    if provider == "openrouter":
        if not OPENROUTER_API_KEY:
            logger.error("请填写 OPENROUTER_API_KEY")
            sys.exit(1)
        client = None
    else:
        if not DEEPSEEK_API_KEY:
            logger.error("请填写 DEEPSEEK_API_KEY")
            sys.exit(1)
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)

    if orig_path.resolve().parent == CANONICAL_DATA_ROOT.resolve():
        originals = load_records(
            orig_path.name, purpose=Purpose.STANDARD, shot=Shot.ZERO,
        )
    else:
        originals = load_jsonl(orig_path)
    pending = originals[: args.limit] if args.limit else originals
    logger.info("provider=%s | 模型=%s | %s 条 | %s", provider, model, len(pending), out_path)

    prompts = load_prompts(PROMPT_YAML)
    rows: list[dict[str, Any]] = []
    failed: list[int] = []

    for rec in tqdm(pending, desc="enriched"):
        rid = int(rec["id"])
        try:
            rows.append(process_one(provider, client, prompts, rec, model))
        except Exception as e:
            logger.error("id=%s 失败: %s", rid, e)
            failed.append(rid)
        if REQUEST_SLEEP > 0:
            time.sleep(REQUEST_SLEEP)

    if failed:
        logger.error("失败 id: %s，未写入", failed)
        sys.exit(1)

    write_jsonl(out_path, rows)
    logger.info("已覆盖写入 %s 条 -> %s", len(rows), out_path)


if __name__ == "__main__":
    main()
