# Changelog

All notable changes are documented here.

## [2.0.0] — Data Analytics Platform Architecture and Curriculum Foundation

### Added

- Rebranded product identity: Data Learning Hub
- Modular content architecture under `content/platform`, `content/statistics`, `content/tracks`, and `content/datasets`
- Nine top-level learning domains with transparent publication status
- Active Data Analyst route and supporting Research & Decision Analyst route
- Reviewed Excel, SQL, Power BI, and Python curriculum maps
- Tool teaching baselines linked to official documentation
- Five-step onboarding covering goal, level, study time, learning mode, and prior tool knowledge
- Projects, Career Paths, and Curriculum routes
- Three documented synthetic datasets and dictionaries
- Retail Sales Foundations Project
- Curriculum architecture audit
- v1-to-v2 browser-local progress migration
- Legacy route redirects for `/catalog/` and `/paths/`

### Changed

- Statistics is now positioned as a foundation within Data Analytics
- Primary navigation is My Learning, Learn, Practice, Projects, and Career Paths
- Product generation is driven by modular domain files rather than one monolithic curriculum source
- Generated content payload uses `window.DLH_CONTENT`
- Browser events and storage use the `dlh-*` namespace
- Footer, metadata, manifest, sitemap, robots, and social identity use Data Learning Hub

### Preserved

- 108 comprehensive bilingual lessons
- 20 statistical labs
- English/Bangla switching
- Light/dark theme
- Guided learning workflow
- Local bookmarks and completion tracking
- Static Netlify deployment

### Publication boundary

Excel, SQL, Power BI, and Python are curriculum-ready but not yet published as complete lessons. No planned item is represented as finished content.

## [1.2.0] — Comprehensive Lesson Experience

The tagged v1.2.0 release remains the stable Statistics Learning Hub historical baseline. Its release documentation is archived under `docs/archive/v1/`.
