# 기획: 시리 대신 클로드로 아이폰 쓰기

## 분류와 독자

- 상위 카테고리: `Log`
- 하위 카테고리: `AI 개념 · 실전`
- 한 명의 독자: phone-harness가 어떻게 Claude로 아이폰을 조작한다는 것인지 빠르게 이해하고 직접 설치해 보고 싶은 사람
- 검색 의도: 작동 원리, 준비물, 실제 설치 명령, 첫 안전 테스트를 한 글에서 확인

## 글의 중심

- 독자가 기억할 한 문장: phone-harness는 Mac의 Claude Code가 아이폰 미러링 화면을 캡처·OCR하고 탭과 입력을 보내게 만드는 도구입니다.
- 낯선 주제를 붙잡아 줄 장면: Claude에게 “날씨 앱을 열고 내일 비가 오는지 확인해 줘”라고 요청하는 상황
- 답하지 않는 범위: Claude iOS 앱의 일반 사용법, Ask Claude, 시스템 기본 비서 설정, 탈옥, 실제 기기 장기 사용기
- 정직한 한계: Python 패키지 설치는 검증했지만 실제 아이폰 연결·터치·OCR 정확도는 시험하지 않았습니다.

## dev.log만의 근거

- first-party contribution: exact commit `4d2de7a`의 문서·핵심 코드를 감사하고, 상류 AppKit 패키지 결함을 찾아 Python 3.12 venv에서 Cocoa 기반 설치·import를 검증
- 실행 주체: `Codex`
- 보존 원자료: `artifacts/sources/phone-harness/`, `artifacts/sources/web/`
- 표현 원칙: 독자의 첫 질문에 바로 답한 뒤 원리, 준비, 설치, doctor, 첫 테스트, 보안 순서로 진행

## 설명 순서

| 순서 | 독자가 알고 싶은 것 | 답변 |
|---|---|---|
| 1 | Claude가 어떻게 아이폰을 조작하나 | 미러링 창 캡처 → Vision OCR → 좌표 입력 → 재확인 |
| 2 | 무엇이 필요한가 | Mac, iPhone Mirroring, Claude Code, Python, macOS 권한 |
| 3 | 어떻게 설치하나 | 상류 AppKit 오류를 피한 Python 3.12 venv 명령 |
| 4 | 연결됐는지 어떻게 아나 | `--doctor`와 읽기 전용 OCR 테스트 |
| 5 | 무엇을 조심해야 하나 | 외부 영향 작업 승인과 화면 정보의 모델 처리 경계 |

## 시각 자료

- 생성 이미지: 없음
- 스크린샷 1 `phone-harness-github-overview`: 어떤 저장소이며 iPhone Mirroring 기반 도구인지 확인
- 스크린샷 2 `phone-harness-install-doctor`: doctor의 검사 순서와 대표 실패 원인 확인
- 제외: Claude iOS 진입점·앱 연동 화면. 새 원고의 중심인 phone-harness 설치와 직접 관련이 없어 사용하지 않습니다.

## 제목

- 사용자 지정 제목 유지: `시리 대신 클로드로 아이폰 쓰기`
