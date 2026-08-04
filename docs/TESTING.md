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

### JavaScript syntax validation

Before release, every project JavaScript file is checked with Node's parser:

```bash
find assets/js -name '*.js' -print0 | xargs -0 -n1 node --check
```

## Guided-experience QA checklist

### Onboarding

- `/start/` opens from the homepage and primary navigation.
- The wizard presents exactly one decision at a time.
- All five goals can be selected.
- All three levels can be selected.
- All three learning modes can be selected.
- Back and continue controls preserve prior selections.
- The completed plan is saved to `slh-profile` in `localStorage`.
- Changing an existing plan updates the dashboard without deleting bookmarks or progress.
- EN/BN switching updates the wizard copy without losing choices.

### Personalized dashboard

- `/my-learning/` invites profile creation when no profile exists.
- A saved profile produces one recommended next lesson rather than the full catalog.
- The recommended lesson belongs to the selected path.
- Beginner, intermediate, and advanced entry points begin at sensible positions.
- The session sequence reflects concept-first, balanced, or practice-first mode.
- A laboratory appears only when the lesson has an implemented related lab.
- Completing the next lesson advances the recommendation.
- Resetting progress preserves the plan and bookmarks.
- Bookmarked lessons appear in the dashboard.

### Learn, Practice, Apply

- Homepage presents one primary guided action.
- Catalog defaults to the selected path when a profile exists.
- The full 108-lesson catalog remains intentionally accessible.
- Paths page renders five learning paths.
- One path is expanded into four phases at a time.
- Lessons show guided passes, interpretation prompts, and one next action.
- Labs show the controlled-experiment and plain-language interpretation workflow.
- The experience remains useful when a learner chooses not to create a profile.

## General browser QA checklist

- Homepage and primary calls to action render.
- Catalog reports 108 lessons.
- Search and every filter produce expected results.
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

For v1.1.0:

- statistical-core automated tests passed;
- all project JavaScript files passed syntax validation;
- the local audit checked 1,219 HTML and asset references across 137 HTML files;
- zero broken local references were found;
- desktop views were visually reviewed for the homepage, onboarding, personalized dashboard, and a guided lesson;
- the homepage was visually reviewed at a mobile viewport;
- the numerical laboratory engine was unchanged except for the guided instructional shell.

Screenshots are stored in `docs/screenshots-v1.1.0/`.
