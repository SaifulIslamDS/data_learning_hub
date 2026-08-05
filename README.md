# Data Learning Hub

A static, bilingual, tutorial-first platform for learning Data Analytics through complete tutorials, browser practice, exercises, references, synthetic datasets, end-to-end workflows, and portfolio projects.

## Current release

### v2.6.0 — Data Analytics Workflows and Portfolio Projects

This release connects the previously separate subject tutorials into one repeatable analytical lifecycle:

```text
Business question
→ Data understanding
→ Data preparation
→ Analysis plan
→ Exploratory and statistical analysis
→ Cross-tool implementation
→ Validation
→ Communication
→ Portfolio delivery
```

It adds a complete 49-chapter Analytics Workflows tutorial and six downloadable cross-tool portfolio projects.

## Published tutorials

| Tutorial | Chapters | Exercises |
|---|---:|---:|
| Data Foundations | 21 | 63 |
| Excel for Data Analytics | 56 | 168 |
| SQL for Data Analytics | 66 | 198 |
| Power BI for Data Analytics | 77 | 231 |
| Python for Data Analytics | 94 | 282 |
| Data Analytics Workflows | 49 | 147 |
| **Total** | **363** | **1,089** |

The platform also retains 108 comprehensive statistics lessons and 20 interactive statistical labs.

## Portfolio Project Center

Six complete synthetic cases are published:

1. Retail Sales 360° Performance Analysis
2. Customer Retention and Cohort Analysis
3. Marketing A/B Test and Campaign Evaluation
4. HR Workforce and Attrition Analytics
5. Financial Budget and Actual Control
6. NGO Program Monitoring and Impact Analysis

Each project includes:

- Business brief and analytical questions
- Documented synthetic datasets and dictionaries
- Eight-phase implementation workflow
- Excel build guide
- SQL starter script
- Power BI build guide
- Python starter script
- Required deliverables and quality gates
- README, presentation, metric, QA, and insight-log templates
- Downloadable complete project package
- Browser-local phase progress

## Technology

- HTML5
- Modern CSS
- Vanilla JavaScript
- Python static-page generator
- Pyodide for browser-side Python
- sql.js for browser-side SQL
- Chart.js for statistical visualizations
- Browser `localStorage` for optional progress, bookmarks, theme, language, and project phases
- No backend, account, API, or hosted database

## Generate and test

```powershell
npm run build:workflows
npm run generate
npm test
npm run test:browser
```

The quality suite validates:

- Statistical core
- 108 retained lessons
- 363 tutorial chapters and 1,089 exercises
- All SQL, Power BI, and Python practice assets
- Six project definitions, datasets, packages, deliverables, and quality gates
- Curriculum and publication relationships
- Local links and assets
- JavaScript syntax
- Sticky header, bilingual UI, workflow course, project progress, quizzes, retained courses, and mobile navigation

## Main routes

```text
/tutorials/
/tutorials/data-analytics-workflows/
/projects/
/projects/retail-sales-360/
/exercises/
/examples/
/quiz/
/references/
/playground/sql/
/playground/python/
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

The project remains conceptually inspired by the public `tafshir027/stats` repository, with original architecture, interface, curriculum, code, and educational writing. Attribution remains in About/Credits materials rather than the footer-bottom links.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Testing](docs/TESTING.md)
- [Roadmap](docs/ROADMAP.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.6.0 release report](docs/RELEASE-REPORT-v2.6.0.md)
