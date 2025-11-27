from pathlib import Path

from utils.config_loader import load_yaml_config


def test_load_yaml_config_returns_dict(tmp_path: Path) -> None:
    yaml_file = tmp_path / "settings.yaml"
    yaml_file.write_text("app_title: Demo App", encoding="utf-8")

    config = load_yaml_config(yaml_file)

    assert config == {"app_title": "Demo App"}
