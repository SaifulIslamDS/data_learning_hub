# Data Learning Hub

**Version:** v2.7.1 — Documentation & Content Integrity Foundation  
**Production URL:** https://datalearninghub.netlify.app/  
**Package manager:** pnpm 11.20.0  
**Framework:** Next.js 16.2.10 App Router  
**Deployment:** Netlify static export

Data Learning Hub is a bilingual, tutorial-first practical data learning platform focused on real text tutorials, worked examples, hands-on practice, exercises, labs, and projects.

The current stable learning stack covers:

- Data Foundations
- Statistics
- Excel for Data Analytics
- SQL for Data Analytics
- Power BI for Data Analytics
- Python for Data Analytics
- Analytics Workflows
- Portfolio Projects

The long-term platform roadmap expands the same practical learning system into Data Science, Machine Learning, Data Engineering, LLMs, and AI Engineering.

## Product principle

Data Learning Hub should teach the subject directly.

The learning experience should be simple:

**Read → See a real example → Practice → Check → Continue**

The platform should avoid dummy content, generic generated examples, unnecessary onboarding, fake application experiences, and "how to learn" filler in the learner-facing experience.

## v2.7.1 focus

v2.7.1 establishes the documentation and content-quality foundation for the next stage of development.

This release:

- Formalizes `docs/` as the documentation source of truth
- Adds the long-term product vision
- Adds mandatory content and practice standards
- Replaces the short roadmap with the complete staged roadmap
- Adds a versioned v2.7.1 release note
- Adds a v2.7.1 project continuation document
- Preserves the current application architecture and published learning experience

No major learner-facing feature migration is introduced in this release.

## Current application foundation

The v2.7 architecture preserves the complete v2.6 static release through a Next.js App Router compatibility layer while retaining all 549 published routes and their existing URLs.

The current application remains an installable PWA with:

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

## Documentation

The root `README.md` is the main repository entry point.

All detailed project documentation belongs in [`docs/`](docs/).

Start here:

- [Documentation Index](docs/README.md)
- [Product Vision](docs/PRODUCT-VISION.md)
- [Content Standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Release Notes — v2.7.1](docs/RELEASE-NOTES-v2.7.1.md)
- [Project Continuation — v2.7.1](docs/PROJECT-CONTINUATION-v2.7.1.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Testing](docs/TESTING.md)
- [Deployment](docs/DEPLOYMENT.md)
- [PWA](docs/PWA.md)

## Netlify

Use the existing production site:

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

`netlify.toml` contains the current deployment and PWA/security configuration.

## Source architecture

```text
app/                        Next.js App Router, metadata, manifest, sitemap, offline page
src/components/             React migration bridge
src/lib/                    Server-side generated-page registry loader
src/generated/              Migrated route payloads
public/assets/               Design system, downloads, datasets, and runtime modules
public/sw.js                 PWA service worker
content/                     Structured tutorial/project/statistics source
scripts/legacy/              Preserved v2.6 generator and audits for reference
scripts/                     Migration, source, and PWA audits
docs/                        Project documentation and version records
```

## Maintenance rule

The current compatibility renderer is a controlled migration bridge. New development should gradually replace legacy page payloads and DOM scripts with native React components and structured content.

Before large Data Science, Machine Learning, Data Engineering, LLM, or AI Engineering expansion, the Data Analytics platform should first complete:

1. Content integrity remediation
2. Engineering quality automation
3. Native React platform shell
4. Typed content engine
5. Native tutorial renderer
6. Inline practical exercise engine
7. Real dataset registry and provenance system
8. Native Statistics, Excel, Power BI, SQL, Python, and project learning loops

See [ROADMAP.md](docs/ROADMAP.md) for the complete sequence.

## Release workflow

A release tag should be created only after local validation, production deployment, and PWA verification pass.
