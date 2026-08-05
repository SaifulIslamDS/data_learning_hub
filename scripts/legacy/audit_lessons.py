from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "assets" / "js" / "content.js"

raw = CONTENT.read_text(encoding="utf-8")
prefix = "window.DLH_CONTENT = "
if not raw.startswith(prefix):
    raise SystemExit("content.js does not contain the expected generated payload")
data = json.loads(raw[len(prefix):].rstrip().rstrip(";"))

topics = data.get("topics", [])
errors: list[str] = []
required = {
    "lesson_type", "plain_en", "plain_bn", "why_en", "why_bn", "concepts",
    "scenario", "workflow", "implementations", "interpretation", "practice_en",
    "practice_bn", "quiz", "recap", "references",
}

if len(topics) != 108:
    errors.append(f"Expected 108 lessons, found {len(topics)}")

scenario_titles: set[str] = set()
for topic in topics:
    lesson = topic.get("lesson") or {}
    missing = required - set(lesson)
    if missing:
        errors.append(f"{topic.get('id')}: missing {sorted(missing)}")
        continue
    if len(lesson["concepts"]) < 3:
        errors.append(f"{topic['id']}: fewer than three concept cards")
    if len(lesson["workflow"]) < 5:
        errors.append(f"{topic['id']}: workflow is too short")
    if len(lesson["implementations"]) < 2:
        errors.append(f"{topic['id']}: fewer than two implementation guides")
    if len(lesson["quiz"].get("options", [])) < 3:
        errors.append(f"{topic['id']}: quiz has fewer than three options")
    if len(lesson["recap"]) < 4:
        errors.append(f"{topic['id']}: recap is too short")
    if not lesson["references"]:
        errors.append(f"{topic['id']}: no references")
    scenario_title = lesson["scenario"].get("title_en", "")
    if scenario_title in scenario_titles:
        errors.append(f"{topic['id']}: duplicate scenario title {scenario_title!r}")
    scenario_titles.add(scenario_title)
    for field in ("plain_en", "plain_bn", "why_en", "why_bn", "practice_en", "practice_bn"):
        if len(str(lesson.get(field, "")).strip()) < 40:
            errors.append(f"{topic['id']}: {field} is unexpectedly short")
    if re.search(r"A practitioner uses .* to examine a small", lesson["scenario"].get("context_en", "")):
        errors.append(f"{topic['id']}: legacy generic scenario remains")

if errors:
    print("Comprehensive lesson audit failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"Validated {len(topics)} comprehensive bilingual lessons.")
print("Each lesson has concepts, a unique scenario, workflow, implementation guides, interpretation, practice, quiz, recap and references.")
