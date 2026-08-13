# Data Learning Hub — Project Continuation v2.7.1

## Snapshot

- Target release: v2.7.1
- Release name: Documentation & Content Integrity Foundation
- Current production URL: https://datalearninghub.netlify.app/
- Framework baseline: Next.js 16.2.10 App Router
- React baseline: 19.2.4
- Package manager: pnpm 11.20.0
- Hosting: Netlify static export
- Backend/API/database: none in the current architecture
- Current architecture: Next.js compatibility bridge over the proven v2.6 learning runtime

## Product definition

Data Learning Hub is a specialized complete data learning platform.

Its intended learner experience is closer to a practical text tutorial system than to a conventional LMS.

The system should teach through:

```text
Concise text
→ real worked example
→ actual output
→ immediate practice
→ result checking
→ next concept
```

## Current stable domain

The current platform focuses on Data Analytics:

1. Data Foundations
2. Statistics
3. Excel
4. SQL
5. Power BI
6. Python
7. Analytics Workflows
8. Portfolio Projects

## Planned domain expansion

After the Data Analytics platform is fully stable and native:

1. Data Science
2. Machine Learning
3. Data Engineering
4. LLM Foundations
5. AI Engineering
6. Integrated Data + AI projects

Do not expand aggressively into these domains before the reusable learning engine is stable.

## Non-negotiable product rules

1. Very simple, user-friendly UI/UX
2. Tutorial-first, not dashboard-first
3. No mandatory onboarding before learning
4. No fake/dummy learning content
5. No repeated generic generated worked examples
6. No "how to learn" filler replacing actual subject teaching
7. Real worked examples must show real inputs/actions/results
8. Practice stays close to the lesson
9. Serious projects use traceable datasets
10. Browser simulations must be labeled honestly
11. Statistics is a first-class learning track
12. Every published topic must be independently useful
13. English/Bangla learning content must remain technically equivalent
14. Expansion must reuse the same learning engine rather than creating separate architectures

## Current engineering foundation

The v2.7 migration preserved the existing learning platform through a compatibility layer.

Important locations:

```text
app/                              Next.js routes and PWA metadata
src/components/legacy-page.tsx   Compatibility renderer
src/lib/                         Route/page loading
src/generated/                   Migrated route payloads
public/assets/                    CSS, JS, datasets, downloads, runtimes
content/tutorials/               Structured tutorial source
content/projects/                Project source
content/statistics/              Statistics source
scripts/                         Audits/migration utilities
docs/                            Documentation source of truth
```

## Important compatibility rule

Existing `dlh-*` localStorage keys and learner progress should be preserved during native migration unless an explicit storage migration is implemented.

## Key quality finding

The platform already has substantial content and practice infrastructure, but quantity must not be confused with content quality.

Some existing worked-example material follows repeated generic templates.

Before future domain expansion, current learning content must be audited against `CONTENT-STANDARDS.md`.

The target is not merely to have a page for every topic.

The target is for every topic to contain enough real explanation, example, result, and practice to teach the topic directly.

## Documentation rule from v2.7.1 onward

The root remains lean.

Detailed documentation belongs in `docs/`.

Required release documents:

```text
docs/RELEASE-NOTES-vX.Y.Z.md
```

When continuation context materially changes, add:

```text
docs/PROJECT-CONTINUATION-vX.Y.Z.md
```

The current roadmap always remains:

```text
docs/ROADMAP.md
```

Do not fork the roadmap into multiple "latest/final/new" copies.

## Immediate next work after v2.7.1

### v2.7.2 — Engineering Quality Foundation

Implement:

- GitHub Actions
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright
- axe accessibility checks
- Automated typecheck/audit/build/E2E release gate

### v2.8.0 — Native React Platform Shell

Implement:

- Header
- Footer
- Navigation
- Search shell
- Theme state
- Language state
- Progress/bookmarks state
- Preserve existing storage keys

### v2.8.5 — Typed Content Engine

Implement:

- Typed course/chapter schemas
- Chapter-level content files
- Validation
- Dataset registry
- Provenance metadata
- Duplicate-content detection

### v2.9.0+ — Native Tutorial & Practice Engine

Implement:

- Native lesson rendering
- Inline SQL
- Inline Python
- Statistics validators
- Exercises
- Actual-output components
- Common errors
- References
- Previous/next
- Native progress

## Release discipline

Do not tag a version because files were edited.

Before tagging:

```powershell
pnpm install
pnpm typecheck
pnpm test
pnpm build
```

Then verify the production deployment and PWA behavior.

## Files to read first in a future continuation

1. `README.md`
2. `docs/README.md`
3. `docs/PRODUCT-VISION.md`
4. `docs/CONTENT-STANDARDS.md`
5. `docs/ROADMAP.md`
6. Latest `docs/RELEASE-NOTES-vX.Y.Z.md`
7. Latest `docs/PROJECT-CONTINUATION-vX.Y.Z.md`
8. `docs/ARCHITECTURE.md`
9. `docs/TESTING.md`

These documents define both what the platform is and what it must not become.
