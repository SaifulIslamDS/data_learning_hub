# Architecture — v2.4.0

## Runtime model

Data Learning Hub is a generated static website. Production uses HTML, CSS, and browser JavaScript only. No backend, API, account system, or hosted database is required.

## Authoring layers

```text
content/tutorials/
├── data_foundations.json
├── excel_data_analytics.json
├── sql_data_analytics.json
└── power_bi_data_analytics.json

content/platform/       product identity, domains, storage
content/tracks/         career paths and tool curriculum metadata
scripts/                generation and audits
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

## Power BI implementation

Power BI cannot be executed fully inside a static site. The course therefore combines:

- Complete text-based tutorials
- DAX and Power Query examples
- Browser-side decision simulations
- Browser-side measure calculations
- Downloadable star-schema CSV files
- Project and QA checklists
- Explicit instructions for implementation in Power BI Desktop and Service

The browser simulation never pretends to replace Power BI. It teaches reasoning about query, model, DAX, report, and service layers.

## Shared shell

`assets/js/site.js` renders the shared sticky header and footer on all generated routes. The footer-bottom links intentionally contain only the About link.

## Local learner state

Versioned `dlh-*` localStorage keys preserve optional language, theme, progress, bookmarks, and tutorial completion. No personal course data leaves the browser.

## Static generation

`scripts/generate.py` loads platform metadata and tutorial JSON, then delegates tutorial routes to `scripts/tutorial_generator.py`. Generated files are committed and deployed directly by Netlify.

## Quality architecture

- `audit_lessons.py`: retained statistics lessons
- `audit_tutorials.py`: course schemas and files
- `audit_curriculum.py`: relationships and publication state
- `audit_sql.py`: SQL database and starter queries
- `audit_power_bi.py`: Power BI course, star schema, reconciliation, downloads, and official references
- `audit_links.py`: local link and asset integrity
- `browser_smoke.py`: real Chromium interaction and responsive regression
