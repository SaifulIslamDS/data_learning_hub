# Data Learning Hub — Release Notes v2.7.3

## Release name

**Engineering Quality Foundation**

## Purpose

Add automated engineering controls before the native React refactor.

## Added

- GitHub Actions CI
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright
- axe accessibility checks
- production-export static test server
- tutorial-first UI audit
- browser regression tests

## Tutorial-first regression protection

Automated checks now guard against:

- reintroduction of `START HERE / What you will learn`
- reintroduction of the Objectives jump link
- reintroduction of the Bangla toggle before full-site localization
- broken representative tutorial rendering

## Language adjustment

The active learner-facing interface remains English-only.

The Bangla toggle is removed, not merely visually hidden. Legacy Bangla content fields remain dormant so localization can be reconsidered later as a complete-site initiative.

## Next release

**v2.8.0 — Native React Platform Shell**
