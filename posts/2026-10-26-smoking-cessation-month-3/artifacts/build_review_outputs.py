"""Create author-review deliverables; this is not a publication fragment."""
from pathlib import Path
import base64
import hashlib
import json
import re
import shutil
bundle=Path(__file__).resolve().parents[1]
out=Path('/Users/ja2sng/Documents/Codex/2026-10-26/dev-log-rich-post-workspace-v2/outputs')
out.mkdir(parents=True,exist_ok=True)
slug='smoking-cessation-month-3'
asset=bundle/'assets/smoking-cessation-month-3-hero-v1.png'
image_data='data:image/png;base64,'+base64.b64encode(asset.read_bytes()).decode()
files=[]
for theme,root in [('light','preflight'),('dark','preflight-dark')]:
 src=bundle/f'artifacts/qa-v2/{root}/{slug}-rich-preview.html'
 html=src.read_text().replace('../../../assets/smoking-cessation-month-3-hero-v1.png',image_data)
 name=f'{slug}-review'+('-dark' if theme=='dark' else '')+'.html'
 p=out/name;p.write_text(html);files.append(p)
shutil.copy2(asset,out/asset.name);files.append(out/asset.name)
article=(bundle/'article.md').read_text();body=article.split('---',2)[2].lstrip()
body=body.replace('{{media:smoking-cessation-month-3-hero}}',f'![부러뜨린 담배와 분리된 전자담배 기기]({asset.name})\n\n담배와 전자담배를 내려놓고 금연을 이어 가는 시간을 표현했습니다.')
p=out/f'{slug}-review.md';p.write_text('# 17년 흡연자의 금연 3개월차 후기\n\n'+body);files.append(p)
shutil.copy2(bundle/'artifacts/hero-prompt-v1.txt',out/'hero-prompt-v1.txt');files.append(out/'hero-prompt-v1.txt')
record={'stage':'author-review','lifecycle':'reviewing','publication_approved':False,'source_pass':'artifacts/qa-v2/source-pass.json','hero_review':'artifacts/qa-v2/hero-review.md','local_preflight':'artifacts/qa-v2/local-preflight-browser.json','outputs':[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],'next':'Author approves this specific source and media and explicitly asks to publish; then bind native Tistory media and run remote/final-page/publication gates.'}
(bundle/'artifacts/qa-v2/review-handoff.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('\n'.join(str(p) for p in files))
