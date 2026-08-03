# Statistics Learning Hub

A modern, English-first, bilingual learning platform for statistics, data analytics, data science, data engineering, research, and evidence-based decision-making.

The production site is completely static: HTML, CSS, and Vanilla JavaScript. It has no backend framework, API, database, authentication system, or server-side calculator. Learning progress, bookmarks, language, and theme preferences remain in the visitor's browser through `localStorage`.

## Release scope

- 9 structured learning modules
- 108 complete English/Bangla lesson routes
- 20 interactive statistical labs
- 4 career-oriented learning paths
- 40-term bilingual glossary
- English-first EN/BN language switching
- Persistent light/dark theme
- Global search, module filters, bookmarks, and completion tracking
- Responsive desktop, tablet, and mobile layouts
- SEO metadata, sitemap, robots file, web manifest, 404 page, and social artwork
- Netlify headers, cache policy, and fallback configuration
- Automated statistical-core tests and local-link auditing

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

Every module contains 12 published lessons. Every lesson card resolves to an implemented page.

## Interactive labs

The browser-based labs cover summary statistics, weighted means, z-scores, quantiles, histograms, box plots and outliers, Pearson correlation, ordinary least-squares regression, normal/binomial/Poisson probabilities, confidence intervals, one- and two-sample t tests, chi-square independence, A/B proportions, the Central Limit Theorem, Monte Carlo estimation, moving averages, and sample-size planning.

Calculator inputs are processed locally. The statistical engine is implemented in `assets/js/stats-core.js`, with automated reference checks in `scripts/test_stats.mjs`.

## Local use

The site uses root-relative URLs, so serve it through a local web server rather than opening an HTML file directly.

```bash
npm run serve
```

Then open:

```text
http://localhost:8080
```

No package installation is required for the site itself.

## Quality checks

```bash
npm test
```

This runs:

```bash
npm run test:stats
npm run audit:links
```

Regenerate all static topic/tool routes and the sitemap after editing the curriculum source:

```bash
npm run generate
npm test
```

## Netlify deployment

The repository includes `netlify.toml` and does not require a build command.

1. Push this directory to the `main` branch of `statistics_learning_hub`.
2. In Netlify, choose **Add new site → Import an existing project**.
3. Select the GitHub repository.
4. Keep the base directory and build command empty.
5. The publish directory is already configured as `.` in `netlify.toml`.
6. Deploy the site.
7. Replace the placeholder production origin `https://statistics-learning-hub.netlify.app` if Netlify assigns another subdomain or a custom domain is connected.
8. Run `npm run generate` after changing that origin so canonical URLs, Open Graph URLs, `robots.txt`, and `sitemap.xml` remain correct.

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for the full checklist.

## Repository structure

```text
.
├── index.html
├── 404.html
├── about/
├── catalog/
├── glossary/
├── paths/
├── topics/                 # 108 generated lesson routes
├── tools/                  # 20 interactive labs + index
├── assets/
│   ├── css/main.css
│   ├── icons/
│   └── js/
├── scripts/
│   ├── generate.py
│   ├── topic_details.py
│   ├── audit_links.py
│   └── test_stats.mjs
├── docs/
├── manifest.webmanifest
├── robots.txt
├── sitemap.xml
├── netlify.toml
└── package.json
```

## Content and architecture

The curriculum catalog is maintained in the Python generator and exported to `assets/js/content.js`. The generated HTML pages are intentionally thin and reuse a shared design system and rendering logic. Do not hand-edit generated topic pages; update the source data and regenerate instead.

Read:

- [Architecture](docs/ARCHITECTURE.md)
- [Curriculum](docs/CURRICULUM.md)
- [Content standards](docs/CONTENT-STANDARDS.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)

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
