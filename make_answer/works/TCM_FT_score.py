import json
import re
from functools import lru_cache
from pathlib import Path

from make_answer.chat.chat_invoker import ChatInvoker
from mtcmb_datasets import Purpose, load_records

PROMPT_YAML = (
    Path(__file__).resolve().parents[2] / "scripts" / "prompts" / "tcm_qa_points_output.yaml"
)
STANDARD_FT_FILE = "3.TCM_FT.jsonl"
FEW_SHOT_COUNT = 3


@lru_cache(maxsize=1)
def _load_prompt_config() -> dict:
    try:
        import yaml
    except ImportError as e:
        raise RuntimeError("需要 PyYAML: pip install pyyaml") from e
    with PROMPT_YAML.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@lru_cache(maxsize=1)
def _load_few_shot_standard_records() -> tuple[dict, ...]:
    """前 FEW_SHOT_COUNT 条标准答案（按 id 升序），来自 data/3.TCM_FT.jsonl。"""
    records = load_records(STANDARD_FT_FILE, purpose=Purpose.STANDARD)
    records.sort(key=lambda r: int(r["id"]))
    return tuple(records[:FEW_SHOT_COUNT])


def _build_few_shot_prefix(cfg: dict, *, current_id: int | None) -> str:
    intro = str(cfg.get("model_answer_few_shot_intro", "")).strip()
    example_tpl = str(cfg.get("model_answer_few_shot_example", "")).strip()
    tail = str(cfg.get("model_answer_few_shot_tail", "")).strip()

    blocks: list[str] = []
    if intro:
        blocks.append(intro)

    index = 0
    for rec in _load_few_shot_standard_records():
        rid = int(rec["id"])
        if current_id is not None and rid == current_id:
            continue
        index += 1
        blocks.append(
            example_tpl.format(
                index=index,
                question=str(rec.get("question", "")).strip(),
                answer=str(rec.get("answer", "")).strip(),
            )
        )

    if index == 0:
        raise ValueError("few-shot 示例为空，请检查标准答案文件与前 3 条 id")

    if tail:
        blocks.append(tail)
    return "\n\n".join(blocks)


_COT_POINTS_MARKERS = re.compile(
    r"(?:【\s*points\s*】|\[points\]|#+\s*points\s*|【\s*采分要点\s*】|【\s*要点\s*】)",
    re.IGNORECASE,
)
_COT_REASONING_MARKERS = re.compile(
    r"(?:【\s*推理\s*】|\[reasoning\]|#+\s*推理\s*|【\s*思考\s*】|##\s*Thinking)",
    re.IGNORECASE,
)


def _strip_json_and_fence(text: str | None) -> str:
    if text is None:
        return ""
    text = text.strip()
    if text.startswith("{"):
        try:
            obj = json.loads(text)
            if isinstance(obj, dict) and obj.get("points"):
                return str(obj["points"]).strip()
        except json.JSONDecodeError:
            pass
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
    if fence:
        return fence.group(1).strip()
    return text


def _extract_cot_points_body(text: str) -> str:
    """CoT：只保留【points】段，或【推理】后的空行之后、且含 - 列表的段落。"""
    text = _strip_json_and_fence(text)

    m_pts = _COT_POINTS_MARKERS.search(text)
    if m_pts:
        return text[m_pts.end() :].strip()

    m_re = _COT_REASONING_MARKERS.search(text)
    if m_re:
        tail = text[m_re.end() :].strip()
        m_pts2 = _COT_POINTS_MARKERS.search(tail)
        if m_pts2:
            return tail[m_pts2.end() :].strip()
        blocks = [b.strip() for b in re.split(r"\n\s*\n", tail) if b.strip()]
        for block in reversed(blocks):
            if re.search(r"^\s*-\s", block, re.MULTILINE):
                return block
        return tail

    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    if len(blocks) >= 2:
        for block in reversed(blocks):
            if re.search(r"^\s*-\s", block, re.MULTILINE):
                return block
        return blocks[-1]
    return text


def _lines_to_bullets(text: str, *, strict_bullets: bool) -> str:
    bullets: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or _COT_POINTS_MARKERS.match(line) or _COT_REASONING_MARKERS.match(line):
            continue
        if line.startswith("【") and line.endswith("】"):
            continue
        if line.startswith("- "):
            bullets.append(line)
        elif line.startswith("-") and not strict_bullets:
            bullets.append("- " + line[1:].strip())
        elif re.match(r"^\d+[\.\)、]\s*", line):
            bullets.append("- " + re.sub(r"^\d+[\.\)、]\s*", "", line).strip())
        elif not strict_bullets:
            bullets.append("- " + line)
    if bullets:
        return "\n".join(bullets)
    return text.strip()


def _normalize_points_text(text: str | None, *, cot: bool = False) -> str:
    if text is None or not str(text).strip():
        raise ValueError("模型返回为空，请检查额度、max_tokens 或换模型后重试")

    raw = str(text).strip()
    if cot:
        body = _extract_cot_points_body(raw)
        out = _lines_to_bullets(body, strict_bullets=True)
        if not out.strip():
            out = _lines_to_bullets(body, strict_bullets=False)
        if not out.strip():
            out = _lines_to_bullets(_strip_json_and_fence(raw), strict_bullets=False)
    else:
        out = _lines_to_bullets(_strip_json_and_fence(raw), strict_bullets=False)

    if not out.strip():
        raise ValueError(
            "解析后 points 为空（CoT 请确认输出含【points】段且每行以「- 」开头）"
            if cot
            else "解析后 points 为空"
        )
    return out


def _build_prompt(prompt_type: int, question: str, *, record_id: int | None = None) -> str:
    cfg = _load_prompt_config()
    system = str(cfg.get("model_answer_system_prompt", "")).strip()
    user_tpl = str(cfg.get("model_answer_user_template", "")).strip()
    user = user_tpl.format(question=question)

    parts: list[str] = []
    if system:
        parts.append(system)
    if prompt_type == 1:
        parts.append(_build_few_shot_prefix(cfg, current_id=record_id))
    parts.append(user)
    if prompt_type == 2:
        parts.append(str(cfg.get("model_answer_cot_suffix", "")).strip())
    return "\n\n".join(p for p in parts if p)


def tcm_ft(prompt_type: int, data: dict, llm: ChatInvoker) -> dict:
    question = str(data.get("question", "")).strip()
    record_id = int(data["id"]) if data.get("id") is not None else None
    prompt = _build_prompt(prompt_type, question, record_id=record_id)
    response = llm.chat(prompt)
    data["points"] = _normalize_points_text(response, cot=(prompt_type == 2))
    data.pop("model_points", None)
    data.pop("answer", None)

    return data
