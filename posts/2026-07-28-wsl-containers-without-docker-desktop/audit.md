# 최종 감사: WSL2 Docker 설치: Docker Desktop 없이 Ubuntu에서 컨테이너 실행

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

- [x] 제목과 소제목만 읽어도 WSL2 Docker 구성, Desktop과의 선택, 설치,
  실행, 오류 진단, 보안 관리의 흐름이 보입니다.
- [x] 현재 검색 결과에서 `WSL Docker`, `WSL2 Docker 설치`,
  `Docker Desktop 없이 Docker` 의도를 비교했습니다. 검색량 도구를 사용하지
  않은 정성 판단임을 `brief.md`에 기록했습니다.
- [x] 다른 기술 글에도 붙일 수 있던 범용 소제목을 실제 설치 위치·확인 대상·
  오류 범위가 드러나는 표현으로 바꿨습니다.
- [x] 각 소제목만 읽어도 Windows·Ubuntu·Engine·컨테이너 중 무엇을 설치하거나
  확인하는지 알 수 있습니다.
- [x] 문단 사이에서 앞 문단의 실행 위치, 관리 주체, 권한, 오류 문구를 다음
  판단이 이어받도록 연결했습니다.
- [x] 명령·URL·표·수치·Codex 실행 주체·실기기 미검증 한계를 폴리싱 전
  원고와 대조했습니다.
- [x] 자연스러움을 위해 사용자 경험·감정·대화·실패를 새로 만들지 않았습니다.

- 비교 표본(대상 슬러그 제외):
  - 같은 하위 카테고리 `개발 · 디지털`:
    `ccshare-manycode-guide` (`ready`), `duckdb-guide` (`ready`)
  - 대체 표본: `orca-agent-ide-guide` (`ready`),
    `prompt-injection-document-test` (`ready`)
- 대체 기준: 같은 하위 카테고리의 완성 글이 2편뿐이어서 설치·도구 사용법
  형태가 가까운 Orca 글과, 새 폴리싱 기준이 적용된 최근 기술 실험 글을
  보충해 총 4편을 비교했습니다.
- 대표 제목 변경:
  `WSL Containers 사용법 - Docker Desktop 없이 Windows에서 컨테이너 실행`
  -> `WSL2 Docker 설치: Docker Desktop 없이 Ubuntu에서 컨테이너 실행`
- 대표 소제목 변경:
  - `먼저 구분할 네 층` ->
    `WSL2 Docker 구성: Windows·Ubuntu·Docker Engine·컨테이너`
  - `직접 설치가 맞는 경우` ->
    `Docker Desktop과 WSL2 Docker 직접 설치의 차이와 선택 기준`
  - `3. Docker Engine 설치` ->
    `3. Ubuntu에 Docker Engine·Buildx·Compose 설치`
  - `4. 서비스와 사용자 권한 확인` ->
    `4. docker.service와 Docker socket 권한 확인`
  - `5. 첫 웹 컨테이너 실행` ->
    `5. Nginx 컨테이너를 127.0.0.1:8080으로 실행`
  - `7. 실패 지점을 가르는 진단` ->
    `7. WSL2 Docker 오류를 WSL·서비스·권한·경로로 진단`
  - `보안과 운영의 경계` ->
    `WSL2 Docker 보안: docker 그룹·포트·업데이트 관리`
- 대표 문단 연결 수정: 도입부의 기계적인 글 순서 안내를 없애고 공식 문서와
  Codex 진단 검증의 역할을 바로 구분했습니다. Docker Desktop과 직접 설치의
  관리 주체, `docker` 그룹의 편의와 root급 권한, 오류 문구와 첫 확인 명령이
  앞뒤 문단에서 같은 대상을 이어받도록 고쳤습니다.
- 삭제한 빈 문구 또는 반복: `이 글에서는 ... 함께 살펴보겠습니다`,
  `Docker Desktop 없이 시작할 기본 경로는 분명합니다`, 추상적인
  `다음 경계`, `다음 지점` 표현
- 보존 확인한 핵심 사실: Windows 10 2004·빌드 19041 이상 또는 Windows 11,
  Ubuntu 24.04 LTS 예시, Docker 공식 저장소 명령, `docker` 그룹의 root급
  권한, `127.0.0.1:8080:80`, 진단 시나리오 5개와 5/5 통과, Codex 실행 주체,
  실제 WSL 장비에서 설치·성능·VPN 호환성을 검증하지 않은 한계
- 남은 문체·근거 위험: 제목과 소제목을 검색 의도에 맞춰 구체화했지만 실제
  검색량 자료는 없습니다. 제품 설치 성공 여부를 실기기로 확인하지 못한
  근거 한계는 그대로 남아 있으며 본문 도입부와 진단 결과에 명시했습니다.

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
  구조와 `localhost:8080`의 요청 경로를 한 화면에서 보여 주면 Docker
  Desktop을 제거해도 WSL 2는 남는다는 핵심을 더 빨리 이해할 수 있습니다.
- Reflections 예외 근거(해당하는 경우):
- [x] 각 인포그래픽이 장식이나 단순 반복이 아니라 하나의 중요한 관계를 더 빨리 이해하게 합니다.
- [x] 핵심 설명 바로 뒤에 둘 위치를 정했습니다.
- [x] 한국어 문구·수치·화살표·라벨을 결정적으로 조판하고 본문 근거와 대조했습니다.
- [x] 원본 크기와 원본의 360px CSS 표시 환산값을 확인했습니다. 축소 파생
  래스터는 생성하지 않았습니다.
- [x] 두 장 이상이면 각 이미지가 서로 다른 독자 질문에 답합니다. (`1장`이라 해당 없음)

| 최종 파일 | 유형 | 해결하는 독자 질문 | 권장 위치 | 한국어 alt | 문구·수치 근거 |
|---|---|---|---|---|---|
| `assets/wsl-containers-layers-infographic-v7.png` | 원리 | Docker Desktop이 없을 때 Engine과 컨테이너는 어디서 실행되고 Windows 브라우저는 어떻게 접속하는가? | `WSL2 Docker 구성: Windows·Ubuntu·Docker Engine·컨테이너`의 실행 사슬 바로 뒤 | Windows 안의 WSL 2와 Ubuntu, Docker Engine, Linux 컨테이너가 네 층으로 이어지고 localhost 8080으로 연결되는 구조 | 본문 네 층·Nginx 실행, evidence C02~C05·C08~C10 |

- 최종 해상도: `1080x1350` (`4:5`), SHA-256
  `af765879a72a0628544987e8418ffd09677e6095d6ad12016451e89558c59be6`
- 편집 원본: `artifacts/wsl-containers-layers-infographic.html`
- 렌더 스크립트: `artifacts/render-wsl-containers-infographic.cjs`
- 문구 근거 지도: `artifacts/infographic-copy-map.md`
- 제작 방식: Apple SD Gothic Neo를 사용하는 결정론적 HTML/SVG를 설치된
  Chrome과 Playwright로 원본 1080x1350 한 장만 렌더했습니다. 실행 로그의
  `reducedRasterWritten:false`를 확인했으며 축소·재인코딩한 모바일 래스터는
  생성하거나 보존하지 않았습니다. 이미지 생성 계층도 사용하지 않았습니다.
- 이전 v4 객관 평가: 1080px 원본은 선명해 보였고 흐림·압축 손상은 없습니다.
  기존 360x450 파일도 v4 PNG를 후처리 축소한 결과가 아니라 같은 SVG를
  360px에 다시 렌더한 결과였습니다. 문제의 핵심은 보조 문구가 360px 표시
  기준 10~10.7px에 머문 상태에서 다섯 영역, 요청·응답선, 두 명령 입구와
  범위 문구가 한꺼번에 경쟁한 정보 밀도였습니다.
- v7 수정: WSL 2와 Ubuntu를 하나의 2단계로 합치고 응답선·두 명령 입구를
  제거했습니다. 네 단계, Engine에서 컨테이너로 가는 관리 화살표, 브라우저의
  `localhost:8080 -> 8080 → 80` 요청 경로와 Linux 컨테이너 범위만 남겼습니다.
- 360px CSS 환산 글자 크기: 헤드라인 22.7px, 주요 라벨 17.3px·16px,
  보조 문구 13.3px·12px, 범위 문구 12px. 강화한 기본 밴드를 모두
  통과했습니다.
- 헤더 높이 비중: `230 / 1350 = 17.0%`, 상한 22% 이내입니다.
- 최종 전체 관찰: Windows 경계 안에서 `WSL 2 + Ubuntu -> Docker Engine ->
  Linux 컨테이너`가 위에서 아래로 읽힙니다. 브라우저는 Linux 경계 밖에 있고,
  주황 요청선은 `localhost:8080`에서 컨테이너 80번 포트로 이어집니다.
  하단 범위 문구는 Windows 컨테이너와 GUI가 별도임을 분리합니다.
- 360px CSS 표시 검증: `artifacts/infographic-css-preview.html`은
  1080x1350 원본을 그대로 참조해 브라우저에서 360x450으로 표시하도록
  작성했습니다. 인앱 브라우저의 로컬 파일 URL 정책으로 직접 열 수 없었고,
  이를 우회하거나 축소 스크린샷을 만들지 않았습니다. 고정 비율 SVG의 환산
  크기와 원본 전체 관찰에서 네 단계와 한 요청 경로가 먼저 읽혔으며, 실제
  티스토리 테마의 360px 표시는 게시 전 사람이 다시 확인합니다.
- 확대 크롭 관찰: 헤드라인, Windows·브라우저, WSL 2+Ubuntu, Engine,
  포트 경로, 컨테이너·범위를 최종 원본 픽셀에서 각각 잘라 확인했습니다.
  모든 한글 글리프, 포트 수치, 경계, 화살촉에 겹침이나 잘림이 없습니다.
- 확대 검수 파일: `artifacts/infographic-v7-qa/01-header.png`부터
  `06-container-scope.png`까지
- 독립 보조 인포그래픽 검증: `pass`

## 최종 검토와 수정 이력

- [x] 완성 원고를 처음부터 끝까지 외부 독자 관점으로 다시 읽었습니다.
- [x] 렌더된 티스토리 HTML에서 제목·문단·표·코드·링크·이미지 위치를 확인했습니다.
- [x] 대표이미지는 전체·썸네일, 보조 인포그래픽은 원본·CSS 환산·원본 픽셀
  확대 크롭을 확인했습니다.
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
| 12 | 사용자 요청에 따른 v4 객관 재평가 | 원본 화질 손상은 없었지만 360px 표시에서 보조 글자 10~10.7px와 다수의 라벨·선·명령 입구가 경쟁해 구조가 과밀함 | 축소 파생 래스터 생성 절차를 표준·제작·검증 스킬에서 제거하고 모바일 권장 글자 밴드를 상향 | 현재 렌더러는 1080x1350 원본 한 장만 쓰며 `reducedRasterWritten:false`; 기존 360px 파생 QA 4개 삭제 |
| 13 | 인포그래픽 v5~v7 재설계 | v5는 WSL 배지와 포트 라벨이 맞닿고, v6은 브라우저 아이콘과 포트 문구의 CSS 환산 여백이 약 2px | 포트 주소를 브라우저 안으로 통합하고 브라우저 박스를 왼쪽으로 넓힌 뒤 v7 생성 | v7 전체·타입 스케일·원본 픽셀 확대 6구간에서 글리프·수치·경계·화살표 충돌 없음 |
| 14 | 무축소 모바일 표시 검증 | 인앱 브라우저가 로컬 파일 URL을 차단해 CSS 360px 미리보기를 직접 열 수 없음 | 우회하거나 축소 파일을 만들지 않고 고정 SVG의 정확한 환산값과 원본 크롭을 검증, 실제 티스토리 미리보기를 사람 확인 항목으로 유지 | 이미지 자체 결함 없음, infographic `pass`; 테마 CSS 결과는 잔여 위험으로 기록 |
| 15 | 제목·소제목·문단 흐름 | 제목이 최근 기술 글과 같은 `키워드 - 설명` 패턴이고, 범용 소제목과 기계적인 글 순서 안내가 남아 있음 | 검색 의도를 `WSL2 Docker 설치`부터 드러내고, 소제목에 설치 위치·확인 대상·오류 범위를 명시했습니다. 문단은 실행 위치·관리 주체·권한·오류 문구를 이어받도록 수정 | 코드 블록 18개·표 14줄·URL 19개·본문 수치 토큰의 폴리싱 전후 SHA-256 일치. 상투 문구 1→0, 50자 초과 문장 33→28, 교정형 표현 밀도 5.0→2.3. 독립 소스 검증·공식 문서 재대조·개별 check·재렌더·760px·360px 화면 검수 통과 |

- 중대한 문제가 없으면 `발견한 문제`에 `없음`이라고 쓰고 확인 근거를
  `재검증 결과`에 적습니다.
- 현재 종료 판단: `pass`, 글 상태 `ready`. 회차 15 수정본은 독립 소스 검증,
  잠근 내용 대조, Tistory HTML 재렌더, 760px·360px 화면 검수를 통과했습니다.
- 다시 열어 확인한 파일:
  - `article.md`, `evidence.md`, `brief.md`, `audit.md`
  - `artifacts/source-notes.md`, `checker-test-log.txt`,
    `wsl-docker-check.sh`, `test-wsl-docker-check.sh`
  - `dist/wsl-containers-without-docker-desktop.html`
  - `assets/wsl-containers-hero.png`,
    `artifacts/hero-thumbnail-320x180.png`
  - `assets/wsl-containers-layers-infographic-v7.png`,
    `artifacts/infographic-v7-qa/01-header.png`부터
    `06-container-scope.png`까지
  - `artifacts/article-preview-760/section-01.png`부터 `section-07.png`,
    `artifacts/article-preview-360/focus-01.png`부터 `focus-04.png`

## 검사와 남은 위험

- 검사 명령: `python3 scripts/blog.py check posts/2026-07-28-wsl-containers-without-docker-desktop`
- 검사 결과: 최종 `check` 오류 0개·경고 0개, 두 셸 스크립트 구문 검사 통과,
  진단 테스트 5/5 통과. `render` 성공, 글 상태 `ready`
- 표준·스킬 회귀 검사: 저장소 단위 테스트 22/22 통과,
  `python3 scripts/blog.py check --all` 11개 글 오류·경고 0개.
  `dev-log-infographic`와 `dev-log-infographic-validation`은
  `quick_validate.py`를 모두 통과했고 UI 메타데이터도 역할과 일치합니다.
- 무축소 검사: 현재 렌더러는 1080x1350 원본만 생성하고
  `reducedRasterWritten:false`를 출력합니다. 인포그래픽 모바일 파생 파일,
  `mobileOutput`, 360px 재렌더 코드는 현재 워크플로에 없습니다.
- 렌더 결과: `dist/wsl-containers-without-docker-desktop.html`,
  `36,213 bytes`, SHA-256
  `6d820218f70ca252802e35328d85e6a7049f4187c2af524d196eb9d568410a13`
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
  - `WSL2 Docker 구성: Windows·Ubuntu·Docker Engine·컨테이너`의 실행 사슬
    바로 뒤에
    `assets/wsl-containers-layers-infographic-v7.png`를 올리고 기록된 alt를
    적용합니다.
  - PC와 360px 모바일 미리보기에서 테마 CSS가 표·코드 스크롤과 이미지
    안전 여백을 바꾸지 않는지 마지막으로 확인합니다.
