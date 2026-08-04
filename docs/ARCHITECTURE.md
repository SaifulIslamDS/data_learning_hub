# Architecture

## Design objective

Statistics Learning Hub is authored as a maintainable, data-driven project but deployed as ordinary static files. The browser receives only HTML, CSS, JavaScript, icons, and generated content data.

There is no backend framework, API, database, authentication service, or server-side calculation runtime.

## Architectural layers

### Generated static routes

`scripts/generate.py` generates:

- homepage and shared pages;
- guided onboarding;
- personalized learning dashboard;
- catalog and career paths;
- glossary and about page;
- 108 lesson routes;
- 20 interactive lab routes;
- custom 404 page;
- `assets/js/content.js`;
- `sitemap.xml`.

This provides crawlable, shareable routes with per-page metadata while avoiding hand-maintained navigation duplication.

### Curriculum source

`scripts/generate.py` contains:

- modules;
- lesson ordering;
- difficulty and lesson format;
- lab relationships;
- learning paths;
- glossary entries;
- route metadata.

`scripts/topic_details.py` contains the concise reviewed English/Bangla definition for every topic.

### Comprehensive lesson source

`scripts/comprehensive_content.py` contains the v1.2.0 lesson-enrichment model:

- unique bilingual practical scenarios for all 108 lessons;
- explicit analytical questions;
- custom concept definitions for foundational and high-value topics;
- lesson-type classification;
- module-aware implementation guidance;
- practical workflows;
- interpretation standards;
- mini-assignments;
- quizzes and explanations;
- recaps;
- authoritative reference groups.

`build_lesson_content()` combines this material with topic metadata during generation. No remote generation occurs in the browser or during deployment.

### Shared presentation layer

`assets/css/main.css` defines:

- design tokens and light/dark themes;
- responsive header and footer;
- guided onboarding and dashboard;
- catalog, paths, glossary, lessons, and labs;
- the four-phase lesson map;
- concept cards, scenario panels, workflow lists, implementation accordions, quizzes, recaps, and sticky lesson navigation;
- accessibility helpers and print behavior.

The lesson design uses progressive disclosure: essential explanations remain visible while deeper rules, implementation guidance, cautions, and sources can be expanded.

### Shared application shell

`assets/js/site.js` manages:

- header and footer;
- responsive navigation;
- English/Bangla switching;
- global search;
- light/dark theme events;
- local learner-profile helpers;
- guided-path selection;
- bookmarks and completion state;
- homepage recommendations;
- scroll-to-top behavior.

`assets/js/theme-init.js` applies the saved or operating-system theme before normal rendering to reduce theme flashing.

### Guided experience layer

`assets/js/start.js` implements the three-step onboarding flow:

1. learning goal;
2. starting level;
3. preferred learning mode.

`assets/js/dashboard.js` converts the selected profile into one recommended next lesson, a focused session, a short roadmap, bookmarks, and progress controls.

`assets/js/paths.js` presents five learning paths in four phases.

`assets/js/catalog.js` defaults to the learner's selected path while preserving access to the full catalog.

### Comprehensive lesson renderer

`assets/js/topic.js` renders the nested `topic.lesson` data into four phases:

1. **Learn** — plain explanation, importance, concepts, outcomes, and formal rule.
2. **Explore** — real-world scenario, analytical question, worked reasoning, and interpretation boundary.
3. **Apply** — workflow, implementation guidance, related lab, and mini-assignment.
4. **Check** — quiz, explanation, cautions, recap, references, completion, and next lesson.

The renderer also manages:

- language-aware dynamic text;
- local completion and bookmarking;
- guided-path position;
- related laboratory recommendation;
- adjacent and next-plan navigation;
- quiz interaction.

### Statistical engine and labs

`assets/js/stats-core.js` contains reusable numerical functions for descriptive statistics, quantiles, correlation, ordinary least squares, distributions, t critical values, gamma/beta approximations, and discrete probability calculations.

`assets/js/tools.js` provides forms, validation, interpretations, tables, and visual output for the 20 labs. Chart.js is a visualization layer; numerical output does not depend on the chart library.

## Browser storage

The following optional values may be stored in `localStorage`:

- language;
- theme;
- learner profile;
- bookmarked lessons;
- completed lessons;
- last opened topic.

No personal identity, calculator dataset, profile, or progress record is transmitted by the application.

## External dependencies

- Google Fonts for Manrope and Hind Siliguri
- Chart.js 4.5.1 from jsDelivr on lab pages

Lesson text remains available if fonts fail. Textual lab results remain available if Chart.js fails, although charts will not render.

## URL strategy

Clean folder routes are used:

```text
/start/
/my-learning/
/topics/statistics-and-data/
/tools/summary-statistics/
```

Root-relative links are intentional for deployment at the Netlify domain root.

## Editing a lesson

1. Update the topic definition in `scripts/topic_details.py` when the core definition changes.
2. Update the scenario, custom concepts, implementation model, or references in `scripts/comprehensive_content.py`.
3. Do not hand-edit `topics/*/index.html` or `assets/js/content.js`.
4. Run `npm run generate`.
5. Run `npm test`.
6. Run `python scripts/browser_smoke.py` when lesson layout or interaction changes.
7. Review English, Bangla, light, dark, desktop, and mobile presentation.

## Adding a lesson

1. Add topic metadata to the correct module in `scripts/generate.py`.
2. Add the concise bilingual definition to `scripts/topic_details.py`.
3. Add a unique scenario to `SCENARIO_SEEDS`.
4. Add custom concepts when the generated concept structure would be insufficient.
5. Link a lab only when it is fully implemented and pedagogically relevant.
6. Add the topic to a guided path only when sequence is justified.
7. Generate and pass all release gates.

## Adding a lab

1. Add metadata to the generator.
2. Add forms, examples, validation, calculations, interpretation, and visualization in `assets/js/tools.js`.
3. Add or reuse numerical functions in `assets/js/stats-core.js`.
4. Add deterministic reference assertions to `scripts/test_stats.mjs`.
5. Connect the lab only to suitable lessons.
6. Generate routes and run all tests.
