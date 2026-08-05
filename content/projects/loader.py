from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_projects() -> list[dict]:
    return json.loads((ROOT / 'portfolio_projects.json').read_text(encoding='utf-8'))
