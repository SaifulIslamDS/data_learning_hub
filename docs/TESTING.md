# Testing and Release Validation

## Automated checks

Run:

```bash
npm test
```

### Statistical tests

`scripts/test_stats.mjs` checks representative numerical results and edge behavior for the shared statistical engine. Tests include descriptive statistics, quantiles, correlation, ordinary least squares, normal probabilities, inverse-normal values, t critical values, binomial probabilities, Poisson probabilities, and gamma-based calculations.

A new statistical function is incomplete until at least one known reference value and relevant boundary behavior are tested.

### Link audit

`scripts/audit_links.py` scans all HTML files and verifies local HTML, stylesheet, script, image, icon, manifest, and internal fragment references.

Release requirement:

```text
0 broken local references found
```

## Browser QA checklist

- Homepage modules and featured tools render.
- Catalog reports 108 lessons.
- Search and every filter produce expected results.
- All four learning paths render ordered lessons.
- Glossary search works.
- Every lesson switches between English and Bangla.
- Completion and bookmarks persist after reload.
- Theme follows the OS initially and persists after manual selection.
- Mobile navigation opens, closes, and preserves keyboard usability.
- All 20 labs calculate their supplied example without an error.
- Invalid values produce visible, understandable errors.
- Charts respond to theme changes where applicable.
- Pages remain usable when Chart.js cannot load.
- Keyboard focus is visible.
- Skip link works.
- Desktop and mobile layouts have no horizontal overflow.
- 404 page returns a 404 status through Netlify.

## Current release evidence

For v1.0.0, the local audit checked 1,205 local HTML and asset references across 135 HTML files and found zero broken references. The statistical core test suite passed, JavaScript syntax checks passed, and each of the 20 laboratories successfully calculated its packaged example in a headless Chromium runtime.
