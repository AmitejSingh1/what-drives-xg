"""
src/config.py
Utility to load config.yaml and expose it as a simple namespace.
"""

from __future__ import annotations

import yaml
from pathlib import Path


def load_config(path: str | Path = "config.yaml") -> dict:
    """Load and return the project config as a dict."""
    with open(path, "r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    return cfg
