# Testing and Quality Gates

## Run all source-level checks

```powershell
npm test
```

This runs:

1. statistical numerical tests
2. comprehensive lesson audit
3. curriculum architecture audit
4. local link and asset audit
5. JavaScript syntax checks

## Browser smoke test

```powershell
npm run test:browser
```

Representative browser checks cover:

- Data Learning Hub identity
- v1 `slh-*` to v2 `dlh-*` browser-state migration
- English/Bangla controls
- light/dark theme
- guided setup
- learning catalog
- curriculum publication honesty
- datasets and projects
- comprehensive lesson rendering
- responsive mobile header

Screenshots are written to `docs/screenshots-v2.0.0/`.

## Current release evidence

- 108 comprehensive bilingual lessons validated
- 20 statistical labs retained
- 9 domains validated
- 4 curriculum-ready tool tracks validated
- 3 synthetic datasets and dictionaries validated
- 2 project definitions validated
- 143 generated HTML pages
- 1,250 local HTML and asset references checked
- 0 broken local references
- statistical tests passed
- JavaScript syntax checks passed
- browser smoke test passed

## Before every release

```powershell
npm run generate
npm test
npm run test:browser
```

Then inspect:

- generated diff
- navigation and mobile layout
- curriculum statuses
- release documentation
- sitemap and production URL
- Netlify deploy preview or production deploy
