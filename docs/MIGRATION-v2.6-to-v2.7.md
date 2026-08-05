# Migration Guide — v2.6.0 to v2.7.0

## Migration result

- Static HTML generator release → Next.js App Router application
- npm-style static scripts → pnpm-managed application
- Static manifest → Next.js manifest metadata route
- Static deployment root → Netlify `out/` build output
- No route changes
- No localStorage key changes
- No content removal

## Preserved behavior

- English/Bangla switching
- Light/dark mode
- Sticky header
- Tutorial chapter navigation
- Exercises and quizzes
- Course and lesson progress
- Bookmarks
- Statistics labs
- SQL browser playground
- Python browser playground
- Power BI simulations
- Portfolio phase tracking
- Downloadable workbooks, datasets, scripts, and project packages

## Important first install action

The execution environment used to create the release did not allow access to the public npm registry. A bootstrap `pnpm-lock.yaml` is included so Netlify selects pnpm; the first successful install will populate the complete dependency graph.

On the first local setup:

```powershell
corepack enable
corepack prepare pnpm@11.20.0 --activate
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

Commit the generated `pnpm-lock.yaml` before the v2.7.0 release tag.

## Deployment change

Previous static release:

```text
Build command: empty
Publish directory: .
```

v2.7.0:

```text
Build command: pnpm build
Publish directory: out
```
