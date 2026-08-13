# Data Learning Hub — Product & Engineering Roadmap

## Roadmap principle

The platform will not expand aggressively into Data Science, Machine Learning, Data Engineering, LLMs, or AI Engineering until the Data Analytics learning engine is stable, native, practical, and content-quality controlled.

The sequence is:

```text
Build the learning engine
        ↓
Perfect the Data Analytics stack
        ↓
Freeze the content/UX standard
        ↓
Scale into Data Science and ML
        ↓
Expand into Data Engineering
        ↓
Expand into LLM and AI Engineering
        ↓
Integrate cross-track projects
```

## v2.7.1 — Documentation & Content Integrity Foundation

### Goal

Create a single documentation source of truth and lock the product/content standards before the next architectural migration.

### Deliverables

- Formalize `docs/` as the detailed documentation home
- Add `PRODUCT-VISION.md`
- Add `CONTENT-STANDARDS.md`
- Replace the short roadmap with this full roadmap
- Add versioned release notes
- Add v2.7.1 continuation context
- Audit and list duplicated/template learning patterns
- Define the content-integrity remediation rules

### Release gate

- Documentation links valid
- No conflicting roadmap
- Product vision and content standards approved
- Current app behavior preserved

---

## v2.7.2 — Engineering Quality Foundation

### Goal

Add automated engineering quality gates before large refactoring.

### Deliverables

- GitHub Actions CI
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright smoke tests
- Accessibility checks with axe
- Automated checks on push/pull request
- Build, typecheck, audit, and smoke-test pipeline

### Initial E2E coverage

- Homepage
- Tutorial index
- Representative tutorial chapter
- Language persistence
- Theme persistence
- Completion persistence
- Exercise validation
- Search
- SQL execution
- Python execution
- Offline route
- Representative generated URLs

### Release gate

CI must pass before merge/tag.

---

## v2.8.0 — Native React Platform Shell

### Goal

Remove the shared UI shell from the legacy DOM runtime.

### Deliverables

- Native React header
- Native React footer
- Native global navigation
- Native search shell
- Native language state
- Native theme state
- Native progress/bookmark store
- Preserve current localStorage keys
- PWA install/update UI
- Remove shared DOM-generated shell code where safely replaced

### UX rule

No dashboard-heavy redesign. Preserve a simple tutorial-first interface.

### Release gate

Core navigation/state works without legacy shared-shell scripts.

---

## v2.8.5 — Typed Content Engine

### Goal

Prepare the content architecture for thousands of future learning pages.

### Deliverables

- Typed course schema
- Typed chapter schema
- Typed example schema
- Typed exercise/practice schema
- Course manifests
- Chapter-level files instead of monolithic course files where practical
- Schema validation during build
- Dataset registry
- Dataset provenance metadata
- Content duplication detection
- Broken-link/download/reference validation

### Target structure

```text
content/
  data-analytics/
    statistics/
    excel/
    sql/
    power-bi/
    python/
  datasets/
  projects/
```

### Release gate

A new chapter can be added without application-code changes.

---

## v2.9.0 — Native Tutorial Renderer

### Goal

Render structured tutorial content directly through native React.

### Deliverables

- Native chapter renderer
- Explanation blocks
- Syntax/code/formula blocks
- Worked-example blocks
- Actual output/result blocks
- Common-error blocks
- Exercise components
- Reference blocks
- Previous/next navigation
- Native progress handling
- Native bookmarks
- Bilingual rendering
- Remove tutorial-specific legacy HTML payloads where migrated

### Release gate

At least one complete tutorial runs entirely through the native renderer.

---

## v2.9.5 — Practical Exercise Engine

### Goal

Move practice directly inside the learning chapter.

### Deliverables

#### SQL
- Inline SQL editor
- Run query
- Result display
- Answer/result validation
- Equivalent-valid-solution handling where possible

#### Python
- Inline execution
- Hidden tests
- DataFrame/result checks
- Clear execution errors

#### Statistics
- Numeric validators
- Tolerance-based checking
- Interpretation exercises

#### Shared
- Reusable practice component contract
- Attempt/reset/check states
- Accessible keyboard behavior
- Mobile-friendly practice layout

### Release gate

Practical exercises work inside native lessons.

---

## v2.10.0 — Data Analytics Content Integrity Rebuild

### Goal

Replace generic/template content with topic-specific practical teaching.

### Scope

- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows

### Deliverables

- Audit all chapters
- Remove generic repeated worked-example templates
- Add actual inputs
- Add actual code/formulas/actions
- Add actual outputs
- Add explanations tied to the output
- Add immediate practice
- Improve exercises
- Verify references
- Verify EN/BN parity

### Release gate

No known repeated generic worked-example pattern across unrelated chapters.

---

## v2.10.5 — Real Dataset & Provenance System

### Goal

Make serious practical work traceable and credible.

### Deliverables

- Shared dataset registry
- Dataset manifest schema
- Publisher/source
- Source URL
- License/terms
- Snapshot date
- Data dictionary
- Known limitations
- Raw and cleaned versions where appropriate
- Expected results for practice validation
- Cross-course dataset reuse

### Release gate

Every serious project dataset has documented provenance.

---

## v2.11.0 — Statistics as a First-Class Tutorial

### Goal

Unify Statistics with the main tutorial architecture.

### Deliverables

- Migrate Statistics into native tutorial navigation
- Integrate the 108 lessons into the chapter system
- Integrate the 20 labs
- Inline calculation practice
- Real examples and interpretation
- Cross-links to Excel/Python/Power BI statistical functions

### Release gate

Statistics behaves like a primary tutorial, not a separate subsystem.

---

## v2.12.0 — Excel Practical Learning System

### Goal

Provide honest, reproducible Excel practice.

### Deliverables

- Formula micro-practice
- Table/filter/sort practice
- Cleaning exercises
- PivotTable tasks
- Chart tasks
- Real starter workbooks
- Completed reference workbooks
- CSV practice datasets
- Expected-result documentation
- Data dictionaries

### Release gate

A learner can complete a full practical Excel loop using real downloadable workbooks.

---

## v2.13.0 — Power BI Practical Learning System

### Goal

Provide practical Power BI learning without pretending the browser is Power BI.

### Deliverables

- Data model exercises
- Relationship exercises
- Power Query exercises
- DAX challenges
- KPI/result checking
- Honest browser micro-simulations
- Real downloadable datasets
- PBIX/PBIT assets where licensing/distribution allows
- Project specifications and expected results

### Release gate

Browser simulation and real Power BI practice are clearly separated.

---

## v2.14.0 — Projects 2.0

### Goal

Turn projects into credible portfolio-grade analysis.

### Deliverables

- Replace or clearly label synthetic cases
- Add public/licensed real datasets
- Dataset provenance
- Business/data question
- Cleaning
- Analysis
- Validation
- Visualization/reporting
- Deliverable specification
- Completed reference result
- Cross-tool projects

### Release gate

At least five strong source-backed practical projects.

---

## v2.15.0 — Search & Reference Engine

### Goal

Make the growing platform easy to navigate.

### Deliverables

- Fast cross-course search
- Topic synonyms
- Technology-aware results
- Quick references
- Glossary
- Function/formula reference pages
- Related-concept links
- Cross-track concept mapping

### Example

Searching `standard deviation` can connect:

- Statistics
- Excel
- Python
- Power BI
- ML preprocessing
- Reference pages

### Release gate

Search finds concepts across the complete Data Analytics catalog.

---

## v2.16.0 — Accessibility, Mobile & PWA Hardening

### Goal

Make the learning system robust across devices and access needs.

### Deliverables

- WCAG-oriented accessibility audit
- Keyboard navigation
- Focus management
- Screen-reader labels
- Code/editor accessibility
- Responsive tables
- Responsive result grids
- Mobile chapter navigation
- Mobile practice layout
- Offline tutorial verification
- PWA update behavior
- Performance review

### Release gate

Accessibility, mobile, and PWA production checks pass.

---

## v2.17.0 — Data Analytics Release Candidate

### Goal

Freeze features and verify the complete platform.

### Deliverables

- Full E2E regression
- Full content audit
- Reference audit
- Download audit
- Dataset provenance audit
- EN/BN parity review
- Browser/device testing
- Search testing
- PWA/offline testing
- Security review
- Performance review

### Release gate

No P0/P1 release blockers.

---

## v2.18.0 — Stable Data Analytics Platform

### Goal

Declare the Data Analytics stack ready for long-term expansion.

### Stable scope

- Data Foundations
- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows
- Practical Projects
- Search
- References
- Inline practice
- Real datasets
- Native React learning engine

### Release gate

The platform can accept a new technical domain without redesigning the learning engine.

---

# Major Expansion

## v3.0.0 — Data Science Foundations

- Mathematics for Data Science
- Advanced Statistics
- NumPy
- pandas
- SciPy
- Visualization
- EDA
- Experimentation
- Practical Data Science projects

## v3.5.0 — Machine Learning

- Preprocessing
- Feature engineering
- Regression
- Classification
- Clustering
- Model evaluation
- scikit-learn
- Applied ML projects

## v4.0.0 — Data Engineering

- Advanced SQL
- Database design
- Data modeling
- ETL / ELT
- Warehouses
- Lakehouses
- dbt
- Orchestration
- Spark
- Streaming
- Data quality
- Governance
- Cloud data systems

## v5.0.0 — LLM Foundations

- Transformer/LLM concepts
- Tokenization
- Embeddings
- Inference
- LLM APIs
- Prompt engineering
- Structured outputs
- Practical LLM exercises

## v5.5.0 — AI Engineering

- Vector search
- RAG
- Tool calling
- Agents
- Evaluation
- Guardrails
- Observability
- Cost/performance
- Production AI projects

## v6.0.0 — Integrated Data + AI Platform

- Cross-track projects
- SQL + Python + BI + ML + LLM systems
- End-to-end data products
- AI-powered analytics systems
- Data/AI engineering reference system

# Non-negotiable sequencing rule

Do not use new-topic expansion to hide unfinished platform foundations.

The Data Analytics stack must establish the reusable learning standard first. Future domains should inherit that standard rather than create a second learning architecture.
