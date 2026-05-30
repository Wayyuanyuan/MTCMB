# -*- coding: utf-8 -*-
"""数据集展示名、数据文件名与提交/输出目录名的对应关系。"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
CANONICAL_DATA_ROOT = PROJECT_ROOT / "data"

# 提交目录名 -> data/*.jsonl 的文件名主干（不含 .jsonl）
FOLDER_TO_DATA_STEM: dict[str, str] = {
    "TCM-SE-A": "11.TCM_SE_A",
    "TCM-SE-B": "12.TCM_SE_B",
}


def resolve_data_stem(folder_or_stem: str) -> str:
    """将提交目录名（如 TCM-SE-A）解析为数据文件主干（如 11.TCM_SE_A）。"""
    key = folder_or_stem.strip()
    if key.endswith(".jsonl"):
        key = key[: -len(".jsonl")]
    return FOLDER_TO_DATA_STEM.get(key, key)


def resolve_dataset_jsonl(folder_or_stem: str) -> str:
    stem = resolve_data_stem(folder_or_stem)
    return stem if stem.endswith(".jsonl") else f"{stem}.jsonl"
