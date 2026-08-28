# AGENTS.md

## Project

Data Learning Hub v2.7.3 is a Next.js 16 App Router PWA deployed to Netlify.

## Product rule

Data Learning Hub is tutorial first.

**Teach the subject immediately. Explain the learning system elsewhere.**

Do not add visible generic "What you will learn", "Start here", how-to-learn, motivational, or career-dashboard blocks to tutorial pages.

## Language

The active learner-facing interface is English-only.

Do not restore a Bangla toggle until the site is intentionally translated as a complete localization release. Legacy Bangla content fields may remain internally during migration.

## Engineering quality gate

Before merge/tag:

```powershell
pnpm install
pnpm check
pnpm exec playwright install chromium
pnpm test:e2e
```

CI must pass on `main` and pull requests.

## Workflow

- Use pnpm only.
- Preserve routes and production URL.
- Do not add backend/API/auth/database without explicit approval.
- Preserve theme, progress, bookmarks, exercises, quizzes, labs, playgrounds, projects, and PWA behavior.
- Keep new tests close to every regression fix or native component.
