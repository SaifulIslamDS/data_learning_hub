# Architecture

## Design objective

Statistics Learning Hub is authored as a maintainable data-driven project but deployed as ordinary static files. The browser receives only HTML, CSS, JavaScript, icons, and content data. There is no application server.

## Runtime layers

### Static route layer

The repository contains explicit routes for the homepage, catalog, paths, glossary, about page, all lessons, and all labs. This provides crawlable URLs, reliable Netlify routing, shareable pages, and useful per-page metadata.

### Shared presentation layer

`assets/css/main.css` defines the design tokens, responsive layouts, cards, navigation, forms, laboratory workspace, lesson pages, themes, accessibility helpers, and print behavior.

### Shared application shell

`assets/js/site.js` renders and manages:

- header and footer;
- responsive navigation;
- English/Bangla switching;
- global search;
- light/dark theme events;
- local bookmarks and completion state;
- scroll-to-top behavior;
- homepage content grids.

`assets/js/theme-init.js` applies the saved or operating-system theme before the page renders to reduce theme flashing.

### Content model

`scripts/generate.py` contains the module, topic, tool, path, and glossary structures. `scripts/topic_details.py` contains reviewed bilingual topic definitions. The generator writes `assets/js/content.js`, topic HTML routes, tool HTML routes, and `sitemap.xml`.

This gives the site one curriculum source of truth instead of manually maintaining hundreds of independent navigation lists.

### Statistical engine

`assets/js/stats-core.js` contains reusable numerical functions, including descriptive statistics, quantiles, correlation, ordinary least squares, distribution functions, t critical values, gamma/beta approximations, and discrete probability functions.

`assets/js/tools.js` provides the input forms, validation, interpretations, tables, and visual output for the 20 labs. Chart.js is loaded only on lab pages and is used as a visualization layer; numerical results do not depend on the chart library.

## Browser storage

The following preferences may be stored in `localStorage`:

- selected language;
- selected theme;
- bookmarked lessons;
- completed lessons.

No user profile or calculator dataset is transmitted to a server by the application.

## External dependencies

- Google Fonts for Manrope and Hind Siliguri
- Chart.js 4.5.1 from jsDelivr on interactive lab pages

The site continues to render textual calculations if Chart.js is unavailable, although charts will not appear.

## URL strategy

Routes use clean folder URLs such as:

```text
/topics/central-limit-theorem/
/tools/clt-simulator/
```

Root-relative links are intentional for Netlify deployment at the domain root.

## Adding a lesson

1. Add the topic metadata to the appropriate module in `scripts/generate.py`.
2. Add reviewed English and Bangla definitions to `scripts/topic_details.py`.
3. Link a real lab only when that lab is implemented.
4. Run `npm run generate`.
5. Run `npm test`.
6. Browser-check the generated route in both languages and both themes.

## Adding a lab

1. Add lab metadata to the generator.
2. Add form markup, sample values, validation, calculation, interpretation, and visualization in `assets/js/tools.js`.
3. Add or reuse numerical functions in `assets/js/stats-core.js`.
4. Add deterministic reference assertions to `scripts/test_stats.mjs`.
5. Generate routes and run all tests.
