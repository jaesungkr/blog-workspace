# 최종 감사: 공공데이터 API 활용기, 전국 화재 현황 29만 건을 받아보니

## 현재 상태

- lifecycle: `ready`
- format: `rich-post`
- 작성 주체: Codex
- 직접 실행: 사용자 승인·키 입력, Codex 호출·정렬·검산
- Tistory 미디어 URL: 할당 완료, creator·independent 원격 재검증 통과
- ready 판단: 독립 final-page `pass`에 따라 2026-08-08 KST에 `ready`로 전환

## 구조와 독자

- [x] 제목 앞부분이 `공공데이터 API` 검색 의도에서 시작합니다.
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤 익숙한 문제와 직접 확인한 결론이 나옵니다.
- [x] 첫 5~6문장 안에 29만여 건·62개 필드·3~5일 시차가 나옵니다.
- [x] 비개발자는 마켓 탐색과 데이터 성격을 이해할 수 있습니다.
- [x] 개발자는 정확한 URL·헤더·쿼리로 1~5건을 재현할 수 있습니다.
- [x] 등록일과 사건일을 분리해 최신성 판단 사슬을 설명합니다.

## 근거와 독창성

- [x] 마켓 건수는 2026-08-07 시점값으로 한정했습니다.
- [x] 295,105건·최신 접수·등록 시각은 원시 JSON과 헤더에 근거합니다.
- [x] `배치형`은 고정 SLA가 아닌 관찰 기반 해석으로 제한했습니다.
- [x] 다른 API는 목록만 확인했으며 호출했다고 쓰지 않았습니다.
- [x] 첫 정렬의 오판과 `rcptDt` 재정렬을 실패·복구 사례로 남겼습니다.
- [x] 재산피해금액 단위와 데이터 완전성은 미확인 범위로 뺐습니다.
- [x] API 키는 원자료·본문·이미지에 저장하지 않았습니다.

## 미디어 결정

- lead: `koreaconnect-fire-api-batch`
- 유형: 관찰 결과를 결정적으로 조판한 실험 인포그래픽
- 해결하는 질문: 왜 8월 7일에 확인했는데 최신 사건이 8월 2일인가?
- 배치형 해석의 근거: 최신 접수 8월 2일, 동일 묶음 등록 8월 4일,
  확인일 8월 7일
- 제품 UI로 오해하지 않도록 캡션에 직접 관찰 요약임을 표시
- 사용자 제공 화면: 계정 식별 단서 때문에 보존·발행하지 않고 로그아웃 상태로
  재캡처해 내용만 대조
- supporting infographic: `not_applicable`. lead 한 장이 필요한 관계를 설명함
- GIF: `not_applicable`
- 최종 자산: `assets/infographics/koreaconnect-fire-api-batch-v1.png`
- 크기·해시: 1080×1350, `f8e213e979e03a259280fa75262b91f11c0d91f2ee360b6e2af7d46d2dff9669`
- 모바일 환산 글자: 제목 20px, 핵심 수치 15~16.7px, 보조 설명 12~12.7px,
  주의 문구 11px
- 제목 영역 비율: 전체 높이의 21.7%
- 독립 검수: 원본·360 CSS px·확대 크롭 모두 통과. 1초 안에 날짜 흐름과
  `실시간 알림 / 배치 분석` 분기가 인식됐고, 충돌·잘림·프레임드 포스터 문제 없음

## 문제 -> 수정 -> 재검증

| 회차 | 발견한 문제 | 수정 | 재검증 |
|---|---|---|---|
| 1 | 등록일 내림차순 첫 행을 실제 최신 화재로 오인 | 접수일·출동일·등록일을 각각 내림차순으로 재호출 | 최신 접수는 용인시 8월 2일 20:38로 정정 |
| 2 | `배치형 API`가 공식 주기처럼 읽힐 수 있음 | 한 시점의 3~5일 시차와 동일 등록 타임스탬프에 근거한 관찰이라고 제한 | 고정 주기·SLA를 주장하지 않음 |
| 3 | 사용자 제공 화면 상단에 계정 단서가 있음 | 원본을 발행 자산으로 쓰지 않고 로그아웃 상태로 재캡처 | 게시 자산에 이름·키·계정 화면 없음 |
| 4 | 전체 마켓 캡처는 360px에서 카드 본문이 작음 | 화면 캡처를 발행 자산에서 제외하고 큰 글자의 세로형 인포그래픽으로 전환 | 원본·360px·확대 크롭 독립 검수 통과 |
| 5 | 제목과 소제목 일부가 설명서처럼 기계적으로 읽힘 | 제목 구두점과 다섯 소제목을 독자 질문 중심으로 바꾸고 긴 문장을 분리 | 문장 분석기 재검증 완료, 사실·수치·한계 유지 |
| 6 | 모바일 목차에서 소제목의 백틱이 그대로 노출됨 | `` `size=1`부터 확인할 순서 ``를 `1건부터 확인할 순서`로 변경 | 390px·360px 라이트·다크 로컬 렌더에서 목차 재확인 완료 |
| 7 | 실제 호출 주체가 사용자 개인 실행처럼 읽힐 수 있음 | 사용자 승인·키 입력, Codex 호출·검산 역할을 도입부에 명시 | `brief.md`·`evidence.md`·원자료의 authorship와 일치 확인 |
| 8 | 사용 단계 가까이에 공식 상세 명세 링크가 없음 | POST 설명과 2번 시작 단계에 전국 화재 현황 상세 페이지 연결 | 본문 링크와 frontmatter source URL 일치 확인 |
| 9 | `ready` 전환 뒤 감사 문서의 lifecycle과 마지막 게이트가 이전 상태로 남음 | lifecycle과 완료 게이트를 현재 상태로 갱신 | `blog.py check --strict` 오류·경고 0, rich-post strict 재통과 |

## 남은 게이트

- [x] 인포그래픽 제작·독립 시각 검증
- [x] 한국어 문장 폴리싱
- [x] 독립 기사 검증
- [x] 로컬 light·dark 렌더 및 브라우저 확인
- [x] Tistory 미디어 업로드 또는 CDN URL 수령
- [x] creator 원격 미디어 기록과 반응형 QA
- [x] independent 원격 미디어·페이지 QA
- [x] `ready` 전환과 최종 remote 후보 렌더

## 검사와 남은 위험

- 로컬 예비 QA: 1280px, 390px, 360px에서 제목·본문·목차·이미지·표·코드·목록을
  확인했습니다. 표와 코드는 자체 가로 스크롤 영역 안에 머물렀고 페이지 잘림은
  없었습니다. 라이트·다크 테마의 대비도 통과했습니다.
- 독립 기사 검증: `source-level pass`. `blog.py check` 오류·경고 0,
  `check_rich_post.py` 통과, rich preview와 Tistory fragment 생성 성공. preview H1 1개,
  fragment H1 0개, H2 6개이며 원시 JSON 수치·날짜·피해 인원과 본문이 일치했습니다.
- creator final-page QA: Chrome/151.0.7922.108, 세션
  `fb19b264-1a93-488d-ad5c-e178b7d8f5d4`에서 1280×900·390×844·360×800을
  확인했습니다. 세 화면 모두 문서 `clientWidth`와 `scrollWidth`가 같고, H1 1개,
  목차 대상 6개 고유, 원격 이미지 1080×1350 로드를 확인했습니다.
- independent 원격 미디어: `Parfit independent reviewer`가 CDN PNG 794,326바이트,
  1080×1350, SHA-256
  `d61593537b1cfeca8bbaf5f254945ea4c1c98275a4836f8084eb91357b902351`을 다시
  가져와 creator 응답 지문과 일치함을 확인했습니다.
- independent final-page QA: 별도 Chrome 세션
  `d966aeb8-4db0-41aa-820d-3ca7bc949dd1`에서 1280×900·390×844·360×800을
  재캡처했습니다. 문서 가로 넘침 없음, H1 1개, 목차 대상 고유, 원격 이미지 로드,
  figure·caption 결합과 읽기 쉬움을 확인했습니다. fragment는 H1·자리표시자·로컬
  경로가 모두 0입니다.
- independent focused QA: 추가 fresh Chrome 세션
  `5eb7658e-9798-4e78-aa0a-b306f0545e0f`에서 390px·360px의 표 4개와 코드
  블록을 각각 왼쪽·오른쪽 끝까지 직접 확인했습니다. 표는 내부 폭 620px,
  코드 블록은 내부 폭 1185px이며 문서 폭은 390px·360px로 유지됐습니다.
  목차·인포그래픽·불릿 6개·번호 목록 6개의 마커, 항목 간격, 다음 문단 간격도
  충돌이나 잘림 없이 통과했습니다. 증거는
  `artifacts/qa/independent/component-details/`에 보존했습니다.
- final-page 판단: `pass`.
  `artifacts/qa/independent-final-page.json` 생성과
  `check_rich_post.py --require-publish-urls --require-remote-verification
  --require-independent-pass` 통과를 확인했습니다.
- CDN 최종 확인: 2026-08-08 KST `remote_media.py check-live` 통과
- 현재 남은 위험: 알려진 중대한 페이지 결함 없음
- 최종 strict: `blog.py check --strict` 오류·경고 0,
  publish URL·원격 검증·독립 pass를 요구한 rich-post 검사 통과
- Git 전달 범위: 이 글 번들만 focused commit 대상으로 사용
- publication boundary: Codex는 최종 게시를 누르지 않음
