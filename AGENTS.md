# AGENTS.md

## Product

- Name: Data Learning Hub
- Current version: v2.6.0
- Deployment: static Netlify site from `main`
- Stack: HTML, CSS, Vanilla JavaScript, Python generator
- Languages: English-first with Bangla toggle

## Published baseline

- Data Foundations: 21 chapters
- Excel: 56 chapters
- SQL: 66 chapters
- Power BI: 77 chapters
- Python: 94 chapters
- Analytics Workflows: 49 chapters
- Total: 363 chapters and 1,089 exercises
- Portfolio projects: 6 complete cross-tool cases
- Retained statistics: 108 lessons and 20 labs

## Source of truth

- Tutorial content: `content/tutorials/*.json`
- Portfolio definitions: `content/projects/portfolio_projects.json`
- Workflow/project builder: `scripts/build_workflows_projects.py`
- Static generation: `scripts/generate.py` and `scripts/tutorial_generator.py`
- Project UI: `assets/js/projects.js` and `assets/js/portfolio-project.js`

Do not hand-edit generated tutorial or project HTML when structured content or a generator owns it.

## Required tests

```powershell
npm run build:workflows
npm run generate
npm test
npm run test:browser
```

Do not publish when any statistical, tutorial, curriculum, SQL, Power BI, Python, project, link, syntax, or browser test fails.

## UI requirements

- Keep the shared header sticky on every route.
- Footer bottom links must contain only `<a href="/about/">About</a>`.
- Keep English first, EN/BN toggle, and persistent light/dark theme.

## Project publication rules

A project may be marked available only when its page, synthetic data, dictionary, complete package, workflow phases, deliverables, quality gates, and portfolio guidance are present.

## Roadmap

- v2.6.0: complete analytics workflows and portfolio projects
- v2.7.0: assessments, revision, and interview preparation
- v3.0.0: Data Science tutorial path
- v4.0.0: Data Engineering tutorial path
