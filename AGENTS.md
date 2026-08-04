# AGENTS.md

## Product

Data Learning Hub is a static, English-first bilingual Data Analytics learning platform. The active career route is Data Analyst. Data Science and Data Engineering are future advanced routes.

## Source of truth

Read these before changing the product:

1. `docs/ARCHITECTURE.md`
2. `docs/CURRICULUM.md`
3. `docs/CONTENT-STANDARDS.md`
4. `docs/ROADMAP.md`
5. `docs/TESTING.md`

Curriculum and content metadata live under `content/`. Generated HTML and `assets/js/content.js` must not be edited as the primary source.

## Non-negotiable rules

- Keep the deployed product static: HTML, CSS, and Vanilla JavaScript.
- No backend, API, database, authentication, or server-side learner state.
- English is the default language; published learner content must include Bangla.
- Only implemented lessons, labs, and projects may have working content URLs.
- Curriculum-ready and roadmap items must be labeled honestly.
- Preserve stable lesson IDs and migrate browser storage deliberately.
- Use authoritative documentation for tool-specific behavior.
- Do not copy source code or educational prose from the inspiration repository.
- Keep synthetic datasets clearly labeled as synthetic.
- Never weaken statistical interpretation cautions merely to simplify copy.

## Development cycle on main

The project owner works directly on `main` and uses release tags as stable recovery points.

Before every commit:

```powershell
npm run generate
npm test
npm run test:browser
```

Do not tag a release until generated files, documentation, checks, and release notes agree.

## Release boundaries

- v2.0.0: architecture, product transformation, curriculum foundation
- v2.1.0: complete Excel track
- v2.2.0: complete SQL track
- v2.3.0: complete Power BI track
- v2.4.0: complete Python track
- v2.5.0: cross-tool projects and portfolio

Do not add shallow partial tracks to v2.0.0.
