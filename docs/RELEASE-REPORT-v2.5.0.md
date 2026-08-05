# Release Report — v2.5.0

## Release title

**Complete Python for Data Analytics Tutorial**

## Release date

2026-08-05

## Objective

Add a complete tutorial-first Python course that teaches a beginner through practical Data Analytics implementation while preserving the static, bilingual, no-account platform architecture.

## Delivered course

- 94 chapters
- 9 modules
- 282 chapter exercises
- 94 worked examples
- 94 editable browser activities
- Randomized 30-question final quiz
- Complete example and reference libraries
- English-first EN/BN content
- Browser-local progress and completion state

## Curriculum coverage

The release covers Python and Jupyter workflow, core language foundations, NumPy, pandas, cleaning and transformation, EDA and statistics, Matplotlib, time series, reproducibility, delivery, privacy, and a four-part portfolio project.

## Browser practice

The course and standalone playground use pinned Pyodide 314.0.2 to execute Python in browser memory. The integration captures stdout, exceptions, and Matplotlib images and can load NumPy, pandas, Matplotlib, and SciPy when required.

## Practice assets

- 720-row synthetic retail-sales dataset
- 120-row synthetic customer dataset
- Deliberately messy order dataset
- CSV data dictionary
- Starter Jupyter notebook
- Completed example notebook
- Practice script collection
- Requirements file
- Combined practice ZIP

## Platform totals

| Item | Total |
|---|---:|
| Published tutorials | 5 |
| Tutorial chapters | 314 |
| Chapter exercises | 942 |
| Retained statistics lessons | 108 |
| Statistical labs | 20 |
| Generated HTML pages | 489 |
| Checked local references | 31,454 |
| Broken local references | 0 |

## Validation

- Statistical-core tests passed.
- 108 retained comprehensive lessons passed.
- Five-course tutorial audit passed.
- Curriculum and publication-state audit passed.
- SQL and Power BI regression audits passed.
- Python course, datasets, notebooks, downloads, and ZIP audit passed.
- All 94 Python starter snippets executed successfully against the packaged data.
- Local link and JavaScript syntax checks passed.
- Chromium verified the Python course UI, editor, standalone playground UI, completion state, EN/BN switching, exercises, quiz, sticky header, and mobile drawer.
- Existing Data Foundations, Excel, SQL, Power BI, statistics, and footer behavior passed regression testing.

## Runtime verification boundary

The build environment blocks a full external CDN WebAssembly download in Chromium. Therefore the release does not claim an automated end-to-end Pyodide execution in this sandbox. Production tagging requires the simple Netlify runtime smoke test documented in `docs/DEPLOYMENT.md`.

## Next release

**v2.6.0 — Data Analytics Workflows and Portfolio Projects**
