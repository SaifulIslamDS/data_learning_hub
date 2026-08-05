# v2.3.0 Release Report — Complete SQL for Data Analytics Tutorial

## Release objective

Publish a complete tutorial-first SQL learning track for analysts, including browser-side practice, while preserving the static architecture, bilingual interface, sticky header, existing Data Foundations and Excel tutorials, comprehensive statistics lessons, and statistical laboratories.

## Published SQL course

- 66 sequential chapters
- 9 modules
- 264 learning objectives
- 198 chapter exercises
- 66 worked examples
- 66 browser SQL activities
- Randomized 30-question final quiz
- Examples and reference libraries
- Five project-oriented chapters

## Course modules

1. SQL and Relational Foundations
2. Select, Filter, and Sort
3. Expressions and Functions
4. Aggregation and Metrics
5. Joins and Set Operations
6. Subqueries and Common Table Expressions
7. Window Functions and Analytical Patterns
8. Modeling, Quality, and Performance
9. Portfolio Analytics Projects

## Browser SQL practice

The tutorial teaches portable relational concepts with PostgreSQL as the primary explanatory dialect. Interactive exercises execute locally in the visitor's browser using sql.js 1.14.1 and a SQLite-compatible database. No query or practice data is sent to a backend.

A standalone `/playground/sql/` route and chapter-embedded editors provide query editing, result tables, query reset, and database reset. PostgreSQL/SQLite differences are identified in relevant chapters.

## Practice database

The deterministic retail database includes:

- `customers` — 60 rows
- `products` — 12 rows
- `employees` — 7 rows
- `orders` — 180 rows
- `order_items` — 360 rows
- `web_events` — 172 rows

Downloads include the database script, all starter queries, and a data dictionary.

## Platform totals

- 3 published tutorials
- 143 tutorial chapters
- 429 chapter exercises
- 108 retained comprehensive lessons
- 20 retained statistical laboratories
- 307 generated HTML pages
- 12,664 checked local references
- 0 broken local references

## Validation

- Statistical core tests passed.
- All 108 comprehensive lessons passed content audit.
- All 143 tutorial chapters passed schema and completeness audit.
- All 66 SQL starter queries executed successfully against a fresh SQLite database.
- Curriculum, datasets, publication status, local links, and JavaScript syntax passed.
- Browser smoke tests passed for sticky headers, three-course navigation, SQL chapter UI, standalone playground UI, exercises, quizzes, bilingual state, retained routes, and mobile chapter drawer.

## Runtime dependency

The browser SQL engine is loaded from the pinned jsDelivr path for `sql.js@1.14.1`. The site remains deployable as static files. An internet connection is required the first time the SQL runtime and WASM file are loaded unless they are later vendored locally.
