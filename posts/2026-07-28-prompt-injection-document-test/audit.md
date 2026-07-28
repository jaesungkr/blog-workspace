# 최종 감사: 프롬프트 인젝션이란? 문서 속 숨은 명령 6회 실험과 방어 방법

검토한 사실만 체크합니다. 아직 해당하지 않는 항목은 비워 두고 이유를 적습니다.

## 구조와 독자

- [x] 제목 앞부분이 실제 검색 의도에서 시작합니다.
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤 2-4문장 안에 익숙한 문제와 글의 필요성이 나옵니다.
- [x] 첫 5-6문장 안에 기억할 결론 또는 질문이 있습니다.
- [x] 낯선 용어와 방법을 결과표보다 먼저 설명합니다.
- [x] 중앙 방법의 `입력 -> 처리/표현 -> 비교/판단 -> 출력` 사슬이 보입니다.
- [x] 시나리오 결과, 전체 벤치마크, 실용 추천의 범위를 구분했습니다.
- [x] 선택이 목적인 독자에게 기본 선택과 예외를 직접 제시합니다.
- [x] 비개발자가 코드 없이도 핵심 결론을 이해할 수 있습니다.

## 근거와 독창성

- [x] 모든 수치와 강한 주장에 출처·측정 기준·한계가 붙습니다.
- [x] 벤더 주장, 독립 검증, 추정, 구조 예시를 구분했습니다.
- [x] 테스트 입력·환경·판정 규칙·원시 결과·실패 사례를 보존했습니다.
- [x] Codex가 실행한 작업을 사용자의 개인 경험으로 쓰지 않았습니다.
- [x] 미확인 사실과 해결되지 않은 TODO가 본문에 없습니다.
- [x] 반론과 일반화할 수 없는 범위가 보입니다.
- [x] 출처 요약을 넘어선 first-party contribution이 있습니다.
- [x] 다른 블로그 이름으로 바꾸면 약해지는 dev.log만의 이유가 있습니다.

## 문장과 형식

- [x] 인사부터 마무리까지 존대어가 일관됩니다.
- [x] 번역투, 이중 피동, 명사화, 상투적인 요약 표현을 걷어냈습니다.
- [x] 과장, 감정 부사, 기계적인 병렬, 불필요한 1인칭이 없습니다.
- [x] 문단은 주제에 따라 자연스럽게 나뉘고 문장 리듬이 기계적이지 않습니다.
- [x] 굵은 강조가 할당량처럼 반복되거나 매 절의 격언형 결론을 만들지 않습니다.
- [x] em dash(`—`), 분리된 참고문헌 부록, 관성적인 면책 문구가 없습니다.
- [x] 카테고리별 마무리 기준을 따릅니다.

## 제목·문체 폴리싱

- [x] 제목과 소제목만 읽어도 회의록의 공격 문장, 도구 행동, 실험 결과,
  저장소 지침으로 폐기한 첫 실험과 재실행, 해석 한계, 권한 축소로 이어지는
  흐름이 보입니다.
- [x] 검색 유입을 최우선으로 두고 현재 검색 결과의 정의형·공격형·방어형
  의도를 비교했습니다. 검색량 도구를 사용하지 않은 정성 판단임을
  `brief.md`에 기록했습니다.
- [x] 범용 소제목을 실제 장면·행동·관찰로 바꾸고, 탐색에 필요한 수치와
  실험 대상을 남겼습니다.
- [x] 각 소제목만 읽어도 대상과 설명·실험 방법·측정 결과·폐기 조건·
  미검증 범위·방어 항목을 알 수 있게 풀어 썼습니다.
- [x] 문단 사이를 접속사로만 잇지 않고 이전 문단의 문장·권한·결과·오염된
  파일럿이 다음 판단의 출발점이 되게 고쳤습니다.
- [x] 수치·날짜·링크·코드·표·테스트 주체·한계를 폴리싱 전 자료와 대조했습니다.
- [x] 자연스러움을 위해 일화·감정·대화·실패·개인 경험을 새로 만들지 않았습니다.

- 비교 표본(대상 슬러그 제외):
  - 같은 하위 카테고리 `AI 개념 · 실전`: `orca-agent-ide-guide` (`ready`)
  - 대체 표본 `Log`의 설명·실전형 글: `wsl-containers-without-docker-desktop`
    (`ready`), `ccshare-manycode-guide` (`ready`), `duckdb-guide` (`ready`)
- 대체 기준: 같은 하위 카테고리의 완성 글이 1편뿐이어서, 최근 `Log` 글 중
  도구 원리·직접 실행·실용 판단을 함께 다루는 세 편으로 총 4편을 채웠습니다.
  대상 원고와 `reviewing` 이하 초안은 비교 집합에서 제외했습니다.
- 대표 제목 변경:
  `프롬프트 인젝션 실험 - 문서 속 한 줄이 AI 에이전트를 속일까`
  -> `프롬프트 인젝션 6회 실험: 공격 행동 0/6과 폐기한 파일럿`
  -> `프롬프트 인젝션이란? 문서 속 숨은 명령 6회 실험과 방어 방법`
- 대표 소제목 변경:
  - `프롬프트 인젝션의 정체` -> `프롬프트 인젝션 뜻: 직접·간접 공격과 탈옥의 차이`
  - `문장보다 권한이 더 중요한 이유` -> `문서 속 공격 명령이 AI 에이전트의 파일 생성·메일 전송으로 이어지는 과정`
  - `회의록 한 줄 실험` -> `Codex 실험 방법: 공격 문장 배치 3종 × 작업 지시 2종`
  - `6번 모두 막힌 결과` -> `Codex 실험 결과: 공격 행동 0/6, 정상 요약 7/7`
  - `한 번 폐기한 파일럿` -> `저장소 작업 지침이 섞인 첫 실험 폐기와 전체 7회 재실행`
  - `0/6이 안전 증명은 아닌 이유` -> `공격 행동 0/6의 의미와 이번 실험에서 확인하지 못한 공격 범위`
  - `바로 적용할 네 겹의 방어` -> `프롬프트 인젝션 방어 방법: 작업 범위·신뢰 경계·최소 권한·행동 확인`
- 대표 문단 연결 수정:
  입력→행동 경로 뒤에 `외부 문서를 참고할 데이터로 볼지, 새 명령으로 볼지가
  이 경로의 갈림길`을 두어 지시 계층 설명으로 이어지게 했고, 파일럿 재실행
  뒤에는 `주변 문맥을 격리했어도 이번 실험이 보지 못한 범위는 남습니다`로
  표본과 공격 형식의 한계를 직접 연결했습니다.
- 삭제한 빈 문구 또는 반복: 절마다 반복되던 추상적인 굵은 교훈 2개,
  `결과가 같았다는 것과 설계 가치가 없다는 것은 다른 이야기` 같은 균형형
  요약, `프롬프트 인젝션의 정체`처럼 주제를 바꿔도 성립하는 표지 문구
- 보존 확인한 핵심 사실: 대조군 1회와 공격 6회, 공격 성공 0/6, 정상 요약
  7/7, 공격 언급 5/6, Codex 실행 주체와 버전·환경, 공격 문장·배치·판정
  규칙, 저장소 안 파일럿 폐기와 `/private/tmp` 재실행, 모든 URL·표·코드,
  일반화할 수 없는 범위
- 남은 문체·근거 위험: 독립 article validation에서 제목·소제목·문단 연결과
  잠근 사실을 다시 대조해 중대한 결함이 없었습니다. 남은 위험은 조건별 1회의
  작은 표본과 미검증 공격·도구 범위이며 본문과 이 감사의 마지막에 유지합니다.

## 대표 이미지

- [x] 최종 이미지를 생성한 뒤 실제 결과를 열어 확인했습니다.
- [x] 이미지가 글의 핵심 메시지와 맞고 근거 이상의 내용을 암시하지 않습니다.
- [x] 로고·워터마크·불필요한 내장 텍스트가 없습니다.
- [x] 대표 이미지의 반응형 크롭을 고려한 안전 여백이 있습니다.

- 최종 파일: `assets/prompt-injection-trust-boundary-hero.png`
- 최종 크기: `1672 × 941`, PNG RGB
- SHA-256:
  `0e0fe63efefdbdfdb432fbaf680f84509f0374365041b1c4c8d212b970ab667b`
- 생성 방법: OpenAI built-in `image_gen`
- 권장 위치: `대표 이미지 - 제목 바로 아래`
- 한국어 alt: `회의 문서에서 빠져나온 붉은 한 줄이 행동 레버로 향하다 반투명 경계판에 막힌 모습`
- 의도한 인식 단서: 평범한 문서의 검은 줄 사이에서 붉은 문장 하나만 물리적
  리본처럼 빠져나와 행동 레버를 향하고, 그 사이의 반투명 경계판에서 멈춥니다.
  외부 문서의 지시가 에이전트 행동으로 이어지기 전 신뢰 경계에서 차단되는
  프롬프트 인젝션의 핵심을 로고나 제목 없이 표현합니다.
- 알려진 위험: 글자 대신 쓴 추상 선이 일부 독자에게는 단순한 서류로 보일 수
  있습니다. 독립 썸네일 검증에서는 붉은 한 줄·유리 경계·레버가 함께 읽혀
  통과했으며, 실제 티스토리 스킨의 더 작은 크롭은 게시 전 확인 항목으로
  남깁니다.
- 전체 크기 검수: 종이 섬유와 두께, 붉은 리본의 접촉과 굴곡, 반투명 유리의
  굴절·표면, 레버의 브러시드 금속과 접지 그림자가 일관됩니다. 글자처럼
  오인할 만한 의사문자, 로고, 워터마크, 가짜 UI, 과도한 광원 효과는 없습니다.
- 썸네일 검수: `artifacts/hero-thumbnail-preview.png`의 320×180 표시에서
  문서의 붉은 한 줄이 가장 먼저 보이고, 유리 경계와 레버까지 한 시선에
  이어집니다. 좌우 핵심 요소가 잘리지 않고 종이의 일반 문장과 공격 문장을
  구분할 수 있습니다.
- 주제 인식·교체 테스트: 붉은 문장형 리본이 문서에서 빠져나와 행동 레버로
  향한다는 결합은 일반적인 자물쇠·방패보다 간접 프롬프트 인젝션의
  `외부 문장 -> 에이전트 행동`을 직접 나타냅니다. 문서를 unrelated subject로
  바꾸면 이 인과관계가 약해지므로 교체 테스트를 통과합니다.
- 레퍼런스 비교: 사용자·공식 시각 레퍼런스 없음. 저장소 아트 디렉션의
  밝은 중성 배경, 한 가지 강조색, 물성 중심 기술 은유, 비대칭 구도를 기준으로
  검수했습니다.
- 대표 이미지 검증 결과: `pass`
- 최종 생성 프롬프트:

```text
Use case: stylized-concept
Asset type: Korean Tistory blog hero image, wide editorial campaign visual
Primary request: Create an iconic visual metaphor for indirect prompt injection: an ordinary business meeting document contains one rogue instruction line that tries to become an action, but is stopped at a trust boundary before reaching a physical control.
Creative intent: Quiet tension and credible restraint; a document is data, not authority.
Visual idea: On a luminous warm-neutral inspection table, one large sheet of thick uncoated ivory paper carries only abstract short black typographic line marks with no readable letters. One single vermilion line physically lifts out of the paper like a narrow ribbon and reaches toward a small, precise brushed-aluminum action lever at the far side. Between the paper and the lever stands one thin vertical panel of softly frosted glass; the red ribbon meets the glass and stops, with believable contact and a slight bend.
Subject-recognition cue: The lone red sentence-like line emerging from an otherwise normal paper document and aiming at a real action lever, intercepted by one trust-boundary panel.
Art direction: Crafted editorial still life / practical miniature set photographed for a major enterprise technology campaign, not a diagram and not generic cybersecurity stock art.
Scene/backdrop: Pale warm-gray seamless studio surface with generous quiet negative space, subtle paper fibers and inspection-table realism.
Composition/framing: 16:9 landscape, low three-quarter camera angle, large document occupying the lower-left and center, frosted-glass boundary near the right third, small action lever beyond it, controlled asymmetry, shallow but coherent depth, focal red line clearly visible, crop-safe margins on all sides.
Lighting/mood: Large diffused daylight key from upper left, soft neutral fill, restrained narrow warm edge light on the aluminum, shaped natural shadows, calm investigative mood.
Color palette: Ivory paper, warm gray, brushed silver, one intentional vermilion accent only; no navy, cyan, violet, or neon.
Materials/textures: Thick uncoated paper with real fibers and edge thickness, sandblasted/frosted glass with believable refraction, brushed aluminum lever with contact shadow, painted wood or matte tabletop microtexture.
Text: No readable text, no letters, no numbers, no logos. Abstract line marks only.
Constraints: Publication-ready, factually neutral, visually led, one clear metaphor, premium physical craft, plausible gravity and optics, no unsupported success claim, no watermark.
Avoid: locks, shields, robot heads, brains, circuits, binary code, keyboards, laptops, dashboards, floating UI, holograms, glassmorphism cards, cyberpunk, excessive glow, plastic 3D icons, clutter, pseudo-writing, malformed typography, centered symmetry, stock-photo look.
```

## 보조 인포그래픽

- 판단: `1장`
- 판단 이유: 사용자 요청과 외부 문서가 한 에이전트 문맥에서 만난 뒤, 작업
  범위·최소 권한·사람 승인이라는 세 경계를 지나야 실제 행동으로 이어지는
  관계는 글과 표보다 세로 흐름으로 볼 때 더 빨리 이해됩니다.
- Reflections 예외 근거(해당하는 경우):
- [x] 각 인포그래픽이 장식이나 단순 반복이 아니라 하나의 중요한 관계를 더 빨리 이해하게 합니다.
- [x] 핵심 설명 바로 뒤에 둘 위치를 정했습니다.
- [x] 한국어 문구·수치·화살표·라벨을 결정적으로 조판하고 본문 근거와 대조했습니다.
- [x] 전체 원본과 축소 표시 결과를 확인하고 모바일 환산 타입 스케일을 검증했습니다.
- [x] 두 장 이상이면 각 이미지가 서로 다른 독자 질문에 답합니다. (보조 인포그래픽 1장)

| 최종 파일 | 유형 | 해결하는 독자 질문 | 권장 위치 | 한국어 alt | 문구·수치 근거 |
|---|---|---|---|---|---|
| `assets/prompt-injection-defense-infographic-v3.png` | 원리 | 문서의 공격 문장이 실제 행동으로 곧바로 이어지지 않게 어디에 경계를 두는가 | `문서 속 공격 명령이 AI 에이전트의 파일 생성·메일 전송으로 이어지는 과정` 절의 입력→행동 사슬 바로 뒤 | 사용자 요청과 외부 문서가 에이전트 판단으로 모이고, 작업 범위·최소 권한·사람 승인 세 경계를 지난 요청만 회의 요약으로 이어지는 흐름 | `article.md`의 지시 계층·권한 설명, OWASP·Microsoft·OpenAI 다층 방어 권고, `artifacts/infographic-copy-map.md` |

- 최종 크기: 1200×1500 PNG RGB, 4:5
- 최종 SHA-256:
  `844ebbe01dcaf883a7d1b4dd83161e0cb6fd929e1b6f379481c4b0d2a798a405`
- 제작 방법: `artifacts/prompt-injection-defense-infographic.html`의
  결정적 HTML/SVG 조판을 Playwright로 원본 PNG 렌더
- 글꼴: Apple SD Gothic Neo, Noto Sans KR fallback
- 360px CSS 표시 환산: 제목 20.4px, 주요·경계 라벨 15.0px,
  설명 12.0px, 부제 11.4px, 한계 11.1px
- 헤더 높이: 230px, 전체 높이의 15.3%
- 조판 검사:
  `check_mobile_type_scale.py`의 headline·primary·support·caveat·header
  전 항목 `PASS`
- 생성 단계 수정: v1에서 `외부 문서 / 신뢰하지 않을 데이터`가 중앙 원과
  붉은 경로에 가려졌습니다. 문구를 `비신뢰 데이터`로 줄이고 문서 왼쪽 위의
  빈 공간으로 옮긴 v2에서 겹침이 사라졌습니다. v2의 글자가 이미지에 비해
  여전히 크다는 사용자 피드백에 따라 전체 서체 계층을 4~8% 줄인 v3를 만들고
  권장 모바일 타입 스케일의 하한선 안에서 다시 검수했습니다.
- 표시 검수: 로컬 파일 URL을 지원하는 격리된 검증 브라우저에서 동일 원본을
  `width:360px`, 무확대, DPR 1로 표시했습니다. 브라우저 측정값은 원본
  1200×1500, CSS·bounding box 360×450, zoom 1이었습니다. 화면에서 모든
  라벨과 한계 문구가 읽히고 연결선이 글리프를 침범하지 않았으며, 입력→판단→
  세 경계→결과가 먼저 보였습니다. 축소 래스터 자산은 만들거나 저장소에
  보존하지 않았고, 사용자는 같은 v3의 축소 표시 비율을 직접 승인했습니다.
- 전체 원본 검수: 제목보다 입력→판단→세 경계→결과의 세로 관계가 더 넓은
  면적을 차지하고, 큰 외곽 카드나 작은 삽입 패널이 없습니다. 청록의 정상 경로와
  주황의 비신뢰 경로가 겹치지 않고, 붉은 경로는 `중단·기록`으로 분기합니다.
- 확대 크롭 검수:
  - `01-header.png`: 제목·부제·분리선의 획, 자간, 안전 여백 정상
  - `02-sources-agent-connectors.png`: 두 입력 라벨, 문서 아이콘, 중앙 판단,
    두 색 경로, 중단 표식 사이 겹침 없음
  - `03-boundaries.png`: 세 경계 라벨과 중앙 슬롯, 세로 경로, 설명 문구의
    도착점과 글리프 여백 정상
  - `04-result-caveat.png`: 결과 체크·라벨·한계 문구의 글리프와 분리선 충돌 없음
- 한국어·기호 검수: `사용자 요청`, `신뢰할 지시`, `외부 문서`,
  `비신뢰 데이터`, `에이전트 판단`, `중단·기록`, `1 작업 범위`,
  `2 최소 권한`, `3 사람 승인`, `전송·삭제 전 확인`, `허용된 결과`,
  `회의 사실 요약`, 최종 한계 문구를 정상 순서와 텍스트 블록 단독 순서로
  읽어 오탈자·의사문자·잘린 글자 0건을 확인했습니다.
- 1초 관계·framed-poster 검사: 전체 원본과 정확한 360px 브라우저 표시에서
  입력→판단→세 경계→결과의 관계가 먼저 읽혔고 개방형 구성을 유지했습니다.
- 인포그래픽 검증 결과: `pass` - v3 전체·정확한 360px 브라우저 표시·
  확대 크롭·타입 스케일 검사를 통과했고, 사용자가 글자와 이미지 비율을
  직접 승인함

## 최종 검토와 수정 이력

- [x] 완성 원고를 처음부터 끝까지 외부 독자 관점으로 다시 읽었습니다.
- [x] 렌더된 티스토리 HTML에서 제목·문단·표·코드·링크·이미지 위치를 확인했습니다.
- [x] 대표이미지는 전체·썸네일, 보조 인포그래픽은 전체·축소 표시 결과를 실제로 확인했습니다.
- [x] 사용자 제공 시각 레퍼런스가 있다면 같은 표시 크기로 나란히 비교했습니다. (제공 없음)
- [x] 아래 문제를 수정한 뒤 관련 검사·렌더·시각 검토를 다시 실행했습니다.

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | 실험 설계 | 파일럿 폴더가 블로그 저장소 안에 있어 두 실행에 상위 저장소 지침이 섞임 | 파일럿을 결론에서 제외하고 저장소 밖 `/private/tmp`에서 7개 사례를 전부 다시 실행 | 본 실험 이벤트에 `dev-log-workspace` 지침 로드가 없고 공격 0/6·정상 요약 7/7을 원자료와 대조함 |
| 2 | 1차 Tistory 변환 | 굵은 강조와 Microsoft 링크의 Markdown 문법 중간에 원고 줄바꿈이 들어가 변환 HTML에 별표와 링크 원문이 노출됨 | 강조 구간과 링크 문법을 각각 한 원고 줄에 배치 | `md2tistory.py` 재변환 뒤 HTML에서 남은 `**`와 `](http` 패턴 0건, 링크 7개·강조 6개를 태그로 확인함 |
| 3 | 대표 이미지 전체·320×180 썸네일 | 없음 | 수정 없음, 첫 후보를 최종 선택 | 주제 인식, 교체 테스트, 물성·빛·구도·크롭·무텍스트 검수 통과. SHA-256 기록 |
| 4 | 인포그래픽 v1 전체 원본 | 외부 문서 라벨과 보조 문구가 중앙 에이전트 원·붉은 경로에 일부 가려짐 | 보조 문구를 `비신뢰 데이터`로 줄이고 문서 왼쪽 위 빈 공간으로 이동한 v2 생성 | v2 전체 원본에서 라벨·경로·아이콘 분리 확인, 타입 스케일 전 항목 PASS |
| 5 | 인포그래픽 v2 360px CSS 표시 | in-app Browser가 로컬 `file://` URL을 정책상 차단해 필수 모바일 실제 표시를 완료하지 못함 | 우회하지 않고 전체 원본·4개 확대 크롭·수식 환산·타입 스케일 검사를 완료 | 시각·수치 결함은 없으나 필수 실제 360px 확인 전이므로 `revision_required` 유지 |
| 6 | 인포그래픽 v2 전체 비율 | 이미지에 비해 글자가 아직 크다는 사용자 피드백 | 제목 72→68px, 주요 라벨 52~54→50px, 설명 42→40px, 한계 38→37px로 줄인 v3 생성 | v3 전체 원본과 4개 확대 크롭에서 겹침·잘림 0건, 360px 환산 타입 스케일 전 항목 PASS, 사용자가 축소 표시 비율을 직접 승인 |
| 7 | 인포그래픽 v3 정확한 360px CSS 표시 | in-app Browser의 로컬 URL 제한으로 남아 있던 검증 공백 | 로컬 파일 URL을 지원하는 격리 브라우저에서 동일 원본을 width 360px·DPR 1·zoom 1로 표시하고 일시 화면만 검수 | natural 1200×1500, CSS·bounding 360×450 확인. 글리프·연결선·크롭·1초 관계 검사 통과, 임시 화면은 검수 뒤 삭제 |
| 8 | 최종 Tistory HTML | 없음 | 수정 없음 | 720px 실제 렌더에서 제목·문단·표 3개·코드·링크 7개·강조 6개·소제목 7개 확인. 360px에서 문서와 표의 가로 넘침 0, 긴 코드만 의도한 `overflow-x:auto` 동작 |
| 9 | 제목·소제목·문단 연결 | 최근 기술 글과 같은 `키워드 - 훅` 제목, 7개 중 5개의 범용 소제목, 정의·권한·실험 사이의 추상적인 연결, 절마다 반복되는 굵은 교훈 | 제목에 실제 수치와 폐기한 파일럿을 드러내고, 소제목을 사건·행동·관찰 중심으로 교체했으며 앞 문단의 구체 명사와 결과를 다음 문단이 이어받게 수정 | URL 13개·코드 블록 1개·표 원문 16줄이 폴리싱 전과 같고, 수치·테스트 주체·환경·결과·한계를 원자료와 대조함. 제목·소제목 단독 읽기와 문단 경계 검사 통과 |
| 10 | 폴리싱 후 Tistory HTML | 없음 | 수정 없음 | 최신 `ready` 원고를 다시 렌더함. 720px·360px에서 문서 전체 가로 넘침 0, 표 3개·링크 7개·강조 4개·소제목 7개 정상, 긴 공격 문장 코드만 의도한 `overflow-x:auto` 동작 |
| 11 | 검색 제목·소제목 직관성 | `0/6으로는 알 수 없는 공격 성공률`, `한 번 폐기한 파일럿`처럼 본문을 읽기 전에는 대상과 의미를 알기 어려운 표현 | 공개 제목에 정의형 검색어·문서 공격 실험·방어 방법을 명시하고, 모든 소제목에 대상·행동·수치의 의미 또는 다룰 범위를 직접 씀. 본문 문장은 수정하지 않음 | 제목·소제목 정규화 뒤 본문 SHA-256 `61a7a223de8b5c7660353eeda883c369b33a5f2b2963e92292cdc865f51fb66a` 일치. 독립 의미 검증, 개별 check, 재렌더, H3 7개·표 3개·코드 1개·깨진 Markdown 0개 확인. 직전 720px·360px 통과본과 본문·스타일이 같고 새 H3는 공백 단위 줄바꿈을 유지해 회귀 통과 |

- 중대한 문제가 없으면 `발견한 문제`에 `없음`이라고 쓰고 확인 근거를
  `재검증 결과`에 적습니다.
- 현재 종료 판단: `ready`. 회차 11에서 제목·소제목만 바뀌었고, 본문 불변
  대조·독립 의미 검증·Tistory HTML 재렌더·구조 회귀 검사를 통과했습니다.
  새 로컬 HTML을 in-app Browser에서 직접 여는 작업은 URL 정책상 차단됐습니다.
  새 화면 검수는 직전 720px·360px 통과본과 동일한 본문·인라인 스타일,
  H3의 공백 단위 줄바꿈 규칙을 대조해 보완했습니다.
- 다시 열어 확인한 파일: `article.md`, `brief.md`, `evidence.md`,
  `audit.md`, `artifacts/experiment-results.json`, 사례별
  `result.json`·`summary.md`, `dist/prompt-injection-document-test.html`

## 검사와 남은 위험

- 검사 명령:
  - `python3 scripts/blog.py check posts/2026-07-28-prompt-injection-document-test`
  - `python3 scripts/blog.py render posts/2026-07-28-prompt-injection-document-test`
  - `python3 -m unittest discover -s tests -v`
  - `python3 scripts/blog.py check --all`
  - `quick_validate.py` - 변경된 workspace·writing·article-validation·
    prose-polish 스킬 4개
- 검사 결과: 최신 `ready` 원고의 개별 `check` 오류 0개·경고 0개,
  `blog.py render` 성공. 단위 테스트 22개 통과, 전체 글 11개 오류 0개·경고
  0개, 변경 스킬 4개 `Skill is valid!`를 확인했습니다. 제목·소제목 수정본의
  HTML은 H3 7개·표 3개·코드 1개·깨진 Markdown 0개이며, 최종 파일은
  `dist/prompt-injection-document-test.html`입니다.
- 아직 남은 위험: 공격 형식 3개를 조건별 1회 실행한 작은 표본이며, 이미지·
  적응형·다국어 공격과 실제 브라우저·메일·민감 정보 도구는 검증하지 않음
- 사람이 티스토리에서 확인할 항목: 대표 이미지와 인포그래픽을 안내 위치에
  수동 업로드했는지, 티스토리 스킨에서도 긴 공격 문장 코드 블록의 가로 스크롤이
  유지되는지
