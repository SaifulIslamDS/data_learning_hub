# Architecture — v2.7.3

## Current runtime

Data Learning Hub uses Next.js 16 App Router with static export.

The v2.7 compatibility bridge still preserves the complete migrated learning runtime:

1. Next.js statically generates published routes.
2. `src/generated/routes.json` maps routes to migrated page payloads.
3. `LegacyPage` renders migrated HTML and loads the preserved browser modules.
4. `src/lib/tutorial-html.ts` normalizes tutorial HTML so legacy objective UI does not reappear.
5. Shared browser behavior remains in `public/assets/js/` until the native React shell migration.

No backend, API, authentication, or database is required.

## Engineering quality layer

v2.7.3 adds a release-quality system around the compatibility architecture:

- ESLint for active Next.js/TypeScript/test source
- Prettier for new quality/native files
- Vitest for unit tests
- React Testing Library for component tests
- Playwright for production-export browser tests
- axe for accessibility regression
- source/UI audits for migration invariants
- GitHub Actions CI

The formatting gate intentionally does not rewrite generated, legacy, content, or public runtime files. Formatting coverage should expand naturally as those areas move into native typed source.

## Browser test model

`pnpm build` creates the static `out/` export.

`scripts/serve-static.mjs` serves that exact export on port 4173.

Playwright therefore tests the production-style static output rather than only the development server.

## Language state

The active interface is English-only.

The Bangla toggle and its UI wiring are removed. Existing `data-bn` and migrated Bangla content can remain dormant until a future full-site localization release.

## Next architecture milestone

v2.8.0 moves the shared header, footer, navigation, search, theme, progress/bookmark state, and PWA UI into native React while preserving routes and compatible browser-local state.
