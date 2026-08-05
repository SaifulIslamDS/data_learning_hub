from __future__ import annotations

import contextlib
import csv
import io
import json
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_PATH = ROOT / "content" / "tutorials" / "python_data_analytics.json"
DATASET_DIR = ROOT / "assets" / "datasets"
DOWNLOAD_DIR = ROOT / "assets" / "downloads"
EXPECTED_PACKAGES = {"numpy", "pandas", "matplotlib", "scipy"}
EXPECTED_DOWNLOADS = {
    "python-retail-analytics-practice-package.zip",
    "python-retail-analytics-starter.ipynb",
    "python-retail-analytics-completed.ipynb",
    "python-analytics-practice-scripts.py",
    "python-analytics-requirements.txt",
}
EXPECTED_DATASETS = {
    "python_retail_sales.csv",
    "python_customers.csv",
    "python_messy_orders.csv",
    "python_retail_data_dictionary.csv",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_course() -> tuple[dict, list[dict]]:
    data = json.loads(COURSE_PATH.read_text(encoding="utf-8"))
    chapters = data.get("chapters", [])
    modules = data.get("modules", [])
    assert data.get("id") == "python-data-analytics"
    assert data.get("status") == "published"
    assert data.get("version") == "2.5.0"
    assert len(modules) == 9, len(modules)
    assert len(chapters) == 94, len(chapters)
    ids = [chapter.get("id") for chapter in chapters]
    assert len(ids) == len(set(ids)), "Duplicate Python chapter IDs"
    module_ids = {module["id"] for module in modules}
    assert all(chapter.get("module") in module_ids for chapter in chapters)

    for index, chapter in enumerate(chapters, 1):
        prefix = f"Chapter {index} ({chapter.get('id')})"
        for key in ("title_en", "title_bn", "summary_en", "summary_bn"):
            assert str(chapter.get(key, "")).strip(), f"{prefix}: missing {key}"
        assert len(chapter.get("objectives", [])) == 4, f"{prefix}: objectives"
        assert len(chapter.get("sections", [])) >= 3, f"{prefix}: sections"
        assert len(chapter.get("terms", [])) == 4, f"{prefix}: terms"
        assert len(chapter.get("exercises", [])) == 3, f"{prefix}: exercises"
        assert len(chapter.get("recap", [])) >= 4, f"{prefix}: recap"
        assert chapter.get("references"), f"{prefix}: references"
        activity = chapter.get("activity", {})
        assert activity.get("type") == "python-playground", f"{prefix}: activity type"
        assert str(activity.get("code", "")).strip(), f"{prefix}: missing starter code"
        packages = set(activity.get("packages", []))
        assert packages <= EXPECTED_PACKAGES, f"{prefix}: unsupported packages {packages - EXPECTED_PACKAGES}"
        for ex in chapter["exercises"]:
            assert ex.get("type") in {"mcq", "fill", "short"}, f"{prefix}: exercise type"
            assert ex.get("prompt_en") and ex.get("prompt_bn"), f"{prefix}: exercise prompt"

    urls = {item["url"].lstrip("/") for item in data.get("downloads", [])}
    for relative in urls:
        assert (ROOT / relative).is_file(), f"Missing declared download: {relative}"
    return data, chapters


def csv_row_count(path: Path) -> int:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def validate_assets() -> None:
    for name in EXPECTED_DOWNLOADS:
        assert (DOWNLOAD_DIR / name).is_file(), f"Missing download: {name}"
    for name in EXPECTED_DATASETS:
        assert (DATASET_DIR / name).is_file(), f"Missing dataset: {name}"
    assert csv_row_count(DATASET_DIR / "python_retail_sales.csv") == 720
    assert csv_row_count(DATASET_DIR / "python_customers.csv") == 120
    assert csv_row_count(DATASET_DIR / "python_messy_orders.csv") == 4
    dictionary_rows = list(csv.DictReader((DATASET_DIR / "python_retail_data_dictionary.csv").open(encoding="utf-8-sig")))
    assert dictionary_rows and {"file", "field", "type", "description"} <= set(dictionary_rows[0])

    import nbformat

    for notebook_name in ("python-retail-analytics-starter.ipynb", "python-retail-analytics-completed.ipynb"):
        notebook = nbformat.read(DOWNLOAD_DIR / notebook_name, as_version=4)
        assert notebook.cells, f"Notebook contains no cells: {notebook_name}"
        assert any(cell.cell_type == "code" for cell in notebook.cells)

    package_path = DOWNLOAD_DIR / "python-retail-analytics-practice-package.zip"
    with zipfile.ZipFile(package_path) as archive:
        names = set(archive.namelist())
        required = {
            "python_retail_sales.csv",
            "python_customers.csv",
            "python_messy_orders.csv",
            "python_retail_data_dictionary.csv",
            "python-retail-analytics-starter.ipynb",
            "python-retail-analytics-completed.ipynb",
            "python-analytics-practice-scripts.py",
            "python-analytics-requirements.txt",
        }
        assert required <= names, f"Practice ZIP missing: {sorted(required - names)}"


def execute_starter_queries(chapters: list[dict]) -> list[str]:
    os.environ.setdefault("MPLBACKEND", "Agg")
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from IPython.display import display

    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="dlh-python-audit-") as temp:
        temp_path = Path(temp)
        for name in EXPECTED_DATASETS:
            shutil.copy2(DATASET_DIR / name, temp_path / name)
        previous = Path.cwd()
        os.chdir(temp_path)
        try:
            for chapter in chapters:
                code = chapter["activity"]["code"]
                namespace = {
                    "__name__": "__main__",
                    "display": display,
                }
                stdout, stderr = io.StringIO(), io.StringIO()
                try:
                    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                        exec(compile(code, f"<{chapter['id']}>", "exec"), namespace, namespace)
                except Exception as exc:  # noqa: BLE001 - report exact chapter failure
                    failures.append(f"{chapter['id']}: {type(exc).__name__}: {exc}")
                finally:
                    plt.close("all")
        finally:
            os.chdir(previous)
    return failures


def main() -> None:
    data, chapters = validate_course()
    validate_assets()
    failures = execute_starter_queries(chapters)
    if failures:
        print("Python starter-code failures:")
        for failure in failures:
            print(f"- {failure}")
        fail(f"{len(failures)} Python chapter starter snippets failed")
    print(
        "Validated Python for Data Analytics tutorial:\n"
        f"- {len(data['modules'])} modules\n"
        f"- {len(chapters)} chapters\n"
        f"- {sum(len(chapter['exercises']) for chapter in chapters)} exercises\n"
        f"- {len(chapters)}/{len(chapters)} starter snippets executed successfully\n"
        "- practice datasets, notebooks, scripts, requirements, and ZIP package verified"
    )


if __name__ == "__main__":
    main()
