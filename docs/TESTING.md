# Testing and Release Validation

## Automated release command

Run:

```bash
npm test
```

It performs three required checks.

## 1. Statistical-core tests

```bash
npm run test:stats
```

`scripts/test_stats.mjs` checks representative numerical results and boundary behavior for descriptive statistics, quantiles, correlation, ordinary least squares, normal probabilities, inverse-normal values, t critical values, binomial probabilities, Poisson probabilities, and gamma-based calculations.

A new or changed statistical function is incomplete until known reference values and relevant boundary behavior are tested.

## 2. Comprehensive lesson audit

```bash
npm run audit:lessons
```

`scripts/audit_lessons.py` validates the generated `assets/js/content.js` payload.

Release requirements:

- exactly 108 lessons;
- required bilingual comprehensive-lesson fields on every topic;
- at least three concept cards;
- a five-step workflow;
- at least two implementation guides;
- a three-option quiz;
- at least four recap points;
- authoritative references;
- unique scenario titles;
- no legacy generic scenario template;
- meaningful minimum content lengths.

Expected result:

```text
Validated 108 comprehensive bilingual lessons.
```

## 3. Local-link audit

```bash
npm run audit:links
```

`scripts/audit_links.py` scans every HTML file and verifies local HTML, stylesheet, script, image, icon, manifest, and fragment references.

Release requirement:

```text
0 broken local references found
```

## JavaScript syntax validation

Before packaging:

```bash
find assets/js -name '*.js' -print0 | xargs -0 -n1 node --check
```

## Browser smoke test

Run when lesson UI, bilingual interaction, quiz behavior, or theme logic changes:

```bash
python scripts/browser_smoke.py
```

The script uses headless Chromium and validates the representative `Statistics and Data` lesson for:

- English-first rendering;
- four lesson phases;
- explicit Data and Statistics concept cards;
- unique shop-sales scenario;
- implementation accordions;
- three-option quiz and feedback;
- Bangla switching;
- dark-theme switching;
- mobile rendering.

It creates:

```text
docs/screenshots-v1.2.0/statistics-and-data-desktop.png
docs/screenshots-v1.2.0/statistics-and-data-mobile.png
```

## Comprehensive lesson QA checklist

### Learn

- The first explanation is understandable without prior technical knowledge.
- The page defines the actual topic rather than only describing a study workflow.
- Important terms are topic-specific.
- Learning outcomes are observable actions.
- Formula or formal rule states the relevant convention or limitation.

### Explore

- The scenario is realistic and unique to the lesson.
- The analytical question is explicit.
- Worked steps identify observations, variables, parameters, units, design, or grain as appropriate.
- Interpretation distinguishes evidence from unsupported certainty or causality.

### Apply

- Workflow matches concept, formula, method, or operational lesson type.
- Implementation guidance matches the module.
- No nonexistent software function is invented.
- A linked lab exists and works when shown.
- Mini-assignment requires a result and one limitation.

### Check

- Exactly one quiz option is defensible.
- Feedback and explanation switch language.
- Common mistakes are not hidden permanently; they are available by expansion.
- Recap accurately reflects the lesson.
- Further-reading links point to authoritative sources.

## Guided-experience regression checklist

- Onboarding still stores goal, level, and learning preference locally.
- My Learning still recommends one next lesson.
- Completion advances the plan.
- Catalog can still reveal the full 108 lessons intentionally.
- Paths still show five routes in manageable phases.
- Existing v1.1.0 local profile and completion data remains compatible.

## General browser QA checklist

- EN/BN controls work on dynamic and static text.
- Light/dark themes include cards, inputs, quizzes, and labs.
- Keyboard focus is visible.
- Skip link works.
- Mobile navigation opens and closes.
- Desktop and mobile layouts have no horizontal overflow.
- All 20 labs calculate supplied examples and reject invalid input clearly.
- Textual calculations remain usable if Chart.js fails.
- Netlify returns the custom 404 page with a 404 status.

## v1.2.0 validation evidence

- statistical-core tests passed;
- 108 comprehensive bilingual lessons passed the content audit;
- all project JavaScript files passed syntax validation;
- 1,219 local references across 137 HTML files passed with zero broken links;
- representative browser smoke test passed for English/Bangla, quiz, theme, and mobile rendering.
