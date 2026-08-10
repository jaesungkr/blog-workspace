---
title: "게임·디스코드에서 블루투스 이어폰 음질이 나빠질 때 해결법"
slug: bluetooth-headset-audio-quality
date: 2026-08-10
category: "Log"
subcategory: "개발 · 디지털"
status: ready
format: rich-post-v2
tags: [블루투스 이어폰, 디스코드, Windows 11, Hands-Free, HFP, A2DP, LE Audio]
summary: "게임이나 Discord 음성 채팅을 켰을 때 블루투스 이어폰 음질이 떨어지는 원인과 가장 먼저 바꿀 설정을 정리합니다."
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

**먼저 Discord의 `입력 장치`를 블루투스 이어폰이 아닌 노트북·USB 마이크로 바꾸세요.** 음질이 돌아오면 다른 Windows 설정은 건드릴 필요가 없습니다.

별도 마이크가 없다면 선택은 두 가지입니다. 음성 채팅을 끄고 스테레오 음질을 유지하거나, 이어폰 마이크를 쓰면서 통화 음질을 받아들여야 합니다. 일부 최신 PC·이어폰 조합은 예외이며 세 번째 단계에서 확인할 수 있습니다.

아래 내용은 2026년 8월 10일 Microsoft와 Discord 공식 문서를 기준으로 정리했습니다. 실제 기기 성능을 측정한 결과는 아니며, 특정 이어폰의 펌웨어나 무선 간섭은 다루지 않습니다.

{{media:bluetooth-audio-profile-switch}}

### 1. Discord 입력을 별도 마이크로 변경

출력은 블루투스 이어폰으로 두고 입력만 바꿉니다.

1. Discord 왼쪽 아래 톱니바퀴를 눌러 `사용자 설정`을 엽니다.
2. `음성 및 비디오`로 이동합니다.
3. `입력 장치`에서 노트북·USB·웹캠 마이크를 직접 선택합니다.
4. 음악을 재생한 채 음성 채널에 들어가 음질을 비교합니다.

`Default`는 다시 블루투스 이어폰 마이크를 고를 수 있습니다. 아래 공식 화면의 `INPUT DEVICE`에서 사용할 마이크 이름을 직접 지정하세요.

{{media:discord-input-device}}

[Discord 공식 안내](https://support.discord.com/hc/en-us/articles/214925018-Where-d-my-Audio-Input-go-Various-Voice-Issues)와 같은 경로입니다. 마이크 테스트에서 목소리가 들어오는지도 확인하세요.

이 상태에서 음질이 유지되면 해결된 것입니다. 블루투스 이어폰 마이크가 통화용 오디오 전환 조건이었던 경우입니다.

게임을 켤 때만 다시 나빠진다면 게임 안의 음성 채팅도 확인하세요. 입력을 같은 별도 마이크로 바꾸거나 사용하지 않는 음성 채팅을 끕니다.

### 2. 그대로라면 Discord 출력 장치 확인

입력을 바꿔도 Discord 통화에 들어갈 때 음질이 떨어진다면 출력 장치를 분리해 봅니다.

1. `사용자 설정 > 음성 및 비디오`를 엽니다.
2. Discord의 `출력 장치`를 노트북 스피커나 유선 장치로 바꿉니다.
3. 게임 소리는 블루투스 이어폰으로 재생한 채 음질을 비교합니다.

이때 게임 소리가 선명해지면 Discord의 통신용 출력이 전환 조건이었을 가능성이 큽니다. Discord 음성까지 같은 Bluetooth Classic 이어폰으로 들어야 한다면 모노 통신 품질이 남을 수 있습니다.

### 3. 이어폰 하나로 말하고 들으려면 LE Audio 확인

LE Audio를 지원하지 않는 Bluetooth Classic 조합에서는 이어폰 하나로 마이크와 고음질 스테레오를 동시에 쓸 수 없습니다. 먼저 PC에 지원 메뉴가 있는지 확인하세요.

1. `설정 > Bluetooth 및 장치 > 장치`로 이동합니다.
2. `장치 설정`에서 `사용 가능한 경우 LE 오디오 사용`을 찾습니다.
3. 항목이 있으면 켜고 이어폰의 LE Audio 지원도 확인합니다.

[Microsoft 문서](https://support.microsoft.com/en-US/Windows/Hardware/Bluetooth/check-if-a-windows-11-device-supports-bluetooth-low-energy-audio)에 따르면 이 메뉴가 없으면 현재 PC는 LE Audio를 지원하지 않습니다. 이 경우에는 별도 마이크를 사용하거나 통화 중 모노 음질을 받아들여야 합니다. Bluetooth 버전 숫자만으로는 지원 여부를 판단할 수 없습니다.

마이크를 사용하면서 스테레오까지 유지하려면 Windows 11 24H2·빌드 26100.4484 이상이 필요합니다. PC의 공장 출하형 통합 LE Audio 지원, 제조사 드라이버와 호환 이어폰도 필요합니다.

1. `설정 > 시스템 > 소리`를 엽니다.
2. `출력`에서 연결된 LE Audio 이어폰 오른쪽의 화살표를 누릅니다.
3. `출력 설정 > 형식`을 펼칩니다.
4. `마이크가 활성 상태일 때 형식`에서 `스테레오(채널 2개)`를 선택합니다.

아래는 Microsoft 영문 공식 화면입니다. `Format when microphone is active`가 한국어 Windows의 `마이크가 활성 상태일 때 형식`입니다. 이 항목이 없으면 현재 조합은 마이크 사용 중 스테레오를 지원하지 않습니다.

{{media:windows-le-audio-stereo}}

[Microsoft 품질 설정 문서](https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11)는 호환 문제가 생기면 모노로 되돌려 비교하라고 안내합니다.

**왜 이런 일이 생길까?**

Bluetooth Classic은 고음질 스테레오 재생과 이어폰 마이크를 동시에 처리하지 못합니다. 용도에 따라 두 가지 오디오 방식을 번갈아 사용합니다.

| 방식 | 용도 | 들리는 소리 |
|---|---|---|
| A2DP | 음악·영상·게임 재생 | 고음질 스테레오 |
| HFP | 이어폰 마이크와 통화 소리를 함께 처리 | 8kHz 또는 16kHz 모노 통신 품질 |

[Microsoft 문서](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio)에 따르면 이어폰 마이크가 필요할 때 HFP가 선택됩니다. 앱이 출력을 통신용으로 분류할 때도 같은 전환이 일어날 수 있습니다. 공간감과 고음이 줄어드는 이유입니다.

Windows 11은 A2DP와 HFP를 하나의 장치로 표시합니다. `Stereo`와 `Hands-Free`가 따로 보이지 않아도 정상입니다. [Microsoft가 설명한 전환 조건](https://learn.microsoft.com/en-us/windows/win32/coreaudio/communications-audio-format-capabilities)은 앱의 입력과 출력에서 확인해야 합니다.

통화를 끝내도 음질이 돌아오지 않는다면 이 문제와 원인이 다를 수 있습니다. 이때는 Windows 출력 장치, 드라이버, 무선 간섭과 음향 효과를 확인하세요.
