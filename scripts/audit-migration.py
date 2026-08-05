from pathlib import Path
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
import json
import sys

class ReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        attr_map = dict(attrs)
        if tag == 'a' and attr_map.get('href'):
            self.references.append(attr_map['href'])
        elif tag in {'img', 'source', 'video', 'audio'} and attr_map.get('src'):
            self.references.append(attr_map['src'])

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'src' / 'generated' / 'routes.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
errors: list[str] = []
reference_count = 0

if len(manifest) != 549:
    errors.append(f'Expected 549 migrated routes, found {len(manifest)}')

native_routes = {'/offline/'}
known_routes = set(manifest) | native_routes

for route, record in manifest.items():
    page_path = root / 'src' / 'generated' / 'pages' / record['file']
    if not page_path.exists():
        errors.append(f'Missing page data for {route}: {record["file"]}')
        continue
    page = json.loads(page_path.read_text(encoding='utf-8'))
    if page.get('route') != route:
        errors.append(f'Route mismatch: {route}')
    if not page.get('title'):
        errors.append(f'Missing title: {route}')
    if '<main' not in page.get('mainHtml', ''):
        errors.append(f'Missing main content: {route}')

    for src in page.get('scripts', []):
        reference_count += 1
        if src.startswith('/') and not (root / 'public' / src.lstrip('/')).exists():
            errors.append(f'Missing local script {src} for {route}')

    parser = ReferenceParser()
    try:
        parser.feed(page.get('mainHtml', ''))
    except Exception as exc:
        errors.append(f'Unable to parse references in {route}: {exc}')
        continue

    for value in parser.references:
        reference_count += 1
        if value.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:', 'blob:')):
            continue
        parsed = urlparse(value)
        if parsed.scheme in {'http', 'https'}:
            continue
        absolute_path = urlparse(urljoin(f'https://datalearninghub.netlify.app{route}', value)).path
        if absolute_path.startswith(('/assets/', '/icons/')):
            if not (root / 'public' / absolute_path.lstrip('/')).exists():
                errors.append(f'Missing asset {absolute_path} linked from {route}')
            continue
        if absolute_path in {'/sw.js', '/manifest.webmanifest', '/robots.txt', '/sitemap.xml'}:
            continue
        normalized = absolute_path if absolute_path.endswith('/') else absolute_path + '/'
        if normalized not in known_routes:
            errors.append(f'Missing route {normalized} linked from {route}')

required = [
    root / 'app' / 'layout.tsx',
    root / 'app' / '[...slug]' / 'page.tsx',
    root / 'public' / 'sw.js',
    root / 'public' / 'icons' / 'icon-192.png',
    root / 'public' / 'icons' / 'icon-512.png',
    root / 'netlify.toml',
    root / 'pnpm-lock.yaml',
]
for item in required:
    if not item.exists():
        errors.append(f'Missing required file: {item.relative_to(root)}')

if errors:
    for error in errors[:200]:
        print(f'ERROR: {error}')
    if len(errors) > 200:
        print(f'ERROR: {len(errors)-200} additional errors omitted')
    sys.exit(1)

print(f'Validated {len(manifest)} migrated Next.js routes.')
print(f'Checked {reference_count} local page/script references with 0 broken references.')
print('All page payloads, local scripts, PWA files, lockfile bootstrap, and deployment files are present.')
