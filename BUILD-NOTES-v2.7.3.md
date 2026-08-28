# v2.7.3 — Build & Apply Notes

## What this bundle does

This is the **Engineering Quality Foundation** release.

It adds:

- GitHub Actions
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright
- axe accessibility checks
- source/UI regression audits
- production static-export browser testing

It also removes the Bangla toggle code from the active UI. Existing Bangla content fields remain dormant and can be revisited only when the entire site is ready for translation.

## Apply

Extract this ZIP directly into the repository root, allowing new files to be added and the included small documentation/config files to replace their previous versions.

Then run:

```powershell
python apply_v273.py
pnpm install
pnpm format
pnpm check
```

`pnpm install` is important because v2.7.3 adds dev dependencies and must refresh `pnpm-lock.yaml`.

Install Playwright Chromium:

```powershell
pnpm exec playwright install chromium
```

Then:

```powershell
pnpm test:e2e
```

## Expected release checks

- No `START HERE / What you will learn` tutorial card
- No `Objectives` tutorial jump link
- No Bangla toggle
- Theme switching works
- Representative tutorial opens
- Offline page renders
- ESLint passes
- Prettier passes
- TypeScript passes
- audits pass
- unit tests pass
- production build passes
- Playwright/axe passes

## Commit/tag

Only after all validation:

```powershell
git status
git add .
git commit -m "release: v2.7.3 engineering quality foundation"
git push origin main

git tag -a v2.7.3 -m "Data Learning Hub v2.7.3 — Engineering Quality Foundation"
git push origin v2.7.3
```
