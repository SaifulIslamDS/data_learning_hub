#!/usr/bin/env python3
"""
Data Learning Hub v2.7.2 — Tutorial-First Alignment

Run from the repository root:

    python apply_v272.py
    pnpm install
    pnpm check
"""

from pathlib import Path
import json
import re

ROOT = Path.cwd()

def read(path):
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing expected file: {path}")
    return p.read_text(encoding="utf-8")

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"updated {path}")

def require(condition, message):
    if not condition:
        raise SystemExit(message)

# 1) Remove the generic objective UI at render time from current migrated pages.
path = "src/components/legacy-page.tsx"
c = read(path)

if "prepareTutorialHtml" not in c:
    marker = "\nexport function LegacyPage"
    require(marker in c, f"Unexpected {path}: export marker not found")
    helper = """
function prepareTutorialHtml(html: string): string {
  return html
    .replace(/<a href="#objectives">Objectives<\\/a>/g, "")
    .replace(/<section class="tutorial-section tutorial-objectives" id="objectives">[\\s\\S]*?<\\/section>/g, "")
    .replace('<span class="stat-chip"><strong>EN/BN</strong> bilingual</span>', '<span class="stat-chip"><strong>Practice</strong> built in</span>')
    .replace('<span><strong>EN/BN</strong> bilingual</span>', '<span><strong>English</strong> tutorial</span>');
}

"""
    c = c.replace(marker, "\n" + helper + "export function LegacyPage", 1)

if "const renderedHtml = prepareTutorialHtml(page.mainHtml);" not in c:
    old = 'export function LegacyPage({ page }: { page: LegacyPageData }) {\n  const boot ='
    new = 'export function LegacyPage({ page }: { page: LegacyPageData }) {\n  const renderedHtml = prepareTutorialHtml(page.mainHtml);\n  const boot ='
    require(old in c, f"Unexpected {path}: component marker not found")
    c = c.replace(old, new, 1)

c = c.replace(
    "dangerouslySetInnerHTML={{ __html: page.mainHtml }}",
    "dangerouslySetInnerHTML={{ __html: renderedHtml }}"
)
write(path, c)

# 2) Prevent future legacy regeneration from recreating objective UI.
path = "scripts/legacy/tutorial_generator.py"
c = read(path)

c = re.sub(r"\n    objectives = .*?\n", "\n", c, count=1)

pattern = re.compile(
    r'<nav class="chapter-jump" aria-label="On this chapter">[\s\S]*?</nav>\n'
    r'        <section class="tutorial-section tutorial-objectives" id="objectives">[\s\S]*?</section>'
)
replacement = (
    '<nav class="chapter-jump" aria-label="On this chapter">'
    '<a href="#concept-1">Learn</a>'
    '<a href="#worked-example">Example</a>'
    '<a href="#try-it">Practice</a>'
    '<a href="#exercises">Exercises</a>'
    '<a href="#summary">Summary</a>'
    '</nav>'
)
c, n = pattern.subn(replacement, c, count=1)
require(n == 1 or "tutorial-objectives" not in c, f"Could not remove objective section from {path}")

c = c.replace(
    '<span><strong>EN/BN</strong> bilingual</span>',
    '<span><strong>English</strong> tutorial</span>'
)
c = c.replace(
    '<span class="stat-chip"><strong>EN/BN</strong> bilingual</span>',
    '<span class="stat-chip"><strong>Practice</strong> built in</span>'
)

require("tutorial-objectives" not in c, f"{path} still contains tutorial-objectives")
require('href="#objectives"' not in c, f"{path} still contains Objectives jump link")
write(path, c)

# 3) English-only active learner interface.
path = "public/assets/js/site.js"
c = read(path)

c, n = re.subn(
    r"  const state = \{\n    language: .*?\n    theme:",
    "  const state = {\n    language: 'en',\n    theme:",
    c,
    count=1,
)
require(n == 1 or "language: 'en'" in c, f"Could not force English state in {path}")

if "safeStorage.set('dlh-language', 'en');" not in c:
    c, n = re.subn(
        r"  \};\n\n  function t\(en, bn\)",
        "  };\n  safeStorage.set('dlh-language', 'en');\n\n  function t(en, bn)",
        c,
        count=1,
    )
    require(n == 1, f"Could not persist English language in {path}")

c, n = re.subn(
    r"  function languageSwitch\(\) \{[\s\S]*?\n  \}\n  function renderHeader",
    "  function languageSwitch() {\n    return '';\n  }\n  function renderHeader",
    c,
    count=1,
)
require(n == 1 or "function languageSwitch() {\n    return '';" in c, f"Could not hide language switch in {path}")
write(path, c)

# 4) Metadata wording.
path = "app/layout.tsx"
c = read(path)
c = c.replace(
    "A bilingual Data Analytics learning platform covering foundations, statistics, Excel, SQL, Power BI, Python, workflows, and portfolio projects.",
    "A tutorial-first Data Analytics learning platform covering foundations, statistics, Excel, SQL, Power BI, Python, workflows, practice, and portfolio projects.",
)
write(path, c)

path = "app/manifest.ts"
c = read(path)
c = c.replace(
    "Learn Data Analytics through complete bilingual tutorials, browser practice, workflows, and portfolio projects.",
    "Learn Data Analytics through direct tutorials, browser practice, workflows, exercises, and portfolio projects.",
)
write(path, c)

# 5) Version and PWA consistency.
path = "package.json"
pkg = json.loads(read(path))
pkg["version"] = "2.7.2"
pkg["description"] = "Next.js App Router PWA for an English-first, tutorial-first practical data learning platform."
write(path, json.dumps(pkg, indent=2) + "\n")

path = "public/sw.js"
c = read(path)
c, n = re.subn(r"const VERSION = 'dlh-v[^']+';", "const VERSION = 'dlh-v2.7.2';", c, count=1)
require(n == 1, f"Could not update PWA version in {path}")
write(path, c)

audit_pwa = """import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const required = [
  'app/manifest.ts',
  'app/offline/page.tsx',
  'public/sw.js',
  'public/icons/icon-192.png',
  'public/icons/icon-512.png',
  'public/icons/maskable-512.png',
  'netlify.toml',
];

const errors = required
  .filter((file) => !fs.existsSync(path.join(root, file)))
  .map((file) => `Missing ${file}`);

const pkg = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8'));
const expectedVersion = `dlh-v${pkg.version}`;
const sw = fs.readFileSync(path.join(root, 'public/sw.js'), 'utf8');

for (const token of ['install', 'activate', 'fetch', '/offline/', expectedVersion]) {
  if (!sw.includes(token)) errors.push(`Service worker missing token: ${token}`);
}

const syntax = spawnSync(process.execPath, ['--check', path.join(root, 'public/sw.js')], { encoding: 'utf8' });
if (syntax.status !== 0) errors.push(`Service worker syntax error: ${syntax.stderr || syntax.stdout}`);

const netlify = fs.readFileSync(path.join(root, 'netlify.toml'), 'utf8');
if (!netlify.includes('publish = "out"')) errors.push('Netlify publish directory is not out');
if (!netlify.includes('Service-Worker-Allowed')) errors.push('Netlify service worker header missing');

if (errors.length) {
  console.error(errors.join('\\n'));
  process.exit(1);
}

console.log(`PWA manifest source, service worker ${expectedVersion}, icons, offline page, and Netlify headers validated.`);
"""
write("scripts/audit-pwa.mjs", audit_pwa)

# 6) Tutorial standard.
tutorial_standard = """# Data Learning Hub — Tutorial Page Standard

## Primary rule

**Teach the topic immediately.**

A learner arriving from search should begin learning from the title, short introduction, and first teaching section without passing through onboarding or meta-learning content.

## Canonical page pattern

```text
Topic title
Short introduction

1. Direct concept explanation
2. Syntax / formula / tool action, where relevant
3. Simple example
4. Actual output / result
5. Explanation of the result
6. Important rules / behavior
7. More realistic worked example
8. Common mistakes, where useful
9. Practice / Try it
10. Exercises
11. Quick summary or reference
12. Authoritative references
Previous / Next
```

Do not render generic "What you will learn", "Start here" objective cards, generic chapter-objective lists, how-to-study filler, motivational filler, or career dashboards inside the tutorial body.

Authoring objectives may remain in source data for curriculum design and assessments.

## Worked examples

SQL: data context, query, result, explanation.  
Python: input, executable code, output, explanation.  
Statistics: data, method/formula, calculation, result, interpretation.  
Excel: workbook context, formula/action, expected result, explanation.  
Power BI: model context, Power Query/model/DAX/report action, expected output, explanation.

## Career relationship

Career paths, assessments, projects, and portfolio support link to tutorial pages. They do not replace the tutorial page.

The tutorial remains the reusable atomic teaching unit.
"""
write("docs/TUTORIAL-PAGE-STANDARD.md", tutorial_standard)

# 7) Product/content docs.
product_vision = """# Data Learning Hub — Product Vision

## Product identity

Data Learning Hub is a tutorial-first practical learning platform for data careers.

Its primary experience should feel closer to W3Schools than to a conventional LMS.

> **Teach first. Explain the learning system elsewhere.**

Career paths, projects, assessments, progress, and portfolio support sit around the tutorial library rather than taking over individual tutorial pages.

## Core architecture

### Tutorial-first core
Data Foundations, Statistics, Excel, SQL, Power BI, Python, Analytics Workflows, and later Data Engineering, Data Science/ML, and AI Engineering.

### Learning/career layer
Practice, exercises, labs, assessments, projects, mastery, career paths, portfolio preparation, and interview preparation.

## Language direction

The active learner-facing product is English-first. Legacy Bangla fields may remain internally during the compatibility period.

## Product success

A learner can find the exact concept, learn it immediately, reproduce a real example, practice it, verify the result, and continue into deeper exercises/projects/career paths without losing tutorial simplicity.
"""
write("docs/PRODUCT-VISION.md", product_vision)

content_standards = """# Data Learning Hub — Content Standards

## Teach the subject directly

Do not automatically render:

- "What you will learn"
- "Start here" objective cards
- "How to learn SQL"
- "How to study this chapter"
- "Your learning journey"
- generic motivational filler
- repeated objective lists that merely restate the topic

Learning objectives may exist as authoring metadata.

See [Tutorial Page Standard](TUTORIAL-PAGE-STANDARD.md).

## No dummy learning content

Do not publish placeholders, empty examples presented as complete, generic title-swapped examples, repeated generated worked-example templates, or invented output presented as real evidence.

## Standalone topics

Many learners arrive from search. A topic should be independently useful unless a genuine prerequisite exists.

## Practical teaching loop

Where relevant include direct explanation, syntax/action, real input, operation, actual output, explanation, practice, result checking, common mistakes, exercises, summary/reference, navigation, and authoritative sources.

## Reproducible examples

SQL: data context + query + result + explanation.  
Python: input + executable code + output + explanation.  
Statistics: values + method/formula + calculation + result + interpretation.  
Excel: workbook context + formula/action + expected result + explanation.  
Power BI: model context + Power Query/model/DAX/report action + expected result + explanation.

## Practice and assessment

Practice must be real. MCQs may reinforce concepts but should not be the only assessment format.

## Data policy

Synthetic datasets are acceptable for controlled teaching. Serious projects should increasingly use traceable datasets with source, license, snapshot date, dictionary, modifications, and limitations.

## English-first publication

The active learner-facing platform is English-first. Legacy Bangla fields may remain temporarily for compatibility.

## Publication rule

A route is not proof that a topic is complete. A topic is complete only when explanation, examples, results, practice, exercises, references, and required assets are sufficiently complete and validated.
"""
write("docs/CONTENT-STANDARDS.md", content_standards)

# 8) Locked roadmap copied into docs.
roadmap_source = ROOT / "ROADMAP-LOCKED-v2.7.2.md"
require(roadmap_source.exists(), "Place ROADMAP-LOCKED-v2.7.2.md beside apply_v272.py before running.")
write("docs/ROADMAP.md", roadmap_source.read_text(encoding="utf-8"))

# 9) Release/continuation/agents.
release_notes = """# Data Learning Hub — Release Notes v2.7.2

## Release name

**Tutorial-First Alignment**

> **Teach first. Explain the learning system elsewhere.**

## Learner-facing changes

- Remove START HERE / What you will learn from tutorial chapters.
- Remove Objectives from the chapter jump navigation.
- Keep objectives only as internal metadata.
- Make the active learner-facing interface English-only.
- Hide the EN/BN language switch.
- Preserve examples, practice, exercises, summaries, references, completion, projects, and browser runtimes.

## Source changes

- Compatibility renderer strips legacy objective UI.
- Legacy tutorial generator no longer recreates it.
- Add Tutorial Page Standard.
- Fix PWA version/audit drift.
"""
write("docs/RELEASE-NOTES-v2.7.2.md", release_notes)

continuation = """# Data Learning Hub — Project Continuation v2.7.2

## Product rule

Data Learning Hub is tutorial first.

**Teach the subject immediately. Explain the learning system elsewhere.**

The active learner-facing interface is English-only for now. Legacy Bangla fields may remain during migration.

## Next release

v2.7.3 — Engineering Quality Foundation: GitHub Actions, lint/format, unit/component tests, Playwright, axe, and regression checks for the Tutorial Page Standard.
"""
write("docs/PROJECT-CONTINUATION-v2.7.2.md", continuation)

agents = """# AGENTS.md

## Project

Data Learning Hub v2.7.2 is a Next.js 16 App Router PWA deployed to Netlify.

## Product rule

Data Learning Hub is tutorial first.

**Teach the subject immediately. Explain the learning system elsewhere.**

Do not add visible generic "What you will learn", "Start here", how-to-learn, motivational, or career-dashboard blocks to tutorial pages.

Learning objectives may exist as internal metadata.

## Language

The active learner-facing interface is English-only for now.

## Workflow

- Work directly on main unless explicitly changed.
- Use pnpm only.
- Preserve routes and production URL.
- Do not add backend/API/auth/database without explicit approval.
- Preserve theme, progress, bookmarks, exercises, quizzes, labs, playgrounds, projects, and PWA behavior.

## Validation

```powershell
pnpm typecheck
pnpm test
pnpm build
```
"""
write("AGENTS.md", agents)

# 10) Update README and CHANGELOG with a concise version lock.
readme = """# Data Learning Hub

**Version:** v2.7.2 — Tutorial-First Alignment  
**Production URL:** https://datalearninghub.netlify.app/  
**Framework:** Next.js 16.2.10 App Router  
**Deployment:** Netlify static export

Data Learning Hub is an English-first, tutorial-first practical data learning platform.

> **Teach first. Explain the learning system elsewhere.**

A learner should be able to search for a topic, open the page, and begin learning immediately:

**Explain → Example → Result → Practice → Check → Exercises → Continue**

Tutorial pages should not be padded with generic "What you will learn", "Start here", how-to-learn, motivational, or career-dashboard sections.

Career paths, projects, assessments, and portfolio support are built around the tutorial library rather than replacing it.

## Current learning stack

- Data Foundations
- Statistics
- Excel
- SQL
- Power BI
- Python
- Analytics Workflows
- Portfolio Projects

## v2.7.2

- removes the visible objective card and Objectives jump item
- makes the active interface English-only
- adds the Tutorial Page Standard
- locks the product/content roadmap around direct subject teaching
- preserves routes, practice, projects, progress, and PWA behavior
- fixes PWA version-audit drift

## Validation

```powershell
pnpm install
pnpm check
```

## Documentation

- [Product Vision](docs/PRODUCT-VISION.md)
- [Tutorial Page Standard](docs/TUTORIAL-PAGE-STANDARD.md)
- [Content Standards](docs/CONTENT-STANDARDS.md)
- [Roadmap](docs/ROADMAP.md)
- [Release Notes v2.7.2](docs/RELEASE-NOTES-v2.7.2.md)
- [Project Continuation v2.7.2](docs/PROJECT-CONTINUATION-v2.7.2.md)
"""
write("README.md", readme)

changelog = """# Changelog

## v2.7.2 — 2026-08-28

### Changed

- Locked Data Learning Hub to tutorial-first direct teaching.
- Removed visible START HERE / What you will learn objective UI.
- Removed Objectives jump navigation.
- Made active learner-facing UI English-only.
- Added Tutorial Page Standard.
- Locked roadmap around tutorial core → practice → projects → career layer → domain expansion.
- Fixed PWA version/audit drift.

### Preserved

Routes, exercises, quizzes, SQL/Python practice, Power BI simulations, Statistics labs, projects, theme, progress/bookmarks, and PWA behavior.

## v2.7.1 — 2026-08-13

Documentation & Content Integrity Foundation.

## v2.7.0 — 2026-08-05

Next.js App Router compatibility migration preserving the complete v2.6 static release.
"""
write("CHANGELOG.md", changelog)

print("\nApplied Data Learning Hub v2.7.2 Tutorial-First Alignment.")
print("Next: run `pnpm check`, browser regression, production deploy, then tag v2.7.2.")
