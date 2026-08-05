# Testing — v2.3.0

Run the complete validation suite:

```powershell
npm run generate
npm test
npm run test:browser
```

## Automated checks

- Statistical numerical tests
- 108-lesson comprehensive content audit
- 143-chapter tutorial completeness audit
- Curriculum and dataset relationship audit
- SQL database and starter-query execution audit
- Local-link and downloadable-file audit
- JavaScript syntax checks
- Playwright browser smoke tests

## v2.3.0 baseline

```text
3 published tutorials
143 tutorial chapters
429 chapter exercises
66/66 SQL starter queries executed successfully
307 HTML pages
12,664 local references
0 broken references
```

The browser test verifies SQL editor rendering and controls but does not depend on external CDN availability. Query correctness is validated independently with Python's SQLite engine against the same generated seed database.
