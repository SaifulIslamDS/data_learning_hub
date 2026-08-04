# Content Standards

## Accuracy principles

1. Define the target quantity, population, unit, and data-generating process before presenting a method.
2. Separate description, prediction, inference, and causal claims.
3. State the assumptions or conditions that make a result meaningful.
4. Treat p-values as compatibility measures under a null model, not probabilities that a hypothesis is true.
5. Distinguish statistical significance from practical importance.
6. Avoid deleting outliers automatically; investigate cause and analytical impact.
7. Identify calculation conventions when software can legitimately differ, especially quantiles and variance.
8. Explain uncertainty and limitations alongside point estimates.
9. Do not imply that correlation alone establishes causation.
10. Distinguish conceptual data-engineering education from executable production infrastructure.
11. Label implementation patterns clearly and do not invent nonexistent software functions.
12. Prefer authoritative textbooks, standards, and primary software documentation for further reading.

## Bilingual policy

- English is the default language.
- Every user-facing instructional element requires both English and Bangla text.
- Bangla may retain established English technical terms when forced translation would reduce clarity.
- Form labels, validation, results, chart labels, navigation, quiz feedback, scenarios, implementation steps, and accessibility labels belong to the bilingual system—not only headings.
- The selected language persists through `localStorage`.

## Comprehensive lesson standard

Every lesson must contain:

- plain-language explanation;
- why the topic matters;
- at least three topic concepts;
- measurable learning outcomes;
- formal definition, rule, formula, or procedural statement;
- unique practical scenario and analytical question;
- worked reasoning steps;
- responsible interpretation and overclaim warning;
- repeatable workflow;
- at least two implementation guides;
- mini-assignment;
- interactive knowledge check and explanation;
- common mistakes;
- recap;
- further-reading sources;
- related and next lesson controls.

A lesson must not be published when it contains only a title, short definition, generic workflow, or placeholder application text.

## Progressive disclosure

Comprehensive content should not create a new content wall.

- Essential explanations and examples remain visible.
- Formal rules, implementation details, cautions, and references may use accessible accordions.
- The page presents four phases in a stable sequence.
- Mobile layouts remain single-column and avoid horizontal scrolling.
- One primary completion action and one next action are shown at the end.

## Scenario standard

A scenario must:

- use a realistic analytical, research, business, scientific, or engineering context;
- identify a specific question;
- avoid unsupported numerical conclusions;
- show what data, unit, design, parameter, or workflow is relevant;
- include an interpretation boundary or limitation.

## Implementation standard

Implementation guidance must:

- match the topic and module;
- distinguish executable code from conceptual workflow;
- state important defaults, grain, assumptions, or validation checks;
- encourage use of established libraries and official documentation;
- avoid implying that a browser-only lesson reproduces production infrastructure.

## Lab standard

Each lab includes:

- documented input convention;
- example values;
- validation and actionable errors;
- numerical outputs;
- interpretation guidance;
- method or assumption note;
- visualization where useful;
- local-only processing notice.

## Source and review practice

Specialized formulas and reference values should be checked against authoritative textbooks, peer-reviewed sources, standards, or primary software documentation. Reference groups used in lessons include OpenStax, NIST/SEMATECH, official scikit-learn documentation, Apache Parquet, PostgreSQL, and dbt documentation.

Sources support learning and verification; lesson copy remains original and is not copied verbatim from external material.
