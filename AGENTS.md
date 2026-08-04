# Repository Working Rules

## Source of truth

- Curriculum structure and page metadata: `scripts/generate.py`
- Topic definitions: `scripts/topic_details.py`
- Comprehensive lesson content and scenarios: `scripts/comprehensive_content.py`
- Generated browser dataset: `assets/js/content.js`
- Shared visual system: `assets/css/main.css`
- Shared site behavior: `assets/js/site.js`
- Statistical functions: `assets/js/stats-core.js`
- Lab UI and calculations: `assets/js/tools.js`

## Editing policy

1. Do not manually edit files under `topics/*/index.html`; they are generated.
2. Do not manually duplicate shared header, footer, theme, language, or search logic.
3. Add or modify curriculum data in the generator, then run `npm run generate`.
4. Every published card must resolve to a real route. Do not publish placeholder or `#` links.
5. English and Bangla text must be updated together.
6. Statistical claims must state assumptions and avoid causal overclaiming.
7. New calculators require deterministic tests where applicable.
8. Preserve static deployment: no backend, API, database, authentication, or server runtime.
9. Run `npm test` before every commit.
10. Run `python scripts/browser_smoke.py` after changing lesson UI or interaction.
11. Update documentation and `CHANGELOG.md` for material releases.

## Release gate

A release is acceptable only when:

- statistical tests pass;
- the comprehensive lesson audit validates all 108 lessons;
- the link audit reports zero broken local references;
- English and Bangla switching works;
- both themes work;
- mobile navigation works;
- every changed calculator is browser-tested with valid and invalid input;
- canonical production origin is correct;
- Netlify deploy preview has no console-breaking errors.
