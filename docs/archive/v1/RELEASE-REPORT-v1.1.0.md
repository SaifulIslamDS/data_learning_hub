# Statistics Learning Hub v1.1.0

## Guided Learning Experience Release Report

**Release date:** 4 August 2026  
**Release type:** Minor feature and user-experience release  
**Deployment model:** Static HTML, CSS, and Vanilla JavaScript on Netlify

## Executive summary

Version 1.1.0 converts the original content-rich learning hub into a guided learning experience. The complete curriculum remains available, but the primary interface no longer asks a new visitor to choose among 108 lessons, 20 laboratories, nine modules, and multiple career routes at once.

The release introduces a short onboarding flow, deterministic browser-local personalization, a focused My Learning dashboard, and a consistent Learn → Practice → Apply model. The design objective is to reduce choice overload while preserving the depth and openness of the original release.

## User problem addressed

Version 1.0.0 was complete and professional, but a first-time learner could still face several questions:

- Where should I start?
- Which topics are relevant to my goal?
- Do I need to finish everything?
- Which lesson should I open next?
- How does conceptual learning connect to a practical lab?
- How should I transfer the result to Excel, SQL, Python, R, or Power BI?

Version 1.1.0 addresses those questions through guided sequencing and progressive disclosure rather than removing content.

## Major additions

### Three-step onboarding

The new `/start/` experience asks only:

1. the learner's goal;
2. current starting level;
3. preferred learning mode.

The choices are stored locally in the learner's browser. No account, API, or database is introduced.

### Five guided routes

- Statistics Foundations
- Data Analyst
- Data Scientist
- Data Engineer
- Research & Business Decisions

The Statistics Foundations route is new and gives uncertain beginners a safe route before they select a specialist career path.

### My Learning dashboard

The new `/my-learning/` page provides:

- one recommended next lesson;
- one focused session sequence;
- an implemented related lab when available;
- one interpretation or application task;
- a short visible roadmap;
- saved bookmarks;
- completion controls.

The dashboard deliberately avoids displaying the entire curriculum as equal-priority work.

### Learn → Practice → Apply

The release standardizes the core learning loop:

```text
Learn the idea
→ Practice through a controlled example or lab
→ Apply and explain the result in context
```

Lesson pages, lab pages, the homepage, and the dashboard now reinforce this model.

### Progressive disclosure

- The homepage presents one primary starting action.
- Only three featured labs are shown on the homepage.
- Catalog defaults to the learner's selected path when a profile exists.
- The complete catalog remains available through an explicit control.
- The Paths page expands one selected path into four phases.
- Lesson cautions are collapsible rather than competing with the main explanation.

## Interface changes

Primary navigation is simplified to:

```text
Start Here / My Learning
Learn
Practice
Apply
```

Glossary, About, credits, and secondary resources remain available through search, mobile navigation, and the footer.

## Personalization and privacy

The guided recommendation system is deterministic and local.

Stored profile fields:

- goal;
- level;
- learning mode.

The site also continues to store language, theme, bookmarks, and completion state locally. It does not collect a name, email address, identity, calculator dataset, or activity record on a server.

## Content retained

The release preserves:

- 9 modules;
- 108 bilingual lessons;
- 20 statistical laboratories;
- 40-term bilingual glossary;
- English-first EN/BN switching;
- light/dark themes;
- responsive layouts;
- search and filters;
- SEO and Netlify configuration;
- statistical core and its automated tests.

## Validation evidence

Final validation for v1.1.0 produced:

```text
All statistical core tests passed.
Checked 1219 local HTML and asset references across 137 HTML files.
0 broken local references found.
```

All project JavaScript files also passed Node syntax validation.

Visual QA covered:

- desktop homepage;
- desktop onboarding;
- desktop personalized dashboard;
- desktop guided lesson;
- mobile homepage.

Screenshots are stored under `docs/screenshots-v1.1.0/`.

## Files added

- `start/index.html`
- `my-learning/index.html`
- `assets/js/start.js`
- `assets/js/dashboard.js`
- `docs/RELEASE-REPORT-v1.1.0.md`
- `docs/screenshots-v1.1.0/`

## Main files changed

- `index.html`
- `assets/css/main.css`
- `assets/js/site.js`
- `assets/js/catalog.js`
- `assets/js/paths.js`
- `assets/js/topic.js`
- `assets/js/tools.js`
- `scripts/generate.py`
- `README.md`
- `CHANGELOG.md`
- architecture, curriculum, testing, and deployment documentation

## Versioning recommendation

Tag the release as:

```text
v1.1.0
```

Suggested commit message:

```text
feat: add guided learning experience
```

## Known boundaries

- Recommendations are path-based and deterministic; they do not attempt adaptive assessment or AI tutoring.
- Progress is device- and browser-specific because there is no account or backend sync.
- Clearing browser storage removes the saved plan, progress, bookmarks, language, and theme preferences.
- The static site guides conceptual learning but does not replace hands-on work with professional analytical tools and real datasets.
