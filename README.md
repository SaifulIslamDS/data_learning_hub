# Data Learning Hub

**Version:** v2.7.0 — Next.js Application and PWA Migration  
**Production URL:** https://datalearninghub.netlify.app/  
**Package manager:** pnpm 11.20.0  
**Framework:** Next.js 16.2.10 App Router  
**Deployment:** Netlify static export

Data Learning Hub is a bilingual, tutorial-first Data Analytics learning platform. It includes complete Data Foundations, Excel, SQL, Power BI, Python, Analytics Workflows, Statistics lessons/labs, and six portfolio projects.

## v2.7.0 transformation

The complete v2.6.0 static release has been migrated into a Next.js App Router application while preserving all 549 published routes and their existing URLs. The application uses a compatibility content registry: Next.js generates every route, and the proven v2.6 interactive JavaScript modules continue to power language switching, progress, exercises, SQL/Python playgrounds, labs, and project tracking.

The application is also an installable PWA with:

- App manifest and install metadata
- 192px, 512px, maskable, and Apple icons
- Versioned service worker
- Offline fallback route
- Runtime caching for visited pages and local assets
- Standalone display mode and mobile safe-area support

> Core tutorial content works offline after it has been visited. SQL and Python runtime packages may require an online first load because they are loaded from pinned external CDNs.

## Requirements

- Node.js 20.9 or later (Node 22 recommended)
- pnpm 11.20.0 or later

## Local development

```powershell
corepack enable
corepack prepare pnpm@11.20.0 --activate
pnpm install
pnpm dev
```

Open `http://localhost:3000`.

## Validation

```powershell
pnpm typecheck
pnpm test
pnpm build
```

The migration audit validates 549 routes, all generated page payloads, local scripts, PWA files, and Netlify configuration.

## Netlify

Use the existing site and URL:

```text
https://datalearninghub.netlify.app/
```

Netlify settings:

```text
Build command:     pnpm build
Publish directory: out
Production branch: main
Node version:      22
pnpm version:      11.20.0
```

`netlify.toml` already contains these settings and PWA/security headers.

## Source architecture

```text
app/                        Next.js App Router, metadata, manifest, sitemap, offline page
src/components/             React migration bridge
src/lib/                    Server-side generated-page registry loader
src/generated/              549 route payloads migrated from v2.6.0
public/assets/               Existing design system, downloads, datasets, and runtime modules
public/sw.js                 PWA service worker
content/                     Preserved structured tutorial/project/statistics source
scripts/legacy/              Preserved v2.6 generator and audits for reference
scripts/                     v2.7 migration, source, and PWA audits
docs/                        Architecture, deployment, testing, migration, continuation
```

## Maintenance rule

v2.7.0 is a controlled framework migration. The current compatibility renderer intentionally preserves proven v2.6 behavior. Future releases should gradually replace legacy page payloads and DOM scripts with native React Server and Client Components, beginning with the shared header, footer, tutorial chapter renderer, and progress store.

## Main-branch workflow

The project continues directly on `main`. Create a release tag only after Netlify deploy and PWA verification pass.

See [PROJECT-CONTINUATION-v2.7.0.md](docs/PROJECT-CONTINUATION-v2.7.0.md) for the complete continuation context.
