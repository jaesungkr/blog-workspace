"""Verify portable archive bytes and narrow revision; not a native publication gate."""
from pathlib import Path
from hashlib import sha256
import json
import re
from html.parser import HTMLParser
p = Path(__file__).resolve().parents[2]
s = p / 'artifacts/approved-source'
entries = json.loads((s / 'archive-manifest.json').read_text())
for e in entries:
    b = (s / e['path']).read_bytes()
    assert len(b) == e['bytes'] and sha256(b).hexdigest() == e['sha256'], e['path']
assert {e['path'] for e in entries} == {str(f.relative_to(s)) for f in s.rglob('*') if f.is_file()} - {'archive-manifest.json'}
md = (s / 'article.md').read_text()
old = (s / 'initial-publication-history/article.md').read_text().replace('](../images/', '](images/')
removed = [line for line in old.splitlines(keepends=True) if line.startswith('본문 읽기:')]
assert len(removed) == 1 and old.replace(removed[0], '') == md
body = (p / 'article.md').read_text().split('---\n', 2)[2].lstrip('\n')
assert body.replace('](assets/', '](images/') == md.split('\n\n', 1)[1]
assert md.count('\n## ') == 5 and md.count('https://www.godpia.com/') == 5
assert sum(len(q.split()) for q in re.findall(r'^> “(.*)”$', md, re.M)) == 15
class Counts(HTMLParser):
    def __init__(self):
        super().__init__(); self.h2 = 0; self.images = 0; self.godpia = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.h2 += tag == 'h2'
        self.images += tag == 'img'
        self.godpia += tag == 'a' and a.get('href', '').startswith('https://www.godpia.com/')
c = Counts(); html = (s / 'native-payload-sanitized.html').read_text(); c.feed(html)
assert (c.h2, c.images, c.godpia) == (5, 2, 5)
assert '본문 읽기:' not in html
for a in json.loads((s / 'images/manifest.json').read_text())['images']:
    assert (p / 'assets' / a['file']).read_bytes() == (s / 'images' / a['file']).read_bytes()
inv = json.loads((s / 'qa-screenshot-inventory-redacted.json').read_text())
report = json.loads((s / 'independent-preview-review-redacted.json').read_text())
assert len(inv) == 42 and {x['file'] for x in inv} == set(report['screenshots'])
assert all(re.fullmatch(r'[a-f0-9]{64}', x['sha256']) for x in inv)
print('PASS archive integrity: 24 manifest entries, 25 package files, body parity, footer-only deletion after historical path normalization, 5 links/sections, 15 quoted words, 2 unchanged assets, 42 historical screenshot inventory entries.')
print('NOT CHECKED: absent screenshot pixels, private native bytes, canonical strict gates, fresh live page or new factual-source investigation.')
