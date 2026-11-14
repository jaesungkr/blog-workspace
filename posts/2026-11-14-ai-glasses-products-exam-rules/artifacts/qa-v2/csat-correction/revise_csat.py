# -*- coding: utf-8 -*-
from pathlib import Path
import json,shutil,hashlib
post=Path('/Users/ja2sng/dev/blog-workspace/posts/2026-11-14-ai-glasses-products-exam-rules');qa=post/'artifacts/qa-v2/csat-correction';qa.mkdir(exist_ok=True)
for name in ['article.md','evidence.md']:
 shutil.copy2(post/name,qa/('before-'+name))
shutil.copy2(post/'artifacts/qa-v2/source-pass.json',qa/'before-source-pass.json')
f=post/'article.md';s=f.read_text()
s=s.replace('| 2027학년도 수능 | 스마트안경 명시 | 단순 소지는 당해 시험 무효. 사용·착용은 당해 시험 무효와 다음 해 응시자격 박탈 |','| 2027학년도 수능 | 스마트안경 명시 | 가져왔다면 1교시 전 제출. 미제출 소지 적발 시 당해 시험 무효. 시험 중 사용·착용 시 당해 무효·다음 해 응시자격 박탈 |')
old='수능은 [교육부의 스마트안경 안내](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=340&boardSeq=107580&lev=0&m=0202&opType=N&page=1&s=moe)가 단순 소지와 사용을 나눠 설명한다. 사용에는 착용도 포함된다. 감독관의 확인 요구에 응하지 않는 경우도 심의를 거쳐 당해 시험 무효와 다음 해 응시자격 박탈 대상이 된다. ‘전원을 껐으니 착용해도 된다’는 식으로 판단해서는 안 된다.'
new='''수능에 스마트안경을 실수로 가져왔다면 **1교시 시작 전 감독관의 지시에 따라 제출해야 한다.** [공식 Q&A의 ‘시험 응시’ 03번](https://www.ice.go.kr/upload/ice/na/bbs_1482/2026/04/b38c68a1f07bfba215f2107e1e040910.pdf)은 반입 금지 물품을 제출한 뒤 응시하는 모든 영역·과목의 시험이 끝나면 돌려받도록 안내한다. [교육부의 11월 9일 안내](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107599&lev=0&m=020402&s=moe)도 스마트안경을 반입 금지 목록에 넣고, 제출하지 않은 채 계속 가지고 있다가 적발되면 당해 시험이 무효가 된다고 명시한다.

시험 중 사용·착용과 확인 요구 불응은 별도로 처리한다. [교육부의 스마트안경 대응계획](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107520&lev=0&m=020402&s=moe)에 따르면, 시험 중 스마트안경을 사용하면 착용만 한 경우까지 포함해 당해 시험이 무효가 되고 다음 해 응시자격도 박탈된다. 감독관의 확인 요구에 응하지 않는 경우에는 심의를 거쳐 같은 제재를 받는다.'''
assert old in s;s=s.replace(old,new)
s=s.replace('  - https://www.ets.org/pdfs/toefl/toefl-ibt-bulletin.pdf','  - https://www.ets.org/pdfs/toefl/toefl-ibt-bulletin.pdf\n  - https://www.ice.go.kr/upload/ice/na/bbs_1482/2026/04/b38c68a1f07bfba215f2107e1e040910.pdf\n  - https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107599&lev=0&m=020402&s=moe\n  - https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107520&lev=0&m=020402&s=moe')
f.write_text(s)
claims=post/'artifacts/claims.json';d=json.loads(claims.read_text());d['sources'].update({'csat-qa':'https://www.ice.go.kr/upload/ice/na/bbs_1482/2026/04/b38c68a1f07bfba215f2107e1e040910.pdf','csat-plan':'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107520&lev=0&m=020402&s=moe','csat-notice':'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107599&lev=0&m=020402&s=moe'})
for x in d['claims']:
 if x['id']=='E01':
  x.update(claim='수능 실수 반입 물품은1교시 전 감독관 제출·전영역 종료후 반환. 미제출 소지 적발은 당해 무효. 시험 중 사용·착용은 당해 무효+다음해 자격박탈. 확인 불응은 심의 후 같은 제재',source_id='csat-notice',supplementary_source_ids=['csat-qa','csat-plan'],basis_and_limit='Q&A IV시험응시03(인쇄/PDF46쪽), 10/29스마트안경 대응계획 및 11/9교육부 수험생안내 HWPX 원본 대조. 원래 카드의 단순소지 요약만으로 제출전 실수반입까지 무효로 일반화하지 않는다. 별도 제출면제절차는 이 자료들에 없으며, 11/9한문서가 스마트안경 명시와1교시전 제출절차를 함께 안내한다.')
claims.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
e=post/'evidence.md';t=e.read_text();lines=t.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| E01 |'):
  lines[i]='| E01 | 실수 반입은1교시전 제출·전영역 종료후 반환, 미제출 소지 적발은 당해무효, 시험 중 사용·착용은 다음해 자격박탈 추가, 확인불응은심의 | [Q&A03](https://www.ice.go.kr/upload/ice/na/bbs_1482/2026/04/b38c68a1f07bfba215f2107e1e040910.pdf), [교육부11/9](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107599&lev=0&m=020402&s=moe), [스마트안경10/29계획](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=107520&lev=0&m=020402&s=moe) | PDF46쪽과 HWPX 원본 직접대조. 제출 전 실수반입을 무효로 일반화하지 않으며, 시험 중 착용과 검사불응의 심의 조건을 분리한다. |'
t='\n'.join(lines)+'\n';t+='''\n## 수능 제출 조건 정정\n기존 표의 ‘단순 소지는 당해 시험 무효’에는1교시전 제출절차가 빠져 있었다. 사용자 지적후 공식 Q&A03(PDF46쪽)을 다운로드해 텍스트와 실제 렌더를 확인했다. 2026-10-29별도 대응계획 및11-09최신안내 HWPX원문도 다운로드·XML텍스트로 대조했다.\n4월 Q&A는 실수반입 시1교시전 제출/시험종료후반환을 안내한다. 10/29계획의 단순소지 도표만으로 그절차가 없어진다고 해석할 수 없다. 11/9교육부 안내는 스마트안경을 반입금지 목록에 넣고, 같은 문서에서1교시전 수거와 미제출 소지 적발의 시험무효를 명시하며, 시험중착용/확인불응을 별도 안내한다. 11/9충북교육청 공식 발표도 스마트안경과 제출절차를 함께 명시한다. 별도 제출면제나 대체수거절차는 확인한 자료에 없었다.\n이전 근거와 원고는 artifacts/qa-v2/csat-correction/before-*에 역사적 기록으로 보존하며 현재 검토본의 근거로 쓰지 않는다.\n''';e.write_text(t)
a=post/'audit.md';a.write_text(a.read_text()+'''\n## 수능 제출 조건 수정: 재검증 중\n사용자 지적에 따라 기존 수능 표의 제출 조건 누락을 확인했다. 이전 source/local/PDF pass는 이전 원고에 대한 역사적 기록이며 수정본을 승인하지 않는다.\n- 전: ‘단순 소지는 당해 시험 무효.’\n- 후: ‘가져왔다면1교시전 제출. 미제출 소지 적발 시 당해 시험 무효.’\n- 본문을 실수반입→1교시전 제출→모든영역종료후 반환→미제출적발 제재 순서로 보완했다. 다음문단은 시험중사용·착용과 확인불응의 심의 절차를 맡아 서로 다른 조건을 분리했다.\nQ&A46쪽실물과10/29·11/9교육부HWPX원본으로 대조했으며 다른제품/시험사실은 보존했다. 수정한두문단과 직전표·직후SAT문단을 연결해 다시읽었다. 기존LibraryID를 유지해 업데이트하며 게시·Git작업은 하지 않는다.\n''')
b=post/'brief.md';b.write_text(b.read_text()+'''\n## 수능 제출 절차 보완\n실수 반입을 무조건 시험 무효로 표현하지 않는다. Q&A03과11/9교육부안내에 따라1교시전 제출·종료후 반환, 미제출 소지 적발, 시험중사용·착용, 확인불응 심의를 구분한다.\n''')
source=Path('/Users/ja2sng/Documents/Codex/2026-11-14/task-2/csat-correction')
for item in source.iterdir():
 if item.is_file():shutil.copy2(item,qa/item.name)
print('CSAT submission conditions corrected; status reviewing')
