# Data Learning Hub

A static, bilingual, tutorial-first platform for learning Data Analytics through complete tutorials, exercises, examples, references, browser practice, datasets, and projects.

## Current release

### v2.5.0 — Complete Python for Data Analytics Tutorial

This release adds a complete 94-chapter Python course covering the analyst workflow from Python and notebooks through NumPy, pandas, cleaning, exploratory analysis, statistics, Matplotlib, time series, reproducibility, delivery, and a portfolio project.

Python examples can run inside the browser through the pinned Pyodide runtime. The site remains static: no backend, account, API, or hosted execution service is required.

## Published tutorials

| Tutorial | Chapters | Exercises |
|---|---:|---:|
| Data Foundations | 21 | 63 |
| Excel for Data Analytics | 56 | 168 |
| SQL for Data Analytics | 66 | 198 |
| Power BI for Data Analytics | 77 | 231 |
| Python for Data Analytics | 94 | 282 |
| **Total** | **314** | **942** |

The platform also retains 108 comprehensive statistics lessons and 20 interactive statistical labs.

## Python course modules

1. Python and Notebook Workflow
2. Python Language Foundations
3. NumPy for Numerical Analysis
4. pandas DataFrame Foundations
5. Data Cleaning and Transformation
6. Exploratory Analysis and Statistics
7. Visualization with Matplotlib
8. Time Series, Reproducibility, and Delivery
9. Python Analytics Portfolio Project

## Python practice assets

- `assets/downloads/python-retail-analytics-practice-package.zip`
- `assets/downloads/python-retail-analytics-starter.ipynb`
- `assets/downloads/python-retail-analytics-completed.ipynb`
- `assets/downloads/python-analytics-practice-scripts.py`
- `assets/downloads/python-analytics-requirements.txt`
- `assets/datasets/python_retail_sales.csv` — 720 rows
- `assets/datasets/python_customers.csv` — 120 rows
- `assets/datasets/python_messy_orders.csv` — deliberately messy practice data
- `assets/datasets/python_retail_data_dictionary.csv`

All course data is synthetic.

## Technology

- HTML5
- Modern CSS
- Vanilla JavaScript
- Python static-page generator
- Pyodide 314.0.2 for browser-side Python
- Chart.js for retained statistical visualizations
- sql.js for browser-side SQL practice
- Browser `localStorage` for optional progress, bookmarks, theme, and language
- No backend, API, account, or database service

## Run locally

```powershell
python -m http.server 8080
```

Open `http://localhost:8080`.

Browser Python requires internet access on the first run to download the pinned Pyodide runtime and requested packages from jsDelivr.

## Generate and test

```powershell
npm run generate
npm test
npm run test:browser
```

The test suite validates:

- Statistical core
- 108 retained lessons
- 314 tutorial chapters
- 942 chapter exercises
- Curriculum relationships and publication status
- SQL database and all 66 starter queries
- Power BI star-schema practice data and downloads
- Python course structure, notebooks, datasets, package ZIP, and all 94 starter snippets
- Local links and assets
- JavaScript syntax
- Sticky header, bilingual UI, exercises, quizzes, course navigation, and mobile drawers

## Main routes

```text
/tutorials/
/tutorials/data-foundations/
/tutorials/excel-data-analytics/
/tutorials/sql-data-analytics/
/tutorials/power-bi-data-analytics/
/tutorials/python-data-analytics/
/playground/sql/
/playground/python/
/exercises/
/examples/
/quiz/
/references/
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

The project remains conceptually inspired by the public `tafshir027/stats` repository, with original architecture, interface, course structure, code, and educational writing. Attribution remains available in About/Credits materials rather than the footer-bottom links.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Testing](docs/TESTING.md)
- [Roadmap](docs/ROADMAP.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.5.0 release report](docs/RELEASE-REPORT-v2.5.0.md)
