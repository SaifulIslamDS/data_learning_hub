# v2.0.0 Release Report — Data Analytics Platform Architecture and Curriculum Foundation

## Release purpose

Transform the stable Statistics Learning Hub v1.2.0 codebase into a maintainable Data Analytics learning platform without discarding its completed lessons, labs, guided workflow, or learner progress.

## Delivered

### Product and UX

- Data Learning Hub identity
- Data Analytics-first positioning
- simplified career-oriented navigation
- five-step guided onboarding
- active Data Analyst route
- supporting Research & Decision Analyst route
- transparent future routes

### Architecture

- modular platform, statistics, track, and dataset sources
- generated static pages
- stable topic and lab URLs
- legacy route redirects
- versioned browser-storage namespace and v1 migration

### Curriculum foundation

- 108 retained comprehensive bilingual lessons
- 20 retained statistical labs
- reviewed Excel curriculum for v2.1.0
- reviewed SQL curriculum for v2.2.0
- reviewed Power BI curriculum for v2.3.0
- reviewed Python curriculum for v2.4.0
- release sequence through v2.5.0

### Applied learning foundation

- three documented synthetic datasets
- dataset dictionaries
- Retail Sales Foundations Project
- shared-data design for future cross-tool projects

### Quality controls

- curriculum relationship audit
- false-publication checks
- dataset row and file checks
- lesson completeness audit
- statistical core tests
- local-reference audit
- JavaScript syntax checks
- browser smoke tests

## Validation result

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 9 domains, 9 retained modules, 108 lessons and 20 labs.
Validated 4 curriculum-ready tool tracks, 3 synthetic datasets and 2 project definitions.
Checked 1250 local HTML and asset references across 143 HTML files.
0 broken local references found.
Browser smoke test passed.
```

## Honest release boundary

This release does **not** claim that the Excel, SQL, Power BI, or Python lesson tracks are complete. It establishes reviewed scope, prerequisites, sequence, tool baselines, datasets, UX, source architecture, and validation so each later track can be built deeply and consistently.

## Main-branch policy

The owner chose direct work on `main`. The existing `v1.2.0` tag is the stable historical recovery point. Tag this release only after local checks and Netlify deployment are accepted.
