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

평소에는 선명하던 블루투스 이어폰이 게임이나 Discord 음성 채팅을 켜는 순간 전화 통화처럼 답답해질 때가 있습니다. 게임 소리와 친구 목소리가 모두 얇게 들리지만, 통화를 나가면 다시 정상으로 돌아오기도 합니다. 이 증상은 이어폰 고장보다 **Windows가 통화용 오디오 경로로 바뀌었는지** 먼저 확인하는 편이 빠릅니다.

Bluetooth Classic에서는 고음질 스테레오 재생과 이어폰 마이크 사용을 같은 경로로 처리하지 못합니다. 노트북 내장 마이크나 USB 마이크처럼 별도 입력 장치를 고르는 것이 가장 쉬운 첫 분리 테스트입니다. 입력을 바꿔도 음질이 그대로라면 앱의 통신용 출력이 전환을 일으킬 수 있습니다. 이 글은 2026년 8월 10일 Microsoft와 Discord 공식 문서를 대조했습니다. 특정 이어폰을 직접 측정한 사용기가 아니라 공식 문서를 바탕으로 원인과 확인 순서를 좁힌 안내입니다.

{{media:bluetooth-audio-profile-switch}}

### 30초 확인으로 원인부터 분리

설정을 바꾸기 전에 음질이 변하는 순간부터 확인해 보세요.

1. 음악이나 게임 소리를 재생한 상태에서 Discord 음성 채널에 들어갑니다.
2. 소리가 먹먹해지면 음성 채널에서 나옵니다.
3. 몇 초 안에 원래 음질로 돌아오는지 듣습니다.
4. 같은 현상이 게임 내 음성 채팅을 켜고 끌 때도 반복되는지 확인합니다.

통화에 들어갈 때 나빠지고 나올 때 돌아온다면 앱이 블루투스 장치를 통화용 오디오 경로로 바꿨을 가능성이 큽니다. [Microsoft의 통신 오디오 문서](https://learn.microsoft.com/en-us/windows/win32/coreaudio/communications-audio-format-capabilities)는 두 가지 조건을 제시합니다. 앱이 블루투스 마이크를 열거나, 재생 스트림을 통신용으로 분류하면 장치가 통신 모드로 들어갈 수 있습니다. Discord도 통화 참가 시 Bluetooth 헤드셋 프로필로 바뀌어 음질이 낮아질 수 있다고 [별도 안내](https://support.discord.com/hc/en-us/articles/19850083499159--Known-Issue-Audio-Quality-Drops-When-Joining-A-Call)합니다.

통화 전부터 소리가 나쁘거나 통화를 끝내도 돌아오지 않는다면 이 글의 원인과 다를 수 있습니다. 그때는 출력 장치, 드라이버, 무선 간섭, 음향 효과를 따로 확인해야 합니다.

### A2DP는 듣기, HFP는 말하기까지

Bluetooth Classic 오디오에는 이 문제와 관련된 두 프로필이 있습니다. 프로필은 이어폰과 PC가 어떤 방식으로 소리를 주고받을지 정한 규칙입니다.

| 프로필 | 주로 하는 일 | 마이크 사용 중 재생 |
|---|---|---|
| A2DP | 음악·영상·게임의 고음질 스테레오 출력 | 이어폰 마이크 입력을 함께 처리하지 않음 |
| HFP | 통화용 마이크 입력과 소리 출력을 동시에 처리 | 모노 통신 품질로 동작 |

[Microsoft의 Bluetooth Classic 설명](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio)에 따르면 A2DP는 일반 미디어를 위한 고음질 스테레오 재생을 담당합니다. 이어폰의 마이크 입력이 필요해지면 HFP를 사용합니다. HFP에서는 마이크와 출력이 모두 모노로 동작하며, Windows 11은 장치 조합에 따라 8kHz 협대역 또는 16kHz 광대역 음성을 사용합니다.

그래서 평소 48kHz로 재생되던 게임 소리도 블루투스 마이크가 열리면 HFP 형식에 맞춰 다시 처리될 수 있습니다. 볼륨이 작아진 정도가 아니라 공간감과 고음이 줄고, 전체 소리가 통화처럼 바뀌는 이유입니다.

### `Stereo`와 `Hands-Free`가 하나로 합쳐진 Windows 11

예전 해결 글에서는 출력 장치 목록에서 `Headphones (Stereo)`를 고르고 `Headset (Hands-Free)`를 피하라고 안내하곤 합니다. 이 구분은 Windows 10 화면에는 맞을 수 있지만 Windows 11에서는 그대로 보이지 않을 수 있습니다.

Windows 11은 Bluetooth Classic 장치의 A2DP와 HFP 입출력을 하나로 합칩니다. 앱이 이어폰 마이크를 열거나 통신용 출력 스트림을 만들면 Windows가 HFP를 자동으로 선택합니다. 그 밖의 재생에는 A2DP를 사용합니다. 장치 목록에 `Stereo`와 `Hands-Free`가 따로 없어도 두 프로필 전환은 내부에서 계속 일어납니다.

따라서 Windows 11에서는 장치 이름을 찾는 것보다 **앱이 사용하는 입력 장치와 통신용 출력**을 함께 보는 편이 정확합니다.

### 별도 마이크로 첫 원인을 가르는 방법

노트북 내장 마이크, USB 마이크, 웹캠 마이크, 유선 이어셋 마이크 중 하나가 있다면 Discord의 입력 장치를 바꿉니다. 출력은 블루투스 이어폰으로 두고, 입력만 다른 마이크로 나누는 방식입니다.

1. Discord 왼쪽 아래 톱니바퀴를 눌러 `사용자 설정`을 엽니다.
2. `음성 및 비디오`로 이동합니다.
3. `입력 장치`에서 블루투스 이어폰이 아닌 마이크를 장치 이름으로 선택합니다.
4. `출력 장치`는 사용할 블루투스 이어폰으로 둡니다.
5. 음악을 재생한 채 음성 채널에 들어가 음질이 유지되는지 확인합니다.

`Default`를 그대로 두면 Windows 기본 입력이 블루투스 이어폰 마이크일 수 있습니다. 아래 Discord 공식 화면에서 붉은 점선으로 표시된 `INPUT DEVICE`를 열어 노트북 마이크나 USB 마이크 이름을 직접 선택하세요. 선택 뒤에는 Discord의 마이크 테스트로 목소리가 들어오는지도 확인합니다.

{{media:discord-input-device}}

[Discord 공식 입력 장치 안내](https://support.discord.com/hc/en-us/articles/214925018-Where-d-my-Audio-Input-go-Various-Voice-Issues)도 `사용자 설정 > 음성 및 비디오`에서 원하는 마이크를 고르도록 설명합니다. 블루투스 마이크 사용이 전환 조건이었다면 별도 입력을 고른 뒤 Windows가 A2DP 재생을 유지할 수 있습니다.

입력 장치를 바꿨는데도 Discord 통화에 들어가는 순간 소리가 나빠진다면 통신용 출력 스트림이 두 번째 후보입니다. 이를 가르려면 Discord의 `출력 장치`를 노트북 스피커나 유선 장치로 잠시 바꾸고, 게임 소리만 블루투스 이어폰으로 재생해 봅니다. 이때 음질이 유지되면 Discord의 통신용 출력이 Bluetooth Classic 장치를 HFP로 바꾸는 조건에 가까웠다고 볼 수 있습니다. Discord 목소리까지 같은 Bluetooth Classic 이어폰으로 들어야 한다면 통화 중 모노 품질을 받아들여야 할 수 있습니다. 다른 선택지는 뒤에서 설명할 LE Audio 지원 여부를 확인하는 것입니다.

Discord 입력을 바꿨는데도 게임을 실행할 때 다시 음질이 떨어진다면 게임의 음성 채팅 설정도 확인합니다. 게임이 별도로 블루투스 마이크를 사용하면 Discord 설정과 관계없이 HFP가 선택될 수 있습니다. 게임 안에서 입력 장치를 같은 별도 마이크로 바꾸거나, 사용하지 않는 음성 채팅을 끈 뒤 다시 비교하세요.

### 별도 마이크가 없을 때의 선택

Bluetooth Classic 이어폰의 자체 마이크를 반드시 써야 한다면 고음질 스테레오와 마이크를 동시에 유지할 수 없습니다. 설정이 잘못된 것이 아니라 A2DP와 HFP의 역할이 나뉘어 있기 때문입니다.

| 필요한 것 | 현실적인 선택 | 결과 |
|---|---|---|
| 게임 소리의 스테레오 품질 | 이어폰 마이크를 쓰지 않고 음성 채팅을 끔 | A2DP 재생 유지 |
| 음성 채팅과 스테레오를 모두 사용 | 노트북 내장·USB·유선 마이크를 별도 입력으로 사용 | 마이크가 전환 조건이었다면 A2DP 유지 |
| 이어폰 하나로 말하고 듣기 | 이어폰 마이크를 그대로 사용 | HFP의 모노 통신 품질 허용 |

마이크 권한을 끄거나 장치를 사용 중지하는 방법도 있지만, 필요한 앱까지 마이크를 못 쓰게 만들 수 있습니다. 먼저 앱 안에서 입력 장치를 명시적으로 바꾸는 것이 안전합니다.

### LE Audio라면 확인할 두 메뉴

Bluetooth LE Audio는 Classic의 A2DP·HFP와 다른 최신 오디오 경로입니다. 지원되는 Windows 11 PC와 이어폰 조합에서는 마이크 사용 중 음질이 개선되고, 일부 PC는 스테레오 재생도 유지할 수 있습니다.

먼저 PC가 LE Audio를 지원하는지 확인합니다.

1. `설정 > Bluetooth 및 장치 > 장치`로 이동합니다.
2. `장치 설정`에서 `사용 가능한 경우 LE 오디오 사용`이 있는지 봅니다.
3. 항목이 있다면 켜고, 이어폰 제조사 사양에도 LE Audio 또는 TMAP 지원이 있는지 확인합니다.

[Microsoft의 LE Audio 확인 문서](https://support.microsoft.com/en-US/Windows/Hardware/Bluetooth/check-if-a-windows-11-device-supports-bluetooth-low-energy-audio)에 따르면 이 항목이 없으면 현재 PC가 LE Audio를 지원하지 않는 것입니다. 제품 설명에 `Bluetooth LE`나 최신 Bluetooth 버전이 적혀 있어도 LE Audio까지 지원한다는 뜻은 아닙니다. PC의 Bluetooth·오디오 하드웨어와 제조사 드라이버, 이어폰이 모두 맞아야 합니다.

마이크 사용 중 스테레오 형식은 조건이 더 까다롭습니다. Microsoft가 제시한 조건은 Windows 11 24H2 이상과 빌드 26100.4484 이상입니다. 여기에 공장 출하 단계의 통합 Bluetooth LE 지원, 제조사 드라이버, 호환되는 LE Audio 이어폰이 모두 필요합니다. 조건을 충족한다면 다음 메뉴를 확인합니다.

1. `설정 > 시스템 > 소리`를 엽니다.
2. `출력`에서 연결된 LE Audio 이어폰 오른쪽의 화살표를 누릅니다.
3. `출력 설정 > 형식`을 펼칩니다.
4. `마이크가 활성 상태일 때 형식`에서 `스테레오(채널 2개)`를 선택합니다.

아래 이미지는 Microsoft 영문 공식 문서의 Windows 설정 화면입니다. `Format when microphone is active` 항목에 1채널과 2채널 선택지가 나타납니다. 한국어 Windows에서는 `마이크가 활성 상태일 때 형식`으로 표시되며, 항목 자체가 없다면 현재 조합은 마이크 사용 중 스테레오를 지원하지 않습니다.

{{media:windows-le-audio-stereo}}

[Microsoft의 LE Audio 품질 설정 문서](https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11)는 지원되는 조합에서 스테레오를 기본으로 사용한다고 설명합니다. 다만 스테레오 선택 뒤 소리가 끊기거나 사라지는 호환성 문제가 생기면 모노로 되돌려 비교하도록 안내합니다.

### 증상별 첫 확인 지점

설정을 여러 개 한꺼번에 바꾸기보다 현재 보이는 증상에 맞춰 한 단계씩 확인하세요.

| 증상 | 먼저 볼 곳 | 다음 행동 |
|---|---|---|
| Discord에 들어갈 때만 음질 저하 | Discord `입력 장치` | 블루투스 이어폰이 아닌 마이크를 직접 선택 |
| 게임을 켤 때만 음질 저하 | 게임의 음성 채팅·입력 장치 | 음성 채팅을 끄거나 별도 마이크 지정 |
| Windows 11에 `Stereo` 장치가 없음 | 정상적인 통합 입출력 여부 | 장치명 대신 앱의 입력 장치와 통신용 출력 확인 |
| `사용 가능한 경우 LE 오디오 사용`이 없음 | PC 하드웨어·제조사 드라이버 | 외부 마이크 방식 사용, 제조사 지원 여부 확인 |
| `마이크가 활성 상태일 때 형식`이 있음 | 출력 장치의 `형식` | 2채널을 선택하고 통화 중 재생 테스트 |
| 통화를 끝내도 계속 음질이 나쁨 | 앱 종료 후 Windows 출력·드라이버 | HFP 외 원인으로 범위를 넓혀 점검 |

가장 먼저 해볼 일은 Discord의 입력 장치를 `Default`에서 별도 마이크 이름으로 바꾸는 것입니다. 그 상태에서 음악을 틀고 음성 채널에 들어가 보세요. 음질이 유지되면 블루투스 마이크 사용이 전환 조건에 가까웠다고 판단할 수 있습니다. 그대로라면 Discord의 출력 장치를 다른 장치로 옮겨 두 번째 조건을 분리합니다.

별도 마이크가 없고 LE Audio 지원 메뉴도 없다면 설정만으로 두 기능을 모두 얻기 어렵습니다. Bluetooth Classic 이어폰의 마이크와 고음질 스테레오 중 어느 기능을 우선할지 정하는 편이 빠릅니다.
