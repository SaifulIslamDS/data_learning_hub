# Architecture — v2.2.0

## Product model

Data Learning Hub is a static, tutorial-first platform. The primary content unit is a sequential tutorial chapter. Career plans, retained lessons, laboratories, datasets, and projects support the tutorials without blocking direct learning.

## Runtime

The deployed website contains only static HTML, shared CSS, Vanilla JavaScript, local downloadable files, and optional Chart.js use in retained statistical laboratories. There is no backend, API, database, authentication, or cloud learner state.

## Authoring structure

```text
content/tutorials/
├── data_foundations.json
├── excel_data_analytics.json
└── loader.py

scripts/
├── generate.py
└── tutorial_generator.py
```

`generate.py` builds the shared content payload and retained platform pages, then `tutorial_generator.py` emits tutorial indexes, chapter pages, resource libraries, and the homepage.

## Published tutorials

| Tutorial | Modules | Chapters | Exercises |
|---|---:|---:|---:|
| Data Foundations | 4 learning phases | 21 | 63 |
| Excel for Data Analytics | 8 modules | 56 | 168 |
| **Total** |  | **77** | **231** |

## Tutorial schema

Each course defines identity, bilingual descriptions, version, estimated hours, modules, ordered chapters, downloads, final-quiz policy, and reference groups.

Each chapter contains a stable ID, module, title, summary, study time, level, objectives, teaching sections, terms, worked example, interactive activity definition, three exercise types, recap, and references.

## Generated route pattern

```text
/tutorials/
/tutorials/<course>/
/tutorials/<course>/<chapter>/
/exercises/
/exercises/<course>/
/quiz/
/quiz/<course>/
/examples/
/examples/<course>/
/references/
/references/<course>/
```

## Shared browser modules

- `site.js` — sticky global header, navigation, localization, theme, search, footer, and retained platform state
- `tutorial-core.js` — course lookup, local progress, drawer, and exercise primitives
- `tutorial-index.js` — course landing and example-library behavior
- `tutorial.js` — chapter activities, exercises, completion, formula copying
- `tutorial-exercises.js` — complete exercise libraries
- `tutorial-quiz.js` — randomized final assessments

## Sticky header

`#site-header` is the sticky positioning container on every generated page. The nested `.site-header` supplies the visual surface, backdrop blur, border, and scrolled shadow. This avoids the parent-height limitation that can occur when only a nested generated header is sticky.

## Learner state

Examples:

```text
dlh-tutorial-data-foundations-completed
dlh-tutorial-data-foundations-quiz
dlh-tutorial-excel-data-analytics-completed
dlh-tutorial-excel-data-analytics-quiz
```

Language, theme, bookmarks, retained-lesson completion, and profile data continue under `dlh-*`. Storage schema version is 4 and legacy `slh-*` migration remains supported.

## Practice files

Static downloadable files are stored under `assets/downloads/` and `assets/datasets/`. The Excel workbook is generated with `artifact_tool`, but the deployed file is a normal `.xlsx` download.

## Publication statuses

- `tutorial-published` — complete tutorial, exercises, examples, quiz, and references exist
- `available` — retained comprehensive learning material exists
- `curriculum-ready` — reviewed scope exists but is not represented as published tutorial content
- `foundation-ready` — project or dataset foundation exists
- `roadmap` — future route only
