# Changelog

## v2.6.0 — Data Analytics Workflows and Portfolio Projects

### Added

- 49 bilingual Analytics Workflows chapters across eight modules
- 147 workflow exercises and a randomized 30-question final quiz
- Six complete cross-tool portfolio projects
- Synthetic retail, retention, marketing, HR, finance, and NGO program datasets
- Eight-phase project workflow and browser-local progress tracking
- Complete downloadable project packages for Excel, SQL, Power BI, Python, and Statistics implementation
- Reusable project charter, analysis plan, metric dictionary, data-quality audit, insight log, README, presentation, and QA templates
- Dedicated project-content and package audit

### Changed

- Platform totals increased to six tutorials, 363 chapters, and 1,089 exercises
- Projects domain is now fully available rather than curriculum-only
- Homepage, tutorials, career path, curriculum, search, footer, sitemap, and documentation include Analytics Workflows and the Project Center
- v2.6.0 is the current roadmap release

### Validation

- 549 generated HTML pages
- 35,107 local references checked
- 0 broken local references
- Six projects, 48 workflow phases, 6,690 project data rows, packages, templates, deliverables, and quality gates validated
- Browser tests passed for workflow navigation, exercises, quiz, project cards, project progress, bilingual state, sticky header, retained courses, footer behavior, and mobile drawer

## v2.5.0 — Complete Python for Data Analytics Tutorial

### Added

- 94 bilingual Python chapters across nine modules
- 282 chapter exercises, 94 worked examples, and a randomized 30-question final quiz
- Browser-side Python editor powered by pinned Pyodide 314.0.2
- Standalone `/playground/python/` route
- NumPy, pandas, Matplotlib, SciPy, Jupyter, cleaning, EDA, statistics, time-series, reproducibility, and portfolio-project coverage
- Synthetic retail sales, customer, and deliberately messy practice datasets
- Starter and completed Jupyter notebooks
- Downloadable practice scripts, requirements file, data dictionary, and combined ZIP package
- Dedicated Python course and starter-code audit
- Netlify CSP support for WebAssembly execution

### Changed

- Python is now marked `tutorial-published`
- Platform totals increased to five tutorials, 314 chapters, and 942 exercises
- Homepage, tutorial library, career path, curriculum, search, examples, exercises, quizzes, and references include Python
- v2.5.0 is the current roadmap release

### Validation

- 489 generated HTML pages
- 31,454 local references checked
- 0 broken local references
- 94/94 Python chapter starter snippets executed successfully in the local audit environment
- Python browser editor UI, standalone playground UI, course completion, EN/BN switching, exercises, quiz, sticky header, and mobile 94-chapter drawer passed Chromium regression testing
- Existing Data Foundations, Excel, SQL, Power BI, statistics, and footer behavior passed regression testing


## v2.4.0 — Complete Power BI for Data Analytics Tutorial

### Added

- 77 bilingual Power BI chapters across nine modules
- 231 chapter exercises, 77 examples, and a 30-question final quiz
- Browser-side Power BI decision and measure simulations
- Retail star-schema practice dataset and ZIP download
- DAX measure library
- Power Query M examples
- Project and QA checklist
- Power BI data dictionary
- Dedicated Power BI content and practice-data audit

### Changed

- Power BI is now marked `tutorial-published`
- Platform totals increased to four tutorials, 220 chapters, and 660 exercises
- v2.4.0 is the current roadmap release
- Homepage, tutorial library, career path, curriculum, search, and resources include the complete Power BI course

### Footer adjustment

- Removed the `Inspired by tafshir027/stats` link from `.footer-bottom-links`
- Changed `Privacy & credits` to `About`
- The footer-bottom links now contain only `<a href="/about/">About</a>`

### Validation

- 389 generated HTML pages
- 20,367 local references checked
- 0 broken local references
- Power BI data-model integrity and browser simulations passed
- Existing Data Foundations, Excel, SQL, statistics, sticky-header, language, theme, exercises, and quiz behavior passed regression testing

## v2.3.0 — Complete SQL for Data Analytics Tutorial

### Added
- Complete 66-chapter bilingual SQL for Data Analytics tutorial across nine modules.
- Browser-side SQL editor and standalone playground powered by sql.js 1.14.1.
- Deterministic six-table retail analytics practice database.
- 198 SQL chapter exercises, final quiz, examples, glossary, and reference library.
- Downloadable database seed, 66-query collection, and CSV data dictionary.
- Automated execution audit for all 66 chapter starter queries.

### Changed
- SQL domain and curriculum status changed from curriculum-ready to tutorial-published.
- Homepage, tutorials, resource libraries, roadmap, and documentation now reflect three published courses and 143 chapters.
- CSP permits the pinned jsDelivr sql.js runtime and WASM fetch while retaining a static no-backend architecture.

### Validated
- 307 HTML pages and 12,664 local references with zero broken links.
- Sticky header, SQL tutorial navigation, playground UI, exercises, quiz, retained tutorials, statistics labs, and mobile drawer.

All notable changes are documented here.

## [2.2.0] — Complete Excel for Data Analytics Tutorial

### Added

- Complete 56-chapter Excel for Data Analytics Tutorial across eight modules
- Microsoft 365-first coverage of workbook foundations, formulas, analytical functions, lookups, dynamic arrays, PivotTables, charts, Power Query, the Data Model, Power Pivot/DAX basics, auditing, dashboards, and a final project
- Fifty-six chapter-specific interactive Excel activities
- One hundred sixty-eight Excel chapter exercises
- Randomized 30-question Excel final quiz
- Excel worked-example and reference libraries
- Downloadable multi-sheet Excel practice workbook
- Excel course modules in the persistent chapter sidebar and course landing page
- Multi-course Tutorials, Exercises, Examples, Quiz, and References index pages
- Browser tests for XLOOKUP, Excel progress, exercise filtering, final quiz, and mobile navigation

### Changed

- Shared site header is sticky on every route and uses an opaque blurred surface while scrolling
- Excel domain and curriculum status changed from `curriculum-ready` to `tutorial-published`
- Main homepage now presents both published tutorials and starts with the Excel course
- Resource navigation now opens multi-course indexes rather than Data Foundations-only pages
- Storage schema advances to version 4 without deleting prior progress
- SQL, Power BI, Python, and portfolio releases move to v2.3.0–v2.6.0

### Preserved

- Complete 21-chapter Data Foundations tutorial
- 108 comprehensive lessons and 20 statistical laboratories
- Existing routes, theme, language, bookmarks, progress, datasets, projects, and static Netlify deployment

## [2.1.0] — Tutorial Platform Core and Complete Data Foundations Tutorial

### Added

- Tutorial-first homepage and primary navigation
- Complete 21-chapter English/Bangla Data Foundations Tutorial
- Persistent desktop chapter sidebar and searchable mobile chapter drawer
- Static, topic-specific chapter content with objectives, definitions, vocabulary, worked examples, and recaps
- Twenty-one interactive “Try it yourself” activities
- Sixty-three chapter exercises with answer checking and model responses
- Randomized 30-question final quiz with browser-local result storage
- Dedicated exercise, example, and reference libraries
- Previous/next chapter navigation and browser-local chapter completion
- Print-friendly tutorial pages
- Tutorial content schema and generator under `content/tutorials` and `scripts/tutorial_generator.py`
- Automated tutorial completeness audit
- Browser smoke tests for the full tutorial workflow

### Changed

- Primary navigation is now Tutorials, Exercises, Examples, Projects, References, and Career Paths
- Study-plan and curriculum features are supporting tools rather than the main product
- Data Foundations is marked `tutorial-published`
- Excel, SQL, Power BI, and Python tutorial targets move to v2.2.0–v2.5.0
- Storage schema advances to version 3 while preserving existing `dlh-*` and migrated `slh-*` progress
- Search includes individual tutorial chapters

### Preserved

- 108 comprehensive bilingual lessons
- 20 statistical laboratories
- Existing topic and lab URLs
- Guided My Learning dashboard
- Datasets, projects, curriculum maps, theme, language, bookmarks, and Netlify deployment

## [2.0.0] — Data Analytics Platform Architecture and Curriculum Foundation

### Added

- Rebranded product identity: Data Learning Hub
- Modular content architecture under `content/platform`, `content/statistics`, `content/tracks`, and `content/datasets`
- Nine top-level learning domains with transparent publication status
- Active Data Analyst route and supporting Research & Decision Analyst route
- Reviewed Excel, SQL, Power BI, and Python curriculum maps
- Tool teaching baselines linked to official documentation
- Five-step onboarding covering goal, level, study time, learning mode, and prior tool knowledge
- Projects, Career Paths, and Curriculum routes
- Three documented synthetic datasets and dictionaries
- Retail Sales Foundations Project
- Curriculum architecture audit
- v1-to-v2 browser-local progress migration
- Legacy route redirects for `/catalog/` and `/paths/`

### Changed

- Statistics is now positioned as a foundation within Data Analytics
- Primary navigation is My Learning, Learn, Practice, Projects, and Career Paths
- Product generation is driven by modular domain files rather than one monolithic curriculum source
- Generated content payload uses `window.DLH_CONTENT`
- Browser events and storage use the `dlh-*` namespace
- Footer, metadata, manifest, sitemap, robots, and social identity use Data Learning Hub

### Preserved

- 108 comprehensive bilingual lessons
- 20 statistical labs
- English/Bangla switching
- Light/dark theme
- Guided learning workflow
- Local bookmarks and completion tracking
- Static Netlify deployment

### Publication boundary

Excel, SQL, Power BI, and Python are curriculum-ready but not yet published as complete lessons. No planned item is represented as finished content.

## [1.2.0] — Comprehensive Lesson Experience

The tagged v1.2.0 release remains the stable Statistics Learning Hub historical baseline. Its release documentation is archived under `docs/archive/v1/`.
