# manycode 소스 확인 메모

확인일: 2026-07-28

## 저장소와 릴리스

- 공식 저장소: `unworld11/manycode`
- 확인 커밋: `3c43052df63c461af6340528f41fd7a1ebbe0b14`
- `package.json` 버전: `0.6.0`
- GitHub latest release: `v0.6.0`
- 릴리스 공개 시각: `2026-07-16T16:56:47Z`
- 라이선스: MIT
- API 확인 시점의 stars·forks처럼 자주 바뀌는 숫자는 본문에서 사용하지 않음

## 이름 변경

- README: 2026년 7월까지 ccshare였으며 현재 manycode라는 설명
- CHANGELOG 0.4.0: 이름 변경, 기존 `ccshare` 명령과 `CCSHARE_*` 환경 변수 호환
- `package.json`: `manycode`와 `ccshare` bin이 모두 `bin/manycode.js`를 가리킴

## 핵심 동작

- `lib/session.js`: `node-pty`로 명령을 실행하고 참가자 입력을 같은 PTY에 씀
- `lib/session.js`: 읽기 전용이면 입력을 무시함
- `lib/session.js`: 스크롤백은 최근 256KB로 제한함
- `lib/host.js`: 일반 HTTP GET에 브라우저용 xterm.js 페이지를 제공함
- `lib/codes.js`: 코드를 대문자로 정규화하고 SHA-256 해시 앞 16자를 탐색에 사용함
- `lib/discovery.js`: LAN 탐색 패킷에는 코드 원문이 아니라 위 해시를 담음

## 보안 경계

- README: 코드가 유일한 인증이며 기본 참가자는 실제 셸에 입력 가능
- `--read-only`: 참가자 입력 차단
- `--approve`: macOS 직접·LAN·터널 참가자를 승인 전 대기시킴
- relay: 참가자 입력 프레임 귀속 한계 때문에 승인이 best-effort
- `.env` 보호: 파일 값과 일치하는 바이트를 마스킹. 다른 인코딩·변형 값은
  보호하지 못한다고 README가 명시함
- direct/LAN은 plain `ws://`, self-hosted relay는 `wss://` 권장

## 제작자 설명

Product Hunt의 제작자 답변:

- 같은 작업 상태를 공유하며 병렬 세션은 향후 가능성으로 언급함
- 동시 입력 잠금이나 턴제는 없고 공유 키보드에 가깝다고 설명함
- 참가자는 처음부터 입력할 수 있다고 답함

제작자 답변은 제품 방향과 UX 설명에만 쓰고, 보안 보증으로 확대하지 않습니다.
