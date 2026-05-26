# -*- coding: utf-8 -*-
"""从仓库根目录 .env 加载环境变量（不覆盖已存在的系统环境变量）。"""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
ENV_FILE = PROJECT_ROOT / ".env"


def load_dotenv(path: Path | None = None, *, override: bool = False) -> bool:
    env_path = path or ENV_FILE
    if not env_path.is_file():
        return False

    with env_path.open("r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].strip()
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if not key:
                continue
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            if not override and key in os.environ:
                continue
            os.environ[key] = value
    return True
