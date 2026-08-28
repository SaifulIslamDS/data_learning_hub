# Data Learning Hub — Locked Product & Engineering Roadmap

## North star

Data Learning Hub remains **tutorial first**.

The platform should feel closer to W3Schools than to a conventional LMS: a learner searches for a topic, lands directly on that topic, learns the concept, sees a real example, practices it, checks the result, and continues.

> **Teach first. Explain the learning system elsewhere.**

Career paths, projects, assessments, progress, and portfolio support will be built **around** the tutorial library. They must not turn individual tutorial pages into dashboard-heavy LMS screens.

```text
Direct tutorial standard
        ↓
Engineering quality
        ↓
Native tutorial platform
        ↓
Practical exercise engine
        ↓
Deep Data Analytics content
        ↓
Projects and assessments
        ↓
Career-path layer
        ↓
Data Engineering
        ↓
Data Science / ML
        ↓
LLM / AI Engineering
```

## v2.7.2 — Tutorial-First Alignment

### Goal

Lock the clarified product direction into the current application, source-generation rules, and project documentation.

### Deliverables

- Remove the visible **START HERE / What you will learn** objective card from tutorial chapters.
- Remove the **Objectives** jump-link item.
- Keep objectives only as internal authoring/curriculum metadata.
- Keep the learner-facing product **English-only for now**.
- Hide the EN/BN language switch while preserving migrated Bangla fields internally.
- Add a canonical Tutorial Page Standard.
- Rewrite product/content rules around **teach first**.
- Preserve all current routes, exercises, quizzes, projects, progress keys, browser practice, theme, and PWA behavior.
- Fix PWA version drift by deriving the audit expectation from `package.json`.

### Release gate

- Tutorial chapters enter subject teaching directly.
- No visible generic objective card remains.
- No Objectives jump-link remains.
- Header is English-only.
- Existing tutorial interactions continue to work.
- `pnpm check` passes.
- Production deploy and offline/PWA verification pass.

---

## v2.7.3 — Engineering Quality Foundation

Add:

- GitHub Actions CI
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright smoke tests
- axe accessibility checks
- automated typecheck/audit/build/E2E release gates

Regression coverage must explicitly confirm that the generic tutorial-objective card does not return.

---

## v2.8.0 — Native React Platform Shell

Move shared shell behavior out of the legacy DOM runtime:

- header/footer
- global navigation
- search
- theme
- progress/bookmarks
- PWA install/update UI

Keep the active interface English-only and tutorial-first.

---

## v2.8.5 — Typed Content Engine

Introduce:

- typed course/topic schemas
- typed example schema
- typed practice/exercise schema
- chapter-level content files
- build-time validation
- dataset registry
- dataset provenance
- duplicate-content detection
- broken-link/download/reference validation

Learning objectives remain optional internal metadata rather than a required visible page block.

---

## v2.9.0 — Native Tutorial Renderer

Render tutorials natively through React with:

- direct explanation
- syntax/formula/code
- inputs/outputs
- real worked examples
- common mistakes
- practice hooks
- exercises
- summaries
- authoritative references
- previous/next navigation

No generic learner-objective card.

---

## v2.9.5 — Practical Exercise Engine

### SQL
- inline editor
- query execution
- result display
- answer/result validation

### Python
- inline execution
- hidden tests
- DataFrame/result checks

### Statistics
- numeric validators
- tolerance checks
- interpretation tasks

### Excel / Power BI
- real downloadable practice packages
- expected-result checks
- honest browser simulations only where useful

---

## v2.10.0 — Data Analytics Content Integrity Rebuild

Audit:

- Data Foundations
- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows

Replace repeated templates with topic-specific explanation, real inputs/actions/results, stronger practice, better exercises, useful references, and no meta-learning filler.

---

## v2.10.5 — Real Dataset & Provenance System

Create a shared dataset registry with:

- source
- license/terms
- snapshot date
- data dictionary
- raw/cleaned versions
- known limitations
- expected practice results

---

## v2.11.0 — Complete Data Analytics Tutorial Core

Polish the complete tutorial-first experience across:

1. Data Foundations
2. Statistics
3. Excel
4. SQL
5. Power BI
6. Python
7. Analytics Workflows

Quality and reproducibility take priority over maximum chapter count.

---

## v2.12.0 — Labs & Assessment Layer

Add:

- executable SQL tasks
- Python tests
- statistics validators
- Excel practice packages
- Power BI model/DAX challenges
- analytical reasoning tasks

Assessments support the tutorial library without cluttering the reading flow.

---

## v2.13.0 — Progressive Project System

Connect tutorial skills through cross-tool projects using shared traceable datasets and portfolio-ready artifacts.

---

## v2.14.0 — Data Analyst / BI Analyst Career Layer

Add:

- optional diagnostics
- role competency maps
- recommended tutorial sequence
- project requirements
- portfolio guidance
- interview/case preparation
- quiet career-progress view

Career paths point into tutorials. They do not replace them.

---

## v2.15.0 — Data Engineering Tutorial Expansion

Expand the same tutorial engine into:

- advanced SQL
- databases and data modeling
- ETL/ELT
- warehouses/lakehouses
- dbt
- orchestration
- Spark
- streaming
- data quality/governance
- cloud data platforms

---

## v2.16.0 — Data Science & Machine Learning Expansion

Add mathematics, advanced statistics, NumPy/pandas/SciPy, EDA, experimentation, feature engineering, regression, classification, clustering, model evaluation, and applied projects.

---

## v2.17.0 — LLM & AI Engineering Expansion

Add LLM fundamentals, APIs, structured outputs, embeddings, vector search, RAG, tool calling, agents, evaluation, guardrails, observability, performance/cost, and production AI projects.

## Non-negotiable rules

1. Tutorial first.
2. Teach the subject immediately.
3. No visible generic **What you will learn** card on tutorial pages.
4. No mandatory onboarding before learning.
5. No dummy/template learning content presented as complete.
6. Real examples show real inputs/actions/results.
7. Practice stays close to the lesson.
8. Career features live around tutorials, not inside the core teaching flow.
9. Serious projects use traceable datasets.
10. Simulations are labeled honestly.
11. Search and standalone topic usefulness are core.
12. English is the active learner-facing language for now.
13. Expansion reuses the same tutorial engine.
