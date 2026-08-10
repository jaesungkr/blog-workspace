---
title: "게임·디스코드에서 블루투스 이어폰 음질이 나빠지는 이유와 해결 순서"
slug: bluetooth-headset-audio-quality
date: 2026-08-10
category: "Log"
subcategory: "개발 · 디지털"
status: ready
format: rich-post-v2
tags: [블루투스 이어폰, 디스코드, Windows 11, Hands-Free, HFP, A2DP, LE Audio]
summary: "게임이나 Discord 음성 채팅을 켰을 때 블루투스 이어폰이 통화 음질로 바뀌는 원인과, 별도 마이크·Windows 11 LE Audio 지원 여부에 따른 해결 순서를 정리합니다."
hero_image: assets/bluetooth-gaming-voice-chat-hero-v2.png
published_url: ""
sources:
    - https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio
    - https://learn.microsoft.com/en-us/windows/win32/coreaudio/communications-audio-format-capabilities
    - https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11
    - https://support.microsoft.com/en-US/Windows/Hardware/Bluetooth/check-if-a-windows-11-device-supports-bluetooth-low-energy-audio
    - https://support.discord.com/hc/en-us/articles/214925018-Where-d-my-Audio-Input-go-Various-Voice-Issues
    - https://support.discord.com/hc/en-us/articles/19850083499159--Known-Issue-Audio-Quality-Drops-When-Joining-A-Call
---

안녕하세요. dev.log입니다.

게임이나 Discord 음성 채팅에 들어가자마자 블루투스 이어폰 소리가 전화 통화처럼 먹먹해질 때가 있습니다. 통화에서 나오면 다시 선명해진다면 이어폰 고장보다 **Windows의 오디오 경로 전환**을 먼저 확인해야 합니다.

Bluetooth Classic은 고음질 스테레오 재생과 이어폰 마이크를 동시에 처리하지 못합니다. 가장 빠른 확인법은 Discord 입력을 노트북 내장 마이크나 USB 마이크로 바꾸는 것입니다. 아래 순서는 2026년 8월 10일 Microsoft와 Discord 공식 문서를 기준으로 정리했습니다. 실제 기기 성능을 측정한 결과는 아니며, 특정 이어폰의 펌웨어나 무선 간섭은 다루지 않습니다.

{{media:bluetooth-audio-profile-switch}}

### 통화에서 나오면 음질이 돌아오는지 확인

설정을 바꾸기 전에 증상이 통화와 맞물리는지 확인하세요.

1. 음악이나 게임 소리를 재생한 상태에서 Discord 음성 채널에 들어갑니다.
2. 소리가 먹먹해지면 채널에서 나와 원래 음질로 돌아오는지 듣습니다.
3. 게임 내 음성 채팅을 켜고 끌 때도 같은 현상이 생기는지 확인합니다.

통화 중에만 음질이 떨어진다면 앱이 Bluetooth 헤드셋 프로필을 바꿨을 가능성이 큽니다. Discord도 통화 참가 시 이 전환으로 음질이 낮아질 수 있다고 [안내합니다](https://support.discord.com/hc/en-us/articles/19850083499159--Known-Issue-Audio-Quality-Drops-When-Joining-A-Call).

통화 전부터 소리가 나쁘거나 종료 후에도 회복되지 않는다면 이 전환만으로 설명하기 어렵습니다. 이때는 출력 장치, 드라이버, 무선 간섭, 음향 효과를 확인하세요.

### A2DP는 재생, HFP는 마이크와 재생

프로필은 이어폰과 PC가 소리를 주고받는 규칙입니다. Bluetooth Classic은 용도에 따라 A2DP와 HFP를 사용합니다.

| 프로필 | 주로 하는 일 | 마이크 사용 중 재생 |
|---|---|---|
| A2DP | 음악·영상·게임의 고음질 스테레오 출력 | 이어폰 마이크 입력을 함께 처리하지 않음 |
| HFP | 통화용 마이크 입력과 소리 출력을 동시에 처리 | 모노 통신 품질로 동작 |

[Microsoft 문서](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio)에 따르면 A2DP는 고음질 스테레오 재생을 담당합니다. 이어폰 마이크가 필요하면 HFP로 바뀌며, Windows 11에서는 마이크와 출력이 모두 8kHz 또는 16kHz 모노 통신 형식으로 동작할 수 있습니다. 공간감과 고음이 줄어드는 이유입니다.

Windows 11은 A2DP와 HFP 장치를 하나로 표시합니다. 앱이 블루투스 마이크를 열거나 출력을 통신용으로 분류하면 HFP를 자동으로 선택합니다. `Stereo`와 `Hands-Free`가 따로 보이지 않아도 정상이며, [Microsoft가 설명한 두 전환 조건](https://learn.microsoft.com/en-us/windows/win32/coreaudio/communications-audio-format-capabilities)을 앱의 입력과 출력에서 나눠 확인해야 합니다.

### 첫 해결은 Discord 입력 장치 변경

다른 마이크가 있다면 Discord 입력만 바꿉니다. 출력은 블루투스 이어폰으로 둡니다.

1. Discord 왼쪽 아래 톱니바퀴를 눌러 `사용자 설정`을 엽니다.
2. `음성 및 비디오`로 이동합니다.
3. `입력 장치`에서 노트북·USB·웹캠 마이크를 직접 선택합니다.
4. 음악을 재생한 채 음성 채널에 들어가 음질을 비교합니다.

`Default`는 블루투스 이어폰 마이크를 선택할 수 있습니다. 아래 공식 화면의 `INPUT DEVICE`에서 장치 이름을 지정하고 마이크 테스트까지 확인하세요.

{{media:discord-input-device}}

[Discord 공식 안내](https://support.discord.com/hc/en-us/articles/214925018-Where-d-my-Audio-Input-go-Various-Voice-Issues)와 같은 경로입니다. 입력 변경 후 음질이 유지되면 블루투스 마이크가 HFP 전환 조건이었습니다.

그대로라면 Discord `출력 장치`를 노트북 스피커나 유선 장치로 잠시 바꿉니다. 게임 소리만 블루투스 이어폰으로 들을 때 음질이 회복되면 Discord의 통신용 출력이 HFP 전환 조건이었을 가능성이 큽니다. Discord 음성까지 같은 Bluetooth Classic 이어폰으로 들어야 한다면 모노 품질이 남을 수 있습니다.

게임을 켤 때만 나빠진다면 게임의 음성 채팅도 블루투스 마이크를 열고 있는지 확인하세요. 입력을 같은 별도 마이크로 바꾸거나 음성 채팅을 끈 뒤 다시 비교하세요.

### Bluetooth Classic에서 가능한 세 가지 선택

Bluetooth Classic에서는 이어폰 마이크와 고음질 스테레오를 동시에 쓸 수 없습니다. 필요한 기능에 맞춰 고릅니다.

| 필요한 것 | 현실적인 선택 | 결과 |
|---|---|---|
| 게임 소리의 스테레오 품질 | 이어폰 마이크를 쓰지 않고 음성 채팅을 끔 | A2DP 재생 유지 |
| 음성 채팅과 스테레오를 모두 사용 | 노트북 내장·USB·유선 마이크를 별도 입력으로 사용 | 마이크가 전환 조건이었다면 A2DP 유지 |
| 이어폰 하나로 말하고 듣기 | 이어폰 마이크를 그대로 사용 | HFP의 모노 통신 품질 허용 |

Windows에서 마이크 권한이나 장치를 통째로 끄면 다른 앱도 영향을 받습니다. 먼저 앱 안에서 입력 장치를 바꾸세요.

### LE Audio와 마이크 중 스테레오는 따로 확인

Bluetooth LE Audio는 Classic과 다른 오디오 경로입니다. 지원 조합은 마이크 사용 중 재생 음질이 좋아질 수 있고, 일부 PC·이어폰 조합은 스테레오까지 유지합니다.

먼저 PC 지원 여부를 확인합니다.

1. `설정 > Bluetooth 및 장치 > 장치`로 이동합니다.
2. `장치 설정`에서 `사용 가능한 경우 LE 오디오 사용`을 찾습니다.
3. 항목이 있으면 켜고, 이어폰의 LE Audio 또는 TMAP 지원도 확인합니다.

[Microsoft 문서](https://support.microsoft.com/en-US/Windows/Hardware/Bluetooth/check-if-a-windows-11-device-supports-bluetooth-low-energy-audio)에 따르면 이 메뉴가 없으면 현재 PC는 LE Audio를 지원하지 않습니다. Bluetooth 버전 숫자만으로는 판단할 수 없습니다.

마이크 사용 중 스테레오는 Windows 11 24H2·빌드 26100.4484 이상이 필요합니다. PC의 공장 출하형 통합 LE 지원, 제조사 드라이버, 호환 이어폰도 모두 필요합니다.

1. `설정 > 시스템 > 소리`를 엽니다.
2. `출력`에서 연결된 LE Audio 이어폰 오른쪽의 화살표를 누릅니다.
3. `출력 설정 > 형식`을 펼칩니다.
4. `마이크가 활성 상태일 때 형식`에서 `스테레오(채널 2개)`를 선택합니다.

아래는 Microsoft 영문 공식 화면입니다. `Format when microphone is active`가 한국어 Windows의 `마이크가 활성 상태일 때 형식`입니다. 이 항목이 없으면 현재 조합은 마이크 사용 중 스테레오를 지원하지 않습니다.

{{media:windows-le-audio-stereo}}

[Microsoft 품질 설정 문서](https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11)는 호환 문제가 생기면 모노로 되돌려 비교하라고 안내합니다.

### 증상별로 한 곳만 먼저 확인

여러 설정을 동시에 바꾸지 말고 증상에 맞는 한 곳부터 확인하세요.

| 증상 | 먼저 볼 곳 | 다음 행동 |
|---|---|---|
| Discord에 들어갈 때만 음질 저하 | Discord `입력 장치` | 블루투스 이어폰이 아닌 마이크를 직접 선택 |
| 게임을 켤 때만 음질 저하 | 게임의 음성 채팅·입력 장치 | 음성 채팅을 끄거나 별도 마이크 지정 |
| Windows 11에 `Stereo` 장치가 없음 | 정상적인 통합 입출력 여부 | 장치명 대신 앱의 입력 장치와 통신용 출력 확인 |
| `사용 가능한 경우 LE 오디오 사용`이 없음 | PC 하드웨어·제조사 드라이버 | 외부 마이크 방식 사용, 제조사 지원 여부 확인 |
| 통화를 끝내도 계속 음질이 나쁨 | 앱 종료 후 Windows 출력·드라이버 | HFP 외 원인으로 범위를 넓혀 점검 |

별도 마이크도 없고 LE Audio 메뉴도 없다면 설정만으로 두 기능을 함께 쓸 수 없습니다. 이어폰 마이크와 고음질 스테레오 중 하나를 선택해야 합니다.
