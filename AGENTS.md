# AGENTS.md

## Product

- Name: Data Learning Hub
- Current version: v2.4.0
- Deployment: static Netlify site from `main`
- Stack: HTML, CSS, Vanilla JavaScript, Python generator
- Languages: English-first with Bangla toggle

## Published tutorial baseline

- Data Foundations: 21 chapters
- Excel for Data Analytics: 56 chapters
- SQL for Data Analytics: 66 chapters
- Power BI for Data Analytics: 77 chapters
- Total: 220 chapters and 660 exercises

Retain 108 comprehensive statistics lessons and 20 statistical labs.

## Source of truth

- Tutorial content: `content/tutorials/*.json`
- Tutorial loading: `content/tutorials/loader.py`
- Platform metadata: `content/platform/`
- Career and tool curricula: `content/tracks/`
- Static generation: `scripts/generate.py` and `scripts/tutorial_generator.py`
- Power BI course builder: `scripts/build_power_bi_course.py`

Do not hand-edit generated tutorial HTML when the corresponding JSON or generator owns it.

## Required tests

```powershell
npm run generate
npm test
npm run test:browser
```

Do not publish when any link, tutorial, curriculum, SQL, Power BI data-model, syntax, or browser test fails.

## UI requirements

- Keep the shared header sticky on every route.
- Footer bottom links must contain only `<a href="/about/">About</a>`.
- Do not re-add the inspiration link to `.footer-bottom-links`.
- Keep English first, EN/BN toggle, and persistent light/dark theme.

## Publication honesty

Only complete courses may use `tutorial-published`. Planned tracks must not link to empty tutorial pages.

## Release roadmap

- v2.4.0: complete Power BI tutorial
- v2.5.0: complete Python for Data Analytics tutorial
- v2.6.0: cross-tool workflows and portfolio projects
- v3.0.0: Data Science tutorial path
- v4.0.0: Data Engineering tutorial path
