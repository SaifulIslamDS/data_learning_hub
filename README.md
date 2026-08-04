# Statistics Learning Hub

A comprehensive, English-first, bilingual learning platform for statistics, data analytics, data science, data engineering, research, and evidence-based decision-making.

The production site is completely static: HTML, CSS, and Vanilla JavaScript. It has no backend framework, API, database, authentication system, or server-side calculator. A learner's guided plan, progress, bookmarks, language, and theme remain in the browser through `localStorage`.

## Current release: v1.2.0 — Comprehensive Lesson Experience

v1.2.0 preserves the successful guided workflow from v1.1.0 and rebuilds the lesson experience around actual teaching depth.

Each published lesson now follows four clear phases:

```text
Learn
→ Explore
→ Apply
→ Check
```

A learner no longer receives only a short definition and generic study instructions. Every one of the 108 bilingual lessons now includes:

- a plain-language topic explanation;
- a topic-specific explanation of why the concept matters;
- at least three important terms or concepts;
- clear learning outcomes;
- a definition, formula, or formal decision rule;
- a unique real-world scenario;
- a worked reasoning sequence;
- responsible and incorrect interpretation examples;
- a repeatable analytical workflow;
- at least two implementation guides relevant to the module;
- an interactive lab connection where a real lab exists;
- a practical mini-assignment;
- a three-option knowledge check with explanation;
- common mistakes and cautions;
- a lesson recap;
- authoritative sources and further reading.

Advanced details are progressively disclosed through accordions, so lessons remain readable without becoming shallow.

## Release scope

- 9 structured learning modules
- 108 comprehensive English/Bangla lesson routes
- 20 interactive statistical labs
- 5 guided learning paths
- Three-step onboarding wizard
- Personalized `My Learning` dashboard
- Goal-, level-, and learning-style-aware recommendations
- Learn → Explore → Apply → Check lesson architecture
- 108 unique practical lesson scenarios
- Module-relevant spreadsheet, SQL, BI, Python, modelling, or engineering implementation guidance
- 40-term bilingual glossary
- English-first EN/BN language switching
- Persistent light/dark theme
- Global search, module filters, bookmarks, and completion tracking
- Responsive desktop, tablet, and mobile layouts
- SEO metadata, sitemap, robots file, web manifest, 404 page, and social artwork
- Netlify headers, cache policy, and fallback configuration
- Automated statistical, lesson-completeness, JavaScript-syntax, and local-link validation

## Learning model

The primary learning loop is:

```text
Understand the concept and vocabulary
→ Work through a practical scenario
→ Implement the idea in a suitable tool or workflow
→ Interpret the result and test understanding
→ Transfer the concept to a real dataset or professional tool
```

The site teaches statistical reasoning and transparent implementation. It does not claim that reading lessons alone replaces real datasets, Excel, SQL, Python, R, Power BI, portfolio projects, production data systems, domain expertise, or formal academic study.

## Learning modules

1. Data & Statistics Foundations
2. Descriptive Statistics & Visualization
3. Probability & Distributions
4. Statistical Inference & Experimentation
5. Correlation & Regression Modeling
6. Data Analytics & Business Statistics
7. Data Science Statistics
8. Data Engineering Foundations
9. Advanced Statistical Methods

Every module contains 12 published lessons. Every lesson card resolves to an implemented route.

## Guided paths

- Statistics Foundations
- Data Analyst
- Data Scientist
- Data Engineer
- Research & Business Decisions

The guided system still presents one recommended next step instead of exposing all 108 lessons at once. The comprehensive lesson release improves depth inside that focused route; it does not bring back the previous content-wall experience.

## Interactive labs

The browser-based labs cover summary statistics, weighted means, z-scores, quantiles, histograms, box plots and outliers, Pearson correlation, ordinary least-squares regression, normal/binomial/Poisson probabilities, confidence intervals, one- and two-sample t tests, chi-square independence, A/B proportions, the Central Limit Theorem, Monte Carlo estimation, moving averages, and sample-size planning.

Calculator inputs are processed locally. The statistical engine is implemented in `assets/js/stats-core.js`, with deterministic reference checks in `scripts/test_stats.mjs`.

## Local use

The site uses root-relative URLs, so serve it through a local web server rather than opening an HTML file directly.

```bash
npm run serve
```

Then open:

```text
http://localhost:8080
```

No package installation is required for the deployed site itself.

## Quality checks

```bash
npm test
```

This runs:

```bash
npm run test:stats
npm run audit:lessons
npm run audit:links
```

The lesson audit verifies that all 108 lessons contain the complete bilingual v1.2.0 structure and unique scenarios.

Regenerate all static routes and the sitemap after editing curriculum or lesson source data:

```bash
npm run generate
npm test
```

Optional browser smoke test for the representative comprehensive lesson:

```bash
python scripts/browser_smoke.py
```

## Netlify deployment

The repository includes `netlify.toml` and does not require a build command.

1. Push this directory to the `main` branch of `statistics_learning_hub`.
2. In Netlify, choose **Add new site → Import an existing project**.
3. Select the GitHub repository.
4. Keep the base directory and build command empty.
5. The publish directory is configured as `.` in `netlify.toml`.
6. Deploy the site.
7. Replace the placeholder production origin `https://statistics-learning-hub.netlify.app` if Netlify assigns another subdomain or a custom domain is connected.
8. Run `npm run generate` after changing that origin so canonical URLs, Open Graph URLs, `robots.txt`, and `sitemap.xml` remain correct.

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for the complete checklist.

## Repository structure

```text
.
├── index.html
├── 404.html
├── start/                       # Guided onboarding
├── my-learning/                 # Browser-local dashboard
├── about/
├── catalog/
├── glossary/
├── paths/
├── topics/                      # 108 generated lesson routes
├── tools/                       # 20 interactive labs + index
├── assets/
│   ├── css/main.css
│   ├── icons/
│   └── js/
├── scripts/
│   ├── generate.py
│   ├── topic_details.py
│   ├── comprehensive_content.py
│   ├── audit_lessons.py
│   ├── audit_links.py
│   ├── browser_smoke.py
│   └── test_stats.mjs
├── docs/
├── manifest.webmanifest
├── robots.txt
├── sitemap.xml
├── netlify.toml
└── package.json
```

## Content and architecture

The curriculum and routes are maintained in `scripts/generate.py`. Reviewed concise definitions live in `scripts/topic_details.py`. The comprehensive bilingual lesson schema, practical scenarios, implementation patterns, quizzes, recaps, and reference groups live in `scripts/comprehensive_content.py`.

The generator exports the complete browser dataset to `assets/js/content.js`. Generated lesson pages remain intentionally thin and reuse the shared renderer in `assets/js/topic.js`. Do not hand-edit generated topic routes; update source data and regenerate instead.

Read:

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [v1.2.0 release report](docs/RELEASE-REPORT-v1.2.0.md)

## Credits

**Idea and developed by Saiful Islam**

- Website: <https://saifulshuvo.com>
- GitHub: <https://github.com/SaifulIslamDS/>
- LinkedIn: <https://www.linkedin.com/in/saifulislampro/>

Conceptually inspired by the public repository maintained by `tafshir027`:
<https://github.com/tafshir027/stats>

This rebuild uses an original architecture, interface, codebase, curriculum organization, and educational copy. The inspiration repository is credited for the initial idea rather than treated as the implementation source.

## License

Released under the [MIT License](LICENSE).
