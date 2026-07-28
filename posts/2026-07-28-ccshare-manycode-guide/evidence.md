# 근거 지도: ccshare 사용법 - manycode로 바뀐 멀티플레이 Claude Code

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 실제 근거의 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | ccshare는 2026년 7월 manycode로 이름을 바꿨고 `ccshare` 명령은 별칭으로 남음 | 공식 + Codex 확인 | 확인 | 공식 README·CHANGELOG 0.4.0, `package.json`의 두 bin이 같은 파일을 가리킴 | 이전 버전의 모든 마이그레이션 경로는 실행하지 않음 |
| C02 | 호스트는 에이전트를 실제 PTY에서 실행하고 참가자는 같은 화면을 보며 기본값에서 입력도 가능함 | 공식 + Codex 실행 | 확인 | 공식 README·사이트, 테스트 `direct`의 원격 입력과 출력 회수 통과 | 실제 Claude Code 대신 테스트용 bash를 실행함 |
| C03 | Claude Code 외 Codex·OpenCode·Kimi 등 터미널 프로그램도 명령으로 지정할 수 있음 | 공식 + 소스 확인 | 확인 | 공식 README, CLI가 `host` 뒤 명령과 인수를 PTY에 전달 | 각 에이전트를 모두 실행하지 않음 |
| C04 | 같은 Wi-Fi에서는 코드 해시가 담긴 UDP 탐색을 쓰며 코드 원문은 방송하지 않음 | 공식 + 소스 확인 | 확인 | 공식 사이트·README, `lib/codes.js` SHA-256 앞 16자리와 `lib/discovery.js` | 네트워크 패킷을 별도 캡처하지 않음 |
| C05 | 외부 연결용 Cloudflare Quick Tunnel이 기본으로 열리고 `--no-tunnel`로 끌 수 있음 | 공식 + 소스 확인 | 확인 | 공식 사이트·README, CLI 플래그와 host 기본값 | 실제 터널 연결과 지연은 측정하지 않음 |
| C06 | 기본 참가자는 쓰기 가능하고 `--read-only`가 입력을 차단함 | 공식 + 소스 확인 | 확인 | 공식 README, `lib/session.js`의 입력 차단 조건 | 공식 테스트는 별도 read-only 입력 거부 항목을 이름 붙여 출력하지 않음 |
| C07 | macOS의 `--approve`는 참가자를 승인 전 대기시키며 직접·LAN·터널에서 강제됨 | 공식 + Codex 실행 | 확인 | 공식 README, 승인·거절 테스트 2개 통과 | self-hosted relay에서는 best-effort이며 macOS 외 플랫폼은 자동 승인으로 돌아감 |
| C08 | 뒤늦게 들어온 참가자는 최근 256KB 스크롤백을 받음 | 공식 + 소스 확인 | 확인 | 공식 README, `lib/session.js`의 256KB 버퍼, direct replay 테스트 | 실제 민감 정보 노출량은 세션 출력에 따라 달라짐 |
| C09 | `.env` 값은 기본 마스킹되지만 정확한 바이트 일치 방식이라 변형된 값은 샐 수 있음 | 공식 + Codex 실행 | 확인 | 공식 README 보안 절, masked/raw 테스트 모두 통과, `lib/secrets.js` | 모든 비밀 파일·인코딩·파생값을 가리는 DLP가 아님 |
| C10 | 소스는 MIT이며 확인한 버전은 v0.6.0, 커밋은 `3c43052` | 공식 + Codex 확인 | 확인 | GitHub API, release v0.6.0, 로컬 `git rev-parse`, package version | master 직접 설치는 태그 뒤 변경을 포함할 수 있음 |
| C11 | 공식 테스트 19개가 격리된 로컬 환경에서 최종 모두 통과함 | Codex 실행 | 확인 | `artifacts/test-log.md`, 최종 `npm test` exit 0 | 실제 다인 원격 세션·장시간 안정성·체감 UX는 평가하지 않음 |
| C12 | 제작자는 동시 입력에 잠금이나 턴제가 없고 공유 키보드에 가깝다고 설명함 | 제작자 답변 | 확인 | Product Hunt 제작자 댓글 | 현 버전 구현이 바뀔 수 있으며 동시 입력 부하 테스트는 하지 않음 |

## 직접 검증 설계

- 질문: manycode 0.6.0의 핵심 공유·보호 기능이 공식 저장소의 재현 가능한
  테스트에서 실제로 작동하는가?
- 실행 주체: Codex
- 환경과 확인 시점: 2026-07-28, macOS 26.5.2, Apple Silicon arm64,
  Node.js 26.0.0, npm 11.12.1
- 입력: `unworld11/manycode`의 2026-07-28 HEAD
  `3c43052df63c461af6340528f41fd7a1ebbe0b14`, 공식 `npm test`
- 전처리 또는 표현: GitHub 저장소를 depth 1로 복제하고 공식 수동 설치법의
  `npm install`을 실행함. 전역 npm 캐시 오류를 피하기 위해 재시도에서
  `/private/tmp/manycode-npm-cache-20260728`을 사용함
- 비교·판정 규칙: 각 항목이 `PASS`를 출력하고 전체 프로세스가 exit 0이면
  통과. 같은 실패가 반복되면 코드 경로와 환경 권한을 분리해 재검증함
- 성공 기준: direct·relay·backpressure 3개 smoke와 edge 16개, 합계 19개
  모두 통과
- 반복 횟수와 표본 크기: 초기 2회는 동일 1개 실패, 환경 권한을 연 최종 1회는
  19/19 통과
- 보존할 원자료: `artifacts/test-log.md`, `artifacts/source-notes.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 기본 npm 캐시로 설치 | 사용자 전역 npm 캐시 권한 오류로 실패 | `artifacts/test-log.md` | 제품 설치 결함이 아니라 이 실행 환경의 캐시 권한 문제 |
| E02 | 임시 npm 캐시로 설치 후 공식 테스트 | 18 PASS, `stop <code>` 1 FAIL, 2회 동일 | `artifacts/test-log.md` | 샌드박스가 `~/.manycode` 상태 파일 작성을 막은 조건 |
| E03 | `~/.manycode` 테스트 상태 경로 쓰기 허용 후 같은 테스트 | 19/19 PASS, exit 0 | `artifacts/test-log.md` | macOS 로컬의 공식 자동 테스트 범위 |
| E04 | source·README·CHANGELOG 대조 | v0.6.0, 이름 변경, 두 명령 별칭, 보안 경계 확인 | `artifacts/source-notes.md` | 문서와 해당 커밋의 일치 여부 |

## 실패와 반례

- 실패한 입력: 기본 npm 캐시를 쓴 `npm install`은 기존 캐시 소유권 문제로
  `EPERM`이 발생함. 임시 캐시로 설치는 성공함
- 예상과 달랐던 결과: 처음 두 테스트에서 `stop <code>`가 실행 중 호스트를
  찾지 못함. 해당 항목은 `~/.manycode/sessions` 상태 파일에 의존했고 현재
  샌드박스는 그 경로를 차단했음. 정확한 경로 쓰기를 허용한 뒤 통과함
- 정리: 테스트가 만든 `~/.manycode`는 원래 존재하지 않았음을 먼저 확인했고,
  실행 뒤 `/private/tmp/manycode-test-state-20260728`로 옮겨 사용자 홈에 남기지 않음
- 일반화하면 안 되는 범위: 19개 통과는 공식 테스트 시나리오의 동작 확인입니다.
  실제 외부 터널의 보안 감사, 악의적 참가자 방어, 다섯 명의 동시 타이핑 품질,
  기업용 접근 통제 적합성을 뜻하지 않음

## 미해결 항목

- 없음. 실사용 UX와 장시간 원격 안정성은 미해결 주장이 아니라 이 글이 평가하지
  않는 범위로 본문에 명시함

## 출처 메모

- 공식 사이트: https://manycode.vercel.app/
  - 현재 명령, PTY 흐름, LAN·터널·브라우저 참가, 보안 설명의 1차 출처
- 공식 저장소: https://github.com/unworld11/manycode
  - README, source, test, package metadata 확인
- 공식 릴리스: https://github.com/unworld11/manycode/releases/tag/v0.6.0
  - v0.6.0 이름과 공개 시점 확인
- Product Hunt: https://www.producthunt.com/products/ccshare
  - ccshare 이름으로 출시한 배경과 제작자의 동시 입력·초기 제품 범위 답변

긴 원문은 복사하지 않고, 본문 주장 옆에 필요한 링크와 한계를 함께 둡니다.
