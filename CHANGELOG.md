# Changelog

All notable changes to this project are documented here.

## [1.2.0] - 2026-08-04

### Added

- Learn → Explore → Apply → Check architecture across all 108 lessons.
- Plain-language explanations, topic importance, core vocabulary, formal rules, and measurable outcomes.
- 108 unique bilingual real-world scenarios and analytical questions.
- Worked reasoning sequences and responsible-versus-overstated interpretation panels.
- Concept-, formula-, method-, and workflow-specific practical sequences.
- At least two module-relevant implementation guides per lesson.
- Mini-assignments, interactive three-option knowledge checks, answer explanations, and recaps.
- Authoritative further-reading groups using OpenStax, NIST/SEMATECH, scikit-learn, Apache Parquet, PostgreSQL, and dbt documentation.
- `scripts/comprehensive_content.py` as the deterministic comprehensive lesson source.
- `scripts/audit_lessons.py` to validate all 108 generated lessons.
- `scripts/browser_smoke.py` for representative browser-level lesson QA.
- New desktop and mobile screenshots for the comprehensive Statistics and Data lesson.

### Changed

- Replaced generic three-pass lesson summaries with topic-focused comprehensive teaching units.
- Increased study-time estimates to 30, 45, or 60 minutes by difficulty.
- Added four-phase page navigation and a sticky desktop lesson table of contents.
- Added progressive disclosure for formal rules, implementation guidance, cautions, and sources.
- Preserved v1.1.0 onboarding, dashboard, guided paths, local progress, and static architecture.

### Validated

- Statistical-core automated tests pass.
- 108 comprehensive bilingual lessons pass structural and uniqueness validation.
- All JavaScript files pass syntax validation.
- 1,219 local references across 137 HTML files audit with zero broken links.
- Browser smoke testing passes for English-first content, Bangla switching, quiz interaction, theme switching, and mobile rendering.

## [1.1.0] - 2026-08-04

### Added

- Three-step guided onboarding for goal, starting level, and learning preference.
- New Statistics Foundations path, increasing guided paths from four to five.
- Private browser-local learner profile stored in `localStorage`.
- Personalized `My Learning` dashboard with one next lesson, a focused session plan, a short visible roadmap, bookmarks, and progress controls.
- Learn → Practice → Apply experience across the homepage, lessons, and labs.
- Goal-aware application prompts for analysts, scientists, engineers, and researchers.
- Concept-first, balanced, and practice-first session sequencing.
- Path comparison interface with one selected path expanded into four manageable phases.
- Guided catalog mode that shows only the learner's selected path by default while preserving access to all 108 lessons.
- Guided lesson passes, reflection prompts, collapsible caution content, and a clear next-step action.
- Guided lab instructions that encourage controlled input changes and plain-language interpretation.
- Desktop and mobile visual QA screenshots for the guided experience.

### Changed

- Simplified primary navigation to My Learning/Start Here, Learn, Practice, and Apply.
- Replaced the homepage's nine-module content wall with a focused entry experience.
- Reduced homepage featured labs from eight to three.
- Reframed Paths as the application layer and Catalog as the learning layer.
- Updated footer navigation around the learner journey.

### Validated

- Statistical-core automated tests pass.
- All JavaScript files pass syntax validation.
- 1,219 local references across 137 HTML files audit with zero broken links.
- Desktop and mobile layouts were visually reviewed for homepage, onboarding, dashboard, and guided lesson pages.

## [1.0.0] - 2026-08-04

### Added

- Original modern responsive design system with light and dark themes.
- English-first EN/BN bilingual interface with persistent language preference.
- Nine-module curriculum containing 108 implemented lesson routes.
- Twenty interactive browser-based statistical laboratories.
- Four career-oriented learning paths.
- Searchable 40-term bilingual glossary.
- Global search, lesson filters, breadcrumbs, related lessons, bookmarks, and completion tracking.
- Shared statistical engine and automated numerical tests.
- Static page generator, sitemap generation, and local-reference audit.
- SEO metadata, social artwork, manifest, robots file, custom 404 page, and Netlify configuration.
- Architecture, curriculum, content, testing, deployment, and attribution documentation.

### Validated

- Statistical-core automated tests pass.
- JavaScript syntax validation passes.
- 1,205 local references across 135 HTML files audit with zero broken links.
- All 20 laboratories calculate their supplied examples in browser-level testing.
