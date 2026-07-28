# 공식 출처 확인 메모

확인일: 2026-07-28

## Microsoft WSL 설치

- URL: https://learn.microsoft.com/en-us/windows/wsl/install
- Windows 10 2004 빌드 19041 이상 또는 Windows 11에서 `wsl --install` 간편
  설치를 안내합니다.
- 기본 명령은 WSL 기능과 Ubuntu를 설치하며, 이미 WSL이 있으면
  `wsl --list --online`과 `wsl --install -d <DistroName>` 경로를 안내합니다.
- 본문 적용: 설치 전 `wsl --version`, `wsl --update`, 온라인 배포판 이름
  확인을 앞에 두었습니다.

## Microsoft WSL systemd

- URL: https://learn.microsoft.com/en-us/windows/wsl/systemd
- 현재 기본 Ubuntu는 systemd가 기본입니다.
- 다른 배포판이나 기존 설치는 WSL 0.67.6 이상에서 `/etc/wsl.conf`의
  `[boot] systemd=true`를 설정하고 `wsl --shutdown` 뒤 다시 시작하도록
  안내합니다.
- 본문 적용: systemd를 무조건 설정하지 않고 PID 1 확인 뒤 필요한 경우만
  적용합니다.

## Docker Engine on Ubuntu

- URL: https://docs.docker.com/engine/install/ubuntu/
- 공식 GPG 키와 `docker.sources`를 만든 뒤 `docker-ce`,
  `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin`,
  `docker-compose-plugin`을 설치합니다.
- 설치 뒤 `systemctl status docker`, `docker run hello-world`를 검증
  명령으로 안내합니다.
- convenience script는 테스트·개발 환경에만 권장합니다.
- 게시 포트가 `ufw` 규칙을 우회할 수 있다는 경고가 있습니다.

## Docker Linux post-install

- URL: https://docs.docker.com/engine/install/linux-postinstall/
- `docker` 그룹은 Unix socket 접근을 허용하지만 root 수준 권한을 부여합니다.
- `usermod -aG docker`, 새 로그인 또는 `newgrp docker` 뒤
  `docker run hello-world`를 안내합니다.

## WSL 파일과 네트워크

- 파일 URL: https://learn.microsoft.com/en-us/windows/wsl/filesystems
- 네트워크 URL: https://learn.microsoft.com/en-us/windows/wsl/networking
- Linux 명령으로 다루는 프로젝트는 `/mnt/c`보다 `/home` 아래에 둘 때 더
  좋은 파일시스템 성능을 기대할 수 있습니다.
- WSL 안의 로컬 웹 서비스는 Windows 브라우저에서 `localhost`로 접근할 수
  있습니다. LAN 공개는 기본 NAT와 방화벽을 따로 고려해야 합니다.

## Docker Desktop과의 경계

- URL: https://docs.docker.com/desktop/features/wsl/
- Docker Desktop은 자체 `docker-desktop` WSL 배포판과 선택한 배포판의
  통합을 제공합니다.
- Desktop을 쓰기 전에 배포판 안에 직접 설치한 Engine·CLI를 제거하라고
  안내하므로, 한 배포판에서 두 관리 경로를 섞지 않는 판단 근거로 썼습니다.

## 작성 환경에서의 확인 한계

- 운영체제: macOS 26.5.2, Apple Silicon arm64
- 로컬 Docker CLI: 29.2.1
- daemon 상태: Docker socket에 연결할 수 없어 실제 컨테이너 smoke test 미실행
- 판단: Docker Desktop을 켜서 일반 Linux 컨테이너 명령만 실행해도 WSL
  직설치 경로의 통합 검증이 되지 않습니다. 해당 결과를 만들지 않고
  WSL 전용 단계는 공식 출처, first-party 결과는 진단 스크립트 분기 검증으로
  분리했습니다.
