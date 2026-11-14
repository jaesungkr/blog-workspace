# 존대어 최종본 독립 로컬 렌더 검토

검토일: 2026-11-14 UTC. 검토자: independent_article_review.

판정: **local preflight pass**. PDF7쪽·HTML 본문/표/반응형을 독립 검토했다. dark 대표이미지는 독립 정상 baseline과 누락 캡처가 함께 있으며 작성자의 실제 IAB 관찰을 추가해 아래 한계를 보존한다.

원고와 이미지 파일 및 canonical HTML/CSS는 수정하지 않았다. 이 문서는 로컬 검토본 preflight이며 Tistory native/CDN 또는 실제 게시 성공 판정이 아니다. source 판정은 같은 디렉터리 `source-review.md`의 pass를 따른다.

## 실제 검토 대상

- 원고 SHA-256: `fe5dd3626af722c4eb75086dc0683250e1a0318088d32ccef259670c43586966`
- brief: `d144c6fc6b9504ef3d63aa5b57aee93330750ed0a69b016a64fbfab9a36c4909`
- evidence: `47e5dd7b769913e988da16b4a7de82e9ba8cf586f363f86dcae418247d1d81e6`
- embedded light HTML: `2c3528ee74e9211d66bf6a48ee45d8df3b942c73c66b70846ecf2c053745a37c`
- embedded dark HTML: `edf64849d36950a582e7c22959a10e4cd63bed44a063e64584517e7da59b0124`
- PDF `exports/ai-glasses-products-exam-rules-mobile-review.pdf`: `90913b639ab457ee5dc5ab6d595a039b49fa137c4384f2c47c55b202a7557281`

HTML 경로는 bundle `delivery/ai-glasses-products-exam-rules-review-{light,dark}.html`이며, 독립 재현 명령은 `python3 /Users/ja2sng/Documents/Codex/2026-11-14/task-2/capture_local_review.py honorific-independent`다. 결과는 bundle `artifacts/qa-v2/local-browser-honorific-independent/`에 있다. 작성자 캡처를 독립 실행으로 대체하지 않았다.

## PDF 7쪽 실제 raster 검토 — pass

`honorific-publication/pdf-final/page-01.png`부터 `page-07.png`까지 모두 view_image로 열어 확인했다. contact sheet나 텍스트 추출만으로 대신하지 않았다. 실제 페이지 크기는 420×760.08pt, 총 7쪽이다.

1. 1쪽: 제목·두 도입 문단과 Ray-Ban Meta 대표 사진, 카메라/스피커·화면 부재 캡션이 온전히 보인다. 한글 깨짐과 줄 잘림이 없다.
2. 2쪽: 목차와 첫 소제목·설명·제품 유형 표가 이어진다. 표 3열 전체와 마지막 Even G2 행이 한 페이지에 보인다. 좁은 셀에서 단어가 줄바꿈되지만 문장이 잘리거나 겹치지는 않는다.
3. 3쪽: Even 제조사 연출 이미지와 그 의미를 밝힌 본문·캡션이 붙어 있다. 다음 가격 소제목 아래에 비교 기준 문단이 있어 소제목이 혼자 남지 않는다.
4. 4쪽: 가격·시장·판매상태 3열과 7제품 행 전체가 보인다. Display $799의 출시가 표현과 Even 한국 무도수 조건이 유지된다.
5. 5쪽: 삼성 예약/출시 예정 문단, 국가별 가격, 공식 제품 사진과 예약 상태 캡션, 호환 조건이 한 흐름으로 보인다. 사진은 찌그러지거나 잘리지 않았다.
6. 6쪽: 시험 규정 표 3열과 네 시험 행 전체가 한 페이지에 보인다. 수능 셀의 1교시 전 제출·미제출 소지 적발·사용/착용 제재가 빠짐없이 보인다. 표 아래 제출/반환 조건과 확인 불응 시 심의 문단도 하단 여백 안에서 온전히 끝난다.
7. 7쪽: SAT, TOEFL 일반 안경 검사, TOEIC SW의 별도 두 조항 설명 뒤에 마지막 소제목과 결말 두 문단이 함께 배치된다. 이전 8쪽의 고립 결말 문제는 없다.

각 쪽 하단 `dev.log · 검토본 1 / 7`부터 `7 / 7`까지 순서가 맞다. 이미지 3종 모두 실제 픽셀이 보인다. 표 바깥으로 사라진 열·페이지를 걸친 잘린 행·겹친 글자·고립 소제목은 발견하지 못했다. HTML용 가로 스크롤 안내 한 문장이 PDF에서 빠진 것은 인쇄본의 전체 열 표시와 일치한다.

## HTML 독립 6프로필과 모바일 표 — pass

light/dark 각각 1280×900, 360×800, 390×844의 독립 full PNG 6개를 실제 열었다. receipt는 매 프로필에서 문서 scrollWidth=clientWidth, 이미지3개 naturalWidth>0, H1 하나, 목차 링크5개와 서로 다른 target을 기록한다. 페이지 가로 넘침은 0이다. 제목 줄바꿈·문단·소제목·출처 링크·캡션은 잘리거나 겹치지 않는다. 360/390의 긴 표는 의도한 내부 가로 스크롤이다.

- 1280: 표 client/scroll 폭760/760.
- 360: 표3개 모두320/620, overflow auto.
- 390: 표3개 모두350/620, overflow auto.

`honorific-publication/independent_focus.py`로 현재 HTML의 light/dark360에서 각 표를 오른쪽 끝까지 직접 스크롤했다. `independent-{light,dark}-360-table-{1,2,3}-right.png` 6개를 실제 열었다. 유형표의 답변 방식, 가격표의 판매상태, 시험표의 안경 확인/제재 마지막 열을 모두 읽을 수 있다. 수능 긴 셀의 끝 `적용됩니다`, SAT 검사 응대, TOEFL 일반안경 검사/제재, TOEIC SW 제출 안내 뒤4년 제재가 보인다. 줄 높이 부족이나 셀 밖 잘림은 없다. 왼쪽 첫 열은 full PNG에서, 오른쪽 마지막 열은 focused PNG에서 확인했다.

## dark 대표이미지 paint 관찰과 실제 IAB 확인

독립 dark full1280/360/390 PNG의 첫 사진은 밝은 배경 상자만 남았다. 같은 현재 HTML의 `independent-dark-360-lead-decoded.png`도 흰 박스였다. natural dimensions나 decode 성공만으로 이 스크린샷을 이미지 정상 표시라고 기록하지 않는다.

따로 원인을 구분하는 `dark_lead_diagnostic.py`를 한 번 실행했다. 이 세션의 **어떠한 런타임 CSS/이미지 변경 전 baseline** `dark-lead-diagnostic-baseline.png`에서는 동일 원본의 안경이 실제로 보였다. 뒤의 color-scheme=light 임시 변경과 canvas→PNG 임시 src 전환도 정상이다. 이 실험은 DOM에만 적용했으며 저장된 HTML/CSS/asset은 바꾸지 않았다. 정상 결과를 얻기 위해 반복 캡처해 하나를 고른 것이 아니다. 원본 blank 증거와 정상 baseline을 모두 보존한다.

추가 `image_computed_metrics.py`의 light/dark 비교:

| 항목 | light / dark |
|---|---|
| natural dimensions | 둘 다874×492 |
| viewport bounds | 둘 다 x20,y309.78,w320,h181 |
| display / visibility / opacity | 둘 다 block / visible / 1 |
| filter / mixBlendMode | 둘 다 none / normal |
| decoded canvas400,250 픽셀 | 둘 다[75,75,75,255] |
| colorScheme | normal / dark |

따라서 원본 파일이 빈 이미지이거나 CSS가 사진을 숨긴다는 근거는 발견하지 못했다. 동시에 최신 focused 캡처 중에도 누락이 있어 단순히 full-page에만 한정된 현상이라 쓰지 않는다. 현재 관찰은 **headless 캡처에서의 간헐적 paint 누락**과 일치하지만, native Tistory/사용자 브라우저에서도 반드시 정상이라고 확정하지 않는다. 작성자에게 별도 IAB localhost dark 실제 화면 확인을 요청했고 아래 결과를 전달받았다.

보존 증거는 같은 `honorific-publication/` 아래에 있다:

- blank: `independent-dark-360-lead-decoded.png`
- 원본 정상 baseline: `dark-lead-diagnostic-baseline.png`
- 임시 color-scheme 비교: `dark-lead-diagnostic-scheme-light.png`
- 임시 PNG 비교: `dark-lead-diagnostic-canvas-png.png`
- decode/단계 진단: `dark-lead-diagnostic.json`
- 양 theme computed/pixel: `image-computed-metrics.json`

## 작성자의 실제 IAB 관찰 — 독립 headless 증거와 구분

작성자는 동일 localhost dark 검토본을 IAB에서 desktop1280과 viewport360×800으로 실제 열었다고 보고했다. 360 screenshot에서 검은 안경 전체와 정중체 캡션이 정상이며 lead natural874×492, bounds x20/y334.80/w320/h181.01이었다. 페이지/CSS/이미지bytes 변경은 없었다. 이 관찰은 **작성자가 실제 IAB로 확인한 대표사진**에 한정하며 내가 그 IAB 화면을 직접 조작·열람한 것으로 기록하지 않는다. 삼성 lazy 이미지는 해당 viewport에 들어오지 않아 IAB에서 전체3이미지를 검토한 결과가 아니다.

독립 세션에서도 변경 전 정상 dark baseline을 실제 확인했고, 원본 decode 픽셀/표현 CSS에 숨김 문제를 찾지 못했으며, 작성자 IAB에서 desktop/mobile 대표사진이 정상임을 확인한 점을 함께 반영해 로컬 preflight는 pass로 판정한다. 모든 headless 캡처가 정상이라는 뜻은 아니다. 누락/정상 PNG를 함께 보존해 간헐 paint 제한을 최종 보고에 남긴다.

## 범위와 남은 사항

PDF와 source에는 수정 필요점이 없다. HTML의 본문/표/모바일 흐름은 통과했다. dark headless 캡처의 간헐 paint 관찰은 위와 같이 남아 있다. 원고나 사진을 변경할 필요가 있다고 결론내리지는 않았다. Tistory 로그인·native 첨부·CDN·실제 발행 확인은 수행하지 않았다. Git/Library 작업도 수행하지 않았다.
