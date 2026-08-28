# Data Learning Hub

**Version:** v2.7.2 — Tutorial-First Alignment  
**Production URL:** https://datalearninghub.netlify.app/  
**Framework:** Next.js 16.2.10 App Router  
**Deployment:** Netlify static export

Data Learning Hub is an English-first, tutorial-first practical data learning platform.

> **Teach first. Explain the learning system elsewhere.**

A learner should be able to search for a topic, open the page, and begin learning immediately:

**Explain → Example → Result → Practice → Check → Exercises → Continue**

Tutorial pages should not be padded with generic "What you will learn", "Start here", how-to-learn, motivational, or career-dashboard sections.

Career paths, projects, assessments, and portfolio support are built around the tutorial library rather than replacing it.

## Current learning stack

- Data Foundations
- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows
- Portfolio Projects

## v2.7.2

- removes the visible objective card and Objectives jump item
- makes the active interface English-only
- adds the Tutorial Page Standard
- locks the product/content roadmap around direct subject teaching
- preserves routes, practice, projects, progress, and PWA behavior
- fixes PWA version-audit drift

## Validation

```powershell
pnpm install
pnpm check
```

## Documentation

- [Product Vision](docs/PRODUCT-VISION.md)
- [Tutorial Page Standard](docs/TUTORIAL-PAGE-STANDARD.md)
- [Content Standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Release Notes v2.7.2](docs/RELEASE-NOTES-v2.7.2.md)
- [Project Continuation v2.7.2](docs/PROJECT-CONTINUATION-v2.7.2.md)
