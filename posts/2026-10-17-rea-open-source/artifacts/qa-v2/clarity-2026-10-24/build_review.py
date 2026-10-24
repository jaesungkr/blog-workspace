from pathlib import Path
import base64
import hashlib
import html
import json
import re

QA = Path(__file__).resolve().parent
POST = QA.parents[2]
OUT = Path('/Users/ja2sng/Documents/Codex/2026-10-24/d-2/outputs')
manifest = json.loads((POST / 'media.json').read_text())
preview = (QA / 'preflight/rea-open-source-rich-preview.html').read_text()
assets = {Path(item['publish_path']).name: item for item in manifest['items']}
def embed(match):
    name = Path(match[2]).name
    item = assets[name]
    path = POST / item['publish_path']
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    mime = 'image/png' if raw.startswith(b'\x89PNG') else 'image/jpeg'
    return match[1] + 'data:' + mime + ';base64,' + base64.b64encode(raw).decode() + match[3]
preview = re.sub(r'(<img\b[^>]*\bsrc=")([^"]+)("[^>]*>)', embed, preview)
license_text = (POST / 'assets/REA-LICENSE.txt').read_text().strip()
notice = '<details class="review-license"><summary>대표 이미지 출처와 MIT License</summary><p>REA 공식 소개 카드 · Copyright (c) 2026 morluto. <a href="https://github.com/morluto/rea/blob/0c7b6d834af2d044b23196e0e522cc2468327a1e/website/public/assets/social-card.svg">원본</a></p><pre>' + html.escape(license_text) + '</pre></details>'
preview = preview.replace('</article>', '</article>' + notice)
style = '<style>.review-toolbar,.review-license{box-sizing:border-box;width:min(980px,100%);margin:20px auto;padding:16px 24px;font:14px/1.6 system-ui,sans-serif}.review-toolbar{display:flex;justify-content:space-between;gap:16px;border-bottom:1px solid #d8d8df}.review-toolbar button{font:inherit;padding:6px 12px;cursor:pointer;border:1px solid #b8b8bf;border-radius:8px;background:transparent;color:inherit}.review-license pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.6 monospace}.review-license summary{cursor:pointer}</style>'
preview = preview.replace('</head>', style + '</head>')
preview = preview.replace('<body>', '<body><div class="review-toolbar"><span>REA의 역할과 조사 과정을 다시 구성한 원고</span><button type="button" id="review-theme">어두운 화면으로 보기</button></div>', 1)
preview = preview.replace('</body>', '<script>document.getElementById("review-theme").addEventListener("click",function(){const dark=document.documentElement.classList.toggle("dark");this.textContent=dark?"밝은 화면으로 보기":"어두운 화면으로 보기";});</script></body>')
assert len(re.findall(r'<img\b', preview)) == 3
assert not re.search(r'/Users/|file://|src="(?:\.\./|assets/)', preview)
OUT.mkdir(exist_ok=True)
(QA / 'review.html').write_text(preview)
(OUT / 'rea-review.html').write_text(preview)
(OUT / 'rea-revised-article.md').write_text((POST / 'article.md').read_text().split('---', 2)[2].lstrip())
for item in manifest['items'][1:]:
    source = POST / item['publish_path']
    (OUT / source.name).write_bytes(source.read_bytes())
(OUT / 'rea-csv-diagram.html').write_bytes((QA.parent / 'visuals-2026-10-24/rea-csv-escaping-v2.html').read_bytes())
(OUT / 'rea-notes-flow-prompt.txt').write_bytes((QA.parent / 'visuals-2026-10-24/notes-flow-prompt-v1.txt').read_bytes())
record = {'stage': 'author review candidate; not published', 'review_sha256': hashlib.sha256(preview.encode()).hexdigest(), 'source_pass_sha256': hashlib.sha256((POST / 'artifacts/qa-v2/source-pass.json').read_bytes()).hexdigest(), 'media': {item['id']: item['sha256'] for item in manifest['items']}, 'self_contained_images': 3, 'pending': ['specific candidate publication approval', 'native attachment binding', 'remote observations and final-page gate', 'Tistory preview and live verification']}
(QA / 'author-review-handoff.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('Self-contained review built with three verified local image assets.')
