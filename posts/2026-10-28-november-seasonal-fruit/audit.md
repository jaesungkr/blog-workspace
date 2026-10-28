# 11월 제철과일, 뭘 먹을까?

상태: reviewing / local draft. source freeze, independent final QA, ready 미완료.

## 실제 확인
- 원격 origin jaesungkr/blog-workspace 확인, fetch 성공. 기존 작업트리 clean. 기존 글 수정 없음.
- 선택 카테고리 Health > 영양 · 식단.
- 같은 카테고리 최근 ready 제목·소제목 5편 확인: 2026-09-16-september-seasonal-fruits, 2026-09-06-black-soybean-seoritae-guide, 2026-08-14-red-bean-health-benefits, 2026-08-10-plain-cracker-calories, 2026-08-09-greek-yogurt-thick-expensive-guide. 기존 9월 글의 '먹을 날짜' 중심 구성과 구별하여 먹는 편의·식감 중심으로 작성.
- 인사 후 장보기 상황, 선택 질문과 실용 답을 연결. 효능·가격·맛 우열·가짜 경험 없음.
- 수확/유통 경계는 사과와 참다래 본문에 배치. 각 사실은 해당 과일 한 곳에서 설명.
- 제목 후보 '11월 제철과일 추천 4가지'보다 '11월 제철과일, 뭘 먹을까?'가 중심 3종+보너스 취향 선택에 적합.
- 표 3열, 4행. 본문에서 품종·선택·보관 설명을 연결.
- 긴 영양·효능·주의사항 절은 처음부터 제외. 근거가 제공되지 않은 건강 주장은 만들지 않음.

## 미완료
- Wikimedia 이미지 원본 다운로드 HTTP 403. sandbox 기본 및 escalated curl 모두 서버/프록시 403이며 자동 승인 심사 거절은 아님. 실제 이미지 파일 미확보.
- 이미지 Library 전달 대기. source independent review 및 responsive visual QA는 아직 미실행.
- 게시/외부 티스토리 초안 저장/Git commit·push 미실행.

## 실행 결과 추가
- `python3 scripts/blog.py check posts/2026-10-28-november-seasonal-fruit`: 오류 0, 경고 0.
- prose analyzer 실행 완료. generic headings 0, stock phrases 0. 이는 자동 합격 판정이 아님.
- v2 checker: revision_required. media items 비어 있음, lead 미등록 3건. 이미지 확보 전 v2 렌더는 진행하지 않음.
- 일반 blog.py render는 reviewing 상태 때문에 거절됨. 상태를 올려 우회하지 않음.
- 표·본문만의 별도 비게시용 HTML을 md2tistory로 생성: delivery/november-seasonal-fruit-review-text-only.html.
- Chromium 로컬 캡처 시 headless 디렉터리 오류, /tmp 프로필 재시도에서 renderer 오류 및 완료 지연. 시각 검수 합격으로 기록하지 않음.
- Library 저장 미실행. 사진 포함 후보 완성 뒤 전달 예정.

## 부모 검토 후 문장 수정
- 기관명을 반복 소개하던 문장 대신 선택·보관 설명 자체에 원문 링크를 연결.
- 참다래 감황·골드원 숙기 날짜와 헤이워드 출하 기간을 본문에서 삭제. evidence.md C6·C7에는 그대로 보존.
- 사과 수확·저장 유통을 두 문장으로 축약. 10월 중순~11월 수확과 다음해 저장 소비 구별 보존.
- 후숙을 실온에서 부드럽게 익히는 과정으로 설명. 효능·가격·시식 경험 추가 없음.
- Markdown 편집본과 텍스트 검토 HTML 동기화. reviewing 유지.
- 부모 지시에 따라 사진 추가 다운로드 중단. 부모 검토본 사진·문안은 게시 승인 때 대조 예정.
- 이번 수정은 로컬만 수행; Library 저장·게시·Git push 없음.

## 최종 승인본 동기화
- Library 다운로드 2회 실패 후 부모가 별도 승인된 GitHub blob 전송 제공. fetch_blob 내용 base64 1회 디코딩, ZIP 799495 bytes 및 SHA256 일치. 원고 SHA256 a2e018dc26d1ce0ed52fb8caef37292c5f9967fc8b094f03178949da81bfa80e 일치.
- 3장 사진 bytes/hash manifest와 일치; 소비 환경에서 실제 픽셀 inspect 완료. 온주밀감, 후지 사과 3개, 부유 단감·단면을 확인. 국내산 사진으로 주장하지 않음.
- 승인 원문 artifacts/approved-source/article.md 바이트 보존. v2 문법만 가역 변환; 역변환 바이트 완전 일치. 출처 캡션 링크 문단 원문 보존.
- research_november_seasonal_fruits 독립 검수 PASS를 부모로부터 전달받음. 원고·근거·사진 권리만이며 렌더링 제외.
- source-pass 전에 부모가 사진 업로드를 시작하고 중지한 순서 이탈을 기록. 소급해서 사전 검수 통과로 표시하지 않음.
- 부모 실제 티스토리 preview PC1060px·모바일360px 테마검수 진행 중. 정확한1280px 미완료, 예외 승인 없음. final publish 보류.

## 승인본 현재 검사
- v2 non-release checker: pass, media3/directives3. 원격 URL·native embed·final-page gate를 요구하는 엄격 출판 검사 통과를 의미하지 않음.
- blog.py check: 오류1, 실제 사용자 지정 상위 카테고리 생활·기록이 스크립트 고정 분류에 없음. 사용자 지정 실제 카테고리를 보존하며 다른 파일의 분류 규칙은 변경하지 않음.
- light/dark 로컬 preflight HTML 생성 성공. 실제 브라우저 시각 검수 통과는 아직 아님.
- renderer는 매니페스트 짧은 캡션과 승인 원문의 크레딧 문단을 함께 표시. 최종 부모 제출 HTML과 매체 배치를 대조해야 함. 출처 링크를 삭제하거나 승인 문구를 임의 수정하지 않음.

## 독립 source 검수: approved_source_review
- article.md를 먼저 읽은 뒤 brief/evidence/audit와 source-freeze 및 editorial voice 지침을 확인.
- 이해 확인: 11월 장보기 독자가 귤·부사·단감·국산 참다래를 고르고, 먹을 날과 보관 목적에 따라 사과 분리 또는 참다래와 함께 후숙하는 방법을 선택하는 글. 실험이나 시식 결과를 주장하지 않음.
- 제목·소제목만 읽어도 과일별 선택과 보관 분기가 드러남. 도입은 계절 장보기 장면에서 후지 수확·참다래 후숙의 실용 차이로 연결되며, 건강 효능·가격 순위로 범위를 넓히지 않음.
- 부모가 전달한 research_november_seasonal_fruits의 공식 근거·사진 권리 PASS와 구분하여, 이 검토자는 로컬 승인 원문 역변환 바이트 일치, 원문 SHA256, 매체 3장 SHA256, alt·출처 연결 및 brief/evidence 일치를 독립 확인.
- 원문 SHA256 a2e018dc26d1ce0ed52fb8caef37292c5f9967fc8b094f03178949da81bfa80e. 문안 수정 없음. 미디어 문법·제목 수준만 가역 변환.
- source-pass.json 실제 생성. reviewing 유지. 매체 제목 캡션과 승인 원문 출처 문단의 인접 표시 여부는 final renderer QA에서 확인할 항목이며 이 기록은 렌더링 통과가 아님.
- 정확한1280px QA 미완료, 업로드 시작·중지 순서 이탈 소급 정정 없음. 최종 게시 gate 별도.

## 분류 매핑 정정
- 부모 지시에 따라 frontmatter를 Health > 영양 · 식단으로 복원. 실제 사이트 생활·기록 > 음식·장보기 ID847700은 별도 매핑 기록. 본문바이트 불변. 기존 카테고리 검사 오류는 이 수정으로 재검증.
- 원본 signed HTML/URL은 Git 제외. 승인 원고·미디어·해시·redacted receipt만 보관. 실제 제출 HTML은 아직 전달되지 않아 해시를 추정하지 않음.
- 부모 보고: 본문/13개 링크 완전일치 및 원격사진3개 HTTP200/MIME/치수/픽셀 독립검수 PASS. 원본 증거 수신 전 보고로만 기록. 1060/360 테마검수 중 dark table header CSS 수정 후 재검수 대기. 정확1280 미검수, 이번글 예외승인 아직 없음.

## 이번 글 한정 viewport 예외 승인
- 2026-10-28 02:49:13 UTC: 사용자 응답 "응 게시해줘". 실제 1060/360 light/dark 확인 및 1280 미검수 사유를 설명한 질문에 대한 승인.
- 질문/응답 식별자와 정확한 문구는 viewport-exception-approval.json에 보존. 최종 원고·사진 승인 범위 불변.
- 정확1280 검수는 미실행이며 strict 전체 gate PASS가 아님. 다른 글에 적용하지 않음. 부모 최종 게시 진행 중이며 성공 URL 아직 미수신.

## 최초 발행 증거 수신
- Git blob875b5b3c7363de9e2c8a159330916126414f9cad를 1회base64 decode. ZIP2350676 bytes/SHA25613cd16b0ae91101339a5b92c209436901263ea40a18217bb824df8cee250cc41 일치. 모든 manifest 파일 bytes/hash 검증, signed-query scan 통과.
- history/initial-publication에 보관. 최초 게시 확인02:49:52UTC, post157. 이후 사용자 승인된 이미지폭 수정 중이므로 최종상태 아님. exact-input-comparison의 다른 해시는 이력 범위로 구별.

## 게시 후 사용자 요청 사진 폭 수정 및 최종 보관
- 사용자 Sentinel_146d7e2b5dd481918ec153b9d4ad4648가 실제 사진 폭 불일치 확인·수정 요청. 최초발행 이후 라이브 검수는 이 명시적 요청에 근거.
- native 본문 폭 맞춤으로 이미지3장 alignCenter→widthContent. 전역스킨·다른 글·사진원본·문구 변경 없음.
- 부모/독립검토 증거: 새로고침 후 본문·사진3장 모두800px, x182.5, 로드완료·비율유지. 링크13개, 이미지ID, alt, 대표사진, 발행시각 유지.
- 수정 확인03:00:11UTC. 실제 모바일 및 light 테마 수정후 검수 미실행. 정확1280 미검수 예외는 이 글에만 유지.
- 최종 실제 제출SHA25645e4e40d024040f3539b1f806e462e4b42db6eb491c07535245e1c6e9477a504. 비식별HTML SHA25676e289b3ab11042d964f1ae30dd804b7a639991e0beca5129af7f1cf62ece875와 구분.
- 최종패키지1037846bytes/SHA25639c1774d17f615090db232bc5ad7ae58322e1094727ace0d6c8ff4357167879d 검증, manifest 전항목 검증 및 signed query scan PASS.
- 게시성공이 실제 확인되어 published 기록. 모든엄격gate 통과를 주장하지 않으며 native signed자료 미보관과1280예외를 숨기지 않음.

## 보관 전 검사 결과
- blog.py check: 오류0, 경고0.
- published strict v2 checker: revision_required 9건. tistory_url3/native embed3/remote-media/final-page/current final-pass 누락. 사용자 요구로 signed 원본을 Git에 넣지 않으며 별도 redacted 증거를 canonical 완전PASS로 위조하지 않음.
- 본문·사진 무결성 및 번들 signed-query scan PASS. 실제 게시상태와 검수 한계를 함께 보관.
