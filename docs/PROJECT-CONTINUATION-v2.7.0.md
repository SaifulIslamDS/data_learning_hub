# Data Learning Hub — Project Continuation Document

## Snapshot

- **Current release:** v2.7.0
- **Release name:** Next.js Application and PWA Migration
- **Production URL:** https://datalearninghub.netlify.app/
- **Repository workflow:** Direct development on `main`
- **Package manager:** pnpm 11.20.0
- **Framework:** Next.js 16.2.10 App Router
- **React:** 19.2.4
- **Node:** 22 recommended; 20.9 minimum
- **Hosting:** Netlify
- **Deployment output:** Static export in `out/`
- **Backend/API/database:** None

## Product purpose

Data Learning Hub is a bilingual, tutorial-first platform designed to teach Data Analytics from beginner through portfolio implementation. It covers:

1. Data Foundations
2. Statistics
3. Excel for Data Analytics
4. SQL for Data Analytics
5. Power BI for Data Analytics
6. Python for Data Analytics
7. End-to-end Analytics Workflows
8. Portfolio Projects

Future major paths are Data Science and Data Engineering.

## Current published inventory

- 6 complete tutorials
- 363 tutorial chapters
- 1,089 chapter exercises
- 108 comprehensive statistics lessons
- 20 statistical calculator/simulation labs
- 6 complete portfolio projects
- 549 migrated application routes
- Bilingual English/Bangla interface
- Sticky site header
- Dark/light mode
- Browser-local progress and bookmarks
- SQL browser playground
- Python/Pyodide browser playground
- Power BI browser simulations
- Downloadable datasets, workbooks, SQL scripts, Python notebooks, and project packages

## v2.7.0 architectural decision

The complete v2.6.0 site was migrated safely through a **Next.js compatibility content registry** rather than rewriting hundreds of pages and interactive tools simultaneously.

### How it works

- `app/[...slug]/page.tsx` generates all migrated URLs.
- `src/generated/routes.json` is the route manifest.
- `src/generated/pages/*.json` stores each route’s metadata, `<main>` content, body attributes, and required browser scripts.
- `src/components/legacy-page.tsx` renders the migrated content through React and loads the proven v2.6 runtime modules.
- `public/assets/` contains the complete design system, scripts, datasets, workbooks, notebooks, and downloads.
- `content/` preserves structured source content.

This is a migration bridge. New development should increasingly use native React components and structured content directly.

## PWA implementation

- Next.js manifest route: `app/manifest.ts`
- Service worker: `public/sw.js`
- Offline page: `app/offline/page.tsx`
- Icons: `public/icons/`
- Service worker registration: `app/layout.tsx`
- Netlify PWA headers: `netlify.toml`

Core visited content is cached. SQL and Python browser engines require an online first load and depend on external pinned CDN resources.

## Important localStorage compatibility

Do not rename or delete the existing keys without a migration:

```text
dlh-language
dlh-theme
dlh-completed
dlh-bookmarks
dlh-last-topic
dlh-profile
dlh-storage-version
```

Tutorial, quiz, and portfolio scripts also use course/project-specific `dlh-*` keys. Preserve them during native React migration.

## Essential source locations

```text
app/                              Next.js routes and PWA metadata
src/components/legacy-page.tsx    compatibility page renderer
src/lib/page-data.ts              route and payload loader
src/generated/routes.json         URL registry
src/generated/pages/              migrated page payloads
public/assets/css/main.css         current design system
public/assets/js/                  current runtime modules
public/sw.js                       PWA caching
content/tutorials/                 tutorial source JSON
content/projects/                  portfolio project source
content/statistics/                statistics source
scripts/legacy/                    v2.6 generator/audits reference
scripts/audit-migration.py         Next migration audit
scripts/audit-pwa.mjs              PWA audit
scripts/audit-source.mjs           source syntax audit
netlify.toml                       production deployment settings
```

## First local setup after receiving v2.7.0

The artifact-generation environment could not access the public npm registry. A bootstrap lockfile is included. On the first real setup:

```powershell
corepack enable
corepack prepare pnpm@11.20.0 --activate
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

Commit the fully populated `pnpm-lock.yaml` before tagging v2.7.0.

## Netlify configuration

```text
Build command:     pnpm build
Publish directory: out
Production branch: main
Node version:      22
pnpm version:      11.20.0
```

The current production URL must remain:

```text
https://datalearninghub.netlify.app/
```

## Mandatory pre-tag production checks

1. Homepage renders with sticky header.
2. English/Bangla switching works.
3. Dark/light mode works and persists.
4. Tutorial chapter, exercise, and final quiz work.
5. SQL playground executes a query.
6. Python playground executes Python and pandas code.
7. A statistical lab calculates and displays its chart.
8. Portfolio phase completion persists.
9. Manifest and icons are valid.
10. Service worker activates.
11. A visited page loads offline.
12. No console errors on representative routes.

## Git workflow

The user prefers direct work on `main`.

```powershell
git checkout main
git pull origin main
pnpm check
git add -A
git commit -m "feat: migrate Data Learning Hub to Next.js PWA"
git push origin main
```

After production verification:

```powershell
git tag -a v2.7.0 -m "Data Learning Hub v2.7.0 — Next.js Application and PWA"
git push origin v2.7.0
```

## Known limitations / technical debt

- Most migrated pages are rendered through the compatibility HTML payload bridge.
- Header/footer/search and page interactions still use the proven v2.6 DOM modules.
- Internal anchors perform normal page navigation rather than Next.js client navigation.
- The bootstrap lockfile must be refreshed and committed after the first real `pnpm install`.
- SQL and Python runtimes rely on external CDN packages.
- Offline mode caches visited content rather than pre-caching all 549 pages.

These are intentional release boundaries, not hidden defects.

## Recommended next milestone

### v2.8.0 — Native React Shell and Learning State

Build:

- Native React header, footer, mobile menu, search, language toggle, and theme toggle
- Shared React state for profile, progress, bookmarks, and completion
- PWA install prompt and update-available notification
- Preserve all current URLs and localStorage values
- Keep the compatibility page renderer for course content during this milestone

After v2.8.0, port the tutorial renderer and assessment system natively in v2.9.0.

## Instruction for a new chat

Upload:

1. The current repository ZIP or GitHub repository link
2. This continuation document

Then request:

> Continue Data Learning Hub from v2.7.0. Read the continuation document and current repository first. Work directly on `main`. Begin v2.8.0 — Native React Shell and Learning State, preserving all routes, data, progress keys, PWA behavior, and Netlify deployment.
