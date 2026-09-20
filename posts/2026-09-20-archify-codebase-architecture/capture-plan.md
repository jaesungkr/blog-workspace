# 조건부 캡처 계획

`workflow-v2.json`에서 `direct_capture` 또는 `gif`가 참일 때만 이 파일을 사용합니다.

## 독자 행동과 증거

| ID | 시작 상태 | 행동 | 기대 결과 | 필요한 캡처 |
|---|---|---|---|---|
| T01 | Archify main 커밋을 얕게 복제하고 Node.js를 사용할 수 있는 상태 | 한국어 7노드 Architecture JSON을 `deliver`한 뒤 `visual-check` 실행 | 단일 HTML과 라이트·다크 브라우저 증거가 생성되고 오버플로·가독성 검사가 통과 | 2048×1320 다크 결과 화면 1장 |
| T02 | 연결 대상이 존재하지 않는 1노드 JSON | `validate --quality showcase --json` 실행 | 비정상 연결을 거부하고 구조화된 오류와 비정상 종료 코드를 반환 | 캡처하지 않고 원문 JSON과 실행 기록을 보존 |

## 실행 경계

- 실행자: Codex
- 제품·앱 버전: Archify main `72c750bb070d95171dbb2244e5b62b1b7da69c12`, 패키지 표기 `2.17.0-dev.1`
- 운영체제·브라우저: macOS, Node.js v26.0.0, Google Chrome 자동 브라우저 검사
- 실행 날짜: 2026-09-20 17:25 KST
- 직접 확인하지 못한 범위: `npx skills add`로 각 에이전트에 설치하는 전체 과정, 모델별 저장소 해석 정확도, 대형 모노레포 성능, Architecture Delta, PNG·SVG·WebM 내보내기 조작

## 개인정보 준비

- 테스트 계정 또는 공개 데이터만 사용합니다.
- 비밀번호·토큰·QR·이메일·개인 경로가 보이면 저장하지 않고 상태를 정리한 뒤 다시 캡처합니다.
- 원본은 `artifacts/captures/` 또는 `artifacts/recordings/`에 둡니다.

## 실패와 재캡처

| 문제 | 처리 | 최종 결과 |
|---|---|---|
| 존재하지 않는 `missing-node`를 연결 대상으로 지정 | 실패를 의도한 반례로 유지 | 종료 코드 1과 `layout/constraint` 진단을 확인 |
| 1440×900 캡처는 게시용 축소에서 제목 여백이 빠듯해 보임 | 더 넓은 2048×1320 다크 캡처를 대표 이미지로 선택 | 제목, Viewer 조작부, 7개 노드, 카드 3개가 모두 읽힘 |
