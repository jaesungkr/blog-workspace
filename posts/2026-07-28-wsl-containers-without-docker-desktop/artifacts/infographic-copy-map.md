# WSL 컨테이너 네 층 인포그래픽 문구 지도

## 독자 질문

Docker Desktop을 설치하지 않을 때 Docker Engine과 Linux 컨테이너는 정확히
어디에서 실행되고, Windows 브라우저는 어떤 경로로 접속하는가?

## 문구와 근거

| 인포그래픽 문구 | 본문·근거 |
|---|---|
| `WSL 컨테이너의 네 층` | 본문 `먼저 구분할 네 층` |
| `Docker Desktop 없이 Engine은 Ubuntu 안에서 직접 실행됩니다` | 본문 도입부·`먼저 구분할 네 층`, evidence C09·C10 |
| `1 · WINDOWS` | 본문 실행 흐름의 Windows 호스트 |
| `브라우저 · Windows 접속` | 본문 `첫 웹 컨테이너 실행`, evidence C08 |
| `2 · WSL 2 · Linux 커널` | 본문 네 층 표·실행 흐름, evidence C02 |
| `3 · UBUNTU 24.04 · systemd가 서비스 관리` | 본문 1·2절, evidence C03 |
| `4 · Docker Engine · dockerd · 이미지 · 수명주기` | 본문 네 층 설명, evidence C04·C05 |
| `Linux 컨테이너` | 본문 전체 범위, evidence C10 |
| `localhost:8080` | 본문 Nginx 예시, evidence C08 |
| `8080 → 80` | 본문 `-p 127.0.0.1:8080:80` 명령의 포트 매핑 |
| `Ubuntu 셸 · docker ps` | 본문 Compose 절의 기본 실행 위치 |
| `PowerShell · wsl docker ps` | 본문 PowerShell 호출 예시와 Microsoft WSL interop |
| `Linux 컨테이너 · Windows 컨테이너와 GUI는 별도` | 본문 도입부·선택 표, evidence C10 |

## 시각 문법

- 중첩된 경계는 `Windows -> WSL 2 -> Ubuntu -> Docker Engine`의 설치
  위치를 뜻합니다.
- 주황 요청선은 Windows 브라우저에서 컨테이너 80번 포트로 가는 경로,
  초록 응답선은 같은 연결을 따라 돌아오는 경로를 뜻합니다.
- 컨테이너의 세로 골은 실제 화물 컨테이너를 빌린 구조 은유이며
  Docker 로고나 특정 제품 UI를 복제하지 않습니다.
- 하단 두 명령은 서로 다른 Engine이 아니라 같은 Ubuntu Engine에 명령을
  보내는 두 호출 위치입니다.

## 배치

- 유형: `원리`
- 권장 위치: `먼저 구분할 네 층` 절의 실행 사슬 바로 뒤
- 한국어 alt: Windows 안의 WSL 2와 Ubuntu, Docker Engine, Linux 컨테이너가
  중첩되고 localhost 8080으로 브라우저에 연결되는 구조
