from __future__ import annotations

import streamlit as st


def primary_button(label: str, *, key: str | None = None) -> bool:
    """統一したプライマリボタンを描画し、そのクリック状態を返す。"""

    return st.button(label, type="primary", key=key)
