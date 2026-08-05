# Changelog

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
