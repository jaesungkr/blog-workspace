# Archify 직접 실행 기록

## 환경

- 실행자: Codex
- 실행 시각: 2026-09-20T17:25:58+09:00
- 운영체제: macOS
- Node.js: v26.0.0
- npm: 11.12.1
- 브라우저 검사: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- Archify commit: `72c750bb070d95171dbb2244e5b62b1b7da69c12`
- 패키지 표기: `2.17.0-dev.1`

## 정상 입력

입력 파일은 `archify-pipeline.architecture.json`입니다. 다음 명령을 순서대로 실행했습니다.

```bash
node bin/archify.mjs doctor
node bin/archify.mjs validate architecture archify-pipeline.architecture.json --quality showcase --json
node bin/archify.mjs deliver architecture archify-pipeline.architecture.json archify-pipeline.html --quality showcase --json
node bin/archify.mjs visual-check archify-pipeline.html --json
```

`validate`는 9개 검사 모두 통과했고 composition 결과는 오류 0개, 경고 0개였습니다.

- specification SHA-256: `d043a338385b0cd11b4415e37d77f373b0fb4298e4d20fdb7ba17362080d00b2`
- specification bytes: `3370`
- artifact SHA-256: `433912ea1a84599447b45ba543f37a57e952ea988e7659a9adb701ca0761f171`
- artifact bytes: `806884`
- checks passed: `9/9`
- browser viewports: `1440×900`, `1600×1000`, `1920×1080`, `2048×1320`
- containment: `pass`
- readability: `pass`
- viewer chrome: `pass`
- visual review: `pending`

## 실패 입력

`archify-invalid.architecture.json`은 `source`에서 존재하지 않는 `missing-node`로 연결합니다.

```text
exit: 1
stage: render
code: layout/constraint
message: Connection "존재하지 않는 대상" references unknown target "missing-node".
```

검증은 `ok: false`와 종료 코드 1로 끝났습니다. 이 반례는 연결 대상 검증만 확인하며, 저장소 내용의 의미적 완전성을 시험하지 않습니다.
