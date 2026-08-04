from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load_tutorials() -> list[dict]:
    return [json.loads((ROOT / 'data_foundations.json').read_text(encoding='utf-8'))]
