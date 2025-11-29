from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import yaml


def load_yaml_config(path: Path) -> Dict[str, Any]:
    """
    YAML 設定ファイルを読み込む。

    戻り値はプレーンな辞書で、Streamlit や他のモジュールからフレームワークに依存せず
    利用できるようにする。
    """

    data = path.read_text(encoding="utf-8") if path.exists() else "{}"
    return json.loads(json.dumps(yaml.safe_load(data) or {}))


def resolve_project_root() -> Path:
    """.git を含むディレクトリ、すなわちリポジトリのルートを返す。"""

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists():
            return parent
    return current.parent
