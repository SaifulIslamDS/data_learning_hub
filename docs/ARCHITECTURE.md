# Architecture — v2.3.0

Data Learning Hub is generated during development and deployed as static HTML, CSS, JavaScript, datasets, and downloadable files.

## Published tutorial sources

```text
content/tutorials/
├── data_foundations.json        # 21 chapters
├── excel_data_analytics.json    # 56 chapters
├── sql_data_analytics.json      # 66 chapters
└── loader.py
```

`scripts/tutorial_generator.py` generates course pages, chapter pages, exercises, examples, quizzes, and reference libraries. `scripts/generate.py` produces the remaining platform pages, content bundle, sitemap, and metadata.

## SQL practice architecture

```text
Chapter JSON activity
→ assets/js/sql-practice.js
→ sql.js 1.14.1 loaded from jsDelivr
→ SQLite-compatible WASM database in browser memory
→ deterministic SQL seed file
→ result table rendered locally
```

No SQL query is sent to a backend. Refreshing or resetting recreates the in-memory database. PostgreSQL remains the primary teaching dialect; SQLite powers the browser laboratory.

## Validation layers

- `audit_tutorials.py` — tutorial structure and completeness
- `audit_sql.py` — seed integrity and execution of all 66 starter queries
- `audit_curriculum.py` — publication states and relationships
- `audit_links.py` — generated local links and downloads
- `browser_smoke.py` — shared UI, sticky header, courses, SQL editor UI, and mobile navigation
