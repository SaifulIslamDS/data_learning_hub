# v1.2.0 Release Report — Comprehensive Lesson Experience

## Release objective

v1.1.0 successfully reduced navigation overload, but lesson pages still behaved like guided summaries. They explained how to approach a topic without teaching the topic with sufficient depth.

v1.2.0 keeps the guided route and replaces the generic lesson template with a structured, comprehensive learning unit.

## New lesson architecture

Every lesson now uses four phases:

1. **Learn** — plain-language explanation, why the topic matters, core vocabulary, learning outcomes, and formal rule or formula.
2. **Explore** — a unique real-world scenario, analytical question, worked reasoning sequence, and responsible interpretation boundary.
3. **Apply** — a repeatable workflow, module-relevant implementation guides, linked browser lab where available, and a mini-assignment.
4. **Check** — an interactive knowledge check, explanation, common mistakes, recap, and authoritative further reading.

The design uses progressive disclosure. Essential explanations remain visible, while formal rules, implementation details, cautions, and sources can be expanded when needed.

## Content implementation

The release adds `scripts/comprehensive_content.py`, which provides deterministic bilingual content for every topic:

- 108 unique scenario titles;
- 108 topic-specific analytical questions;
- bilingual scenario context and application tasks;
- custom concept definitions for foundational and high-value topics;
- type-aware workflows for concept, formula, method, and operational-workflow lessons;
- module-specific implementation guides;
- responsible versus overstated interpretation examples;
- quizzes, recaps, and reference groups.

No lesson content is generated remotely at runtime.

## Representative improvement: Statistics and Data

The first lesson now explicitly teaches:

- what data is;
- what statistics is;
- descriptive statistics;
- inferential statistics;
- why the distinction matters;
- how a shop-sales dataset becomes an analytical question;
- how to identify observations, variables, units, and decisions;
- how spreadsheet and SQL workflows support implementation;
- how to avoid claiming certainty or causation without evidence;
- a mini-assignment and knowledge check.

This pattern is adapted to the actual lesson type across the complete curriculum rather than copied as one universal block.

## UI and UX changes

- Replaced the three-pass lesson banner with a four-phase lesson map.
- Added anchor navigation for Learn, Explore, Apply, and Check.
- Added clear phase headers and section hierarchy.
- Added core-vocabulary cards.
- Added scenario question and worked-reasoning panels.
- Added responsible-interpretation and overclaim-warning panels.
- Added expandable implementation guides.
- Added interactive knowledge checks with answer explanations.
- Added lesson recaps and further-reading accordions.
- Added a sticky “On this lesson” sidebar on desktop.
- Added responsive single-column presentation for mobile.
- Increased realistic study-time estimates to 30, 45, or 60 minutes by level.

## Validation results

- 108 comprehensive bilingual lessons validated.
- Every lesson contains concepts, one unique scenario, workflow, at least two implementation guides, interpretation guidance, mini-assignment, quiz, recap, and references.
- Statistical-core automated tests pass.
- JavaScript syntax validation passes.
- 1,219 local references across 137 HTML files audit with zero broken links.
- Browser smoke testing passes for the representative comprehensive lesson, including:
  - English-first rendering;
  - Bangla toggle;
  - four-phase navigation;
  - concept cards;
  - implementation guides;
  - quiz interaction;
  - light/dark theme switching;
  - mobile rendering.

## Compatibility

The release remains:

- static HTML, CSS, and Vanilla JavaScript;
- deployable directly to Netlify;
- free of backend frameworks, APIs, databases, and authentication;
- compatible with the existing local progress and guided-plan data.

No migration is required for browser-local v1.1.0 profiles or progress.
