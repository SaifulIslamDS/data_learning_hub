from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TUTORIAL_FILES = [
    'data_foundations.json',
    'excel_data_analytics.json',
]

def load_tutorials() -> list[dict]:
    tutorials = []
    for name in TUTORIAL_FILES:
        tutorials.append(json.loads((ROOT / name).read_text(encoding='utf-8')))
    return tutorials
