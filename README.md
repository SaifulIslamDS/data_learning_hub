# Data Learning Hub

**Data Analytics first. Data Science and Data Engineering next.**

Data Learning Hub is an English-first, bilingual, browser-only learning platform for structured Data Analytics education. It begins with comprehensive Data Foundations and Statistics, then provides reviewed curriculum foundations for Excel, SQL, Power BI, Python, and cross-tool portfolio projects.

## Current release

### v2.0.0 — Data Analytics Platform Architecture and Curriculum Foundation

This is a major product transformation from the tagged Statistics Learning Hub v1.2.0 baseline.

Available now:

- 108 comprehensive English/Bangla lessons retained from v1.2.0
- 20 browser-based statistical labs
- Active Data Analyst learning route
- Supporting Research & Decision Analyst route
- Five-step guided onboarding
- Browser-local progress, bookmarks, language, theme, and learning preferences
- Three documented synthetic datasets
- One complete foundation project
- Reviewed curriculum maps for Excel, SQL, Power BI, and Python
- Netlify-ready static deployment

Curriculum-ready, not yet published as lessons:

- Excel — target v2.1.0
- SQL — target v2.2.0
- Power BI — target v2.3.0
- Python — target v2.4.0
- Cross-tool projects and portfolio — target v2.5.0

Planned entries are never exposed as fake lesson pages or dead links.

## Product learning model

```text
Learn → Practice → Build → Explain
```

A learner should finish each skill with an observable output: a calculation, analytical note, query, report, notebook, project deliverable, or decision-ready explanation.

## Architecture

The authored source is modular but the deployed site is ordinary static HTML, CSS, and JavaScript.

```text
content/
├── platform/       # identity, domains, glossary, compatibility paths
├── statistics/     # retained lessons, labs and lesson enrichment
├── tracks/         # career paths and Excel/SQL/Power BI/Python curricula
└── datasets/       # dataset and project metadata

scripts/
├── generate.py
├── audit_curriculum.py
├── audit_lessons.py
├── audit_links.py
├── browser_smoke.py
└── test_stats.mjs
```

Generated pages are committed to the repository so Netlify does not require a build command.

## Main routes

- `/` — product home and current learning status
- `/start/` — five-step guided setup
- `/my-learning/` — browser-local learning dashboard
- `/learn/` — available lessons and domain overview
- `/practice/` — statistical labs and datasets
- `/projects/` — available projects and dataset library
- `/career-paths/` — active and future career routes
- `/curriculum/` — reviewed tool-track scope and release sequence
- `/glossary/` — bilingual glossary

Legacy `/catalog/` and `/paths/` routes redirect to the new information architecture.

## Generate and validate

Python and Node.js are used only for development and validation.

```powershell
npm run generate
npm test
npm run test:browser
```

Expected core result:

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 9 domains, 4 curriculum-ready tool tracks and 3 synthetic datasets.
0 broken local references found.
```

## Deploy to Netlify

Use:

```text
Base directory:     leave empty
Build command:      leave empty
Publish directory:  .
Production branch:  main
```

The repository includes `netlify.toml` for security headers, cache policy, compatibility redirects, and custom 404 handling.

After Netlify assigns the final production URL, update `site_url` in `content/platform/config.py`, then run:

```powershell
npm run generate
npm test
git add .
git commit -m "chore: configure production site URL"
git push origin main
```

## Progress migration

On first use, v2 copies compatible browser-local settings from legacy `slh-*` keys into `dlh-*` keys. The old keys are not deleted. Existing completion IDs are preserved wherever the lesson ID remains valid.

## Privacy

There is no backend, API, database, analytics account, or cloud learner profile. User preferences and progress remain in the browser through `localStorage`. Statistical lab input is processed locally.

## Credits

Idea and developed by **Saiful Islam**.

- Website: https://saifulshuvo.com
- GitHub: https://github.com/SaifulIslamDS/
- LinkedIn: https://www.linkedin.com/in/saifulislampro/
- Inspired by: https://github.com/tafshir027/stats

See [CREDITS.md](CREDITS.md) and [docs/CONTENT-STANDARDS.md](docs/CONTENT-STANDARDS.md).

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Migration from v1](docs/MIGRATION-v1-to-v2.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v2.0.0 release report](docs/RELEASE-REPORT-v2.0.0.md)
