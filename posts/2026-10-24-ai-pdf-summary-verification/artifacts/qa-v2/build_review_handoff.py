# -*- coding: utf-8 -*-
"""Export an author-review candidate. This does not create a publishable fragment."""
import argparse
import base64
import hashlib
import html
import json
import re
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--output-dir', required=True)
args = parser.parse_args()
post = Path(__file__).resolve().parents[2]
out = Path(args.output_dir).resolve()
out.mkdir(parents=True, exist_ok=True)
(out / 'media').mkdir(exist_ok=True)
slug = 'ai-pdf-summary-verification'
manifest = json.loads((post / 'media.json').read_text())
category = 'AI·개발 → AI 이해·활용'
for item in manifest['items']:
    shutil.copy2(post / item['publish_path'], out / 'media' / Path(item['publish_path']).name)

for theme, folder, suffix in [('light', 'preflight', 'review'), ('dark', 'preflight-dark', 'review-dark')]:
    source = post / 'artifacts' / 'qa-v2' / folder / f'{slug}-rich-preview.html'
    markup = source.read_text()
    def image_data(match):
        path = (source.parent / html.unescape(match.group(1))).resolve()
        if not path.is_relative_to(post / 'assets'):
            raise ValueError('Preview image is outside the approved assets directory')
        return 'src="data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode() + '"'
    markup = re.sub(r'src="([^\"]+)"', image_data, markup)
    markup = markup.replace('<p>Log</p>', '<p>' + html.escape(category) + '</p>', 1)
    nav = '''<nav style="max-width:1040px;margin:18px auto 0;padding:0 20px;font:14px/1.7 system-ui,sans-serif;color:inherit">검토용 원고 · <a style="color:inherit" href="ai-pdf-summary-verification-review.html">밝은 화면</a> / <a style="color:inherit" href="ai-pdf-summary-verification-review-dark.html">어두운 화면</a></nav>'''
    markup = markup.replace('<body>', '<body>\n' + nav, 1)
    (out / f'{slug}-{suffix}.html').write_text(markup)

raw = (post / 'article.md').read_text()
body = raw.split('---', 2)[2].lstrip()
by_id = {item['id']: item for item in manifest['items']}
def markdown_image(match):
    item = by_id[match.group(1)]
    path = out / 'media' / Path(item['publish_path']).name
    return '![' + item['alt'] + '](' + str(path) + ')\n\n' + item['caption']
body = re.sub(r'\{\{media:([a-z0-9-]+)\}\}', markdown_image, body)
(out / f'{slug}.md').write_text('# AI에게 PDF 요약을 맡겨도 될까?\n\n분류: ' + category + '\n\n' + body)
record = {
    'stage': 'author_review',
    'lifecycle': 'reviewing',
    'source_pass_sha256': hashlib.sha256((post / 'artifacts/qa-v2/source-pass.json').read_bytes()).hexdigest(),
    'source_article_sha256': hashlib.sha256((post / 'article.md').read_bytes()).hexdigest(),
    'publication_category': category,
    'media': {item['id']: item['sha256'] for item in manifest['items']},
    'outputs': {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in out.glob(f'{slug}*') if path.is_file()},
    'pending': ['author approval and instruction to publish', 'native Tistory image attachment binding', 'remote media observation', 'independent final light/dark page gate', 'live publication and verification'],
    'note': 'Review HTML embeds the approved local media and shows the requested publication category in the preview header. Publication body text is unchanged. No paste-ready or final-page pass is asserted.'
}
(post / 'artifacts/qa-v2/user-handoff.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out / f'{slug}-review.html')
