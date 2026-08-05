from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

GLOBAL_SCRIPTS = {
    '/assets/js/theme-init.js',
    '/assets/js/content.js',
    '/assets/js/site.js',
}

class DocumentMetaParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.description = ''
        self.canonical = ''
        self.body_attrs: dict[str, str | list[str]] = {}

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta' and attr_map.get('name') == 'description':
            self.description = attr_map.get('content', '')
        elif tag == 'link' and attr_map.get('rel') == 'canonical':
            self.canonical = attr_map.get('href', '')
        elif tag == 'body':
            self.body_attrs = {key: value or '' for key, value in attrs}

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title_parts.append(data)

    @property
    def title(self):
        return ' '.join(' '.join(self.title_parts).split()) or 'Data Learning Hub'


def route_for_file(file: Path, source: Path) -> str:
    rel = file.relative_to(source).as_posix()
    if rel == 'index.html': return '/'
    if rel == '404.html': return '/404/'
    if rel.endswith('/index.html'): return '/' + rel[:-10]
    return '/' + rel[:-5] + '/'


def extract_main(raw: str) -> str:
    start = raw.find('<main')
    end = raw.rfind('</main>')
    if start < 0 or end < 0:
        return '<main id="main-content"></main>'
    return raw[start:end + len('</main>')]


def extract_scripts(raw: str):
    scripts, inline_scripts = [], []
    pattern = re.compile(r'<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>', re.I | re.S)
    for match in pattern.finditer(raw):
        attrs = match.group('attrs')
        src_match = re.search(r'\bsrc=["\']([^"\']+)["\']', attrs, re.I)
        if src_match:
            src = html.unescape(src_match.group(1))
            if src not in GLOBAL_SCRIPTS: scripts.append(src)
        else:
            body = match.group('body').strip()
            if body: inline_scripts.append(body)
    return scripts, inline_scripts


def main() -> None:
    parser = argparse.ArgumentParser(description='Import a generated static Data Learning Hub release into the Next.js route registry.')
    parser.add_argument('source', type=Path, help='Path to the generated static release root')
    parser.add_argument('--project', type=Path, default=Path(__file__).resolve().parents[1], help='Next.js project root')
    args = parser.parse_args()
    source = args.source.resolve()
    project = args.project.resolve()
    pages_dir = project / 'src' / 'generated' / 'pages'
    pages_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    for file in sorted(source.rglob('*.html')):
        route = route_for_file(file, source)
        raw = file.read_text(encoding='utf-8', errors='replace')
        metadata = DocumentMetaParser()
        metadata.feed(raw)
        scripts, inline_scripts = extract_scripts(raw)
        canonical = metadata.canonical or 'https://datalearninghub.netlify.app' + route
        payload = {
            'route': route,
            'title': metadata.title,
            'description': metadata.description,
            'canonical': canonical,
            'bodyAttrs': metadata.body_attrs,
            'mainHtml': extract_main(raw),
            'scripts': scripts,
            'inlineScripts': inline_scripts,
        }
        page_file = hashlib.sha1(route.encode()).hexdigest()[:16] + '.json'
        (pages_dir / page_file).write_text(json.dumps(payload, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        manifest[route] = {
            'file': page_file,
            'title': metadata.title,
            'description': metadata.description,
            'canonical': canonical,
            'bodyAttrs': metadata.body_attrs,
            'scripts': scripts,
        }

    (project / 'src' / 'generated' / 'routes.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Imported {len(manifest)} routes from {source}')

if __name__ == '__main__':
    main()
