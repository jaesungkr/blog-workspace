# 시험 지역·기관 맥락 수정본 독립 렌더 검토

2026-11-14 UTC / independent_article_review.

최종 판정: **local preflight pass**. PDF와HTML본문·목차·반응형은독립검토했고dark대표사진은독립headless누락증거와작성자의현재Chrome실화면정상관찰을구분해반영한다. source는 같은 디렉터리 source-review.md에서 별도로 pass다. 로컬 검토이며 native Tistory/CDN나 실제 게시 성공을 뜻하지 않는다.

## 재현과 실제 시각검토

`python3 /Users/ja2sng/Documents/Codex/2026-11-14/task-2/capture_local_review.py exam-context-independent`를 독립 실행했다. bundle `artifacts/qa-v2/local-browser-exam-context-independent/`의 light/dark1280×900,360×800,390×844 full PNG6개를 모두 view_image로 직접 열었다. 작성자 캡처를 독립 실행으로 간주하지 않았다.

- 6프로필 모두 문서가로넘침0, H1하나, 목차5개/고유target, 이미지3개 natural dimensions, 표2개를 기록한다.
- 첫 화면의 바뀐 두번째 도입 문단이 대표사진 앞에 들어가고 제목/본문이 화면 밖으로 잘리지 않는다.
- 목차4/5번이 새 국내 대응·미국SAT/ETS국제시험 소제목과 일치한다. 삭제한 시험 비교표나 구매목적 결말 링크가 남아 있지 않다.
- 국내절 첫 수능제출 문장부터 MBC·현행/추진·현장 대응·TOEIC SW가 연속해 보인다. 표를 없앤 자리에 빈 박스나 과도한 고정 높이가 남지 않았다.
- TOEIC SW의 복원된 제출안내 후 소지/사용4년·성적무효·퇴실과 별도 답교환4년이 모두 보인다. 국내절 끝에서 미국/국제시험 소제목으로 정상 연결된다.
- 미국/국제절의 SAT기관·승인예외, TOEFL국제성·시험센터일반안경검사·퇴실/성적취소가능성이 끝까지 보인다. 360에서 두 소제목이 자연스럽게2줄로,390에서는 더 적은 줄로 감긴다. 글자겹침·본문누락·고립소제목은 없다.
- light/dark 본문·출처링크·법정형강조·TOC대비는 읽을 수 있다. 별도 인용상자나 생성 이미지가 추가되지 않았다.

새 `exam-context-revision/independent_focus.py`로 남은표2개의 오른쪽 끝을 light/dark360에서 실제 스크롤했고 결과4PNG도 열었다. 유형표의 답변방식과 가격표의 판매상태/끝행이 잘리지 않는다. 원래 시험표가 사라졌으므로세번째표를검사했다고쓰지않는다. 표폭은 desktop760/760,360에서는320/620,390에서는350/620의내부스크롤이다.

## PDF7쪽 실제 raster — pass

현재 `exam-context-revision/pdf-final/page-01.png`~`page-07.png`7개를 모두 view_image로 직접 열었다. contact sheet/텍스트추출만으로 대신하지 않았다.

1. 제목·새도입·Ray-Ban사진/캡션이 정상이다. `1/7` footer다.
2. 새목차5개와 첫소제목, 유형표3열전체/마지막행이 함께 보인다.
3. Even제조사연출사진·한계캡션, 가격소제목과 뒤기준문단이 함께 있다.
4. 가격표3열/7행과 짧아진 가격/지역/배송본문이 온전히 보인다. Display출시가와 Even무도수조건이 남아 있다.
5. 삼성예약절·국가별가격·사진/예약캡션·조건문장이 정상이다. 마지막계정조건이쪽아래로빠지거나footer와겹치지않는다.
6. `수능과 국내 어학시험의 대응`소제목과국내6문단이한쪽에서끝난다. 제출/반환,미제출무효,사용착용,확인불응심의,MBC법정형과혐의조건,현행1년/추진3년,전담/탐지기,TOEICSW두제재가잘리지않는다. 삭제한네시험표는없다.
7. `미국 SAT와 ETS의 국제시험`소제목과두본문문단이함께있다. 마지막TOEFL검사비교까지온전히끝나고`7/7`footer다. 일반준비체크리스트가재등장하지않는다.

한글깨짐·글자겹침·행/줄잘림·표열손실·고립소제목은발견하지못했다.사진3종의실제픽셀이모두보이며종횡비와캡션의미가유지된다.PDF스크린리더추출순서까지검증한결과는아니다.

## dark 대표사진 — 자동통과하지 않음

최신dark full1280/360/390에서Ray-Ban대표사진은안경픽셀이빠진밝은상자로보였다. 같은현재HTML의별도viewport `independent-dark-360-lead-decoded.png`에서도흰상자였다. decode3개성공·natural874×492만으로정상표시라고쓰지않는다. light원본사진과Even/삼성은실제픽셀이보인다.

이전버전의dark IAB정상관찰은역사적기록으로보존한다. 이번원고/레이아웃의안경을실제로다시확인한것으로자동재사용하지않았다. 현재localhost dark대표사진을작성자에게별도실화면으로확인하도록요청했다. 최신사용자의MacChrome선호에따라작성자가현재Chrome에서확인한결과를아래에추가했다. canonical사진bytes·HTML/CSS는수정하지않았으며우연히정상캡처를얻기위한반복을하지않았다.

## 작성자의 현재 Chrome 실화면 관찰

작성자는**이번수정본의현재localhost darkHTML**을Chrome1710×895,1280×900,360×800에서실제로열고screenshot으로대표안경전체와정중체캡션이정상표시됨을확인했다고전달했다. 모바일lead natural874×492, bounds x20/y438.3359/w320/h181.0078이었다. source/CSS/media bytes는바꾸지않았고기존IAB관찰을이번관찰로재사용하지않았다. 이내용은작성자의실화면관찰이며이독립검토자가ChromeUI에서직접본것으로기록하지않는다. 이번확인은대표사진에한정하며3사진전체의Chrome실화면QA로확장하지않는다.

이전원본decode/CSS검사에서이미지파일공백이나숨김스타일근거를찾지못했고,이번현재HTML에서도작성자Chrome의desktop/mobile대표사진이정상인점을독립headlessblank와함께보존한다. 로컬preflight는종합pass로판정한다. 모든headless캡처의그림이정상이라는뜻은아니며간헐paint누락은미해결캡처제한으로남긴다. nativeTistory첨부/CDN/공개페이지까지정상이라고확정하지않는다.

## 해시와 전달 경계

- article: `da43b0297cae9f36c3cd32b67d9e391770318a4fedda095ad3384049ba5ea764`
- brief: `a1701be45c03f033cff8b1e1acaeb7e3e5f383fba11232f574675f527db0d07a`
- evidence: `5837c6c8e506abc784f17b5bc70d138ea68fc365b1a64800d705c7030cef220b`
- lightHTML: `a009510622445d4e7a86427e0bb7324f5c001f49f46427b01be55060b64b8a91`
- darkHTML: `6e5c44ab1eb1ae0591e06308445bc5be87f96a60531e76836aa54518ac73ab2b`
- PDF: `2880e957ad24290de29e67a467f840fda403c2593344e23e4b3ca4d12ef48fcc`

보고서와 독립 재현 증거 외에 원고·HTML·사진·PDF를 변경하지 않았다. Git/Library/로그인/게시 작업은 수행하지 않았다.
