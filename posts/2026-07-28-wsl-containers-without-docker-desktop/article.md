---
title: "WSL Containers 사용법 - Docker Desktop 없이 Windows에서 컨테이너 실행"
slug: wsl-containers-without-docker-desktop
date: 2026-07-28
category: "Log"
subcategory: "개발 · 디지털"
status: ready
tags: [WSL Containers, WSL2, Docker Engine, Docker Desktop, Windows, Ubuntu, 컨테이너]
summary: "WSL 2의 Ubuntu에 Docker Engine을 직접 설치해 Docker Desktop 없이 Linux 컨테이너를 실행하는 순서와 권한·경로·네트워크 오류 진단법을 정리했습니다."
hero_image: assets/wsl-containers-hero.png
published_url: ""
sources:
    - https://learn.microsoft.com/en-us/windows/wsl/install
    - https://learn.microsoft.com/en-us/windows/wsl/systemd
    - https://learn.microsoft.com/en-us/windows/wsl/filesystems
    - https://learn.microsoft.com/en-us/windows/wsl/networking
    - https://docs.docker.com/engine/install/ubuntu/
    - https://docs.docker.com/engine/install/linux-postinstall/
    - https://docs.docker.com/engine/security/
    - https://docs.docker.com/desktop/features/wsl/
---

안녕하세요. dev.log입니다.

Windows에서 컨테이너 하나를 실행하려고 Docker Desktop까지 꼭 설치해야 하는지
궁금할 때가 있습니다. 결론부터 말하면 **Linux 컨테이너만 필요하고 터미널 관리가 괜찮다면, WSL 2의 Ubuntu 안에 Docker Engine을 직접 설치해 실행할 수 있습니다.**
다만 Windows 컨테이너, 그래픽 관리 화면(GUI), 자동 통합까지
사라지는 것은 감수해야 합니다.

이 글에서는 공식 설치 경로를 따라 WSL 2부터 Docker Compose까지 구성하고,
어디서 막혔는지 한 번에 가르는 진단 스크립트도 함께 살펴보겠습니다. 실제 WSL
장비에서 전 과정을 실행한 후기가 아니라, Microsoft·Docker 공식 문서와
Codex가 검증한 진단 로직을 바탕으로 한 재현 가이드입니다.

### 먼저 구분할 네 층

`WSL Containers`라는 별도 제품을 설치하는 것은 아닙니다.
WSL(Windows Subsystem for Linux)은 Windows 안에서 Linux 환경을 실행하는
기능입니다. 그중 WSL 2를 놓고, 그 안의 Ubuntu에 일반 Linux용 Docker
Engine을 설치하는 구성입니다.

| 층 | 맡는 역할 | 문제가 생겼을 때 확인할 것 |
|---|---|---|
| Windows | WSL을 실행하고 브라우저로 접속 | Windows 버전, 가상화, `wsl --version` |
| WSL 2·Ubuntu | Linux 커널과 사용자 공간 제공 | 배포판의 VERSION 2, systemd |
| Docker Engine | 이미지·컨테이너 수명주기 관리 | `docker.service`, daemon 연결 권한 |
| 컨테이너 | Nginx 같은 실제 앱 실행 | 이미지, 포트, 로그 |

실행 흐름은 다음처럼 이어집니다.

`Windows -> WSL 2 -> Ubuntu의 systemd -> Docker Engine -> Linux 컨테이너 -> Windows 브라우저의 localhost`

Docker Desktop을 빼도 WSL 2는 남습니다. Docker Desktop은 자체 WSL 배포판과
통합 기능을 제공하지만, 이 글의 방식은 사용자가 만든 Ubuntu 배포판 안에서
`dockerd`라는 Docker daemon을 직접 관리합니다. daemon은 명령을 받아 이미지와
컨테이너를 만들고 지우는 백그라운드 서비스입니다.

Docker Compose는 `compose.yaml` 한 파일에 여러 컨테이너의 이미지, 포트,
실행 조건을 적고 함께 관리하는 도구입니다. 뒤에서 단일 컨테이너를 먼저
확인한 다음 같은 웹 서버를 Compose로 바꿉니다.

### 직접 설치가 맞는 경우

두 방식은 같은 Linux 컨테이너 명령을 많이 공유하지만 관리 주체가 다릅니다.

| 필요 | Ubuntu에 Engine 직접 설치 | Docker Desktop |
|---|---|---|
| Linux 컨테이너와 Compose | 적합 | 적합 |
| 터미널 중심의 가벼운 구성 | 적합 | 가능 |
| GUI에서 상태·설정 관리 | 직접 명령으로 관리 | 적합 |
| Windows 컨테이너 | 이 글의 범위 아님 | 지원 환경에서 선택 가능 |
| 여러 WSL 배포판의 간편한 통합 | 각각 직접 구성 | 통합 설정 제공 |
| 업데이트·보안 정책 | 사용자가 Ubuntu 패키지 명령과 설정 관리 | Desktop 기능으로 관리 |

**개인 개발 장비에서 Linux 컨테이너 몇 개를 터미널로 다루는 경우가 직접 설치의 기본 대상입니다.**
Windows 컨테이너나 조직의 중앙 관리, GUI 기반
문제 해결이 필요하다면 Docker Desktop이 더 단순할 수 있습니다.

두 엔진을 한 Ubuntu 배포판에서 섞지는 않는 편이 좋습니다. Docker의
[WSL 문서](https://docs.docker.com/desktop/features/wsl/)도 Docker Desktop을
사용할 때 배포판에 직접 설치한 Docker Engine과 CLI를 먼저 제거하라고
안내합니다. 아래 단계는 Docker Desktop을 사용하지 않는 한 경로만 다룹니다.

### 1. WSL 2와 Ubuntu 준비

Microsoft의 [WSL 설치 문서](https://learn.microsoft.com/en-us/windows/wsl/install)에
따르면 아래 간편 설치 명령은 Windows 10 버전 2004, 빌드 19041 이상 또는
Windows 11에서 사용할 수 있습니다. 관리자 권한 PowerShell을 열고 먼저
현재 상태를 확인합니다.

```powershell
wsl --version
wsl --update
wsl --list --online
```

`wsl --version`이 인식되지 않으면 구형 inbox WSL일 수 있으므로 업데이트를
먼저 끝냅니다. 새 설치에서는 온라인 목록에 표시된 이름을 확인한 뒤, Docker가
공식 지원하는 Ubuntu LTS 배포판을 선택합니다. 이 글의 예시는 Ubuntu 24.04
LTS입니다.

```powershell
wsl --install -d Ubuntu-24.04
```

설치가 끝나면 Windows를 재시작하고 Ubuntu를 처음 열어 Linux 사용자 이름과
비밀번호를 만듭니다. PowerShell에서 배포판이 WSL 2로 잡혔는지도 확인합니다.

```powershell
wsl -l -v
```

목록의 `Ubuntu-24.04` 옆 VERSION이 `2`여야 합니다. 기존 배포판이 VERSION
1이라면 이름을 정확히 확인한 뒤 변환합니다.

```powershell
wsl --set-version Ubuntu-24.04 2
```

### 2. systemd 확인

Docker Engine은 daemon을 계속 실행해야 합니다. Ubuntu에서는 systemd라는
서비스 관리자가 `docker.service`를 시작하고 상태를 추적합니다. Ubuntu
터미널에서 PID 1, 즉 Linux 환경의 첫 프로세스를 확인합니다.

```bash
ps -p 1 -o comm=
```

현재 기본 Ubuntu는 systemd가 기본입니다. 결과가 `systemd`가 아니라면
Microsoft의 [WSL systemd 안내](https://learn.microsoft.com/en-us/windows/wsl/systemd)에
따라 `/etc/wsl.conf`를 설정합니다.

```bash
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
EOF
```

이 변경은 터미널만 닫아서는 적용되지 않습니다. PowerShell에서 모든 WSL
인스턴스를 종료한 뒤 Ubuntu를 다시 엽니다.

```powershell
wsl --shutdown
```

다시 `ps -p 1 -o comm=`를 실행해 `systemd`가 나오는지 확인합니다.

### 3. Docker Engine 설치

apt는 Ubuntu에서 프로그램 패키지를 설치하고 업데이트하는 관리자입니다.
Ubuntu 기본 저장소의 비슷한 패키지와 섞이지 않도록 Docker 공식 apt 저장소를
사용합니다. Docker는 빠른 설치 스크립트도 제공하지만 테스트·개발 환경에만
권장합니다. 업데이트 경로가 보이는 공식 저장소 방식을 택하겠습니다.

```bash
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

sudo tee /etc/apt/sources.list.d/docker.sources >/dev/null <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

마지막 명령은 Docker Engine과 CLI뿐 아니라 이미지를 빌드하는 Buildx,
여러 컨테이너 구성을 실행하는 Compose 플러그인까지 설치합니다. 공식
[Ubuntu 설치 문서](https://docs.docker.com/engine/install/ubuntu/)의 지원
버전과 명령은 바뀔 수 있으므로 실제 설치 시점에도 원문을 함께 확인하는 편이
좋습니다.

이전에 `docker.io`, `docker-compose`, `containerd`, `runc` 같은 패키지를
따로 설치했다면 공식 문서의 충돌 패키지 제거 단계를 먼저 적용해야 합니다.
새 Ubuntu 배포판이라면 대개 해당하지 않습니다.

### 4. 서비스와 사용자 권한 확인

패키지가 설치된 것과 daemon이 작동하는 것은 다른 문제입니다. Docker CLI는
`/var/run/docker.sock`이라는 로컬 통신 파일을 통해 daemon에 명령을
보냅니다. 먼저 systemd가 관리하는 서비스 상태와 첫 컨테이너를 `sudo`로
확인합니다.

```bash
sudo systemctl status docker --no-pager
sudo docker run --rm hello-world
```

서비스가 멈춰 있다면 시작합니다.

```bash
sudo systemctl start docker
```

매번 `sudo`를 쓰지 않으려면 현재 사용자를 `docker` 그룹에 추가할 수 있습니다.

```bash
sudo usermod -aG docker "$USER"
newgrp docker
docker version
docker compose version
```

여기서 편의만 보면 안 됩니다. Docker의
[Linux 설치 후 문서](https://docs.docker.com/engine/install/linux-postinstall/)는
`docker` 그룹이 사용자에게 root 수준 권한을 준다고 경고합니다. 개인 개발
장비의 신뢰하는 계정에만 적용하고, 여러 사용자가 함께 쓰는 장비라면 관리자
정책이나 Rootless mode를 별도로 검토해야 합니다.

### 5. 첫 웹 컨테이너 실행

프로젝트는 Windows의 `C:\`가 WSL에서 보이는 `/mnt/c`보다 Ubuntu 홈 아래에
두는 편이 좋습니다. Microsoft도 Linux 명령으로 작업할 파일은 WSL
파일시스템에 저장하도록 권장합니다.

```bash
mkdir -p ~/projects/wsl-container-demo
cd ~/projects/wsl-container-demo
```

이제 Nginx 이미지를 내려받아 백그라운드로 실행합니다. `127.0.0.1`을 붙여
로컬 장비의 8080번 포트에만 게시합니다.

```bash
docker run -d --name wsl-web \
  -p 127.0.0.1:8080:80 \
  nginx:alpine

docker ps
curl http://localhost:8080
```

`docker ps`에 `wsl-web`이 보이고 `curl`이 HTML을 돌려주면 컨테이너와 포트
게시까지 연결된 상태입니다. Microsoft의
[WSL 네트워킹 문서](https://learn.microsoft.com/en-us/windows/wsl/networking)에
따르면 WSL 안의 웹 앱은 일반적인 로컬 구성에서 Windows 브라우저의
`http://localhost:8080`으로 열 수 있습니다.

테스트를 끝내면 컨테이너를 지웁니다.

```bash
docker rm -f wsl-web
```

### 6. Compose로 같은 구성 관리

한 줄 명령이 길어지면 `compose.yaml`에 실행 조건을 보존하는 편이 낫습니다.
다음 파일을 `~/projects/wsl-container-demo/compose.yaml`로 저장합니다.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
    restart: unless-stopped
```

Compose 플러그인은 `docker-compose`가 아니라 띄어 쓴 `docker compose`로
실행합니다.

```bash
docker compose up -d
docker compose ps
docker compose logs --tail=20
docker compose down
```

PowerShell에서 Ubuntu 셸을 열지 않고 상태만 보고 싶다면 WSL을 통해 명령을
전달할 수도 있습니다.

```powershell
wsl -d Ubuntu-24.04 -- docker ps
```

직접 설치한 Engine은 Ubuntu 안에 있으므로 PowerShell의 독립된 `docker.exe`가
자동으로 생기는 구성은 아닙니다. Ubuntu 터미널을 기본 작업 공간으로 쓰거나
`wsl ...` 앞부분을 붙이는 이유입니다.

### 7. 실패 지점을 가르는 진단

설치 오류를 한꺼번에 `Docker가 안 된다`고 보면 원인을 찾기 어렵습니다.
다음은 WSL, systemd, CLI, 서비스, daemon socket, Compose, 작업 경로를
순서대로 나누는 본문용 핵심 버전입니다.

```bash
#!/usr/bin/env bash
set -u

failed=0
check() {
  label="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    printf '[PASS] %s\n' "$label"
  else
    printf '[FAIL] %s\n' "$label"
    failed=$((failed + 1))
  fi
}

check "WSL 환경" grep -qi microsoft /proc/version
check "PID 1이 systemd" sh -c '[ "$(ps -p 1 -o comm= | tr -d " ")" = systemd ]'
check "Docker CLI 설치" sh -c 'command -v docker'
check "docker.service 실행" systemctl is-active --quiet docker
check "현재 사용자의 daemon 접근" docker info
check "Compose 플러그인" docker compose version

case "$PWD" in
  /mnt/*) printf '[WARN] 프로젝트를 ~/projects 아래로 옮기는 편이 좋습니다.\n' ;;
  *) printf '[PASS] Linux 파일시스템의 작업 경로\n' ;;
esac

exit "$failed"
```

Codex는 오류 문구를 더 세분한 보존용 스크립트에 정상 상태, `/mnt/c` 경로,
socket 권한 거부, systemd·서비스 중지, Docker CLI 누락을 각각 주입했습니다.
종료 코드와 핵심 문구가 5개 시나리오 모두 기대값과 일치했습니다. 이는
**진단 분기가 맞는지 확인한 결과이지, WSL 실기기에서 설치 성공률이나 성능을 측정한 결과는 아닙니다.**

오류별로 다음 지점부터 확인하면 됩니다.

- `Cannot connect to the Docker daemon`: `systemctl status docker`로 systemd와 서비스 시작 여부를 확인합니다.
- `permission denied`와 `docker.sock`: `id`와 `ls -l /var/run/docker.sock`을 확인하고, 그룹 추가 뒤 새 셸을 열어 권한 의미를 다시 살핍니다.
- `docker: command not found`: `apt-cache policy docker-ce`로 공식 저장소와 패키지 설치 단계를 확인합니다.
- 브라우저에서 8080 접속 실패: `docker ps`와 `curl localhost:8080`으로 컨테이너, 포트, Windows 방화벽을 순서대로 나눕니다.
- 빌드와 bind mount가 유난히 느림: `pwd`를 확인하고 `/mnt/c` 대신 `~/projects`로 옮깁니다.
- PowerShell에서 `docker`를 못 찾음: `wsl docker version`으로 Ubuntu 안의 Engine이라는 실행 위치를 확인합니다.

### 보안과 운영의 경계

Docker Engine을 직접 설치하면 관리 책임도 Ubuntu 안으로 들어옵니다. 최소한
다음 경계는 지키는 편이 좋습니다.

- `sudo apt update`와 `sudo apt upgrade`로 Engine 업데이트를 직접 관리합니다.
- 신뢰하는 이미지를 고르고, 필요하지 않은 `--privileged`와 호스트 루트 bind
  mount를 피합니다.
- Docker daemon의 TCP 포트를 인증 없이 열지 않습니다. 기본 Unix socket을
  그대로 쓰는 편이 안전합니다.
- `-p 8080:80`처럼 주소를 생략하면 의도보다 넓게 게시될 수 있습니다. 로컬
  테스트는 `127.0.0.1:8080:80`처럼 범위를 적습니다.
- Docker 공식 문서상 게시 포트는 `ufw` 규칙을 우회할 수 있으므로, LAN이나
  외부 공개는 로컬 테스트와 별도의 방화벽 설계로 다룹니다.
- 이미지와 volume은 Ubuntu 배포판의 가상 디스크 공간을 사용합니다.
  `docker system df`로 사용량을 보고, 확인 없이 전체 정리 명령을 실행하지
  않습니다.

컨테이너가 가볍다는 말도 완전한 보안 경계를 뜻하지 않습니다. Docker
[Engine 보안 문서](https://docs.docker.com/engine/security/)처럼 daemon은
기본적으로 root 권한을 사용하며, 이를 제어하는 사용자는 호스트 파일까지
영향을 줄 수 있습니다.

Docker Desktop 없이 시작할 기본 경로는 분명합니다.
**WSL 2와 systemd를 먼저 확인하고, Ubuntu에 공식 Docker Engine을 설치한 뒤 `hello-world -> Nginx -> Compose` 순서로 범위를 한 단계씩 넓혀 보세요.**
오류가 나면 재설치부터 하지
말고 WSL, 서비스, socket, 경로 중 어느 층에서 멈췄는지 먼저 가르는 것이
가장 빠른 다음 행동입니다.
