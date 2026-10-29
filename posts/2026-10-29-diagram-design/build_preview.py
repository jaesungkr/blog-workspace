from pathlib import Path
import base64
import html
import json
import mimetypes
import re
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'article-draft.md').read_text()
title = source.splitlines()[0].removeprefix('# ').strip()

def inline(s):
    s = html.escape(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
    return s

out = []
lines = source.splitlines()
i = 0
while i < len(lines):
    line = lines[i]
    if not line.strip():
        i += 1
        continue
    if line.startswith('```'):
        code = []
        i += 1
        while i < len(lines) and not lines[i].startswith('```'):
            code.append(lines[i]); i += 1
        out.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
        i += 1
        continue
    if line in ['<details>', '</details>'] or line.startswith('<summary>'):
        out.append(line); i += 1; continue
    if line == '---':
        out.append('<hr>'); i += 1; continue
    match = re.match(r'^(#{1,3}) (.+)$', line)
    if match:
        level = len(match[1])
        out.append(f'<h{level}>{inline(match[2])}</h{level}>')
        i += 1; continue
    match = re.match(r'^!\[([^\]]+)\]\(([^)]+)\)$', line)
    if match:
        image_path = ROOT / match[2]
        raw = image_path.read_bytes()
        mime = mimetypes.guess_type(image_path)[0] or 'application/octet-stream'
        if mime == 'image/svg+xml':
            svg_root = ET.fromstring(raw)
            viewbox = [float(v) for v in svg_root.attrib['viewBox'].split()]
            image_width, image_height = (int(viewbox[2]), int(viewbox[3]))
        else:
            with Image.open(image_path) as opened_image:
                image_width, image_height = opened_image.size
        data = 'data:' + mime + ';base64,' + base64.b64encode(raw).decode()
        alt = html.escape(match[1], quote=True)
        figure_classes = ['portrait'] if image_height > image_width else []
        if 'moving-' in image_path.name:
            figure_classes.append('moving')
        if image_path.name == '04-github-diagram-types.png':
            figure_classes.append('reference')
        figure_class = ' class="' + ' '.join(figure_classes) + '"' if figure_classes else ''
        out.append(f'<figure{figure_class}><button class="diagram" type="button" aria-label="이미지 크게 보기: {alt}"><img src="{data}" alt="{alt}" width="{image_width}" height="{image_height}" loading="lazy"></button><span class="zoom-hint" aria-hidden="true">이미지를 누르면 크게 볼 수 있습니다</span></figure>')
        i += 1
        if i < len(lines) and not lines[i]: i += 1
        if i < len(lines) and lines[i].startswith('*'):
            out[-1] = out[-1].replace('</figure>', '<figcaption>' + inline(lines[i]) + '</figcaption></figure>')
            i += 1
        continue
    if re.match(r'^\d+\. ', line):
        items = []
        while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
            items.append('<li>' + inline(re.sub(r'^\d+\. ', '', lines[i])) + '</li>')
            i += 1
        out.append('<ol>' + ''.join(items) + '</ol>'); continue
    if line.startswith('- '):
        items = []
        while i < len(lines) and lines[i].startswith('- '):
            items.append('<li>' + inline(lines[i][2:]) + '</li>')
            i += 1
        out.append('<ul>' + ''.join(items) + '</ul>'); continue
    if line.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[-:| ]+\|$', lines[i + 1]):
        cells = lambda row: [cell.strip() for cell in row.strip('|').split('|')]
        headers = cells(line)
        i += 2
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            rows.append('<tr>' + ''.join('<td>' + inline(c) + '</td>' for c in cells(lines[i])) + '</tr>')
            i += 1
        out.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in headers) + '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>')
        continue
    if line.startswith('> '):
        quoted = []
        while i < len(lines) and lines[i].startswith('> '):
            quoted.append(inline(lines[i][2:])); i += 1
        out.append('<blockquote><p>' + '<br>'.join(quoted) + '</p></blockquote>'); continue
    para = [line]
    i += 1
    while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '>', '<', '```')):
        para.append(lines[i]); i += 1
    out.append('<p>' + inline(' '.join(para)) + '</p>')

styles = r'''
:root { color-scheme: light dark; --paper:#fff; --ink:#25282b; --muted:#667078; --rule:#dfe3e6; --soft:#f4f6f8; --link:#2e5d7c; }
* { box-sizing:border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans CJK KR","Malgun Gothic",sans-serif; font-size:17px; line-height:1.9; word-break:keep-all; overflow-wrap:anywhere; }
main { max-width:850px; margin:auto; padding:56px 32px 84px; }
.draft { color:var(--muted); font-size:13px; letter-spacing:.03em; margin:0 0 20px; }
h1 { font-size:39px; line-height:1.4; letter-spacing:-.04em; margin:0 0 34px; font-weight:750; }
h2 { font-size:25px; line-height:1.45; letter-spacing:-.03em; margin:60px 0 20px; }
h3 { font-size:20px; line-height:1.5; letter-spacing:-.02em; margin:38px 0 14px; }
p { margin:0 0 19px; }
strong { font-weight:700; }
a { color:var(--link); text-decoration-thickness:1px; text-underline-offset:4px; }
blockquote { margin:20px 0 24px; padding:4px 0 4px 20px; border-left:3px solid var(--rule); color:var(--ink); }
blockquote p { margin:0; }
figure { margin:28px 0 30px; }
figure.portrait { max-width:520px; margin-inline:auto; }
figure.moving { max-width:440px; }
figure.reference { max-width:716px; margin-inline:auto; }
.diagram { display:block; background:transparent; border:0; padding:0; width:100%; cursor:zoom-in; }
.diagram img { display:block; width:100%; height:auto; }
.zoom-hint { display:block; text-align:right; color:var(--muted); font-size:12px; margin-top:6px; }
figcaption { font-size:13px; color:var(--muted); line-height:1.7; margin-top:7px; }
figcaption em { font-style:normal; }
ol,ul { margin:20px 0; padding-left:25px; }
li { padding-left:3px; margin:9px 0; }
.table-wrap { width:100%; overflow-x:auto; margin:24px 0; }
table { width:100%; border-collapse:collapse; table-layout:fixed; font-size:15px; line-height:1.65; }
th,td { padding:12px 14px; text-align:left; vertical-align:top; border-bottom:1px solid var(--rule); overflow-wrap:anywhere; }
th { background:var(--soft); font-weight:650; }
th:first-child { width:36%; }
code { font-family:ui-monospace,SFMono-Regular,Consolas,monospace; font-size:.86em; background:var(--soft); padding:2px 4px; border-radius:3px; }
pre { padding:18px 20px; background:var(--soft); overflow:auto; line-height:1.65; }
pre code { padding:0; background:none; white-space:pre; }
details { margin:24px 0; padding:16px 0; border-block:1px solid var(--rule); }
summary { cursor:pointer; font-size:15px; font-weight:650; }
details[open] summary { margin-bottom:18px; }
details p { font-size:15px; }
hr { border:0; border-top:1px solid var(--rule); margin:40px 0 24px; }
hr ~ p { color:var(--muted); font-size:13px; line-height:1.7; }
dialog { max-width:96vw; width:1240px; max-height:94vh; padding:16px; border:1px solid var(--rule); background:var(--paper); color:var(--ink); }
dialog::backdrop { background:#000b; }
.modal-bar { display:flex; gap:12px; justify-content:flex-end; margin-bottom:12px; }
.modal-bar button { border:1px solid var(--rule); background:var(--soft); color:var(--ink); padding:9px 14px; font:inherit; font-size:14px; cursor:pointer; }
.modal-scroll { overflow:auto; max-height:78vh; }
.modal-scroll img { width:100%; height:auto; display:block; }
.modal-scroll img.original { width:var(--image-native-width,1180px); max-width:none; }
@media (prefers-color-scheme:dark) { :root { --paper:#171b1e; --ink:#e7eaed; --muted:#a2adb5; --rule:#424b52; --soft:#232a2f; --link:#a7cde9; } }
@media (max-width:600px) { body { font-size:16px; line-height:1.85; } main { padding:32px 22px 60px; } h1 { font-size:29px; margin-bottom:27px; } h2 { font-size:23px; margin-top:44px; } h3 { font-size:19px; margin-top:30px; } blockquote { padding-left:15px; } figure { margin-inline:-4px; } .draft {font-size:12px;} }
@media print { .draft,.zoom-hint,dialog { display:none; } main { max-width:none; padding:0; } body { color:#000; background:#fff; font-size:11pt; } h2,h3 {break-after:avoid;} figure {break-inside:avoid;} a {color:#000;} details {display:block;} }
'''
script = r'''
const dialog=document.querySelector('dialog');
const expanded=document.querySelector('#expanded-image');
document.querySelectorAll('.diagram').forEach(button=>button.addEventListener('click',()=>{
  const original=button.querySelector('img');
  expanded.src=original.src; expanded.alt=original.alt;
  expanded.style.setProperty('--image-native-width',original.naturalWidth+'px');
  expanded.classList.remove('original');
  document.querySelector('#size-toggle').textContent='원본 크기로 보기';
  dialog.showModal();
}));
document.querySelector('#close-image').addEventListener('click',()=>dialog.close());
document.querySelector('#size-toggle').addEventListener('click',event=>{
  expanded.classList.toggle('original');
  event.target.textContent=expanded.classList.contains('original')?'화면에 맞추기':'원본 크기로 보기';
});
dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
'''
license_text = (ROOT / 'images/LICENSE-diagram-design.txt').read_text()
document = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · dev.log</title><meta name="description" content="현업에서 자주 활용하는 diagram-design AI 스킬 소개와 비개발자도 따라갈 수 있는 사용법."><style>{styles}</style></head>
<body><main><p class="draft">dev.log · 스킬 소개 초안</p><article>{''.join(out)}</article></main>
<dialog aria-label="다이어그램 크게 보기"><div class="modal-bar"><button id="size-toggle" type="button">원본 크기로 보기</button><button id="close-image" type="button">닫기</button></div><div class="modal-scroll"><img id="expanded-image" alt=""></div></dialog><script>{script}</script>
<!-- Diagram Design upstream license retained with this article and its adapted diagrams:\n{license_text.replace('--','—')} -->
</body></html>'''
(ROOT / 'diagram-design-article-review.html').write_text(document)
(ROOT / 'build-summary.json').write_text(json.dumps({
    'article_word_count_whitespace':len(source.split()),
    'article_char_count':len(source),
    'html_bytes':len(document.encode()),
    'embedded_image_count':sum(1 for item in out if item.startswith('<figure')),
    'external_assets':False,
    'publication_status':'private draft only',
    'installation_tested':False,
    'visual_examples_provenance':json.loads((ROOT/'examples-provenance.json').read_text()) if (ROOT/'examples-provenance.json').exists() else 'See article captions and production notes'
}, ensure_ascii=False, indent=2))
print(ROOT / 'diagram-design-article-review.html')
