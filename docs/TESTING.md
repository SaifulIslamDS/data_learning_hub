# Testing — v2.2.0

## Commands

```powershell
npm run generate
npm test
npm run test:browser
```

## Automated test layers

### Statistical core

Validates the retained browser-statistics functions.

### Comprehensive lesson audit

Confirms that all 108 retained lessons preserve their required content structure.

### Tutorial audit

Validates both published tutorials, chapter IDs, modules, bilingual fields, teaching-section depth, terms, worked examples, activities, exercise types, references, downloads, and generated routes.

Expected tutorial totals:

- Data Foundations: 21 chapters and 63 exercises
- Excel for Data Analytics: 56 chapters and 168 exercises
- Combined: 77 chapters and 231 exercises

### Curriculum audit

Checks publication status, domain URLs, curriculum relationships, datasets, project references, tool baselines, active career route, storage migration, and release identity.

### Link audit

Scans every generated HTML file and local asset/download reference. The v2.2.0 baseline is 235 HTML files, 6,704 checked references, and zero broken local references.

### JavaScript syntax

Runs `node --check` against every shared browser module.

### Browser smoke test

Covers:

- sticky header at initial and scrolled positions
- homepage and tutorial library
- 56-chapter, eight-module Excel course landing
- downloadable workbook link
- XLOOKUP chapter, formula, activity, and completion state
- EN/BN switch and theme-compatible rendering
- 168-item Excel exercise library and filtering
- randomized 30-question Excel quiz
- retained Data Foundations route
- retained statistical lab route
- 56-link mobile course drawer

Screenshots are written to `docs/screenshots-v2.2.0/`.

## Spreadsheet validation

The Excel practice workbook is built with `artifact_tool`, inspected for sheet structure and key formula regions, imported back from the exported `.xlsx`, and checked for formula errors.
