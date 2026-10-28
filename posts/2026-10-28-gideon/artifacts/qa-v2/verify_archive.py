"""Verify portable archive bytes and narrow revision; not a native publication gate."""
from pathlib import Path
from hashlib import sha256
import json
import re
from html.parser import HTMLParser
p = Path(__file__).resolve().parents[2]
s = p / 'artifacts/qa-v2/revision-2026-10-28-shortened'
entries = json.loads((s / 'archive-manifest.json').read_text())
for e in entries:
    b = (s / e['path']).read_bytes()
    assert len(b) == e['bytes'] and sha256(b).hexdigest() == e['sha256'], e['path']
assert {e['path'] for e in entries} == {str(f.relative_to(s)) for f in s.rglob('*') if f.is_file()} - {'archive-manifest.json'}
md = (s / 'article.md').read_text()
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
prov = json.loads((s / 'source-provenance.json').read_text())
for a in prov['images_unchanged']:
    assert sha256((p / 'assets' / a['file']).read_bytes()).hexdigest() == a['sha256']
inv = json.loads((s / 'qa-screenshot-inventory-redacted.json').read_text())
report = json.loads((s / 'independent-shortened-review-redacted.json').read_text())
assert len(inv) == 30 and {x['file'] for x in inv} == {x['file'] for x in report['screenshots']}
assert all(re.fullmatch(r'[a-f0-9]{64}', x['sha256']) for x in inv)
assert md.count('https://commons.wikimedia.org/') == 2
receipt = json.loads((s / 'shortened-revision-receipt-redacted.json').read_text())
assert receipt['sourceSha256'] == prov['current_approved_markdown_sha256'] == report['md_sha256']
assert receipt['exactNativeSha256'] == report['prepared_sha256']
assert receipt['originalPublicationTimeKST'] == '2026-10-28 16:21'
assert '본문 읽기:' not in md
print('PASS: 9 manifest entries / 10 delta files; current shortened body parity; 5 sections / 5 GODpia / 2 Commons links; 15 quoted words; two unchanged image hashes; 30 current screenshot inventory entries; matching source/native provenance across reports.')
print('NOT CHECKED: absent screenshot pixels/private native bytes/canonical strict gates, producer body-word counting method, fresh live page or new factual-source investigation.')
