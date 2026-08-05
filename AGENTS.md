# AGENTS.md

## Project

Data Learning Hub v2.7.0 is a Next.js 16 App Router PWA deployed to Netlify.

## Workflow

- Work directly on `main` unless the user explicitly changes the policy.
- Use pnpm only.
- Preserve all routes and current production URL.
- Do not add a backend, API, authentication, or database without explicit approval.
- Preserve EN/BN, theme, progress, bookmarks, exercises, quizzes, labs, playgrounds, projects, and PWA behavior.

## Before changing architecture

Read:

1. `docs/PROJECT-CONTINUATION-v2.7.0.md`
2. `docs/ARCHITECTURE.md`
3. `docs/TESTING.md`
4. `docs/ROADMAP.md`
5. `README.md`

## Validation

```powershell
pnpm typecheck
pnpm test
pnpm build
```

Run browser and PWA checks before a release tag.
