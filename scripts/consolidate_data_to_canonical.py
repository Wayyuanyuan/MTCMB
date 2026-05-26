#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查权威 data/ 是否就绪（历史合并脚本；重复目录已删除）。"""

from __future__ import annotations

from pathlib import Path

from mtcmb_datasets import CANONICAL_DATA_ROOT, list_dataset_files

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    files = list_dataset_files()
    if not files:
        print(f"错误：{CANONICAL_DATA_ROOT} 下无 JSONL")
        raise SystemExit(1)
    print(f"权威目录 {CANONICAL_DATA_ROOT} 共 {len(files)} 个数据集文件")
    for p in files:
        print(f"  - {p.name}")


if __name__ == "__main__":
    main()
