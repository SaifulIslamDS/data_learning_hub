# Changelog

## v2.7.3 — 2026-08-28

### Added

- GitHub Actions engineering quality gate
- ESLint with Next.js/TypeScript rules
- Prettier formatting gate
- Vitest unit-test runner
- React Testing Library test coverage
- Playwright Chromium smoke tests
- axe accessibility regression test
- Tutorial-first UI source audit
- Static export test server
- Unit tests for tutorial HTML normalization
- Browser regression for objective-card removal, theme behavior, and English-only UI

### Changed

- Removed remaining Bangla-toggle rendering/wiring from the active interface
- Extracted tutorial HTML normalization into a testable library function
- Expanded `pnpm check` to include lint, formatting, typecheck, audits, unit tests, and production build
- CI now runs browser/accessibility tests after the build

### Preserved

- Existing routes
- Tutorial content
- Exercises and quizzes
- SQL/Python browser practice
- Power BI simulations
- Statistics labs
- Projects
- Theme/progress/bookmark storage
- PWA/offline behavior
- Dormant legacy Bangla content fields for possible future full-site localization

## v2.7.2 — 2026-08-28

Tutorial-First Alignment.

## v2.7.1 — 2026-08-13

Documentation & Content Integrity Foundation.

## v2.7.0 — 2026-08-05

Next.js App Router compatibility migration preserving the complete v2.6 static release.
