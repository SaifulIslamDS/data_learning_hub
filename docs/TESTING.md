# Testing — v2.4.0

## Commands

```powershell
npm run generate
npm test
npm run test:browser
```

## Automated baseline

- 108 retained bilingual lessons
- 20 statistical labs
- 4 published tutorials
- 220 tutorial chapters
- 660 chapter exercises
- 77 Power BI chapters across 9 modules
- 66 SQL starter queries executed against fresh SQLite databases
- 389 HTML pages
- 20,367 local references
- 0 broken local references

## Power BI audit

`scripts/audit_power_bi.py` validates:

- Course version, chapter count, and module count
- `powerbi-demo` activity on every chapter
- Official Microsoft Learn chapter references
- Required download files
- ZIP contents
- Dimension and fact row counts
- Unique sales-line keys
- Foreign-key integrity
- Date coverage
- `GrossProfit = Revenue - Cost`

## Browser regression

Chromium smoke tests verify:

- Sticky header
- Four published tutorial cards
- Exact footer adjustment
- 77-chapter Power BI course and nine modules
- Power BI activity and completion state
- English/Bangla switching
- 231 Power BI exercises
- 30-question Power BI quiz
- Mobile 77-chapter drawer
- Data Foundations, Excel, SQL, SQL playground, and statistical-lab regression

## Release rule

Do not tag a release until the complete test suite passes from a freshly extracted release archive.
