# Testing — v2.7.0

## Pre-install audits

```powershell
python scripts/audit-migration.py
node scripts/audit-pwa.mjs
node scripts/audit-source.mjs
```

These can run before installing Next.js dependencies.

## Full application verification

```powershell
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

## Required browser regression

- Homepage and sticky header
- EN/BN switch
- Theme switch
- Tutorial course and chapter
- Chapter completion and exercise feedback
- SQL playground query
- Python playground output and chart
- Power BI simulation
- Statistical lab calculation and chart
- Portfolio phase progress
- Search
- Mobile chapter drawer
- PWA install and offline fallback

## Release gate

Do not tag v2.7.0 until:

- `pnpm-lock.yaml` is committed
- `pnpm check` passes
- Netlify production deploy passes
- Service worker is activated
- Manifest and icons are valid
- A visited tutorial page opens offline
- SQL and Python playgrounds run online
