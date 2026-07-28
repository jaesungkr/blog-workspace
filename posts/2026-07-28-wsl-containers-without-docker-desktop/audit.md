# 최종 감사: WSL Containers 사용법 - Docker Desktop 없이 Windows에서 컨테이너 실행

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
- [x] 굵은 강조가 문단마다 반복되지 않습니다.
- [x] em dash(`—`), 분리된 참고문헌 부록, 관성적인 면책 문구가 없습니다.
- [x] 카테고리별 마무리 기준을 따릅니다.

## 대표 이미지

- [x] 최종 이미지를 생성한 뒤 실제 결과를 열어 확인했습니다.
- [x] 이미지가 글의 핵심 메시지와 맞고 근거 이상의 내용을 암시하지 않습니다.
- [x] 로고·워터마크·불필요한 내장 텍스트가 없습니다.
- [x] 대표 이미지의 반응형 크롭을 고려한 안전 여백이 있습니다.

- 최종 파일: `assets/wsl-containers-hero.png`
- 최종 크기: `1672x941` PNG, SHA-256
  `96347656185893f9fd7cfdfe4885fd44c270c7a7ac78a0229cc88e73bece5415`
- 권장 위치: `대표 이미지 - 제목 바로 아래`
- 한국어 alt: 밝은 창문형 구조 안의 주황색 Linux 엔진이 레일을 통해 파란 컨테이너를 내보내는 모습
- 생성 방법: OpenAI 내장 이미지 생성 워크플로, 신규 생성 뒤 검은 글자 타일만
  국소 편집, 참조 이미지 없음
- 주제 인식 단서: 밝은 건축 창문 안에 주황색 Linux 기계실이 중첩되고, 그
  안의 엔진이 골이 진 컨테이너 모듈 하나를 직접 내보냅니다. Docker Desktop
  화면이나 로고 없이도 `Windows -> WSL의 Linux Engine -> container`라는
  핵심 구조를 물리적 은유로 보여 줍니다.
- 후보 전체 관찰: 벽체·세라믹·알루미늄·케이블·컨테이너의 표면 반응과 접촉
  그림자가 일관되고, 레일이 기계 장치에서 컨테이너까지 끊기지 않습니다.
  1차 후보의 왼쪽 아래 검은 타일에 `L_`처럼 읽히는 문구가 있어 제거했으며,
  수정본에는 글자·로고·가짜 UI가 없습니다.
- 후보 320x180 관찰: 창문형 외곽, 주황색 엔진, 파란 컨테이너와 전진 레일이
  한 번에 읽힙니다. 오른쪽의 여백과 사방의 안전 여백이 유지되고 작은 기계
  부품이 문구처럼 보이지 않습니다.
- 주제 인식·교체 테스트: 파란 화물 컨테이너만 떼어 보면 물류 자동화로 바꿀
  수 있지만, 최종 화면에서는 밝은 창문형 외곽 안에 주황색 Linux 기계실이
  중첩되고 그 엔진이 컨테이너를 직접 내보냅니다. 일반 물류·클라우드·데이터
  베이스로 주제를 바꾸면 `window -> Linux chamber -> container`의 세 겹
  구조가 불필요해져 핵심 은유가 약해지므로 `pass`입니다.
- 캠페인 품질 관찰: 비대칭 전진 레일이 한 번에 초점을 만들고, 우측 여백과
  사방 안전 여백이 반응형 크롭을 견딥니다. 넓은 확산광과 내부의 절제된
  난색광이 같은 방향의 그림자를 만들며, 벽체의 미세 요철·세라믹의 무광·금속
  결·케이블 직조·컨테이너 골이 서로 다른 표면으로 보입니다. 레일 연결,
  컨테이너 모서리, 문 잠금봉과 접촉 그림자에도 변형·부유·halo가 없습니다.
- 레퍼런스 비교: 사용자 또는 공식 시각 레퍼런스가 없어 해당 없음. 글의
  실행 사슬과 공식 제품 범위만 인식 근거로 사용했습니다.
- 독립 대표 이미지 검증: `pass`
- 후보 생성 프롬프트:

  `Use case: stylized-concept. Korean Tistory 16:9 hero for running Linux
  containers inside WSL 2 on Windows without Docker Desktop. A meticulously
  crafted practical miniature of a luminous architectural window cut into a
  thick warm-ivory wall. Inside is a compact Ubuntu-toned Linux machine room
  made from matte orange ceramic, woven cable, and brushed aluminum; a precise
  mechanical rail carries one unmistakable small corrugated cargo-container
  module outward through the open window. The window, inner Linux chamber,
  engine mechanism, and single container read as nested layers. Museum-catalog
  object photography, controlled asymmetry, three-quarter camera, broad
  diffused daylight, soft neutral fill, coherent contact shadows, warm ivory,
  sand, silver, restrained burnt orange and one muted container-blue accent.
  Believable plaster, ceramic, anodized aluminum, corrugated painted metal and
  woven cable. No desktop app, laptop, dashboard, logos, brand marks,
  watermark, title, labels, readable letters, pseudo-code, fake UI,
  explanatory panels, people, Docker whale, Windows logo, glowing cloud,
  floating cubes, circuit background, cyberpunk, neon, glassmorphism, plastic
  icons, perfect symmetry or clutter.`
- 후보 국소 편집 프롬프트:

  `Remove only the small black square terminal tile with the white
  L_-like marks from the lower-left ledge. Replace it with matching warm
  ivory mineral plaster. Keep the architectural window, orange Linux chamber,
  brushed-metal engine, blue corrugated container, rail, camera, crop,
  lighting, materials and shadows unchanged. Add no text, symbol, logo or new
  object.`

## 보조 인포그래픽

- 판단: `1장`
- 판단 이유: Windows -> WSL 2 -> Ubuntu·Docker Engine -> 컨테이너의 중첩
  구조와 `localhost:8080`의 반환 경로를 한 화면에서 보여 주면 Docker
  Desktop을 제거해도 WSL 2는 남는다는 핵심을 더 빨리 이해할 수 있습니다.
- Reflections 예외 근거(해당하는 경우):
- [x] 각 인포그래픽이 장식이나 단순 반복이 아니라 하나의 중요한 관계를 더 빨리 이해하게 합니다.
- [x] 핵심 설명 바로 뒤에 둘 위치를 정했습니다.
- [x] 한국어 문구·수치·화살표·라벨을 결정적으로 조판하고 본문 근거와 대조했습니다.
- [x] 전체 크기와 360px 모바일 너비에서 실제 결과를 확인했습니다.
- [x] 두 장 이상이면 각 이미지가 서로 다른 독자 질문에 답합니다. (`1장`이라 해당 없음)

| 최종 파일 | 유형 | 해결하는 독자 질문 | 권장 위치 | 한국어 alt | 문구·수치 근거 |
|---|---|---|---|---|---|
| `assets/wsl-containers-layers-infographic-v4.png` | 원리 | Docker Desktop이 없을 때 Engine과 컨테이너는 어디서 실행되고 Windows 브라우저는 어떻게 접속하는가? | `먼저 구분할 네 층`의 실행 사슬 바로 뒤 | Windows 안의 WSL 2와 Ubuntu, Docker Engine, Linux 컨테이너가 중첩되고 localhost 8080으로 브라우저에 연결되는 구조 | 본문 네 층·Nginx 실행·PowerShell 호출, evidence C02~C05·C08~C10 |

- 최종 해상도: `1080x1350` (`4:5`), SHA-256
  `e1e26c5b58ddb288ea202b0c878e6e4ba1a91428ef7c289c9ac0fb638b13d137`
- 편집 원본: `artifacts/wsl-containers-layers-infographic.html`
- 렌더 스크립트: `artifacts/render-wsl-containers-infographic.cjs`
- 문구 근거 지도: `artifacts/infographic-copy-map.md`
- 제작 방식: Apple SD Gothic Neo를 사용하는 결정론적 HTML/SVG를 설치된
  Chrome과 Playwright로 1080x1350·360x450에 렌더했습니다. 이미지 생성
  계층은 사용하지 않았습니다.
- 360px 환산 글자 크기: 헤드라인 20px, 주요 라벨 14px·12.7px, 보조 문구
  10.7px·10px, 범위 문구 10px. 모두 기본 밴드 안입니다.
- 헤더 높이 비중: `225 / 1350 = 16.7%`, 상한 22% 이내입니다.
- 최종 전체 관찰: Windows 바깥 경계 안에 WSL 2, Ubuntu 24.04, Docker
  Engine, Linux 컨테이너가 단계별로 중첩됩니다. 오른쪽의 주황 요청선은
  `localhost:8080 -> 8080 → 80 -> container`로 내려가고 초록 응답선은
  브라우저로 올라갑니다. 하단의 Ubuntu 셸과 PowerShell은 같은 Engine에
  명령을 보내는 두 입구로 분리됩니다.
- 최종 360x450 관찰: 헤드라인보다 중첩된 네 층이 더 큰 면적으로 먼저
  보이고, 다섯 핵심 영역과 두 연결선, 두 명령 입구, 범위 문구를 확대 없이
  읽을 수 있습니다.
- 확대 크롭 관찰: 헤드라인, Windows·WSL·브라우저, Ubuntu·Engine,
  연결선, 컨테이너, 명령·범위 문구를 최종 PNG에서 각각 잘라 확인했습니다.
  주황 화살촉은 컨테이너를, 초록 화살촉은 브라우저를 가리켜 색을 제외해도
  방향을 구분할 수 있습니다. 글리프·라벨·경계·화살표 사이의 겹침은 없습니다.
- 확대 검수 파일: `artifacts/infographic-v4-qa/01-headline.png`부터
  `06-commands-caveat.png`까지
- 독립 보조 인포그래픽 검증: `pass`

## 최종 검토와 수정 이력

- [x] 완성 원고를 처음부터 끝까지 외부 독자 관점으로 다시 읽었습니다.
- [x] 렌더된 티스토리 HTML에서 제목·문단·표·코드·링크·이미지 위치를 확인했습니다.
- [x] 대표이미지는 전체·썸네일, 보조 인포그래픽은 전체·360px 결과를 실제로 확인했습니다.
- [x] 사용자 제공 시각 레퍼런스가 있다면 같은 표시 크기로 나란히 비교했습니다. (제공된 레퍼런스 없음)
- [x] 아래 문제를 수정한 뒤 관련 검사·렌더·시각 검토를 다시 실행했습니다.

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | 진단 스크립트 테스트 | CLI 누락 시나리오가 예상한 실패 4개 대신 3개를 반환 | service가 active인 fixture 조건에 맞춰 기대 종료 코드를 4에서 3으로 수정 | 같은 5개 시나리오 재실행에서 5/5 통과 |
| 2 | 원고 구조·근거 | WSL 실기기 없이 일반 Docker 명령만 실행하면 제목의 직설치 경로를 검증한 것처럼 보일 위험 | WSL 단계는 공식 문서, first-party 결과는 진단 분기 검증으로 분리하고 한계를 도입부·결과에 명시 | `evidence.md`의 주장 유형과 본문 표현을 대조해 과장 없음 확인 |
| 3 | 1차 독립 글 검증 | WSL·Compose·apt·daemon socket이 설명 전 표나 문장에 먼저 등장하고, E04 종료 코드가 원자료의 2와 달리 1로 기록됨 | 각 용어를 첫 표 전후에 쉬운 말로 정의하고 표의 `apt`를 풀어 씀. E04를 종료 2로 정정 | 본문을 처음부터 다시 읽고 `checker-test-log.txt`와 E01~E05를 재대조해 선행 용어·수치 불일치 없음 |
| 4 | 1차 자동·렌더 검증 | 원고와 근거는 통과했지만 `reviewing` 상태라 렌더 명령이 수명주기 규칙에 따라 중단됨 | 이미지 검증 전에는 상태를 올리지 않고 최종 글 검증 단계로 렌더를 넘김 | `blog.py check` 오류·경고 0, 셸 구문 검사 통과, 진단 테스트 5/5 통과, source-level `pass` |
| 5 | 대표 이미지 전체·썸네일 | 1차 생성본 왼쪽 아래 타일의 `L_` 형태가 불필요한 내장 문구로 읽힘 | 구도·조명·재질은 유지하고 검은 타일만 같은 미장 벽체로 국소 편집 | 수정본 1672x941·320x180 재검토에서 문구·로고·가짜 UI 0, 구조 인식·물성·크롭 통과, hero `pass` |
| 6 | 인포그래픽 렌더 환경 | Playwright 번들 브라우저가 없어 첫 렌더가 중단됨 | 설치된 Chrome을 자동 감지하도록 렌더 스크립트를 보완 | 추가 설치 없이 1080x1350·360x450 렌더 성공 |
| 7 | 인포그래픽 v1~v3 조기 검토 | v1은 배지·브라우저·층 라벨이 서로 겹쳤고, v2는 브라우저·커널 라벨과 도형이 닿았으며, v3의 문 잠금봉은 모바일에서 `H`처럼 보임 | 브라우저를 WSL 밖으로 올리고 오른쪽 연결 통로를 분리한 뒤, 라벨 여백을 넓히고 오독되는 잠금봉을 제거해 v4 생성 | v4 전체·360px에서 문구와 경계 분리, 타입 스케일 전 항목과 독립 확대 검증 통과 |
| 8 | 인포그래픽 v4 독립 검증 | 최종 PNG 자체에는 결함이 없었지만 문구 지도에 v4에서 제거한 응답 문장과 문 잠금봉 설명이 남아 있었음 | 실제 조판 문구만 남기고 잠금봉을 세로 골 설명으로 정정. 최종 PNG에서 여섯 영역을 확대 크롭 | 전체·360px·확대 크롭에서 한글 글리프, 화살촉 방향, 라벨 여백과 경계 충돌 없음. infographic `pass` |
| 9 | 1차 티스토리 HTML 렌더 | 줄바꿈을 가로지른 굵은 강조 4곳이 `<strong>`으로 바뀌지 않고 `**`와 내부 백틱을 그대로 노출 | 네 강조 문장을 각각 한 줄의 Markdown 범위로 정리하고 글 상태를 `reviewing`으로 되돌림 | 2차 HTML에서 literal Markdown 0, `<strong>` 4개, 760px 강조 문장 정상 표시 |
| 10 | 2차 HTML 360px 모바일 렌더 | 진단 3열 표의 최소 폭이 460px이 되어 360px 본문을 478px까지 밀어냄 | 여섯 진단 항목을 같은 `증상 -> 명령 -> 조치` 정보를 가진 목록으로 변경 | 최종 360px에서 본문 360/360px, 넘치는 본문 자식·표 0. 긴 코드 5개만 자체 가로 스크롤 |
| 11 | 최종 원고·HTML·시각 산출물 | 중대한 문제 없음 | 없음 | 원고 전체 재독, 760px 7구간·360px 4핵심 구간, 대표 이미지 전체·320px, 인포그래픽 전체·360px·확대 6구간에서 결함 없음 |

- 중대한 문제가 없으면 `발견한 문제`에 `없음`이라고 쓰고 확인 근거를
  `재검증 결과`에 적습니다.
- 최종 종료 판단: `pass`, 글 상태 `ready`
- 다시 열어 확인한 파일:
  - `article.md`, `evidence.md`, `brief.md`, `audit.md`
  - `artifacts/source-notes.md`, `checker-test-log.txt`,
    `wsl-docker-check.sh`, `test-wsl-docker-check.sh`
  - `dist/wsl-containers-without-docker-desktop.html`
  - `assets/wsl-containers-hero.png`,
    `artifacts/hero-thumbnail-320x180.png`
  - `assets/wsl-containers-layers-infographic-v4.png`,
    `artifacts/wsl-containers-layers-infographic-v4-mobile.png`,
    `artifacts/infographic-v4-qa/01-headline.png`부터
    `06-commands-caveat.png`까지
  - `artifacts/article-preview-760/section-01.png`부터 `section-07.png`,
    `artifacts/article-preview-360/focus-01.png`부터 `focus-04.png`

## 검사와 남은 위험

- 검사 명령: `python3 scripts/blog.py check posts/2026-07-28-wsl-containers-without-docker-desktop`
- 검사 결과: 최종 `check` 오류 0개·경고 0개, 두 셸 스크립트 구문 검사 통과,
  진단 테스트 5/5 통과. `render` 성공, 글 상태 `ready`
- 렌더 결과: `dist/wsl-containers-without-docker-desktop.html`,
  `35,769 bytes`, SHA-256
  `f3f7074dc7979356b2c7d88776ff5bbf899f23418bd6d65dafe9155087f69ca7`
- HTML 구조 검사: H3 10개, 표 2개, 코드 블록 18개, 외부 링크 7개,
  `<strong>` 4개, literal Markdown·TODO·FIXME 0개
- 레이아웃 검사: 760px에서 본문 760/760px·표 넘침 0·가로 스크롤 코드
  2개, 360px에서 본문 360/360px·넘치는 본문 자식 0·표 넘침 0·가로
  스크롤 코드 5개. 모든 코드 블록의 `overflow-x:auto` 적용 확인
- 아직 남은 위험: 실제 WSL 장비의 설치·성능·VPN·보안 제품 호환성은
  검증하지 않았습니다. 이 한계는 도입부, 근거 지도, 진단 결과에 명시했습니다.
  티스토리 테마의 추가 CSS와 수동 이미지 업로드 뒤의 최종 공개 화면은
  게시 직전에 사람이 확인해야 합니다.
- 사람이 티스토리에서 확인할 항목:
  - 제목 바로 아래에 `assets/wsl-containers-hero.png`를 올리고 기록된 한국어
    alt를 적용합니다.
  - `먼저 구분할 네 층`의 실행 사슬 바로 뒤에
    `assets/wsl-containers-layers-infographic-v4.png`를 올리고 기록된 alt를
    적용합니다.
  - PC와 360px 모바일 미리보기에서 테마 CSS가 표·코드 스크롤과 이미지
    안전 여백을 바꾸지 않는지 마지막으로 확인합니다.
