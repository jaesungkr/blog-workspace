# manycode 직접 검증 로그

## 실행 기준

- 실행일: 2026-07-28 (Asia/Seoul)
- 실행 주체: Codex
- 저장소: `https://github.com/unworld11/manycode`
- commit: `3c43052df63c461af6340528f41fd7a1ebbe0b14`
- package version: `0.6.0`
- OS: macOS 26.5.2 (25F84), arm64
- Node.js: `v26.0.0`
- npm: `11.12.1`

## 설치 1차 실패

명령:

```bash
npm install
```

대표 출력:

```text
npm error code EPERM
npm error syscall open
npm error path /Users/ja2sng/.npm/_cacache/tmp/***
npm error Your cache folder contains root-owned files
```

판단: 현재 사용자 전역 npm 캐시의 소유권 문제입니다. 제품 저장소의 의존성
해결 실패와 구분하기 위해 프로젝트 전용 임시 캐시로 재시도했습니다.

## 임시 캐시 설치 성공

명령:

```bash
npm install --cache /private/tmp/manycode-npm-cache-20260728
node bin/manycode.js version
```

출력:

```text
added 5 packages, and audited 6 packages in 3s
found 0 vulnerabilities
manycode 0.6.0 (3c43052)
```

## 공식 테스트 1·2차

두 번 모두 같은 결과였습니다.

```text
PASS direct: join, replay, remote typing, resize, bad-code reject
PASS relay: hosted code, join through relay, replay, remote typing
PASS backpressure: stalled joiner dropped instead of buffering unbounded
PASS normalized --code matches joiner
PASS --port abc rejected clearly
PASS --code AB rejected clearly
PASS missing agent explained
PASS version prints a number
PASS stop with no sessions is clean
FAIL stop <code> ends the host: manycode: no active session with code STOPME
PASS browser join page served
PASS approve: allowed joiner held then admitted
PASS approve: denied joiner told so
PASS chat: B hears A with stamped name
PASS chat: A is not echoed her own message
PASS chat: late joiner gets the log
PASS secrets: masked by default
PASS secrets: raw with --share-secrets
PASS record: asciinema cast written
```

exit code: `1`

원인 추적: 실패한 항목은 호스트가 `~/.manycode/sessions`에 기록한 상태를 다른
프로세스가 읽어 종료합니다. 실행 전 `~/.manycode`는 존재하지 않았고, 현재
샌드박스는 새 경로 쓰기를 차단했습니다. 나머지 네트워크·PTY 테스트는 상태
목록을 쓰지 않아 통과했습니다.

## 상태 경로 허용 뒤 최종 테스트

명령:

```bash
npm test
```

출력:

```text
PASS direct: join, replay, remote typing, resize, bad-code reject
PASS relay: hosted code, join through relay, replay, remote typing
PASS backpressure: stalled joiner dropped instead of buffering unbounded
PASS normalized --code matches joiner
PASS --port abc rejected clearly
PASS --code AB rejected clearly
PASS missing agent explained
PASS version prints a number
PASS stop with no sessions is clean
PASS stop <code> ends the host
PASS browser join page served
PASS approve: allowed joiner held then admitted
PASS approve: denied joiner told so
PASS chat: B hears A with stamped name
PASS chat: A is not echoed her own message
PASS chat: late joiner gets the log
PASS secrets: masked by default
PASS secrets: raw with --share-secrets
PASS record: asciinema cast written
```

exit code: `0`

합계: `19 PASS / 0 FAIL`

## 테스트 상태 정리

테스트가 만든 `~/.manycode`에는 세션 JSON과 `update.json`만 있었습니다. 사용자
홈에 설정을 남기지 않기 위해 전체 디렉터리를 다음 임시 경로로 옮겼습니다.

`/private/tmp/manycode-test-state-20260728`

## 해석 제한

- 테스트용 bash를 공유했으며 실제 Claude Code 모델 응답은 평가하지 않았습니다.
- 실제 지인을 Cloudflare 터널로 초대하지 않았습니다.
- 장시간 연결, 다섯 명 동시 입력, 악의적 참가자, Windows·Linux UX는
  시험하지 않았습니다.
