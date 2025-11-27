from __future__ import annotations

import streamlit as st

from components.controls import primary_button
from utils.config_loader import load_yaml_config
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "settings.yaml"


@st.cache_data
def load_settings() -> dict:
    return load_yaml_config(CONFIG_PATH)


def main() -> None:
    settings = load_settings()
    st.header(settings.get("welcome_message", "Hello Streamlit"))

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("This home page lives inside the `pages/` directory.")
        st.write(
            "Organize related content into additional pages to keep the entry point clean."
        )
    with col2:
        if primary_button(settings.get("button_label", "Click me"), key="home_button"):
            st.toast("Home button clicked")


if __name__ == "__main__":
    main()
