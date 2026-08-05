# Data Learning Hub

A static, bilingual, tutorial-first platform for learning Data Analytics through complete tutorials, exercises, examples, references, browser practice, datasets, and projects.

## Current release

### v2.4.0 — Complete Power BI for Data Analytics Tutorial

This release adds a complete 77-chapter Power BI course across Power BI Desktop and Service, Power Query, semantic modeling, DAX, visual analytics, publishing, security, governance, performance, accessibility, QA, and a portfolio project.

The shared sticky header remains active on every route. The footer now contains one bottom link—`About`—and no longer displays the original inspiration link.

## Published tutorials

| Tutorial | Chapters | Exercises |
|---|---:|---:|
| Data Foundations | 21 | 63 |
| Excel for Data Analytics | 56 | 168 |
| SQL for Data Analytics | 66 | 198 |
| Power BI for Data Analytics | 77 | 231 |
| **Total** | **220** | **660** |

The platform also retains 108 comprehensive statistics lessons and 20 interactive statistical labs.

## Power BI course modules

1. Power BI Foundations and Workflow
2. Connect and Transform with Power Query
3. Design the Semantic Model
4. DAX Foundations
5. Analytical DAX and Time Intelligence
6. Visual Analytics and Report Experience
7. Publish, Secure, Refresh, and Govern
8. Performance, Accessibility, and Quality Assurance
9. Portfolio Project

## Power BI practice assets

- `assets/downloads/power-bi-retail-practice-data.zip`
- `assets/downloads/power-bi-dax-measures.txt`
- `assets/downloads/power-bi-power-query-m-examples.txt`
- `assets/downloads/power-bi-project-qa-checklist.csv`
- `assets/datasets/power_bi_data_dictionary.csv`

The practice ZIP contains a connected retail star-schema dataset:

- `DimDate.csv` — 730 rows
- `DimProduct.csv` — 12 rows
- `DimCustomer.csv` — 60 rows
- `DimRegion.csv` — 4 rows
- `FactSales.csv` — 360 rows
- `FactTargets.csv` — 96 rows

All data is synthetic.

## Technology

- HTML5
- Modern CSS
- Vanilla JavaScript
- Python static-page generator
- Chart.js for retained statistical visualizations
- sql.js for browser-side SQL practice
- Browser `localStorage` for optional progress, bookmarks, theme, and language
- No backend, API, account, or database service

## Run locally

```powershell
python -m http.server 8080
```

Open `http://localhost:8080`.

## Generate and test

```powershell
npm run generate
npm test
npm run test:browser
```

The main test suite validates:

- Statistical core
- 108 retained lessons
- 220 tutorial chapters
- 660 chapter exercises
- Curriculum relationships
- SQL database and 66 starter queries
- Power BI star-schema practice data and downloads
- Local links and assets
- JavaScript syntax

## Main routes

```text
/tutorials/
/tutorials/data-foundations/
/tutorials/excel-data-analytics/
/tutorials/sql-data-analytics/
/tutorials/power-bi-data-analytics/
/exercises/
/examples/
/quiz/
/references/
/playground/sql/
/projects/
```

## Deployment

The site is configured for Netlify with no build command:

```text
Production branch: main
Base directory:    empty
Build command:     empty
Publish directory: .
```

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md).

## Credits

Idea and developed by **Saiful Islam**.

- Website: https://saifulshuvo.com
- GitHub: https://github.com/SaifulIslamDS/
- LinkedIn: https://www.linkedin.com/in/saifulislampro/

The project remains conceptually inspired by the public `tafshir027/stats` repository, with original architecture, interface, course structure, code, and educational writing. Attribution remains available on the About/Credits materials rather than the footer-bottom links.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Testing](docs/TESTING.md)
- [Roadmap](docs/ROADMAP.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.4.0 release report](docs/RELEASE-REPORT-v2.4.0.md)
