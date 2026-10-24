from pathlib import Path
import re,json,html
p=Path(__file__).resolve().parent.parent
original=(p/'artifacts/original/editor-before.html').read_text()
body=(p/'artifacts/candidate-body.html').read_text()
css=re.search(r'<style>(.*?)</style>',original,re.S).group(1)
css+='''
.devlog-dark-compatible th {background:var(--devlog-soft-bg)!important;}
.devlog-dark-compatible table thead + tbody tr:first-child > td {background:transparent!important;font-weight:400;}
.devlog-dark-compatible :not(pre) > code {color:var(--devlog-code-text)!important;background:var(--devlog-soft-bg)!important;overflow-wrap:anywhere;}
.devlog-dark-compatible .devlog-table-scroll {margin:1.5em 0;}
.devlog-dark-compatible h3 {scroll-margin-top:80px;}
'''
# Preserve the native attachment references rather than publishing expiring CDN links.
image_macro=re.search(r'\[##_Image\|.*?_##\]',original,re.S).group(0)
image_macro=image_macro.replace('"style":"alignCenter"','"style":"alignCenter","alt":"제작사가 공개한 VibeThinker-3B 수학·코딩 평가 비교 화면"')
file_macro=re.search(r'\[##_File\|.*?_##\]',original,re.S).group(0)
body,n=re.subn(r'<p[^>]*><img\b[^>]*></p>',lambda m:image_macro,body)
assert n==1,n
body,n=re.subn(r'<li[^>]*><a\b[^>]*>이 블로그의 기존 실행 로그\(cmd\.txt\)</a></li>','<li>이 블로그의 기존 실행 로그는 아래 첨부 파일에서 확인할 수 있습니다.</li>',body)
assert n==1,n
body=re.sub(r'(<table\b.*?</table>)',r'<div class="devlog-table-scroll">\1</div>',body,flags=re.S)
fragment='<div>\n<style>'+css+'</style>\n</div>\n<article class="devlog-dark-compatible">\n'+body+'\n'+file_macro+'\n</article>\n'
(p/'artifacts/tistory-fragment.html').write_text(fragment)
# Local preview replaces only native media markup with already observed public URLs.
r=json.loads((p/'artifacts/original/public-record.json').read_text())
preview=fragment.replace(image_macro,'<img alt="제작사가 공개한 VibeThinker-3B 수학·코딩 평가 비교 화면" style="width:100%;height:auto" src="'+html.escape(r['images'][0]['src'],quote=True)+'">')
log=next(x['href'] for x in r['links'] if 'cmd.txt' in x['text'])
preview=preview.replace(file_macro,'<p><a href="'+html.escape(log,quote=True)+'">cmd.txt · 기존 실행 로그 다운로드</a></p>')
base='''<!doctype html><html lang="ko" {theme}><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VibeThinker-3B 개정 원고</title><style>body{{margin:0;background:{bg};font-family:Arial,"Apple SD Gothic Neo",sans-serif;}}main{{max-width:{width}px;margin:0 auto;padding:28px 20px;box-sizing:border-box;}}h1{{font-size:25px;line-height:1.5;color:{color};margin:0 0 36px;}}img{{max-width:100%;}}</style><main><h1>VibeThinker-3B 사용 후기 - 맥북 실험과 한국어 한계</h1>{body}</main></html>'''
for name,width,theme,bg,color in [('desktop-dark',820,'class="dark"','#1c1c1e','#f2f2f7'),('mobile-light',390,'','#ffffff','#333333')]:
 (p/f'artifacts/preview-{name}.html').write_text(base.format(width=width,theme=theme,bg=bg,color=color,body=preview))
print('Native image macros:',fragment.count('[##_Image|'),'file macros:',fragment.count('[##_File|'),'tables:',fragment.count('<table '))
