# Claude Duet과 ChatGPT Dots, AI에게 계속 업무를 맡기는 방법

## 작업 범위와 상태

- 사용자 요청: 제목 후보 3개·추천 1개, 출처·비교 표를 포함한 완성 원고, 별도 편집 메모. 게시·배포 금지.
- 원고는 reviewing입니다. 이번 인계는 원고 검토용이며 출판 단계의 미디어·원격 바인딩·페이지 승인·ready·Git 배포로 진행하지 않습니다.
- 실제 제품 사용과 성능 평가를 수행하지 않았습니다. 공식 문서에 근거한 업무·이용 조건 비교입니다.

## 독자와 이해 순서

- 독자: Claude·ChatGPT에서 질문한 경험은 있으나 Duet·Dots는 처음 접하는 개발자와 지식 노동자입니다.
- 계약: 회의 준비에서 반복되는 확인 업무를 계속 맡길 때 무엇을 정하고 확인해야 하는지 이해하도록 합니다.
- 도입: 내일 회의를 앞두고 회의록·메일·일정을 대조하는 구체적 상황 → 새로운 자료마다 요청이 필요한 문제 → 회의까지 관리하는 책임 → 두 제품의 평이한 정체 → 현재 제공 단계.
- 제외: 성능 순위, 성공률, 실행 시간, 개인 사용 후기, 근거 없는 앱·가격·수치, 사용자 구독 전환 권고.

## 문체 다듬기

- 읽은 비교 기준: dev-log-prose-polish/SKILL.md와 references/human-prose-benchmarks.md.
- 최근 동일 하위 분류 원고 3개 제목·소제목 검토: 2026-10-24-ai-pdf-summary-verification(published), 2026-09-20-higgsfield-ai-video-guide(ready), 2026-09-01-openclaw-2(ready). 동일 분류 3개가 있어 대체 표본은 사용하지 않았습니다.
- 제목 후보 3개는 title-candidates.md에 보관했습니다. 추천 제목은 제품명을 모르는 독자에게 계속 맡기는 업무라는 주제를 드러냅니다.
- 소제목 교정: '처음 맡길 책임을 고르는 기준' → '회의 준비부터 개발 후속 점검까지'. 추상적인 판단 기준보다 해당 절의 실제 업무를 보여줍니다.
- 문장 교정: '별도 Dots 앱을 설치하는 방식은 아닙니다' → 'Dots는 ChatGPT 안의 기능으로…'. 직접 정체를 설명합니다.
- 문장 교정: 'Slack에서 대화할 수 있다는 사실만으로…아닙니다'를 삭제하고 앱·연락수단·컴퓨터 연결이 각각 필요하다는 문장만 남겼습니다.
- 삭제: '후속 업데이트도 있었습니다', '한국 이용 조건은 뒤에서 따로 설명합니다', '개발자는 … 궁금할 수 있습니다'. 앞뒤 문장에 없는 정보를 주지 않았습니다.
- 삭제: 최초 소개 방식에 의존하면 변화를 놓친다는 평가. 실제 모바일·위젯 업데이트 사실만 남겼습니다.
- 안전 경계는 회사 설계와 독립 검증을 구분하는 사실로 기록했습니다. 승인·중단·완료 행동 비가역성은 축약하지 않았습니다.
- 분석기 전후 결과를 artifacts/prose-before.txt, prose-after.txt에 보관했습니다. 지표를 통과 점수로 사용하지 않았습니다.

## 정보의 주 소유 절

1. 도입: 문제와 두 제품의 평이한 정체.
2. Duet 절: 최초 발표·앱·진입·결과 확인·주기·Claude Code 관계.
3. Dots 절: 최초 소개·설정·Work/Codex 관계·실행 장소·후속 업데이트.
4. 회의 절: 일반 대화·예약·책임의 차이, 회사 사례와 가상 시나리오 구분, 사건 기반과 상시 실행 뜻.
5. 표: 앞선 차이를 압축해 검색할 수 있도록 비교합니다. 미확인 항목을 채우지 않습니다.
6. 통제 절: 승인·수정·중단·브라우저 관찰 차이·회사 안전 주장.
7. 이용 조건 절: 한국·계정·기기·한도. 확인일과 실제 활성화 구분.
8. 활용 절: 공식 업무 예시와 독자별 적용 판단, Microsoft 365 문서 상충, 책임 요청에 필요한 내용.

## 보호한 사실

- 10월 21일 Duet 공개와 10월 23일 후속 안전 자료.
- Dots 주간 소개 범위와 9월 29일 DevDay 날짜, 10월 9일·12~16일 후속.
- Duet 미국 Pro·Max 대기 명단 연구 프리뷰, Dots 적격 계정 점진적 배포.
- Duet 몇 시간 간격 확인, Dots 중단·재개 및 지원 서비스 사건 조건. 정확한 간격은 미확인.
- Duet 백그라운드도 Claude 한도, Dots 대화와 위임 작업의 사용량 구분.
- Dots Pause·Activity·Scheduled의 다른 중단 효과와 완료된 행동은 되돌아가지 않는다는 경계.
- Microsoft 365 로고와 명시적인 미지원 문구의 상충.

## 추가 검토 사항

- 독립 검증자는 article.md를 먼저 읽고 공식 원문과 대조합니다. 감사 기록은 실제 독립 결과가 나온 뒤 보완합니다.
- 사용자 요청은 권장 4,000~6,000자이며 현재 원고는 필요한 통제·제공 조건 설명을 보존하면서 그 범위에 가깝게 조정했습니다.

## 독립 검토에서 반영한 수정

- '문자나 음성'은 SMS로 읽힐 수 있어 '텍스트를 입력하거나 음성'으로 고쳤습니다.
- '기존 Work·Codex 작업까지'는 기존 작업 접근 범위를 과장하므로 'Work·Codex에 업무를 나눠 맡기고 기존 로컬 Codex 작업도'로 좁혔습니다.
- 회의 공통 상황의 Dots 단락에 기한·결과·알림 위치를 포함한 가상 요청을 먼저 넣고 사건 기반 예시를 뒤에 두었습니다.
- 표 소제목은 비교 제품을 직접 명시했습니다.
- blog.py check는 오류·경고 0개입니다. 일반 blog.py render는 reviewing 상태를 이유로 실행을 거부했습니다. 이를 통과시키려고 ready로 변경하지 않았습니다. 별도 검토용 HTML을 생성하며 출판용 페이지 승인으로 취급하지 않습니다.

- 독립 검토 추가 반영: 긴급 소식이 다음 확인까지 누락될 수 있다는 직접 문장으로 수정했고, 반복 승인에 관한 가정 금지 문장을 범위 내 향후 행동을 허용할 수 있다는 문장으로 바꿨습니다. 메모리는 과거 공유 정보 전체를 뜻하지 않도록 기능으로 풀이했습니다.

## 저자 피드백에 따른 결말 수정

- 문제: '도입 판단의 첫 조건입니다'는 구체적인 확인 행동을 추상적인 명사구로 바꾸고 근거 없는 우선순위를 붙여 보고서처럼 들립니다.
- 수정: '한국에서 사용하려면 두 제품의 차이와 함께, 내 계정으로 지금 이용할 수 있는지도 확인해야 합니다.'
- 보호한 내용: 한국 계정별 제공 여부를 확인해야 한다는 의미, 제품 비교와 이용 조건, 모든 수치·출처·나머지 본문은 유지했습니다.
- 저자 선호: 불필요하게 '판단의 조건', '선택의 기준' 등으로 명사화해서 단정하지 않습니다. 누가 무엇을 확인하거나 해야 하는지 동사로 직접 씁니다.
- 원고·사용자용 Markdown·검토용 HTML을 같은 문장으로 갱신했습니다. 이전 검증 기록은 history/closing-revision에 보존했습니다.

## 대표 이미지와 로컬 미리보기 준비

- 사용자 후속 요청으로 대표 이미지 제작·모바일 및 라이트/다크 검토·이용 조건 재확인 범위가 추가됐습니다. 게시·배포 금지는 유지합니다.
- 대표 이미지는 내장 image_gen으로 생성했습니다. 프롬프트는 artifacts/qa-v2/hero/hero-v1-prompt.txt에 보관했습니다.
- 후보: assets/claude-duet-chatgpt-dots-hero-v1.png. 촬영 세트 형식으로 이어지는 종이, 세 시점의 받침, 검토 클립을 표현했습니다. 주황색 접힌 종이와 녹색 원형 돌로 두 제품을 상징하며 실제 로고나 제품 UI로 제시하지 않습니다.
- 배치: 도입부에서 두 제품의 기본 개념과 기준일을 설명한 뒤, 첫 제품 절 앞. 그림이 설명을 앞서지 않도록 했습니다.
- 제작자 관찰: 종이의 두께·접촉 그림자·주름과 돌·황동 표면이 실제 촬영 세트처럼 일관됩니다. 360px 썸네일에서도 이어지는 문서와 두 모티프를 식별할 수 있습니다. 정확한 제품명 인식은 제목과 함께 읽어야 하므로 별도 검증자가 주제 적합성을 평가합니다.
- 로컬 검토는 미디어 바인딩·Tistory 원격 페이지 최종 승인과 구분합니다. 외부 앱 접속·업로드·발행·Git push는 하지 않습니다.

## 대표 이미지 검수 및 수정 결과

- 독립 검수자 /root/hero_review가 v1에 regenerate를 판정했습니다. 재질·조명은 양호하지만 긴 종이와 장식이 일반적인 문서 자동화에 그대로 쓰일 수 있어 주제 인식이 부족했습니다.
- v2는 새 메일, 변경된 캘린더 카드, 회의 자료, 검토하는 손을 하나의 장면으로 다시 제작했습니다. 프롬프트와 검수 기록은 artifacts/qa-v2/hero/hero-v2-prompt.txt 및 hero-v2-review.md에 있습니다.
- 독립 검수자는 전체 크기와 360px 썸네일을 직접 열고 pass로 판정했습니다. 손의 해부학·종이·클립·조명에 뚜렷한 결함이 없고, 본문이 다루는 회의 준비와 검토가 드러납니다. 생성 장면은 실제 제품 화면이나 사용 결과를 입증하지 않습니다.
- 최종 선택: assets/claude-duet-chatgpt-dots-hero-v2.png, 1672×941. 원본 픽셀을 편집하거나 재인코딩하지 않았습니다.
- 원고 재검토에서 '회의 전 자료 준비는 두 제품을 이해하기 좋은 시작점입니다'라는 평가 문장은 삭제했습니다. 실제 공식 업무 예시부터 설명하도록 하여 새 문체 지침을 적용했습니다. 그 외 본문 사실·수치·출처는 유지했습니다.

## 로컬 페이지 사전 점검

- 대표 이미지 v2를 반영한 v2 렌더러의 라이트·다크 미리보기를 생성했습니다. 원본 이미지의 픽셀은 유지했습니다.
- 사용자에게 전달하는 HTML에는 같은 이미지를 data URI로 포함해 다른 파일이나 원격 이미지 주소 없이 열리도록 했습니다. 이 정확한 출력 파일을 새 Chrome 프로필에서 1280×900, 360×800으로 각각 열고 전체 페이지와 주요 구성요소를 캡처했습니다.
- 결과: 두 테마 모두 문서 폭이 각각 1280px·360px와 일치합니다. H1은 1개, 목차 링크는 7개이며 대상 ID가 모두 유일합니다. 대표 이미지는 실제로 로드됐고 캡션과 분리되지 않았습니다.
- 데스크톱 표 너비는 760px입니다. 모바일 표는 320px 영역 안에서 620px 너비로 가로 스크롤됩니다. 좌측 열과 우측 Dots 열을 각각 노출한 실제 캡처를 보관했습니다. 독자가 마지막 열을 찾도록 표 앞에 좌우로 밀어 읽는 방법을 안내했습니다.
- 제작자는 전체 페이지의 섹션 순서, 여백, 라이트·다크 대비, 모바일 제목과 본문 줄바꿈, 대표 이미지와 캡션, 표의 양끝을 직접 확인했습니다. 알려진 배치 결함은 발견하지 못했습니다.
- 측정과 캡처: artifacts/qa-v2/local-output-preflight/. 이는 로컬 사전 점검이며 Tistory 원격 최종 페이지 승인이나 실제 스킨 검증을 대신하지 않습니다.
- 현재 상태: 대표 이미지와 로컬 미리보기를 갖춘 검토용 원고입니다. reviewing을 유지하며 게시·배포·Git push를 하지 않았습니다.
- 독립 검수자 /root/source_review가 실제 라이트·다크의 데스크톱·모바일 전체 캡처, 본문 구간, 대표 이미지·캡션과 표 양끝을 열어 local-layout pass로 판정했습니다. 기록은 artifacts/qa-v2/local-output-preflight/independent-review.md에 있습니다. 이 판정에도 원격 Tistory 승인이나 게시 검증은 포함하지 않습니다.

## 사용자 피드백: 생성 이미지 대신 공식 화면

- 사용자는 추상적인 생성 이미지가 글에 어울리지 않는다고 판단하고 각 공식 홈페이지에서 화면을 찾아 대체하도록 요청했습니다. 기존 생성 이미지 검수 통과는 이 취향 판단을 대신하지 않습니다. 생성 이미지는 현행 원고와 미리보기에서 제외하며 이전 후보만 보관합니다.
- Claude Duet 제품 페이지의 스크롤 데모와 공식 안전 설명의 Tasks 이미지를 비교했습니다. 작업 상태를 읽기 쉬운 Tasks 이미지를 선택하고, 공식 원본의 왼쪽 휴대폰만 잘랐습니다. UI 문구와 상태를 재작성하거나 합성하지 않았습니다.
- Dots는 공식 소개의 How dots work 대화 예시를 선택했습니다. Codex 인앱 브라우저에서 보이는 예시 영역을 600×324로 캡처했고, 사이트 맥락이 보이는 원본 화면도 별도로 보관했습니다.
- 두 이미지 모두 작성자 계정에서 직접 실행한 결과로 제시하지 않습니다. 주변 본문에 회사가 공개한 예시임을 밝히고 출처를 연결했습니다. 미디어의 저작권은 원 제공자에게 있으며 공개 재사용 라이선스를 부여받았다고 기록하지 않습니다.
- 배치: Duet의 Tasks·Make 설명 뒤와 Dots의 기본 개념 설명 뒤에 각 화면을 배치했습니다. Duet의 대표 이미지가 낯선 제품을 설명하기 전에 등장하지 않도록 했습니다. Dots 대화 문구는 모바일에서 축소하지 않고 600px로 유지해 좌우로 읽도록 안내했습니다.
- 출처·원본·캡처 방법·잘라낸 좌표: artifacts/sources/official-screens/selection.json. 현재 미디어는 media.json의 공식 화면 2개입니다.
- 인앱 브라우저에서 실제 사용자용 HTML을 라이트·다크 각각 1280×900 및 360×800으로 확인했습니다. 두 이미지가 모두 로드됐으며 페이지 전체 폭은 각 뷰포트와 일치했습니다. Dots 이미지만 320px 영역 안에서 600px 너비로 스크롤되고 표는 별도 스크롤을 유지합니다.
- 독립 원고 검수자는 두 공식 이미지를 원본과 대조하고 새 문장의 출처·공식 예시와 사용 경험의 구분을 검증해 source-level pass로 판정했습니다. 기록은 artifacts/qa-v2/source-review-official-screens.md에 있습니다.
- 독립 로컬 검수에서 Duet 캡션의 마지막 글자가 한 줄에 남는 문제를 발견했습니다. 캡션을 'Tasks에서 작업 상태를 확인하는 화면입니다.'로 줄여 두 모바일 테마에서 한 줄로 표시됨을 재확인했습니다.
- 최종 로컬 검수는 local-layout pass입니다. 대표 화면·Dots 스크롤 양끝·두 테마·두 폭의 실제 캡처와 검토 기록은 artifacts/qa-v2/official-output-preflight/에 보관했습니다. 원격 Tistory 승인과 게시 검증은 포함하지 않습니다.


## Tistory publication and cover layout correction

- The author explicitly requested publication. The exact 24,232-character native fragment matched the editor clipboard and the real preview. Public publication succeeded as post 151 at 2026-10-25 09:20 KST.
- The new-post preview did not represent the eventual automatic screenshot cover. The first live page placed the task screenshot behind the title, reducing readability. A post-scoped CSS rule now hides only that header crop and sets readable theme colors; the approved body screenshots, title, claims, URL and original date are preserved.
- Independent final-page evidence is being refreshed for this layout correction. No new source claim or image was added.
- Repository verification after the scoped CSS change: all 75 unit tests passed; all 89 article checks passed with no warnings.
- Actual publication category maps the repository category to AI·개발 > AI 이해·활용 (847694).

- Final public verification passed at 2026-10-25T09:28:06+09:00: both official screenshots loaded with approved alt text and captions; all seven TOC targets exist; desktop/mobile light/dark title and body were checked. Dots and table reached their actual horizontal right edges at 312px and 332px. Mobile article client/scroll widths both 328px.
- Header automatic cover is hidden only for this post; the date/category and logged-in management controls wrap as complete units. Original post 151 URL and 09:20 publication date were retained. The final editor text exactly matched the 25,209-character TXT.
- Third-party Google ad host extends outside the mobile width but is clipped by the skin body overflow rule; the public page remained at scrollX=0 and the article has no uncontrolled horizontal overflow.
- No direct product usage or runtime/safety test was claimed. This release verifies the publication and attachment rendering, not the vendors’ product behavior.
