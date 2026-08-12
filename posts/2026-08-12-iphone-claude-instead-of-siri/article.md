---
title: "시리 대신 클로드로 아이폰 쓰기"
slug: iphone-claude-instead-of-siri
date: 2026-08-12
category: "Log"
subcategory: "AI 개념 · 실전"
status: ready
format: rich-post-v2
tags: [클로드, Claude, 아이폰, phone-harness, 아이폰 미러링, Claude Code]
summary: "Mac의 Claude Code가 아이폰 미러링 화면을 읽고 탭·스크롤·입력하게 만드는 phone-harness의 작동 원리와 설치 방법을 핵심만 설명합니다."
hero_image: assets/phone-harness-github-overview.jpg
published_url: ""
sources:
    - https://github.com/ShawnPana/phone-harness
    - https://support.apple.com/en-ie/120421
    - https://code.claude.com/docs/en/getting-started
    - https://code.claude.com/docs/en/authentication
    - https://code.claude.com/docs/en/data-usage
---

안녕하세요. dev.log입니다.

`phone-harness`를 사용하면 Claude에게 “날씨 앱을 열고 내일 비가 오는지 확인해 줘”라고 요청해 아이폰 화면을 직접 읽고 누르게 할 수 있습니다. Claude가 화면에서 `날씨`라는 글자를 찾고, 그 위치를 탭한 뒤, 바뀐 화면을 다시 읽어 결과를 확인하는 방식입니다.

다만 아이폰 안에서 Claude가 시리처럼 실행되는 구조는 아닙니다. **Mac의 Claude Code가 아이폰 미러링 화면을 눈으로 보고, 마우스와 키보드 입력을 손처럼 보내는 방식**입니다. 따라서 Mac과 아이폰이 함께 있어야 합니다.

가장 먼저 Mac에서 아이폰 미러링을 직접 연결해 보세요. 미러링이 정상 작동해야 `phone-harness`도 아이폰 화면을 읽고 누를 수 있습니다.

{{media:phone-harness-github-overview}}

### Claude가 아이폰을 보고 누르는 방법

1. Mac의 아이폰 미러링 창을 캡처합니다.
2. Apple Vision OCR로 화면의 글자와 좌표를 찾습니다.
3. 해당 좌표에 탭·스크롤·키 입력을 보냅니다.
4. 화면을 다시 캡처해 작업이 제대로 됐는지 확인합니다.

예를 들어 Claude에게 “설정 앱에서 소프트웨어 업데이트 화면까지 이동해 줘”라고 요청하면, 화면에서 `설정`을 찾고 누른 뒤 다음 화면을 다시 읽습니다. 이어서 `일반`, `소프트웨어 업데이트`를 차례로 찾아 이동합니다. 웹 브라우저의 DOM처럼 버튼 정보가 따로 있는 것은 아니며, 실제 화면을 보고 글자 위치를 추적합니다.

앱 열기, 메뉴 이동, 글자 읽기, 스크롤, 간단한 입력을 자동화할 수 있습니다. 카메라·마이크·Face ID·멀티터치는 지원하지 않습니다. 글자가 없는 아이콘이나 같은 문구가 여러 번 나오는 화면에서는 엉뚱한 곳을 누를 수도 있습니다.

### 준비할 것은 Mac, 아이폰 미러링, Claude Code

[Apple 안내](https://support.apple.com/en-ie/120421) 기준으로 Apple Silicon 또는 T2 칩이 있는 Mac, macOS Sequoia 15 이상, iOS 18 이상이 필요합니다. 두 기기는 같은 Apple 계정과 2단계 인증을 사용해야 하며 Wi-Fi와 Bluetooth가 켜져 있어야 합니다.

`phone-harness`는 아이폰 앱이 아니라 Mac에서 실행하는 Python 도구입니다. 다음 준비물이 필요합니다.

| 준비물 | 필요한 이유 |
|---|---|
| Claude Code | 사용자의 요청을 해석하고 다음 조작을 결정합니다. |
| Python 3.12 | phone-harness와 PyObjC 모듈을 실행합니다. |
| 화면 기록 권한 | 아이폰 미러링 화면을 캡처합니다. |
| 손쉬운 사용 권한 | 미러링 창에 탭과 키 입력을 보냅니다. |

Claude Code가 없다면 [공식 설치 안내](https://code.claude.com/docs/en/getting-started)에 따라 먼저 설치합니다.

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
claude
```

처음 `claude`를 실행하면 브라우저 로그인 화면이 열립니다. 로그인 뒤 터미널에 `Login successful`이 표시되는지 확인하세요. Claude Code는 Pro·Max·Team·Enterprise 또는 Console 계정이 필요합니다.

### phone-harness 설치 명령은 그대로 복사하면 실패

2026년 8월 12일 기준 저장소의 설치 문서에는 `pyobjc-framework-AppKit`가 적혀 있습니다. 하지만 이 이름의 패키지는 PyPI에 없어 그대로 설치하면 실패합니다. AppKit 바인딩이 포함된 `pyobjc-framework-Cocoa`를 대신 설치해야 합니다.

아래 명령은 Python 3.12 새 가상 환경에서 패키지 설치, 모듈 import, `phone-harness --help`까지 확인했습니다.

```bash
git clone https://github.com/ShawnPana/phone-harness ~/.phone-harness
cd ~/.phone-harness

python3.12 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install pyobjc-framework-Quartz pyobjc-framework-Vision \
  pyobjc-framework-Cocoa pyobjc-framework-ApplicationServices
python -m pip install -e . --no-deps

python -c 'import Quartz, Vision, AppKit, ApplicationServices, phone_harness; print("imports-ok")'
phone-harness --help
```

설치가 끝나면 Claude Code가 이 도구를 자동으로 찾도록 스킬을 등록합니다.

```bash
mkdir -p ~/.claude/skills/phone-harness
phone-harness skill > ~/.claude/skills/phone-harness/SKILL.md
```

다음부터 새 터미널을 열었을 때는 `source ~/.phone-harness/.venv/bin/activate`로 가상 환경을 먼저 활성화해야 합니다.

### 권한을 켜고 doctor의 첫 FAIL부터 해결

`시스템 설정 > 개인정보 보호 및 보안`에서 명령을 실행할 터미널 앱에 두 권한을 허용합니다.

- `화면 기록`: 아이폰 미러링 화면을 읽는 권한입니다. 켠 뒤 터미널을 완전히 다시 시작합니다.
- `손쉬운 사용`: 화면을 누르고 글자를 입력하는 권한입니다.

아이폰을 잠근 상태로 Mac의 아이폰 미러링을 연결한 뒤 진단을 실행합니다.

```bash
phone-harness --doctor
```

진단은 PyObjC, 손쉬운 사용, 화면 기록, 미러링 앱, 창 탐색, 캡처, OCR 순서로 진행됩니다. 여러 설정을 한꺼번에 바꾸지 말고 첫 번째 `FAIL`부터 해결하세요.

{{media:phone-harness-install-doctor}}

### 처음에는 날씨 앱처럼 안전한 작업만 맡기기

연결 직후 메시지 전송이나 결제부터 맡기지 마세요. 먼저 화면을 읽을 수 있는지만 확인합니다.

```bash
phone-harness <<'PY'
print(connection_state())
print([item["text"] for item in ocr()][:10])
PY
```

`ready`와 현재 화면의 글자가 나오면 캡처와 OCR이 연결된 것입니다. 그다음 Claude Code에서 아래처럼 범위를 좁힌 작업을 시켜 보세요.

```text
아이폰에서 날씨 앱만 열어 줘.
다른 앱은 열지 말고, 실행하기 전에 나에게 확인해 줘.
```

작업마다 화면을 다시 확인하도록 요청하는 것이 중요합니다. 메시지 발송, 게시물 등록, 구매, 삭제, 설정 변경은 실행 직전에 반드시 확인을 받도록 해야 합니다.

### 화면 정보가 완전히 로컬에만 남는 것은 아님

화면 캡처와 Apple Vision OCR 자체는 Mac에서 실행됩니다. 하지만 Claude Code가 판단하도록 OCR 결과나 스크린샷을 보여 주면 해당 내용이 모델 요청의 일부로 전송될 수 있습니다. [Claude Code 데이터 안내](https://code.claude.com/docs/en/data-usage)에 따르면 보존 기간과 모델 개선 사용 여부는 계정 종류와 개인정보 설정에 따라 달라집니다.

인증 코드, 금융 정보, 사적인 대화가 보이는 화면에서는 사용하지 않는 편이 안전합니다. 작업이 끝나면 아이폰 미러링을 종료하고, 더 이상 필요하지 않다면 터미널의 화면 기록·손쉬운 사용 권한도 해제하세요.

`phone-harness`는 시리를 아이폰 안에서 Claude로 바꾸는 기능이 아닙니다. **Mac의 Claude Code에 아이폰 화면과 손을 빌려주는 도구**입니다.

이 글은 저장소 커밋 `4d2de7a`의 문서와 코드를 감사하고 Python 패키지 설치를 검증해 작성했습니다. 실제 아이폰 연결과 터치·OCR 정확도는 직접 시험하지 않았습니다.
