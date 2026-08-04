# Content and Accuracy Standards

## 1. English-first bilingual publication

English is the default interface and lesson language. Published learner-facing content must include a meaningful Bangla equivalent. Bangla copy may retain established English technical terms where forced translation would reduce clarity.

## 2. No fake completeness

A curriculum title is not a lesson. A topic becomes `available` only when it has:

- complete bilingual teaching content
- examples and implementation guidance
- practice or assessment
- working navigation
- reviewed references
- validation coverage

Planned items must not have pretend lesson URLs.

## 3. Authority and freshness

Use primary or authoritative sources for version-sensitive behavior:

- Microsoft documentation for Excel and Power BI
- PostgreSQL documentation for the primary SQL dialect
- Python and official library documentation for Python behavior
- recognized statistics references for statistical definitions and methods

Clearly distinguish stable concepts from tool-specific or version-sensitive behavior.

## 4. Originality

Do not copy code, page text, or explanations from the inspiration repository. Statistical names, formulas, and general concepts may be taught using original explanations and properly acknowledged references.

## 5. Practical relevance

Every tool lesson should answer:

- What problem does this solve?
- When should an analyst use it?
- What input is required?
- What output is produced?
- How should the output be checked?
- What business or analytical interpretation is justified?
- What common mistake should be avoided?

## 6. Statistical responsibility

- Do not imply causation from association alone.
- State assumptions and limitations.
- Separate statistical significance from practical importance.
- Explain sample, population, unit, context, and uncertainty.
- Do not hide invalid or undefined input behind fabricated outputs.

## 7. Dataset integrity

Bundled practice data must be synthetic or openly licensed, documented, and safe to redistribute. Every dataset requires a data dictionary and explicit grain.

## 8. Code and formula quality

Examples should be executable with the stated baseline, use consistent naming, include expected output where appropriate, and avoid unexplained shortcuts. SQL dialect differences must be disclosed.

## 9. Accessibility and UX

- preserve semantic headings and landmarks
- label icon-only controls accessibly
- support keyboard use
- keep contrast readable in light and dark themes
- use progressive disclosure rather than removing necessary content
- keep one clear next action in guided flows

## Tutorial publication standard — v2.1+

A course may be labeled `tutorial-published` only when:

- Its full intended chapter sequence is present.
- Every chapter teaches the subject directly rather than describing a study plan.
- English and Bangla content are complete.
- Definitions are explained in beginner-friendly language.
- Examples are topic-specific and show context, process, result, and interpretation.
- Each chapter includes an activity and at least three exercises.
- Previous/next navigation, course contents, progress, examples, references, and assessment work.
- Primary or authoritative references support factual claims.
- Automated content, relationship, link, syntax, and browser checks pass.

A tutorial chapter should normally include:

```text
Introduction
→ Learning objectives
→ Core explanations
→ Key vocabulary
→ Worked example
→ Try it yourself
→ Exercises
→ Summary
→ References
→ Previous / Next
```

Progressive disclosure may simplify the first view, but it must not replace substantive teaching content.
