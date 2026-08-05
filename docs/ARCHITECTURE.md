# Architecture — v2.5.0

## Runtime model

Data Learning Hub is a generated static website. Production uses HTML, CSS, browser JavaScript, and optional WebAssembly runtimes only. No backend, API, account system, or hosted database is required.

## Authoring layers

```text
content/tutorials/
├── data_foundations.json
├── excel_data_analytics.json
├── sql_data_analytics.json
├── power_bi_data_analytics.json
└── python_data_analytics.json

content/platform/       product identity, domains, storage
content/tracks/         career paths and tool curriculum metadata
scripts/                generation, course builders, and audits
assets/js/              shared UI and interactive tutorial behavior
assets/css/             shared responsive design system
```

## Generated tutorial routes

Every published course receives:

```text
/tutorials/<course>/
/tutorials/<course>/<chapter>/
/exercises/<course>/
/examples/<course>/
/quiz/<course>/
/references/<course>/
```

SQL and Python also receive standalone browser practice routes:

```text
/playground/sql/
/playground/python/
```

## Python implementation

`assets/js/python-practice.js` loads pinned Pyodide 314.0.2 from jsDelivr when a learner first runs code. It then:

1. Initializes CPython compiled to WebAssembly.
2. Copies the synthetic practice CSV files into the browser runtime filesystem.
3. Loads only the packages required by the chapter.
4. Executes edited learner code.
5. Captures stdout, exceptions, and Matplotlib figures.
6. Displays output and charts without sending code or course data to a backend.

The Netlify CSP includes `wasm-unsafe-eval` for WebAssembly compilation and permits the pinned jsDelivr runtime.

## Python authoring and validation

- `scripts/build_python_course.py` owns the Python tutorial JSON, datasets, notebooks, scripts, requirements, and practice ZIP.
- `scripts/audit_python.py` validates the 94 chapters, assets, notebooks, ZIP contents, dataset row counts, and executes every starter snippet in an isolated temporary directory.
- `scripts/browser_smoke.py` validates the browser editor interface, progress state, course navigation, exercises, quiz, sticky header, and mobile drawer.

## Shared shell

`assets/js/site.js` renders the shared sticky header and footer on all generated routes. The footer-bottom links intentionally contain only the About link.

## Local learner state

Versioned `dlh-*` localStorage keys preserve optional language, theme, progress, bookmarks, and tutorial completion. No personal course data leaves the browser.

## Static generation

`scripts/generate.py` loads platform metadata and tutorial JSON, then delegates tutorial routes to `scripts/tutorial_generator.py`. Generated files are committed and deployed directly by Netlify.

## Quality architecture

- `audit_lessons.py`: retained statistics lessons
- `audit_tutorials.py`: five-course schemas and generated files
- `audit_curriculum.py`: relationships and publication state
- `audit_sql.py`: SQL database and 66 starter queries
- `audit_power_bi.py`: Power BI course, star schema, reconciliation, downloads, and references
- `audit_python.py`: Python course, datasets, notebooks, downloads, and 94 starter snippets
- `audit_links.py`: local link and asset integrity
- `browser_smoke.py`: Chromium interaction and responsive regression
