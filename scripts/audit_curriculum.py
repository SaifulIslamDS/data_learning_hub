from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "assets" / "js" / "content.js"
PREFIX = "window.DLH_CONTENT = "
raw = CONTENT.read_text(encoding="utf-8")
if not raw.startswith(PREFIX):
    raise SystemExit("content.js does not contain the expected Data Learning Hub payload")
data = json.loads(raw[len(PREFIX):].rstrip().rstrip(";"))
errors: list[str] = []


def unique(items, key, label):
    seen = set()
    for item in items:
        value = item.get(key)
        if not value:
            errors.append(f"{label}: missing {key}")
        elif value in seen:
            errors.append(f"{label}: duplicate {key} {value!r}")
        seen.add(value)
    return seen

domain_ids = unique(data.get("domains", []), "id", "domain")
module_ids = unique(data.get("modules", []), "id", "module")
topic_ids = unique(data.get("topics", []), "id", "topic")
tool_ids = unique(data.get("tools", []), "id", "tool")
path_ids = unique(data.get("paths", []), "id", "path")
career_ids = unique(data.get("career_paths", []), "id", "career path")
curriculum_ids = unique(data.get("tool_curricula", []), "id", "tool curriculum")
dataset_ids = unique(data.get("datasets", []), "id", "dataset")
project_ids = unique(data.get("projects", []), "id", "project")

for module in data.get("modules", []):
    if module.get("domain") not in domain_ids:
        errors.append(f"module {module.get('id')}: unknown domain {module.get('domain')}")
    for topic_id in module.get("topics", []):
        if topic_id not in topic_ids:
            errors.append(f"module {module.get('id')}: unknown topic {topic_id}")

for topic in data.get("topics", []):
    if topic.get("module") not in module_ids:
        errors.append(f"topic {topic.get('id')}: unknown module {topic.get('module')}")
    if topic.get("domain") not in domain_ids:
        errors.append(f"topic {topic.get('id')}: unknown domain {topic.get('domain')}")
    lab = topic.get("lab")
    if lab and lab not in tool_ids:
        errors.append(f"topic {topic.get('id')}: unknown lab {lab}")

for path in data.get("paths", []):
    for topic_id in path.get("topics", []):
        if topic_id not in topic_ids:
            errors.append(f"path {path.get('id')}: unknown topic {topic_id}")

for career in data.get("career_paths", []):
    for topic_id in career.get("available_topics", []):
        if topic_id not in topic_ids:
            errors.append(f"career {career.get('id')}: unknown available topic {topic_id}")
    if career.get("status") in {"roadmap"} and career.get("available_topics"):
        errors.append(f"career {career.get('id')}: roadmap route must not publish available topics")

for domain in data.get("domains", []):
    status = domain.get("status")
    url = domain.get("url") or ""
    if status == "available" and not url.startswith("/learn/"):
        errors.append(f"domain {domain.get('id')}: available domain must point to /learn/")
    if status == "tutorial-published" and not url.startswith("/tutorials/"):
        errors.append(f"domain {domain.get('id')}: tutorial-published domain must point to /tutorials/")
    if status == "curriculum-ready" and not url.startswith("/curriculum/"):
        errors.append(f"domain {domain.get('id')}: curriculum-ready domain must point to curriculum")

for curriculum in data.get("tool_curricula", []):
    if curriculum.get("status") != "curriculum-ready":
        errors.append(f"curriculum {curriculum.get('id')}: expected curriculum-ready status")
    if not curriculum.get("reference_url"):
        errors.append(f"curriculum {curriculum.get('id')}: missing official reference")
    if len(curriculum.get("modules", [])) < 5:
        errors.append(f"curriculum {curriculum.get('id')}: fewer than five modules")
    for module in curriculum.get("modules", []):
        if len(module.get("lessons", [])) < 4:
            errors.append(f"curriculum {curriculum.get('id')} / {module.get('title_en')}: too few planned lessons")

for dataset in data.get("datasets", []):
    for field in ("file", "dictionary"):
        path = ROOT / str(dataset.get(field, "")).lstrip("/")
        if not path.exists():
            errors.append(f"dataset {dataset.get('id')}: missing {field} {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
    csv_path = ROOT / dataset.get("file", "").lstrip("/")
    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            rows = sum(1 for _ in csv.reader(handle)) - 1
        if rows != dataset.get("rows"):
            errors.append(f"dataset {dataset.get('id')}: metadata says {dataset.get('rows')} rows, found {rows}")

for project in data.get("projects", []):
    if project.get("dataset") not in dataset_ids:
        errors.append(f"project {project.get('id')}: unknown dataset {project.get('dataset')}")
    if project.get("status") == "available" and not project.get("url"):
        errors.append(f"project {project.get('id')}: available project has no URL")
    if project.get("status") == "roadmap" and project.get("url"):
        errors.append(f"project {project.get('id')}: roadmap project must not expose a URL")

site = data.get("site", {})
storage = data.get("storage", {})
if site.get("name") != "Data Learning Hub" or site.get("version") != "2.1.0":
    errors.append("site identity/version is not Data Learning Hub v2.1.0")
if storage.get("prefix") != "dlh-" or storage.get("legacy_prefix") != "slh-":
    errors.append("storage migration prefixes are not configured")
if not any(c.get("id") == "data-analyst" and c.get("status") == "active" for c in data.get("career_paths", [])):
    errors.append("Data Analyst is not the active career route")

if errors:
    print("Curriculum architecture audit failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"Validated {len(domain_ids)} domains, {len(module_ids)} retained modules, {len(topic_ids)} lessons and {len(tool_ids)} labs.")
print(f"Validated {len(curriculum_ids)} curriculum-ready tool tracks, {len(dataset_ids)} synthetic datasets and {len(project_ids)} project definitions.")
print("No orphaned curriculum relationships, false roadmap links or dataset row-count mismatches found.")
