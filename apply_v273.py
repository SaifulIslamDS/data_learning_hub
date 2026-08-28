#!/usr/bin/env python3
"""
Apply Data Learning Hub v2.7.3 after extracting this bundle into the project root.

The ZIP already places all new/config/documentation files in their final paths.
This script performs the small edits to existing runtime files that should not
be replaced wholesale.

Run:
    python apply_v273.py
    pnpm install
    pnpm check
"""

from pathlib import Path
import re

ROOT = Path.cwd()

def read(path):
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing required repository file: {path}")
    return p.read_text(encoding="utf-8")

def write(path, content):
    (ROOT / path).write_text(content, encoding="utf-8")
    print(f"patched {path}")

# ------------------------------------------------------------------
# Extract tutorial HTML normalization to a unit-testable library.
# ------------------------------------------------------------------
path = "src/components/legacy-page.tsx"
c = read(path)

import_line = 'import { prepareTutorialHtml } from "@/src/lib/tutorial-html";\n'
if import_line not in c:
    first_import = 'import type { LegacyPageData } from "@/src/lib/page-data";\n'
    if first_import not in c:
        raise SystemExit(f"Unexpected {path}: LegacyPageData import not found")
    c = c.replace(first_import, first_import + import_line, 1)

c = re.sub(
    r'\n+function prepareTutorialHtml\(html: string\): string \{[\s\S]*?\n\}\n',
    '\n',
    c,
    count=1,
)

if 'const renderedHtml = prepareTutorialHtml(page.mainHtml);' not in c:
    raise SystemExit(f"Unexpected {path}: renderedHtml normalizer call is missing")

write(path, c)

# ------------------------------------------------------------------
# Remove Bangla toggle renderer/wiring from active runtime.
# Keep dormant translated data for a future complete localization phase.
# ------------------------------------------------------------------
path = "public/assets/js/site.js"
c = read(path)

c = re.sub(
    r"\n  function languageSwitch\(\) \{\n    return '';\n  \}",
    '',
    c,
    count=1,
)

c = c.replace('${languageSwitch()}', '')

c = re.sub(
    r"\n    root\.querySelectorAll\('\.language-button'\)\.forEach\(button => button\.addEventListener\('click', \(\) => setLanguage\(button\.dataset\.lang\)\)\);",
    '',
    c,
    count=1,
)

c = re.sub(
    r"\n    document\.querySelectorAll\('\.language-button'\)\.forEach\(button => \{[\s\S]*?\n    \}\);",
    '',
    c,
    count=1,
)

if 'function languageSwitch' in c or 'language-button' in c or 'data-lang="bn"' in c:
    raise SystemExit(f"{path}: Bangla toggle code remains after patch")

write(path, c)

# ------------------------------------------------------------------
# Bump service-worker cache version.
# ------------------------------------------------------------------
path = "public/sw.js"
c = read(path)
c, count = re.subn(
    r"const VERSION = 'dlh-v[^']+';",
    "const VERSION = 'dlh-v2.7.3';",
    c,
    count=1,
)
if count != 1:
    raise SystemExit(f"Could not update service-worker version in {path}")
write(path, c)

# ------------------------------------------------------------------
# Lock v2.7.3 as delivered in the existing roadmap without replacing
# later roadmap stages.
# ------------------------------------------------------------------
path = "docs/ROADMAP.md"
c = read(path)

pattern = re.compile(
    r"## v2\.7\.3 — Engineering Quality Foundation[\s\S]*?(?=\n---\n\n## v2\.8\.0|\n## v2\.8\.0)"
)

replacement = """## v2.7.3 — Engineering Quality Foundation

### Goal

Add automated engineering quality gates before the native React migration.

### Delivered

- GitHub Actions CI
- ESLint
- Prettier
- Vitest
- React Testing Library
- Playwright Chromium smoke tests
- axe accessibility checks
- tutorial-first UI regression audit
- production static-export test server
- automated lint, format, typecheck, audit, unit-test, build, E2E, and accessibility gates
- regression coverage for the removed objective card
- regression coverage ensuring the Bangla toggle remains absent until full-site localization

### Release gate

- `pnpm check` passes
- Playwright browser tests pass
- GitHub Actions passes
- `pnpm-lock.yaml` is refreshed and committed
- Netlify production deployment is verified

---

"""

c, count = pattern.subn(replacement, c, count=1)
if count != 1:
    raise SystemExit(f"Could not locate v2.7.3 section in {path}")
write(path, c)

print()
print("v2.7.3 runtime patches applied.")
print("Next:")
print("  pnpm install")
print("  pnpm format")
print("  pnpm check")
print("  pnpm exec playwright install chromium")
print("  pnpm test:e2e")
