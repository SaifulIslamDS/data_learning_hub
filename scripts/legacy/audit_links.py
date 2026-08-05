from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs: list[tuple[str,str]] = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag in {'a','link'} and data.get('href'):
            self.refs.append(('href', data['href']))
        if tag in {'script','img','source'} and data.get('src'):
            self.refs.append(('src', data['src']))


def resolve(source: Path, ref: str) -> Path | None:
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc or ref.startswith(('mailto:','tel:','javascript:','#')):
        return None
    path = unquote(parts.path)
    if not path:
        return None
    target = ROOT / path.lstrip('/') if path.startswith('/') else source.parent / path
    target = target.resolve()
    if target.is_dir():
        target = target / 'index.html'
    elif not target.suffix and (target / 'index.html').exists():
        target = target / 'index.html'
    return target

broken=[]
checked=0
for source in ROOT.rglob('*.html'):
    parser=Parser()
    parser.feed(source.read_text(encoding='utf-8', errors='replace'))
    for kind,ref in parser.refs:
        target=resolve(source,ref)
        if target is None:
            continue
        checked+=1
        try:
            target.relative_to(ROOT)
        except ValueError:
            broken.append((source.relative_to(ROOT),ref,'outside project'))
            continue
        if not target.exists():
            broken.append((source.relative_to(ROOT),ref,str(target.relative_to(ROOT))))

print(f'Checked {checked} local HTML and asset references across {len(list(ROOT.rglob("*.html")))} HTML files.')
if broken:
    for source,ref,target in broken:
        print(f'BROKEN: {source} -> {ref} ({target})')
    raise SystemExit(f'{len(broken)} broken references found.')
print('0 broken local references found.')
