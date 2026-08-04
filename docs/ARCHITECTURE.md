# Architecture — v2.1.0

## Product model

Data Learning Hub is now tutorial-first. The primary content unit is a **tutorial chapter**, while learning plans, career paths, the retained statistics lesson library, laboratories, and projects provide optional support.

## Runtime

The deployed website contains only:

- Static HTML
- Shared CSS
- Vanilla JavaScript
- Local downloadable datasets
- Optional CDN-loaded Chart.js for existing statistics laboratories

There is no server application, API, database, authentication, or cloud learner state.

## Authoring layers

```text
content/tutorials/
├── data_foundations.json  # authored tutorial source
└── loader.py

scripts/
├── generate.py            # existing platform generator
└── tutorial_generator.py  # tutorial pages, indices, libraries, homepage
```

`generate.py` loads all product data, emits `assets/js/content.js`, creates retained platform pages, then invokes the tutorial generator. Generated files are committed for direct Netlify deployment.

## Tutorial content schema

Each course defines:

- Identity, language titles, description, status, version, estimated hours
- Ordered chapters
- Final quiz policy
- Reference groups

Each chapter contains:

- Stable ID and sequence
- English/Bangla title and summary
- Estimated study time
- Four learning objectives
- Three or more topic-specific teaching sections
- Four or more key terms
- One worked example with steps and conclusion
- One interactive activity definition
- Three exercises: multiple choice, fill, and short response
- Four-point recap
- Two or more authoritative references

## Generated tutorial routes

```text
/tutorials/
/tutorials/data-foundations/
/tutorials/data-foundations/<chapter>/
/exercises/data-foundations/
/quiz/data-foundations/
/examples/data-foundations/
/references/data-foundations/
```

## Browser modules

- `tutorial-core.js` — tutorial lookup, progress, drawer, exercise primitives
- `tutorial-index.js` — course and example-library behavior
- `tutorial.js` — chapter activity, chapter exercises, completion
- `tutorial-exercises.js` — all-chapter exercise library
- `tutorial-quiz.js` — randomized final assessment and scoring

## Learner state

Stored under the `dlh-*` namespace:

- `dlh-tutorial-data-foundations-completed`
- `dlh-tutorial-data-foundations-quiz`
- Existing language, theme, bookmarks, lesson completion, and profile keys

The storage schema is version 3. Existing v1/v2 progress remains compatible.

## Publication rules

A subject can be labeled:

- `tutorial-published` — complete chapter-based tutorial exists
- `available` — comprehensive legacy lesson/library content exists
- `curriculum-ready` — reviewed scope exists but tutorial is not published
- `foundation-ready` — shared project or dataset foundation exists
- `roadmap` — future path only

Only published or available content receives working learning URLs.
