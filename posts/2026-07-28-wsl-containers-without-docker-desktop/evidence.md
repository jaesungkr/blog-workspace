# 근거 지도: WSL2 Docker 설치: Docker Desktop 없이 Ubuntu에서 컨테이너 실행

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 실제 근거의 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Windows 10 2004 빌드 19041 이상 또는 Windows 11은 관리자 PowerShell의 `wsl --install`로 WSL과 기본 Ubuntu를 설치할 수 있음 | 공식 | 확인 | Microsoft WSL 설치 문서 | 기존 WSL 설치 여부와 조직 정책에 따라 추가 단계가 생길 수 있음 |
| C02 | `wsl --install`은 기본값에서 WSL 2를 쓰며 `wsl -l -v`로 배포판 버전을 확인할 수 있음 | 공식 | 확인 | Microsoft WSL 설치·환경 문서 | 구형 inbox WSL은 먼저 업데이트가 필요할 수 있음 |
| C03 | 현재 기본 Ubuntu는 systemd가 기본이고, 다른 배포판·기존 설치는 `/etc/wsl.conf`에 `systemd=true`를 넣은 뒤 `wsl --shutdown`이 필요함 | 공식 | 확인 | Microsoft WSL systemd 문서 | 배포판에 따라 `systemd-sysv` 패키지가 추가로 필요할 수 있음 |
| C04 | Docker 공식 apt 저장소는 Engine, CLI, containerd, Buildx, Compose 플러그인을 함께 설치하는 명령을 제공함 | 공식 | 확인 | Docker Engine Ubuntu 설치 문서 | 저장소 패키지와 지원 Ubuntu 버전은 이후 바뀔 수 있음 |
| C05 | 설치 뒤 `systemctl status docker`와 `docker run hello-world`로 서비스·컨테이너 실행을 분리해 확인할 수 있음 | 공식 | 확인 | Docker Engine Ubuntu 설치 문서 | 이 글 작성 환경에서는 WSL 실기기로 실행하지 못함 |
| C06 | `docker` 그룹은 `sudo` 없는 CLI 사용을 허용하지만 사용자에게 root 수준 권한을 줌 | 공식 | 확인 | Docker Linux post-install 문서 | 다중 사용자·기업 장비에서는 관리 정책 검토가 필요함 |
| C07 | Linux 도구로 작업할 프로젝트는 `/mnt/c`보다 WSL의 `/home` 아래에 둘 때 파일시스템 성능이 좋음 | 공식 | 확인 | Microsoft WSL 파일시스템 문서 | 실제 차이는 작업 종류·파일 수·장비에 따라 달라 수치화하지 않음 |
| C08 | WSL 안에서 게시한 웹 서비스는 일반적인 로컬 개발 구성에서 Windows 브라우저의 `localhost`로 접근할 수 있음 | 공식 | 확인 | Microsoft WSL 네트워킹 문서 | LAN 공개, VPN, 방화벽, mirrored mode는 별도 범위임 |
| C09 | Docker Desktop과 배포판 안의 직접 설치 Engine을 한 배포판에서 섞으면 충돌할 수 있어 한 경로를 선택해야 함 | 공식 | 확인 | Docker Desktop WSL 문서가 직접 설치 Engine·CLI 제거를 선행 조건으로 안내 | 이미 설치된 이미지·volume의 이전 절차는 다루지 않음 |
| C10 | 이 글의 Ubuntu 직접 설치 방식은 Linux 컨테이너용이며 Windows 컨테이너 실행을 다루지 않음 | 공식 + 기술 범위 | 확인 | Ubuntu용 Linux Engine 설치 범위와 Docker Desktop Windows 문서 | Windows Server의 Windows 컨테이너 엔진은 별도 제품·절차임 |
| C11 | 진단 스크립트가 정상, `/mnt/c` 경고, socket 권한 거부, systemd·서비스 중지, Docker CLI 누락을 구분함 | Codex 실행 | 확인 | 자동 테스트 5개와 `artifacts/checker-test-log.txt` | 명령 분기 검증이며 실제 WSL 커널·Docker daemon 통합 테스트가 아님 |
| C12 | 로컬 Docker CLI는 있었지만 daemon이 실행되지 않아 컨테이너 smoke test는 수행하지 못함 | Codex 실행 | 확인 | 2026-07-28 macOS, Docker CLI 29.2.1, socket 연결 실패 | WSL 설치의 실패나 성공을 뜻하지 않음 |

## 직접 검증 설계

- 질문: 설치 뒤 흔히 만나는 다섯 상태를 진단 스크립트가 올바른 층의
  `PASS`·`WARN`·`FAIL`로 구분하는가?
- 실행 주체: Codex
- 환경과 확인 시점: 2026-07-28, macOS 26.5.2, Apple Silicon arm64,
  Bash 3.2.57
- 입력: 정상 WSL, `/mnt/c` 작업 경로, Docker socket 권한 거부,
  PID 1과 서비스 중지, Docker CLI 누락의 5개 모의 시나리오
- 전처리 또는 표현: 테스트 전용 임시 `PATH`, `/proc/version` 대체 파일,
  작업 경로 대체 값을 주입하고 실제 진단 스크립트는 수정하지 않음
- 비교·판정 규칙: 각 시나리오의 종료 코드와 핵심 진단 문구가 기대값과 모두
  같으면 통과
- 성공 기준: 5개 시나리오 모두 기대 종료 코드와 문구 일치
- 반복 횟수와 표본 크기: 시나리오당 1회, 총 5회
- 보존할 원자료: `artifacts/wsl-docker-check.sh`,
  `artifacts/test-wsl-docker-check.sh`, `artifacts/checker-test-log.txt`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | WSL·systemd·service·socket·Compose 정상, Linux 홈 경로 | 종료 0, 모든 핵심 단계 PASS | `artifacts/checker-test-log.txt` | 정상 분기 |
| E02 | 정상 상태에서 작업 경로만 `/mnt/c/projects/demo` | 종료 0, 파일 위치만 WARN | `artifacts/checker-test-log.txt` | 성능 권고는 실행 차단이 아님 |
| E03 | Docker daemon socket이 `permission denied` 반환 | 종료 1, 권한 문제로 특정한 FAIL | `artifacts/checker-test-log.txt` | 그룹·socket 계층 진단 |
| E04 | WSL이지만 PID 1이 `init`, docker.service가 inactive | 종료 2, systemd와 서비스에 각각 FAIL | `artifacts/checker-test-log.txt` | 서비스 관리 계층 진단 |
| E05 | 서비스는 active지만 Docker CLI 자체가 없음 | 종료 3, CLI·daemon·Compose FAIL과 service PASS | `artifacts/checker-test-log.txt` | 패키지 구성과 서비스 상태가 독립적일 수 있음을 확인 |

## 실패와 반례

- 실패한 입력: 로컬 macOS의 Docker CLI 29.2.1로 daemon 정보를 읽으려 했지만
  Docker Desktop daemon이 실행 중이 아니어서 socket 연결에 실패함
- 예상과 달랐던 결과: 제품 실험을 위해 Docker Desktop을 켜는 것은 글의 WSL
  직접 설치 경로를 검증하지 못하므로, 일반 컨테이너 smoke test를 근거로
  확대하지 않고 진단 스크립트의 분기 검증으로 범위를 좁힘
- 일반화하면 안 되는 범위: 5/5 통과는 스크립트의 판단 로직을 검증한
  결과입니다. Windows 10·11의 모든 빌드, 회사 VPN·보안 제품, 실제 WSL
  네트워킹과 Docker 패키지 설치 성공률을 측정한 결과가 아님

## 미해결 항목

- 없음. WSL 실기기 설치·성능·VPN 호환성은 미해결 주장이 아니라 이 글이
  검증하지 않은 범위로 본문에 명시함

## 출처 메모

- Microsoft WSL 설치:
  https://learn.microsoft.com/en-us/windows/wsl/install
- Microsoft WSL systemd:
  https://learn.microsoft.com/en-us/windows/wsl/systemd
- Microsoft WSL 파일시스템:
  https://learn.microsoft.com/en-us/windows/wsl/filesystems
- Microsoft WSL 네트워킹:
  https://learn.microsoft.com/en-us/windows/wsl/networking
- Docker Engine Ubuntu 설치:
  https://docs.docker.com/engine/install/ubuntu/
- Docker Linux post-install:
  https://docs.docker.com/engine/install/linux-postinstall/
- Docker Engine 보안:
  https://docs.docker.com/engine/security/
- Docker Desktop WSL:
  https://docs.docker.com/desktop/features/wsl/

긴 원문은 복사하지 않고, 본문 주장 옆에 필요한 링크와 한계를 함께 둡니다.
