# Data Learning Hub

**A tutorial-first, English-first bilingual platform for learning Data Analytics.**

Data Learning Hub is a completely static learning website built with HTML, CSS, Vanilla JavaScript, and a Python page generator used only during development. The deployed site requires no backend, API, database, account, or Netlify build process.

## Current release

### v2.2.0 — Complete Excel for Data Analytics Tutorial

Published tutorial content now includes:

- Complete **Data Foundations Tutorial** — 21 chapters
- Complete **Excel for Data Analytics Tutorial** — 56 chapters across 8 modules
- 77 sequential tutorial chapters in total
- 231 chapter exercises
- Interactive activity in every chapter
- Randomized 30-question final quiz for each tutorial
- Dedicated exercise, example, quiz, and reference libraries
- Downloadable Excel practice workbook and synthetic datasets
- Persistent desktop chapter sidebar and mobile chapter drawer
- Browser-local chapter completion and quiz results
- English-first EN/BN content
- Print-friendly tutorial chapters
- Sticky shared header on every generated route

The previous platform resources remain available:

- 108 comprehensive statistics and analytics lessons
- 20 browser-based statistical laboratories
- Three documented synthetic datasets
- Projects, career paths, curriculum maps, bookmarks, and optional guided learning

## Excel tutorial modules

1. Excel Foundations
2. Organize and Control Data
3. Formula Foundations
4. Analytical Functions
5. Lookups and Dynamic Arrays
6. Analysis, PivotTables, and Visualization
7. Power Query, Data Model, and Advanced Analysis
8. Quality, Delivery, and Final Project

The course progresses from workbook and data-entry fundamentals through formulas, conditional aggregation, text/date functions, XLOOKUP, INDEX/MATCH, dynamic arrays, PivotTables, charts, Power Query, the Data Model, introductory Power Pivot/DAX, auditing, dashboard design, and a two-part retail-sales project.

## Primary learning experience

```text
Tutorials
→ Open a subject
→ Read the next chapter
→ Learn the concept
→ Study the worked example
→ Try the interactive activity
→ Complete exercises
→ Continue to the next chapter
→ Take the final quiz
→ Complete the project
```

No learning-plan setup is required before studying.

## Important routes

- `/tutorials/` — published tutorial library
- `/tutorials/data-foundations/` — 21-chapter foundations course
- `/tutorials/excel-data-analytics/` — 56-chapter Excel course
- `/exercises/` — tutorial exercise libraries
- `/quiz/` — tutorial assessments
- `/examples/` — worked-example libraries
- `/references/` — official references, glossary, and downloads
- `/projects/` — datasets and applied projects
- `/practice/` — retained statistics laboratories
- `/learn/` — retained comprehensive lesson library
- `/my-learning/` — optional browser-local dashboard

## Excel practice files

- `assets/downloads/excel-analytics-practice-workbook.xlsx`
- `assets/datasets/retail_sales.csv`
- `assets/datasets/retail_sales_dictionary.csv`

The workbook contains Raw Sales, Formula Practice, Lookup Tables, Cleaning Practice, Pivot Practice, Dashboard Brief, and Answer Guide sheets.

## Source architecture

```text
content/
├── tutorials/
│   ├── data_foundations.json
│   ├── excel_data_analytics.json
│   └── loader.py
├── platform/
├── statistics/
├── tracks/
└── datasets/

scripts/
├── generate.py
├── tutorial_generator.py
├── audit_tutorials.py
├── audit_curriculum.py
├── audit_lessons.py
├── audit_links.py
├── browser_smoke.py
└── test_stats.mjs
```

Authored tutorial content lives in `content/tutorials/`. Generated HTML and `assets/js/content.js` are derived outputs.

## Generate and validate

```powershell
npm run generate
npm test
npm run test:browser
```

Expected v2.2.0 validation includes:

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 2 published tutorials with 77 complete chapters.
Checked 6,704 local HTML and asset references across 235 HTML files.
0 broken local references found.
Browser smoke test passed.
```

## Netlify deployment

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

Generated files are committed to the repository, so Netlify serves them directly.

## Privacy

Progress, quiz results, language, theme, bookmarks, and optional learning preferences remain in the visitor’s browser through `localStorage`. Practice data are processed locally.

## Credits

Idea and developed by **Saiful Islam**.

- Website: https://saifulshuvo.com
- GitHub: https://github.com/SaifulIslamDS/
- LinkedIn: https://www.linkedin.com/in/saifulislampro/
- Inspired by: https://github.com/tafshir027/stats

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.2.0 release report](docs/RELEASE-REPORT-v2.2.0.md)
- [v1-to-v2 migration](docs/MIGRATION-v1-to-v2.md)
