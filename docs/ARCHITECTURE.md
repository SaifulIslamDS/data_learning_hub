# Architecture

## Design objective

Statistics Learning Hub is authored as a maintainable, data-driven project but deployed as ordinary static files. The browser receives only HTML, CSS, JavaScript, icons, and structured content data. There is no application server, API, database, authentication system, or server-side calculator.

The v1.1.0 architecture adds a guided experience layer without changing that static deployment model. Personalization is calculated entirely in the browser from the learner's selected goal, starting level, preferred learning mode, completion state, and bookmarks.

## Runtime layers

### Static route layer

The repository contains explicit routes for:

- homepage;
- guided onboarding;
- personalized learning dashboard;
- catalog;
- learning paths;
- glossary;
- about page;
- 108 lessons;
- 20 interactive labs;
- custom 404 page.

This provides crawlable URLs, reliable Netlify routing, shareable pages, and useful per-page metadata.

### Shared presentation layer

`assets/css/main.css` defines:

- design tokens and themes;
- responsive layouts;
- navigation and footer;
- onboarding controls;
- personalized dashboard panels;
- lesson and laboratory workspaces;
- cards, forms, progress indicators, and callouts;
- accessibility helpers;
- print behavior.

The guided release intentionally uses progressive disclosure: the full curriculum remains available, but primary pages show only the next useful choices.

### Shared application shell

`assets/js/site.js` renders and manages:

- header and footer;
- responsive navigation;
- English/Bangla switching;
- global search;
- light/dark theme events;
- learner profile helpers;
- guided path selection helpers;
- local bookmarks and completion state;
- homepage recommendations;
- scroll-to-top behavior.

`assets/js/theme-init.js` applies the saved or operating-system theme before the page renders to reduce theme flashing.

### Guided experience layer

`assets/js/start.js` implements the three-step onboarding flow:

1. learning goal;
2. starting level;
3. preferred learning mode.

`assets/js/dashboard.js` converts the selected profile into a focused dashboard containing:

- one recommended next lesson;
- a Learn → Practice → Apply session;
- a short visible roadmap;
- saved bookmarks;
- completion controls.

`assets/js/paths.js` renders five path choices and reveals one selected path in four manageable phases.

`assets/js/catalog.js` defaults to the learner's selected path when a profile exists, while preserving a clear way to display the full 108-lesson catalog.

`assets/js/topic.js` renders lessons as guided passes and connects each lesson to reflection, practice, and a next action.

`assets/js/tools.js` provides both the statistical laboratory runtime and the guided practice shell used to frame input changes, observation, interpretation, and transfer to professional tools.

### Content model

`scripts/generate.py` contains the module, topic, tool, path, glossary, route, and metadata structures. `scripts/topic_details.py` contains reviewed bilingual topic definitions. The generator writes:

- `assets/js/content.js`;
- topic HTML routes;
- tool HTML routes;
- onboarding and dashboard routes;
- shared static pages;
- `sitemap.xml`.

This gives the site one curriculum source of truth instead of manually maintaining hundreds of independent navigation lists.

### Statistical engine

`assets/js/stats-core.js` contains reusable numerical functions, including descriptive statistics, quantiles, correlation, ordinary least squares, distribution functions, t critical values, gamma/beta approximations, and discrete probability functions.

`assets/js/tools.js` provides the input forms, validation, interpretations, tables, and visual output for the 20 labs. Chart.js is loaded only on lab pages and is used as a visualization layer; numerical results do not depend on the chart library.

## Browser storage

The following values may be stored in `localStorage`:

- selected language;
- selected theme;
- learner profile (`slh-profile`);
- bookmarked lessons;
- completed lessons.

The learner profile contains only the selected goal, level, and learning mode. No personal identity, learner profile, progress record, or calculator dataset is transmitted to a server by the application.

## Recommendation model

The recommendation system is deterministic rather than AI-generated.

- The selected goal maps to one of five reviewed learning paths.
- The selected level determines a reasonable starting index in that ordered path.
- The selected learning mode changes the order and emphasis of concept, practice, and application actions.
- Completion state determines the next unfinished lesson.
- A linked laboratory is recommended only when an implemented lab exists for the current lesson.

This avoids fake personalization, unsupported content generation, and hidden remote processing.

## External dependencies

- Google Fonts for Manrope and Hind Siliguri
- Chart.js 4.5.1 from jsDelivr on interactive lab pages

The site continues to render textual calculations if Chart.js is unavailable, although charts will not appear.

## URL strategy

Routes use clean folder URLs such as:

```text
/start/
/my-learning/
/topics/central-limit-theorem/
/tools/clt-simulator/
```

Root-relative links are intentional for Netlify deployment at the domain root.

## Adding a lesson

1. Add the topic metadata to the appropriate module in `scripts/generate.py`.
2. Add reviewed English and Bangla definitions to `scripts/topic_details.py`.
3. Link a real lab only when that lab is implemented.
4. Add the lesson to a guided path only when its sequence is educationally justified.
5. Run `npm run generate`.
6. Run `npm test`.
7. Browser-check the route in both languages, both themes, and the relevant guided path.

## Adding a lab

1. Add lab metadata to the generator.
2. Add form markup, sample values, validation, calculation, interpretation, and visualization in `assets/js/tools.js`.
3. Add or reuse numerical functions in `assets/js/stats-core.js`.
4. Add deterministic reference assertions to `scripts/test_stats.mjs`.
5. Connect the lab only to lessons for which it provides meaningful practice.
6. Generate routes and run all tests.

## Modifying guided paths

1. Update the reviewed ordered path in `scripts/generate.py`.
2. Confirm that every referenced topic exists.
3. Confirm that level-based entry points remain sensible.
4. Review the path in `/start/`, `/my-learning/`, `/paths/`, and `/catalog/`.
5. Run generation and link validation before release.
