# Release Report — v2.7.0

## Title

Next.js Application and PWA Migration

## Production URL

https://datalearninghub.netlify.app/

## Delivered

- Next.js 16.2.10 App Router application
- pnpm 11.20.0 project configuration
- TypeScript source
- Static export for Netlify
- 549 preserved published routes
- Dynamic metadata and canonical URLs
- Generated robots and sitemap routes
- PWA manifest, icons, service worker, and offline fallback
- Preserved bilingual, theme, progress, exercise, lab, playground, and project behavior
- Migration, PWA, source, deployment, and continuation documentation

## Content retained

- Six complete tutorials
- 363 tutorial chapters
- 1,089 chapter exercises
- 108 statistics lessons
- 20 statistical labs
- Six complete portfolio projects
- SQL and Python browser practice
- Excel, Power BI, SQL, Python, datasets, notebooks, workbooks, and project downloads

## Validation completed in the build environment

- 549 route payloads migrated
- Every route has main content and metadata
- All local route scripts exist
- PWA files and icons exist
- Service-worker lifecycle and offline tokens validated
- TypeScript/TSX source parsed without syntax errors

## Validation boundary

The build environment did not have access to the public npm registry. Dependency installation, `pnpm-lock.yaml` generation, Next.js type checking, and the actual `next build` must be completed locally or on Netlify before tagging. Exact commands and release gates are documented.
