# Testing — v2.1.0

## Full validation

```powershell
npm run generate
npm test
npm run test:browser
```

## Automated checks

### Statistical core

Validates the retained browser statistical engine.

### Comprehensive lesson audit

Validates all 108 retained bilingual lessons.

### Tutorial audit

Validates:

- One published tutorial
- Exactly 21 Data Foundations chapters
- Stable, unique chapter IDs
- Complete English/Bangla content
- Minimum teaching depth
- Objectives, sections, terms, examples, activities, exercises, recaps, and references
- Required tutorial routes

### Curriculum audit

Validates domain status, paths, datasets, projects, and honest publication boundaries.

### Link audit

Checks all local HTML links and assets across generated pages.

### JavaScript syntax

Checks all shared platform and tutorial JavaScript files.

### Browser smoke test

Uses headless Chromium to verify:

- Tutorial-first homepage and navigation
- Published tutorial index
- 21-chapter course contents
- Topic-specific chapter content
- Interactive classification activity
- EN/BN switching
- Chapter completion storage
- 63-exercise library and chapter filtering
- 30-question final quiz generation
- Mobile chapter drawer

Screenshots are written to `docs/screenshots-v2.1.0/`.

## v2.1.0 release result

```text
All statistical core tests passed.
Validated 108 comprehensive bilingual lessons.
Validated 1 published tutorial with 21 complete bilingual chapters.
Validated 84 objectives, 63+ teaching sections, 84+ terms,
21 examples, 21 activities, and 63 exercises.
Checked 2,233 local references across 170 HTML files.
0 broken local references found.
Browser smoke test passed.
```
