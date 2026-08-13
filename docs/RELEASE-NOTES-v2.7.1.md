# Data Learning Hub — Release Notes v2.7.1

## Release name

**Documentation & Content Integrity Foundation**

## Status

Release candidate documentation patch.

Tag only after the repository patch is applied, validation passes, Netlify deployment is verified, and the intended version metadata is confirmed.

## Purpose

v2.7.1 does not expand the tutorial catalog.

It establishes the product, content, and documentation rules required before the next major engineering and content migration.

## Added

- `docs/README.md`
  - Documentation index
  - Documentation naming policy
  - Version-document rules

- `docs/PRODUCT-VISION.md`
  - Tutorial-first product identity
  - Data Analytics → Data Science → ML → Data Engineering → LLM/AI Engineering scope
  - Simple UI/UX principles
  - Practice-first learning-loop definition

- `docs/CONTENT-STANDARDS.md`
  - No dummy/placeholder content rule
  - Topic-specific worked-example standard
  - Real practice requirements
  - Dataset provenance rules
  - Assessment standards
  - Reference quality standards
  - Content-audit requirements

- Updated `docs/ROADMAP.md`
  - Replaces the previous short post-v2.7 roadmap
  - Adds staged v2.7.1 → v2.18 Data Analytics stabilization
  - Adds Data Science, ML, Data Engineering, LLM, and AI Engineering expansion stages

- `docs/PROJECT-CONTINUATION-v2.7.1.md`
  - Current project identity
  - Non-negotiable product rules
  - Immediate next-build priorities

## Changed

- Root `README.md`
  - Clarifies the complete long-term product vision
  - Links the documentation index and new standards
  - Keeps detailed documentation out of the repository root

## Preserved

This documentation foundation must not change or break:

- Existing published routes
- Current tutorial content
- Existing progress/localStorage data
- Existing PWA behavior
- SQL playground
- Python playground
- Power BI simulations
- Statistics labs
- Downloadable learning assets
- English/Bangla behavior
- Theme behavior

## Known architectural boundary

The application still uses the v2.7 compatibility renderer for migrated legacy HTML and runtime behavior.

This is intentional for the current release.

The roadmap moves shared UI/state to native React first, then the tutorial renderer and practical learning engine.

## Content-quality finding carried into the roadmap

Existing content requires a systematic audit for repeated/template worked examples and generic practical instructions.

A route count or exercise count must not be treated as proof of educational completeness.

The remediation standard is defined in `CONTENT-STANDARDS.md`.

## Validation before tagging

Run:

```powershell
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

Then verify on Netlify:

1. Homepage
2. Tutorial navigation
3. English/Bangla switching
4. Theme persistence
5. Progress persistence
6. SQL playground
7. Python playground
8. Representative Statistics lab
9. Representative Power BI simulation
10. Offline/PWA behavior

## Next release

**v2.7.2 — Engineering Quality Foundation**

Primary targets:

- GitHub Actions
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright
- Accessibility testing
- Automated release gates
