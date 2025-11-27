from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import yaml


def load_yaml_config(path: Path) -> Dict[str, Any]:
    """
    Load a YAML configuration file.

    The return value is a plain dictionary so it can easily be consumed by
    Streamlit or other modules without adding framework-specific coupling.
    """

    data = path.read_text(encoding="utf-8") if path.exists() else "{}"
    return json.loads(json.dumps(yaml.safe_load(data) or {}))


def resolve_project_root() -> Path:
    """Return the repository root (directory containing .git)."""

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists():
            return parent
    return current.parent
