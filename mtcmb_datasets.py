# -*- coding: utf-8 -*-
"""从权威 data/ 目录加载 JSONL，并按用途与 few-shot 策略派生视图。"""

from __future__ import annotations

import copy
import json
from enum import Enum
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
CANONICAL_DATA_ROOT = PROJECT_ROOT / "data"

# 权威 benchmark 子集（与 data/*.jsonl 文件名 stem 一致）
BENCHMARK_DATASET_STEMS = frozenset({
    "TCM-ED-A", "TCM-ED-B", "TCM-FT", "TCMeEE", "TCM-CHGD", "TCM-LitData",
    "TCM-MSDD", "TCM-Diagnosis", "TCM-PR", "TCM-FRD", "TCM-SE-A", "TCM-SE-B",
})

# 与提示词中硬编码示例对应的样本 id（few-shot 评测时排除）
FEW_SHOT_EXCLUDE_IDS: dict[str, frozenset[int]] = {
    "TCM-ED-A": frozenset({0, 1, 2}),
    "TCM-FT": frozenset({1, 2, 3}),
}


class Purpose(str, Enum):
    BENCHMARK = "benchmark"
    STANDARD = "standard"


class Shot(str, Enum):
    ZERO = "zero"
    FEW = "few"


def shot_from_prompt_type(prompt_type: int) -> Shot:
    return Shot.FEW if prompt_type == 1 else Shot.ZERO


def _dataset_stem(name: str) -> str:
    stem = name.strip()
    if stem.endswith(".jsonl"):
        stem = stem[:-len(".jsonl")]
    return stem


def _should_include(dataset_file: str, record_id: int, shot: Shot) -> bool:
    if shot != Shot.FEW:
        return True
    excluded = FEW_SHOT_EXCLUDE_IDS.get(_dataset_stem(dataset_file), frozenset())
    return record_id not in excluded


def list_dataset_files() -> list[Path]:
    return sorted(
        p for p in CANONICAL_DATA_ROOT.glob("*.jsonl")
        if p.stem in BENCHMARK_DATASET_STEMS
    )


def iter_benchmark_files():
    for path in list_dataset_files():
        yield path.name, str(path)


def load_records(
    dataset_name: str,
    purpose: Purpose = Purpose.STANDARD,
    shot: Shot = Shot.ZERO,
) -> list[dict]:
    stem = _dataset_stem(dataset_name)
    path = CANONICAL_DATA_ROOT / f"{stem}.jsonl"
    if not path.is_file():
        raise FileNotFoundError(path)

    records: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    if shot == Shot.FEW:
        excluded = FEW_SHOT_EXCLUDE_IDS.get(stem, frozenset())
        records = [r for r in records if int(r.get("id", -1)) not in excluded]

    if purpose == Purpose.BENCHMARK:
        benchmark: list[dict] = []
        for record in records:
            item = copy.deepcopy(record)
            item.pop("answer", None)
            item.pop("points", None)
            benchmark.append(item)
        return benchmark

    return records
