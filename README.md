# Data Learning Hub

**A tutorial-first, English-first bilingual platform for learning Data Analytics.**

Data Learning Hub is a completely static learning website built with HTML, CSS, Vanilla JavaScript, and a Python page generator used only during development. The deployed site requires no backend, API, database, account, or Netlify build process.

## Current release

### v2.3.0 — Complete SQL for Data Analytics Tutorial

Published tutorial content now includes:

- Complete **Data Foundations Tutorial** — 21 chapters
- Complete **Excel for Data Analytics Tutorial** — 56 chapters across 8 modules
- Complete **SQL for Data Analytics Tutorial** — 66 chapters across 9 modules
- 143 sequential tutorial chapters in total
- 429 chapter exercises
- Interactive activity in every chapter
- Randomized 30-question final quiz for each tutorial
- Dedicated exercise, example, quiz, and reference libraries
- Downloadable Excel practice workbook, SQL database scripts, query collection, data dictionaries, and synthetic datasets
- Browser-side SQL playground powered by SQLite-compatible sql.js; no backend or server-executed query
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

## SQL tutorial modules

1. SQL and Relational Foundations
2. Select, Filter, and Sort
3. Expressions and Functions
4. Aggregation and Metrics
5. Joins and Set Operations
6. Subqueries and Common Table Expressions
7. Window Functions and Analytical Patterns
8. Modeling, Quality, and Performance
9. Portfolio Analytics Projects

The tutorial uses PostgreSQL as the primary explanatory dialect while browser practice runs SQLite-compatible queries locally through sql.js. Every chapter identifies dialect-sensitive behavior where relevant.

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
- `/tutorials/sql-data-analytics/` — 66-chapter SQL course
- `/playground/sql/` — standalone browser SQL playground
- `/exercises/` — tutorial exercise libraries
- `/quiz/` — tutorial assessments
- `/examples/` — worked-example libraries
- `/references/` — official references, glossary, and downloads
- `/projects/` — datasets and applied projects
- `/practice/` — retained statistics laboratories
- `/learn/` — retained comprehensive lesson library
- `/my-learning/` — optional browser-local dashboard

## Practice files

- `assets/downloads/excel-analytics-practice-workbook.xlsx`
- `assets/datasets/retail_sales.csv`
- `assets/datasets/retail_sales_dictionary.csv`

The workbook contains Raw Sales, Formula Practice, Lookup Tables, Cleaning Practice, Pivot Practice, Dashboard Brief, and Answer Guide sheets. SQL practice assets include a deterministic six-table retail database, 66 starter queries, and a CSV data dictionary.

- `assets/downloads/sql-analytics-practice-database.sql`
- `assets/downloads/sql-analytics-practice-queries.sql`
- `assets/datasets/sql_practice_data_dictionary.csv`

## Source architecture

```text
content/
├── tutorials/
│   ├── data_foundations.json
│   ├── excel_data_analytics.json
│   ├── sql_data_analytics.json
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
├── audit_sql.py
├── build_sql_course.py
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

Expected v2.3.0 validation includes:

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 3 published tutorials with 143 complete chapters.
Executed 66/66 SQL chapter starter queries successfully.
Checked 12,664 local HTML and asset references across 307 HTML files.
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
- [v2.3.0 release report](docs/RELEASE-REPORT-v2.3.0.md)
- [v1-to-v2 migration](docs/MIGRATION-v1-to-v2.md)
