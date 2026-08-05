# Architecture — v2.6.0

## Product model

Data Learning Hub is a generated static site. Source content is stored as structured Python/JSON modules; `scripts/generate.py` publishes ordinary HTML, CSS, and Vanilla JavaScript pages.

The primary learner surfaces are:

- Tutorials
- Exercises
- Examples
- Quizzes
- References
- Browser SQL/Python playgrounds
- Portfolio Project Center
- Retained statistics lessons and labs

## Source domains

```text
content/
├── platform/       # identity, navigation, domains, storage
├── tutorials/      # six complete tutorial definitions
├── statistics/     # retained lessons and lab curriculum
├── tracks/         # career and tool curriculum metadata
├── datasets/       # legacy reusable datasets
└── projects/       # portfolio project definitions
```

## Workflow and project generation

`scripts/build_workflows_projects.py` produces:

- `content/tutorials/data_analytics_workflows.json`
- `content/projects/portfolio_projects.json`
- synthetic project CSV files and dictionaries
- starter SQL and Python files
- Excel and Power BI implementation guides
- project packages and portfolio templates

`scripts/generate.py` then publishes tutorial, project, sitemap, and content-payload routes.

## Client-side architecture

- `site.js` — shared sticky header, footer, language, theme, search, storage migration
- `tutorial-core.js` — tutorial progress and chapter navigation
- `tutorial.js` — chapter activities and completion
- `projects.js` — Project Center rendering
- `portfolio-project.js` — phase-level project progress
- `sql-practice.js` — browser SQL editor
- `python-practice.js` — browser Python editor

## Storage

No server-side storage is used. Optional browser-local state includes:

- language and theme
- lesson/tutorial completion
- bookmarks
- learner profile
- portfolio project phase completion

Project progress keys follow:

```text
dlh-project-<project-id>-tasks
```

## Static deployment

The repository can be served directly from its root. Netlify is the production target. There is no build command in production because generated pages are committed to the repository.
