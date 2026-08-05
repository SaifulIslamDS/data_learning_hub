# Testing — v2.5.0

## Commands

```powershell
npm run generate
npm test
npm run test:browser
```

## Automated baseline

- 108 retained bilingual lessons
- 20 statistical labs
- 5 published tutorials
- 314 tutorial chapters
- 942 chapter exercises
- 94 Python chapters across 9 modules
- 66 SQL starter queries executed against fresh SQLite databases
- 94 Python starter snippets executed in isolated temporary workspaces
- 489 HTML pages
- 31,454 local references
- 0 broken local references

## Python audit

`scripts/audit_python.py` validates:

- Course ID, publication status, version, module count, and chapter count
- Unique chapter IDs and module relationships
- English/Bangla summaries, sections, terms, worked examples, activities, exercises, recaps, and references
- `python-playground` activity and package allowlist on every chapter
- Required datasets and row counts
- Data dictionary schema
- Starter and completed notebooks through `nbformat`
- Practice ZIP contents
- Successful execution of all 94 chapter starter snippets

## Browser regression

Chromium smoke tests verify:

- Sticky header and exact footer behavior
- Five published tutorial cards
- 94-chapter Python course and nine modules
- Python editor interface and starter code
- Standalone Python playground interface
- Completion state and EN/BN switching
- 282 Python exercises
- 30-question Python final quiz
- Mobile 94-chapter drawer
- Data Foundations, Excel, SQL, SQL playground, Power BI, and statistical-lab regression

The sandbox browser cannot complete an external CDN WebAssembly download, so release testing separates concerns: every starter snippet is executed locally against the packaged datasets, while the browser suite validates the production Pyodide integration UI and controls. A final deployed-site smoke test should run one simple Python command after Netlify deployment.

## Release rule

Do not tag a release until the complete test suite passes from a freshly extracted release archive and the deployed Python playground successfully runs a simple command.
