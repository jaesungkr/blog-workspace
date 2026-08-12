# phone-harness 설치 검증 기록

- 검증 일시: 2026-08-12 (Asia/Seoul)
- 검증 환경: macOS, Python 3.12 새 `venv`
- 저장소 커밋: `4d2de7a4b8780a386545c986543c83dda66764dd`
- 실제 아이폰 미러링 연결·OCR·입력: 실행하지 않음

## 상류 문서 명령의 실패

실행:

```bash
python3.12 -m pip install --dry-run pyobjc-framework-AppKit
```

종료 코드: `1`

핵심 출력:

```text
ERROR: Could not find a version that satisfies the requirement pyobjc-framework-AppKit (from versions: none)
ERROR: No matching distribution found for pyobjc-framework-AppKit
```

## 격리 환경 우회 경로의 성공

실행 순서:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install pyobjc-framework-Quartz pyobjc-framework-Vision \
  pyobjc-framework-Cocoa pyobjc-framework-ApplicationServices
.venv/bin/python -m pip install -e /path/to/phone-harness --no-deps
.venv/bin/python -c 'import Quartz, Vision, AppKit, ApplicationServices, phone_harness; print("imports-ok")'
.venv/bin/phone-harness --help
```

관찰 결과:

- `pyobjc-core`, `Cocoa`, `Quartz`, `CoreML`, `Vision`, `CoreText`, `ApplicationServices` 12.2.2 설치 성공
- `phone-harness` 0.1.0 editable wheel 빌드·설치 성공
- 네 프레임워크와 `phone_harness` import 성공: `imports-ok`
- `phone-harness --help` 사용법 출력 성공

이 검증은 Python 패키지 설치 경로만 다룹니다. macOS 권한, 아이폰 미러링 세션, 캡처와 OCR 성공을 보장하지 않습니다.
