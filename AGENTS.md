# AGENTS.md

## Product

- Name: Data Learning Hub
- Current version: v2.5.0
- Deployment: static Netlify site from `main`
- Stack: HTML, CSS, Vanilla JavaScript, Python generator
- Languages: English-first with Bangla toggle

## Published tutorial baseline

- Data Foundations: 21 chapters
- Excel for Data Analytics: 56 chapters
- SQL for Data Analytics: 66 chapters
- Power BI for Data Analytics: 77 chapters
- Python for Data Analytics: 94 chapters
- Total: 314 chapters and 942 exercises

Retain 108 comprehensive statistics lessons and 20 statistical labs.

## Source of truth

- Tutorial content: `content/tutorials/*.json`
- Tutorial loading: `content/tutorials/loader.py`
- Platform metadata: `content/platform/`
- Career and tool curricula: `content/tracks/`
- Static generation: `scripts/generate.py` and `scripts/tutorial_generator.py`
- Python course builder: `scripts/build_python_course.py`
- Browser Python runtime: `assets/js/python-practice.js`

Do not hand-edit generated tutorial HTML when JSON or a generator owns it.

## Required tests

```powershell
npm run generate
npm test
npm run test:browser
```

Do not publish when any link, tutorial, curriculum, SQL, Power BI, Python, syntax, or browser test fails.

## UI requirements

- Keep the shared header sticky on every route.
- Footer bottom links must contain only `<a href="/about/">About</a>`.
- Do not re-add the inspiration link to `.footer-bottom-links`.
- Keep English first, EN/BN toggle, and persistent light/dark theme.

## Browser Python rules

- Pin Pyodide to an explicit stable version.
- Do not use an unversioned or development CDN path.
- Keep learner code and datasets in browser memory.
- Explain that the first run downloads the runtime and requested packages.
- Distinguish browser execution from a local Jupyter or production Python environment.

## Publication honesty

Only complete courses may use `tutorial-published`. Planned tracks must not link to empty tutorial pages.

## Release roadmap

- v2.5.0: complete Python for Data Analytics tutorial
- v2.6.0: cross-tool workflows and portfolio projects
- v3.0.0: Data Science tutorial path
- v4.0.0: Data Engineering tutorial path
