# AGENTS.md

## Product

Data Learning Hub is a static, tutorial-first, English-first bilingual Data Analytics learning platform. Tutorials are the primary product; career plans and progress dashboards are optional support.

## Source of truth

Read before changing the product:

1. `docs/ARCHITECTURE.md`
2. `docs/CURRICULUM.md`
3. `docs/CONTENT-STANDARDS.md`
4. `docs/ROADMAP.md`
5. `docs/TESTING.md`

Authored tutorial content lives in `content/tutorials/`. Generated HTML and `assets/js/content.js` are outputs, not primary editing sources.

## Non-negotiable rules

- Keep deployment static: HTML, CSS, and Vanilla JavaScript.
- No backend, API, database, authentication, or server-side learner state.
- English is default; every published tutorial chapter must include Bangla.
- Tutorials must contain actual teaching content, examples, practice, and assessment—not curriculum summaries.
- Only complete tutorials may be labeled `tutorial-published`.
- Preserve stable chapter, lesson, and lab IDs.
- Use authoritative references for factual and tool-specific content.
- Do not copy code or prose from the inspiration repository.
- Keep datasets clearly labeled synthetic.
- Never weaken interpretation, privacy, quality, or causality cautions.

## Main-branch development cycle

```powershell
npm run generate
npm test
npm run test:browser
```

Do not tag until authored content, generated files, documentation, tests, screenshots, and release notes agree.

## Release boundaries

- v2.0.0: architecture and curriculum foundation
- v2.1.0: tutorial platform core and complete Data Foundations
- v2.2.0: complete Excel tutorial
- v2.3.0: complete SQL tutorial
- v2.4.0: complete Power BI tutorial
- v2.5.0: complete Python tutorial
- v2.6.0: cross-tool Data Analytics workflows and portfolio
