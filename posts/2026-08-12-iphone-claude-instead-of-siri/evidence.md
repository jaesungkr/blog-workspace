# 근거 지도: 시리 대신 클로드로 아이폰 쓰기

## 주장별 상태

| ID | 본문 주장 | 유형 | 상태 | 근거 | 한계 |
|---|---|---|---|---|---|
| C01 | phone-harness는 iPhone Mirroring 창을 캡처하고 Vision OCR과 좌표 입력으로 아이폰을 조작한다. | 프로젝트 문서·코드 감사 | 확인 | README, `helpers.py`, `mirror.py`, `ocr.py`, commit `4d2de7a` | 실제 기기 성공률은 검증하지 않음 |
| C02 | 앱 열기, 탭, 스크롤, 입력, 재캡처 검증이 가능하다. | 프로젝트 문서·코드 감사 | 확인 | README, SKILL.md | 글자 없는 아이콘과 중복 문구는 오작동 가능 |
| C03 | 카메라·마이크·Face ID·멀티터치·DRM 영상에는 제한이 있다. | Apple 공식 + 프로젝트 문서 | 확인 | Apple iPhone Mirroring, README Limits | 업데이트에 따라 범위가 바뀔 수 있음 |
| C04 | iPhone Mirroring은 호환 Mac, macOS 15+, iOS 18+, 같은 Apple 계정, 2단계 인증, Wi-Fi·Bluetooth를 요구한다. | Apple 공식 | 확인 | Apple Support 120421 | EU 지역 제한 등 추가 조건 존재 |
| C05 | Claude Code는 공식 설치와 지원 계정 로그인이 필요하다. | Anthropic 공식 | 확인 | getting started, authentication | Free 계정만으로는 Claude Code 접근 불가 |
| C06 | 상류 문서의 `pyobjc-framework-AppKit`는 PyPI에 없어 그대로 설치하면 실패한다. | Codex 설치 검증 | 확인 | Python 3.12 pip 실패 기록 | 2026-08-12 PyPI 상태 기준 |
| C07 | Cocoa를 포함한 네 PyObjC 패키지를 먼저 설치하면 editable 설치·import·CLI help가 통과한다. | Codex 설치 검증 | 확인 | `install-validation.md` | 미러링·권한·OCR·터치는 실행하지 않음 |
| C08 | `--doctor`는 PyObjC, 접근성, 화면 기록, 앱, 창, 캡처, OCR 순서로 검사한다. | 코드·문서 감사 | 확인 | `admin.py`, `install.md` | 알려진 조건만 검사 |
| C09 | 기본 백그라운드 입력은 비공개 SkyLight API를 사용하고 실패 시 전면 방식으로 폴백한다. | 코드 감사 | 확인 | `helpers.py`, `background.py` | macOS 버전별 안정성 미측정 |
| C10 | 캡처·OCR은 Mac에서 실행되지만 Claude Code에 제공한 출력은 모델 요청 문맥으로 전송될 수 있다. | 코드 + 공식 데이터 흐름의 보수적 해석 | 확인 | `mirror.py`, `ocr.py`, Claude Code data usage | phone-harness의 별도 전송 명세는 없음 |

## 직접 검증

- 저장소: `ShawnPana/phone-harness`
- 감사 커밋: `4d2de7a4b8780a386545c986543c83dda66764dd`
- 환경: macOS, Python 3.12 새 venv
- 성공: PyObjC 12.2.2 설치, phone-harness 0.1.0 editable 설치, Quartz·Vision·AppKit·ApplicationServices·phone_harness import, CLI help
- 실패: 상류 문서의 `pyobjc-framework-AppKit` 설치, 종료 코드 1
- 실행하지 않은 것: 실제 아이폰 페어링, 화면 기록·손쉬운 사용 권한 부여, OCR 정확도, 탭·입력
- 기록: `artifacts/sources/phone-harness/install-validation.md`

## 보존 원자료

- exact commit 문서와 코드: `artifacts/sources/phone-harness/`
- 파일별 SHA-256: `artifacts/sources/phone-harness/SHA256SUMS.md`
- Apple·Anthropic 원문: `artifacts/sources/web/`

## 해석 경계

- 시리나 iOS 기본 비서를 교체한다고 주장하지 않습니다. Mac의 Claude Code가 미러링 창을 조작하는 방식으로 한정합니다.
- 실제 기기 사용기처럼 성공률과 안정성을 표현하지 않습니다.
- 화면 정보의 전송 범위는 phone-harness 코드의 로컬 처리와 Claude Code 공식 데이터 흐름을 합친 보수적 해석임을 밝힙니다.
