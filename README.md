# Data Learning Hub

**Version:** v2.7.3 — Engineering Quality Foundation  
**Production URL:** https://datalearninghub.netlify.app/  
**Framework:** Next.js 16.2.10 App Router  
**Deployment:** Netlify static export

Data Learning Hub is an English-first, tutorial-first practical data learning platform.

> **Teach first. Explain the learning system elsewhere.**

The current learner loop remains:

**Explain → Example → Result → Practice → Check → Exercises → Continue**

## v2.7.3

v2.7.3 adds the engineering quality foundation required before the native React migration:

- GitHub Actions CI
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright
- axe accessibility checks
- tutorial-first UI regression audit
- automated lint → format → typecheck → audit → unit test → build → E2E release gate

The Bangla toggle is removed from the active interface for now. Legacy Bangla content fields may remain internally until the entire site is ready for a deliberate translation/localization phase.

## Quality commands

```powershell
pnpm install
pnpm lint
pnpm format:check
pnpm typecheck
pnpm test
pnpm build
```

Complete local quality gate:

```powershell
pnpm check
```

Browser tests require Chromium:

```powershell
pnpm exec playwright install chromium
pnpm test:e2e
```

## Current learning stack

- Data Foundations
- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows
- Portfolio Projects

## Documentation

- [Product Vision](docs/PRODUCT-VISION.md)
- [Tutorial Page Standard](docs/TUTORIAL-PAGE-STANDARD.md)
- [Content Standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Testing](docs/TESTING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Release Notes v2.7.3](docs/RELEASE-NOTES-v2.7.3.md)
- [Project Continuation v2.7.3](docs/PROJECT-CONTINUATION-v2.7.3.md)
