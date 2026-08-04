# Data Learning Hub

**A tutorial-first, English-first bilingual platform for learning Data Analytics.**

Data Learning Hub is a completely static learning website built with HTML, CSS, Vanilla JavaScript, and a Python-based page generator used only during development. The published site requires no backend, API, database, account, or build process on Netlify.

## Current release

### v2.1.0 — Tutorial Platform Core and Complete Data Foundations Tutorial

The primary product is now a chapter-based tutorial system rather than a curriculum or study-plan dashboard.

Published in this release:

- Complete **Data Foundations Tutorial**
- 21 sequential bilingual chapters
- 84 learning objectives
- 63+ topic-specific teaching sections
- 84+ key terms and definitions
- 21 worked analytical examples
- 21 interactive “Try it yourself” activities
- 63 chapter exercises
- 30-question randomized final quiz
- Dedicated example and reference libraries
- Persistent desktop chapter sidebar
- Mobile chapter drawer
- Previous/next chapter navigation
- Browser-local chapter completion and quiz result
- Tutorial chapter search
- Print-friendly tutorial pages

The previous platform features remain available as supporting resources:

- 108 comprehensive statistics and analytics lessons
- 20 browser-based statistical laboratories
- Three documented synthetic datasets
- Data Analytics project foundation
- Career paths, curriculum maps, bookmarks, and guided learning plan

## Primary learning experience

```text
Tutorials
→ Open a subject
→ Read Chapter 1
→ Learn the concept
→ Study the worked example
→ Try the activity
→ Complete exercises
→ Continue to the next chapter
→ Take the final quiz
```

A learner does not need to create a study plan before starting.

## Data Foundations course

The complete course covers:

1. Welcome to Data Analytics
2. Data and Statistics
3. Observations, Variables, and Values
4. Rows, Columns, Tables, and Datasets
5. Categorical and Numerical Data
6. Discrete and Continuous Data
7. Measurement Scales
8. Structured, Semi-structured, and Unstructured Data
9. Data Sources and Collection Methods
10. Population, Sample, Parameter, and Statistic
11. Sampling Methods
12. Bias, Confounding, and Error
13. Data Quality Dimensions
14. Missing, Duplicate, Invalid, and Outlier Values
15. Tidy Data and Data Organization
16. Frequency Tables and Summary Views
17. Analytical Questions and Defining Metrics
18. Exploratory Data Analysis Workflow
19. Reproducible Analysis and Documentation
20. Data Ethics, Privacy, and Responsible Use
21. Mini Project: Audit a Retail Dataset

## Main routes

- `/tutorials/` — tutorial library
- `/tutorials/data-foundations/` — complete course contents
- `/tutorials/data-foundations/<chapter>/` — tutorial chapters
- `/exercises/data-foundations/` — complete exercise library
- `/quiz/data-foundations/` — final assessment
- `/examples/data-foundations/` — worked-example library
- `/references/data-foundations/` — source and term reference
- `/projects/` — datasets and applied projects
- `/career-paths/` — role-oriented routes
- `/practice/` — statistics laboratories and datasets
- `/learn/` — retained comprehensive lesson library
- `/my-learning/` — optional browser-local learning dashboard

## Source architecture

```text
content/
├── tutorials/
│   ├── data_foundations.json
│   └── loader.py
├── platform/
├── statistics/
├── tracks/
└── datasets/

scripts/
├── generate.py
├── tutorial_generator.py
├── audit_tutorials.py
├── audit_curriculum.py
├── audit_lessons.py
├── audit_links.py
├── browser_smoke.py
└── test_stats.mjs
```

Authored tutorial content lives in `content/tutorials/`. Generated HTML and `assets/js/content.js` should not be edited as the primary source.

## Generate and validate

```powershell
npm run generate
npm test
npm run test:browser
```

Expected release result:

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 1 published tutorial with 21 complete bilingual chapters.
Checked 2,233 local HTML and asset references across 170 HTML files.
0 broken local references found.
Browser smoke test passed.
```

## Netlify deployment

```text
Production branch:  main
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
```

Generated files are committed to the repository, so Netlify serves the site directly.

## Privacy

Tutorial progress, quiz results, language, theme, bookmarks, and optional learning preferences remain in the visitor’s browser through `localStorage`. No learner data are sent to a server.

## Credits

Idea and developed by **Saiful Islam**.

- Website: https://saifulshuvo.com
- GitHub: https://github.com/SaifulIslamDS/
- LinkedIn: https://www.linkedin.com/in/saifulislampro/
- Inspired by: https://github.com/tafshir027/stats

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.1.0 release report](docs/RELEASE-REPORT-v2.1.0.md)
- [v1-to-v2 migration](docs/MIGRATION-v1-to-v2.md)
