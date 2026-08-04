# Architecture — Data Learning Hub v2

## 1. Architectural objective

Data Learning Hub must support a growing bilingual curriculum without turning hundreds of lessons into manually duplicated HTML files. The source is structured and generated; the deployed output remains static.

## 2. Runtime boundary

Production uses only:

- HTML
- CSS
- Vanilla JavaScript
- static CSV files
- selected client-side visualization libraries for existing labs
- browser `localStorage`

There is no backend, API, database, authentication, server session, or cloud learner state.

## 3. Authoring layers

### Platform layer

`content/platform/`

Contains product identity, domain definitions, glossary content, storage namespace, tool baselines, and compatibility paths.

### Statistics layer

`content/statistics/`

Contains the tagged v1.2.0 lesson foundation migrated into v2: modules, topics, formulas, comprehensive lesson content, and lab definitions.

### Track layer

`content/tracks/`

Contains career routes and reviewed curriculum maps for Excel, SQL, Power BI, and Python. Curriculum-ready entries are metadata only until a later release supplies complete bilingual lesson content and validation.

### Dataset layer

`content/datasets/`

Contains synthetic dataset and project metadata. Actual CSV files and dictionaries live under `assets/datasets/`.

## 4. Generation

`scripts/generate.py` creates:

- `assets/js/content.js`
- site index and shared product pages
- all 108 lesson pages
- all 20 lab pages
- project pages
- redirects and compatibility pages
- sitemap and robots files

Generated output may be reviewed, but content changes should be made in the source modules and regenerated.

## 5. Publication states

- `available`: complete, tested, and clickable
- `active`: selectable career route
- `supporting`: selectable secondary route
- `foundation-ready`: supporting structure exists but full project track is incomplete
- `curriculum-ready`: reviewed scope exists; lessons are not published
- `roadmap`: future direction only
- `legacy`: compatibility metadata, hidden from primary navigation

The UI and audits enforce this distinction.

## 6. Browser storage

Current keys use `dlh-*`. During first load, compatible legacy `slh-*` values are copied when the corresponding v2 key is absent.

Migration principles:

- do not delete legacy values
- preserve stable lesson IDs
- map obsolete career goals to an active v2 route
- keep migration idempotent
- allow users to reset v2 state independently

## 7. URL design

- `/learn/`: published lesson catalog
- `/practice/`: published labs and datasets
- `/projects/`: published projects and roadmap
- `/career-paths/`: career routes
- `/curriculum/`: planned tool curricula
- `/topics/<id>/`: published lessons
- `/tools/<id>/`: published labs

Legacy routes redirect rather than becoming duplicate content.

## 8. Validation architecture

- `test_stats.mjs`: numerical statistical core
- `audit_lessons.py`: comprehensive lesson completeness
- `audit_curriculum.py`: IDs, relationships, statuses, datasets, projects, and migration configuration
- `audit_links.py`: local HTML and asset references
- JavaScript syntax checks
- `browser_smoke.py`: representative runtime and responsive checks

## 9. Growth rule

A new tool track should be added as a complete vertical slice:

```text
curriculum source
→ bilingual lessons
→ examples
→ exercises/assets
→ assessments
→ project integration
→ audits
→ generated pages
→ release documentation
```

Do not expose placeholder lesson URLs during partial development.
