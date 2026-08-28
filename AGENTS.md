# AGENTS.md

## Project

Data Learning Hub v2.7.2 is a Next.js 16 App Router PWA deployed to Netlify.

## Product rule

Data Learning Hub is tutorial first.

**Teach the subject immediately. Explain the learning system elsewhere.**

Do not add visible generic "What you will learn", "Start here", how-to-learn, motivational, or career-dashboard blocks to tutorial pages.

Learning objectives may exist as internal metadata.

## Language

The active learner-facing interface is English-only for now.

## Workflow

- Work directly on main unless explicitly changed.
- Use pnpm only.
- Preserve routes and production URL.
- Do not add backend/API/auth/database without explicit approval.
- Preserve theme, progress, bookmarks, exercises, quizzes, labs, playgrounds, projects, and PWA behavior.

## Validation

```powershell
pnpm typecheck
pnpm test
pnpm build
```
