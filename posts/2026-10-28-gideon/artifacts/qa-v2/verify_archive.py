"""Verify portable archive bytes and narrow revision; not a native publication gate."""
from pathlib import Path
from hashlib import sha256
import json
import re
from html.parser import HTMLParser
p = Path(__file__).resolve().parents[2]
s = p / 'artifacts/qa-v2/revision-2026-10-28-polish'
entries = json.loads((s / 'archive-manifest.json').read_text())
for e in entries:
    b = (s / e['file']).read_bytes()
    assert len(b) == e['bytes'] and sha256(b).hexdigest() == e['sha256'], e['file']
assert {e['file'] for e in entries} == {str(f.relative_to(s)) for f in s.rglob('*') if f.is_file()} - {'archive-manifest.json'}
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
prior = (p / 'artifacts/qa-v2/revision-2026-10-28-shortened/article.md').read_text()
changes = json.loads((s / 'changes.json').read_text())
assert len(changes) == 4
expected = prior
for change in changes:
    assert expected.count(change['before']) == 1
    expected = expected.replace(change['before'], change['after'], 1)
assert expected == md
assert re.findall(r'^>.*$', prior, re.M) == re.findall(r'^>.*$', md, re.M)
assert re.findall(r'\]\((.*?)\)', prior) == re.findall(r'\]\((.*?)\)', md)
inv = json.loads((s / 'qa-inventory-redacted.json').read_text())
assert len(inv) == 4 and all(re.fullmatch(r'[a-f0-9]{64}', x['sha256']) for x in inv)
assert md.count('https://commons.wikimedia.org/') == 2
receipt = json.loads((s / 'polish-revision-receipt-redacted.json').read_text())
review = json.loads((s / 'independent-reader-review-redacted.json').read_text())
assert receipt['sourceSha256'] == prov['current_approved_markdown_sha256'] == review['source_sha256']
assert receipt['exactNativeSha256'] == prov['private_native_hashes']['exact-native-private.txt']['sha256']
assert receipt['originalPublicationTimeKST'] == '2026-10-28 16:21'
assert '본문 읽기:' not in md
print('PASS: 9 manifest entries / 10 files; exact four replacements from prior shortened source; current body parity; 5 sections / 5 GODpia / 2 Commons; 15 quoted words; unchanged quotations, link targets and image hashes; four narrow-preview hash entries; source/native provenance matches.')
print('NOT CHECKED: absent screenshot pixels/private native bytes/canonical gates; no new full-page QA, live inspection or factual investigation.')
