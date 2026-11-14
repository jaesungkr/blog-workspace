# -*- coding: utf-8 -*-
from pathlib import Path
import base64,json,hashlib,re,sys,shutil
post=Path(__file__).resolve().parents[2];repo=post.parents[1];out=post/'delivery';out.mkdir(exist_ok=True)
slug='ai-glasses-products-exam-rules'
for theme in ('light','dark'):
 source=post/f'artifacts/qa-v2/local-{theme}/{slug}-rich-preview.html';html=source.read_text()
 for item in json.loads((post/'media.json').read_text())['items']:
  f=post/item['publish_path'];typ='image/webp' if f.suffix=='.webp' else 'image/jpeg';data='data:'+typ+';base64,'+base64.b64encode(f.read_bytes()).decode()
  html=html.replace('../../../'+item['publish_path'],data)
 assert '__TISTORY_' not in html and 'file:' not in html
 (out/f'{slug}-review-{theme}.html').write_text(html)
fragment=(post/f'artifacts/qa-v2/local-light/{slug}-tistory-fragment.html').read_bytes()
(out/f'{slug}-tistory-fragment.txt').write_bytes(fragment)
shutil.copy2(post/'article.md',out/f'{slug}-draft.md')
(out/'읽어주세요.txt').write_text('AI 안경 초안 검토본 | 2026-11-14\n\nreview-light.html / review-dark.html: 사진을 포함한 단일 파일. 휴대폰 브라우저로 열 수 있습니다. 넓은 표는 표 안에서 좌우로 움직입니다.\ndraft.md: 수정 가능한 원고.\ntistory-fragment.txt: 정식 v2 렌더러의 현재 초안 HTML과 동일합니다. 이미지 업로드 전 자리표시자가 있어 최종 발행용이 아닙니다. 본문 승인과 사진 업로드 후 원본 이미지 첨부를 연결해야 합니다.\n\n현재 상태: reviewing. 티스토리 게시·Git 커밋·push는 하지 않았습니다. Instagram 링크는 접근 제한으로 보지 못했으며 내용과 사진을 인용하지 않았습니다.\n')
files={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in out.iterdir() if f.is_file()}
(out/'review-integrity.json').write_text(json.dumps({'canonical_renderer':'.agents/skills/dev-log-rich-post-workspace-v2/scripts/render_rich_post_v2.py','renderer_sha256':hashlib.sha256((repo/'.agents/skills/dev-log-rich-post-workspace-v2/scripts/render_rich_post_v2.py').read_bytes()).hexdigest(),'canonical_css_sha256':hashlib.sha256((repo/'.agents/skills/dev-log-rich-post-workspace/assets/rich-post.css').read_bytes()).hexdigest(),'modification':'preview image src only converted from relative local files to identical embedded bytes; canonical CSS/prose/DOM retained','files':files},ensure_ascii=False,indent=2)+'\n')
print('standalone review files created')
