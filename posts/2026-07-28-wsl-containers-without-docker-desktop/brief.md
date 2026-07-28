# 기획: WSL2 Docker 설치: Docker Desktop 없이 Ubuntu에서 컨테이너 실행

## 분류와 독자

- 상위 카테고리: `Log`
- 하위 카테고리: `개발 · 디지털`
- 한 명의 독자: Windows에서 Linux 컨테이너를 실행하고 싶지만 Docker
  Desktop의 GUI나 통합 기능은 필요하지 않은 개발자
- 검색 의도: `WSL Containers`, `WSL Docker`, `Docker Desktop 없이 Docker`,
  `WSL2 Docker Engine 설치`를 검색해 설치 순서, 실행 명령, 실패 원인과 한계를
  한 번에 확인함
- 검색 결과 판단: 2026-07-28 현재 `WSL Docker`, `WSL2 Docker 설치`,
  `Docker Desktop 없이 Docker` 검색 결과에서 WSL 2·Docker 설치와 Desktop
  제외 의도가 반복됨. 검색량 도구를 사용하지 않은 정성 판단이며 순위나 유입을
  보장하지 않음
- 독자가 이미 아는 것: PowerShell과 터미널에서 명령을 복사해 실행할 수 있음.
  WSL 2, Docker Engine, daemon, systemd는 쉬운 설명이 필요함

## 글의 중심

- 독자가 기억할 한 문장: Linux 컨테이너만 필요하다면 WSL 2의 Ubuntu 안에
  Docker Engine을 직접 설치해 Docker Desktop 없이 실행할 수 있지만, 엔진의
  업데이트·권한·문제 해결은 직접 맡아야 함
- 낯선 주제를 붙잡아 줄 익숙한 장면: Docker 명령 한 번 쓰려고 Windows에서
  별도 데스크톱 앱을 계속 실행해야 하는지 고민하는 장면
- 이 글이 답하지 않는 범위: Windows 컨테이너, GPU 패스스루, Kubernetes,
  기업용 중앙 정책, Docker Desktop 라이선스 판단, 실제 Windows 장비별 성능
  벤치마크
- 가장 정직한 한계 또는 반론: 작성 환경에 Windows·WSL 2가 없어 설치 전 과정을
  실기기로 재현하지 못함. 공식 명령을 교차 검토하고 상태 진단 스크립트의
  분기 5개를 모의 환경에서 검증했지만, 특정 Windows 빌드·VPN·보안 제품에서의
  성공을 보장하지 않음

## dev.log만의 근거

- first-party contribution: WSL 여부, systemd, Docker CLI, 서비스, daemon 접근,
  Compose, 프로젝트 경로를 한 번에 나누는 진단 스크립트를 만들고 정상·느린
  `/mnt/c` 경로·권한 거부·systemd 중지·CLI 누락의 5개 시나리오를 Codex가
  자동 검증함
- 실제 실행 주체: `Codex`
- 보존할 원자료: `artifacts/wsl-docker-check.sh`,
  `artifacts/test-wsl-docker-check.sh`, `artifacts/checker-test-log.txt`,
  `artifacts/source-notes.md`
- 기존 글 또는 시리즈 연결: dev.log의 Windows 문제 해결 글과 개발 도구
  실전 가이드 흐름을 잇고, 설치 명령보다 실패 지점을 분리하는 판단 순서를 강조함
- 다른 블로그 이름으로 바꿔도 성립하는 부분: Microsoft와 Docker의 공식 설치
  명령. 다섯 상태를 판정하는 진단 스크립트와 각 실패가 어느 층에서 생겼는지
  읽는 표가 dev.log의 검증 근거를 만듦
- 자율 주제 점수: 9/10
  - first-party evidence 2, search intent 2, cluster fit 1, reader action 2,
    trust and scope 2

## 설명 순서

| 순서 | 독자가 먼저 알아야 할 것 | 다음 내용과의 연결 |
|---|---|---|
| 1 | WSL 2, Ubuntu, Docker Engine, 컨테이너는 서로 다른 층임 | 어느 층의 오류인지 구분함 |
| 2 | 직접 설치 방식은 Linux 컨테이너와 터미널 중심 사용에 맞음 | Docker Desktop이 더 나은 예외를 먼저 정함 |
| 3 | WSL 2와 systemd를 준비해야 daemon을 서비스로 관리할 수 있음 | Docker Engine 설치 전제와 이어짐 |
| 4 | 공식 apt 저장소로 Engine·Buildx·Compose를 함께 설치함 | 단일 컨테이너와 Compose 실행으로 이어짐 |
| 5 | 상태 진단은 WSL -> systemd -> 서비스 -> socket -> 경로 순서임 | 오류 문구별 해결책을 빠르게 고름 |
| 6 | docker 그룹과 공개 포트는 편의가 아니라 권한 경계임 | 로컬 개발용 범위와 보안 한계를 정함 |

## 중앙 방법의 계산 또는 판단 사슬

실행 사슬:

`Windows -> WSL 2의 Linux 커널 -> Ubuntu의 systemd -> dockerd ->
이미지·컨테이너 -> 게시 포트 -> Windows 브라우저의 localhost`

문제 해결 사슬:

`WSL 2인가 -> PID 1이 systemd인가 -> docker.service가 active인가 ->
현재 사용자가 daemon socket에 접근하는가 -> Compose가 설치됐는가 ->
프로젝트가 Linux 파일시스템에 있는가`

## 보조 인포그래픽 판단

- 결정: `1장`
- 한눈에 보여 줄 관계: Windows 안의 WSL 2, 그 안의 Ubuntu·Docker Engine,
  컨테이너가 중첩되고 `localhost:8080`으로 Windows 브라우저까지 이어지는 구조
- 글이나 표만으로 충분하지 않은 이유: Docker Desktop을 뺀다는 말이 WSL 2까지
  없앤다는 뜻으로 오해되기 쉽습니다. 네 층과 요청 흐름을 한 화면에 놓으면
  설치 위치와 오류 경계를 더 빨리 이해할 수 있음
- 유형: `원리`
- 핵심 설명 뒤 권장 위치:
  `WSL2 Docker 구성: Windows·Ubuntu·Docker Engine·컨테이너` 절의 실행 사슬
  바로 뒤
- 추가 이미지가 있다면 각 이미지가 답할 서로 다른 질문: 1장으로 충분함

## 독자가 이어서 물을 질문

- Docker Desktop을 지우면 Windows에서도 `docker` 명령을 바로 쓸 수 있나요?
  -> Engine은 Ubuntu 안에 있으므로 Ubuntu 셸에서 쓰거나 PowerShell에서
  `wsl docker ...`로 호출한다고 설명함
- Windows 컨테이너도 실행할 수 있나요? -> 이 구성은 Ubuntu의 Linux Engine을
  쓰므로 Linux 컨테이너만 범위에 둠
- `permission denied`가 나오면 `sudo`만 계속 붙이면 되나요? -> docker 그룹은
  root급 권한을 주므로 개인 개발 장비에서만 판단해 추가하고 새 세션을 열어야 함
- 소스 코드를 `C:\`에 두어도 되나요? -> 작동은 가능하지만 Linux 도구와 bind
  mount 중심 작업은 `~/projects`가 공식 권장 경로임
- 결국 무엇부터 선택하면 되나요? -> Linux 컨테이너·터미널·직접 관리가
  괜찮으면 Engine 직설치, Windows 컨테이너·GUI·통합 관리가 필요하면
  Docker Desktop을 선택함

## 제목 후보

1. WSL2 Docker 설치: Docker Desktop 없이 Ubuntu에서 컨테이너 실행 (선택)
2. Docker Desktop 없이 Docker 설치: WSL2 Ubuntu 구성과 오류 해결
3. WSL2 Docker Engine 설치: Ubuntu 24.04 준비부터 권한 오류 진단

선택 이유: 가장 넓고 직접적인 검색 표현인 `WSL2 Docker 설치`를 앞에 두고,
글의 실제 차별점인 `Docker Desktop 없이`와 설치 위치인 Ubuntu를 이어
붙였습니다. 제목만 읽어도 설치 대상과 실행 결과를 알 수 있고, 본문이 다루지
않는 Windows 컨테이너나 실기기 성공률은 약속하지 않습니다.
