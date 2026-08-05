# AGENTS.md

## Product

Data Learning Hub is a static, tutorial-first bilingual Data Analytics learning platform.

## Current baseline

- Product version: v2.3.0
- Published tutorials: Data Foundations and Excel for Data Analytics
- 143 tutorial chapters and 429 chapter exercises
- 108 retained lessons and 20 retained statistical labs
- Static HTML/CSS/Vanilla JavaScript; Python is development-time generation only
- Netlify production branch: `main`

## Source of truth

Edit authored files under `content/`, shared assets under `assets/`, and generators/tests under `scripts/`. Do not hand-edit hundreds of generated HTML pages as the primary implementation method.

## Required validation

```powershell
npm run generate
npm test
npm run test:browser
```

A release must not be accepted with broken links, missing downloads, invalid curriculum relationships, JavaScript syntax errors, failed browser tests, or planned content labeled as published.

## Publication rules

- `tutorial-published`: complete course, chapters, exercises, quiz, examples, references, downloads, and QA exist
- `curriculum-ready`: reviewed future scope only
- Preserve existing route IDs and browser-local progress keys where possible
- English is default; Bangla explanations retain official technical names when needed for precision

## Roadmap

- v2.3.0: complete SQL tutorial
- v2.4.0: complete Power BI tutorial
- v2.5.0: complete Python tutorial
- v2.6.0: cross-tool analytics projects and portfolio
