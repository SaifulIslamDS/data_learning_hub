# Testing — v2.6.0

## Commands

```powershell
npm run build:workflows
npm run generate
npm test
npm run test:browser
```

## Automated coverage

`npm test` validates:

- statistical calculations
- 108 comprehensive bilingual lessons
- six published tutorials and 363 chapters
- 1,089 chapter exercises
- curriculum relationships and publication states
- SQL database and all starter queries
- Power BI star-schema assets and calculations
- Python datasets, notebooks, packages, and all starter snippets
- six portfolio projects, 48 workflow phases, datasets, dictionaries, ZIP packages, templates, deliverables, and quality gates
- every local HTML and asset reference
- JavaScript syntax

## Browser coverage

The Playwright smoke test verifies:

- sticky header
- six-course tutorial library
- Analytics Workflows course and chapter navigation
- bilingual switching
- tutorial completion
- workflow exercises and 30-question quiz
- six-card Project Center
- project phase progress and persistence
- downloadable project package links
- retained Data Foundations, Excel, SQL, Power BI, Python, and statistics routes
- exact footer behavior
- mobile chapter drawer

## Current validated output

```text
Tutorials:          6
Tutorial chapters:  363
Exercises:          1,089
Portfolio projects: 6
Project phases:     48
HTML pages:         549
Local references:   35,107
Broken references:  0
```
