from __future__ import annotations

from pathlib import Path

import streamlit as st

from components.controls import primary_button
from utils.config_loader import load_yaml_config

CONFIG_PATH = Path(__file__).parent / "configs" / "settings.yaml"


@st.cache_data
def load_settings() -> dict:
    """YAML ファイルからアプリ設定を読み込む。"""

    return load_yaml_config(CONFIG_PATH)


def main() -> None:
    settings = load_settings()
    title = settings.get("app_title", "Hello Streamlit")
    welcome_message = settings.get("welcome_message", title)
    button_label = settings.get("button_label", "Click me")

    st.set_page_config(page_title=title, page_icon="👋", layout="wide")

    st.title(welcome_message)
    if primary_button(button_label, key="welcome_button"):
        st.success("Button clicked! You can wire this up to your logic layer.")

    st.markdown(
        """
        This landing page demonstrates a minimal Streamlit entry point. Use the
        `pages/` directory to add more pages, and group reusable pieces under
        `components/`, `services/`, and `utils/`.
        """
    )

    with st.expander("Project layout", expanded=False):
        st.json(
            {
                "configs": "Configuration and constants (YAML, JSON, or Python)",
                "pages": "Multi-page scripts auto-discovered by Streamlit",
                "components": "Reusable UI helpers (buttons, cards, etc.)",
                "services": "Business logic and integrations (APIs, DB, files)",
                "domain": "Data models for type safety",
                "utils": "General utilities (caching helpers, formatting)",
                "assets": "Static assets such as images or CSS",
                "tests": "Unit tests for non-UI logic",
            }
        )


if __name__ == "__main__":
    main()
