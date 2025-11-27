from __future__ import annotations

import streamlit as st


def primary_button(label: str, *, key: str | None = None) -> bool:
    """Render a consistent primary button and return its click state."""

    return st.button(label, type="primary", key=key)
