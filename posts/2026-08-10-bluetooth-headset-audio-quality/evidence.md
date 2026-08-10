# 근거 지도: 게임·디스코드에서 블루투스 이어폰 음질이 나빠질 때 해결법

확인일은 모두 2026-08-10입니다. Microsoft와 Discord 공식 문서 원문, 본문에 사용할 공식 UI 이미지 원본은 `artifacts/sources/`에 보존했습니다.

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Bluetooth Classic의 A2DP는 일반적인 고음질 스테레오 재생에 쓰이고, 이어폰 마이크를 사용하려면 HFP가 필요합니다. | 공식 | 확인 | [Microsoft Bluetooth Classic audio](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio), `microsoft-bluetooth-classic-audio.html` | 코덱과 실제 음질은 PC·이어폰 조합에 따라 달라집니다. |
| C02 | HFP에서는 마이크 입력과 재생이 모두 모노로 동작하며 Windows 11은 8kHz 또는 16kHz 통신 모드를 지원합니다. | 공식 | 확인 | [Microsoft communications audio formats](https://learn.microsoft.com/en-us/windows/win32/coreaudio/communications-audio-format-capabilities), `microsoft-communications-audio-formats.html` | 숫자는 Bluetooth Classic HFP 통신 모드 기준이며 모든 저음질 현상의 원인은 아닙니다. |
| C03 | Windows 11은 A2DP와 HFP 입출력 지점을 하나로 합치며, 앱이 블루투스 마이크를 열거나 통신용 출력 스트림을 만들면 HFP를 자동으로 선택합니다. | 공식 | 확인 | [Microsoft Bluetooth Classic audio](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/bluetooth-classic-audio), `microsoft-bluetooth-classic-audio.html` | Windows 10은 `Stereo`와 `Hands-Free`가 별도 장치로 보일 수 있어 화면이 다릅니다. |
| C04 | Discord에서는 `사용자 설정 > 음성 및 비디오`의 입력 장치에서 사용할 마이크를 고를 수 있습니다. | 공식 | 확인 | [Discord audio input guide](https://support.discord.com/hc/en-us/articles/214925018-Where-d-my-Audio-Input-go-Various-Voice-Issues), `discord-audio-input.json`, `discord-input-device.png` | Discord UI 이름과 배치는 업데이트로 바뀔 수 있습니다. |
| C05 | 별도 마이크 지정은 Bluetooth 입력이 HFP 전환 조건인지 가르는 첫 테스트이며, 입력을 바꿔도 계속되면 앱의 통신용 출력 스트림을 따로 확인해야 합니다. | 공식 근거를 적용한 판단 | 확인 | C01-C04의 두 HFP 선택 조건을 각각 입력·출력 장치 변경으로 분리 | 앱별 오디오 범주를 사용자가 직접 바꿀 수 있다는 뜻은 아니며 특정 Discord 버전의 내부 범주를 단정하지 않습니다. |
| C06 | Windows 11의 Bluetooth LE Audio는 지원 조합에서 마이크 사용 중 더 높은 품질을 제공하고, 일부 PC는 마이크 사용 중 스테레오 재생도 지원합니다. | 공식 | 확인 | [Microsoft LE Audio quality settings](https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11), `microsoft-le-audio-quality.html` | PC·이어폰·드라이버·Windows 빌드가 모두 조건을 충족해야 합니다. |
| C07 | 마이크 사용 중 스테레오에는 Windows 11 24H2 이상, 빌드 26100.4484 이상, 공장 출하 단계의 통합 LE Audio 지원과 제조사 드라이버, LE Audio 이어폰이 필요합니다. | 공식 | 확인 | [Microsoft LE Audio quality settings](https://support.microsoft.com/en-us/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11), `microsoft-le-audio-quality.html` | Bluetooth 버전 숫자만으로 지원 여부를 판단할 수 없습니다. |
| C08 | `설정 > Bluetooth 및 장치 > 장치`에 `사용 가능한 경우 LE 오디오 사용`이 없으면 현재 PC가 LE Audio를 지원하지 않는 것이며, 마이크 활성 시 형식 항목이 없으면 스테레오 동시 사용을 지원하지 않습니다. | 공식 | 확인 | [Microsoft LE Audio support check](https://support.microsoft.com/ko-KR/Windows/Hardware/Bluetooth/check-if-a-windows-11-device-supports-bluetooth-low-energy-audio), [LE Audio quality settings](https://support.microsoft.com/ko-kr/windows/hardware/bluetooth/configuring-bluetooth-le-audio-quality-settings-on-windows-11), `microsoft-check-le-audio.html`, `microsoft-check-le-audio-ko.html`, `microsoft-le-audio-quality-ko.html`, `microsoft-le-audio-format.png` | 나중에 제조사 드라이버 업데이트로 지원이 추가될 수 있습니다. |
| C09 | Discord도 통화 참가 시 Bluetooth 헤드셋 프로필로 바뀌어 음질이 낮아질 수 있다고 안내합니다. | 공식 | 부분 확인 | [Discord known issue](https://support.discord.com/hc/en-us/articles/19850083499159--Known-Issue-Audio-Quality-Drops-When-Joining-A-Call), `discord-audio-quality-drop.json` | 2023년 문서이며 휴대전화와 당시 LE Audio 지원 계획을 함께 다룹니다. Windows 11의 현재 LE Audio 조건 근거로 사용하지 않습니다. |
| C10 | 증상 시작 시점, Bluetooth 마이크와 통신용 출력, LE Audio 지원 여부를 순서대로 확인하면 해결 선택지를 좁힐 수 있습니다. | Codex 작성 결정 프레임워크 | 확인 | C01-C09를 원인 판별 순서로 재배열 | 특정 기기 성공률을 측정한 실험 결과는 아닙니다. |

## 직접 검증 설계

- 질문: 공식 문서에 흩어진 프로필·앱 입력·LE Audio 조건을 일반 사용자가 확인할 순서로 줄일 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: 2026-08-10, Microsoft 공식 영문 문서 4개·한국어 UI 문서 2개와 Discord 공식 문서 2개 대조
- 입력: A2DP·HFP 선택 조건, Discord 입력 장치 경로, LE Audio 지원 조건과 UI 표식
- 전처리 또는 표현: `증상 시작 시점 -> 앱의 입력·통신용 출력 -> Classic/LE Audio -> 가능한 해결`로 분류
- 비교·판정 규칙: 설정 변경 전에 원인을 가르는 항목을 앞에 두고, 지원되지 않는 기능은 대안과 분리
- 성공 기준: 독자가 자신의 화면에서 보이는 항목 하나로 다음 행동을 고를 수 있음
- 반복 횟수와 표본 크기: 공식 문서 8개, 실제 Bluetooth 기기 성능 실험 없음
- 보존할 원자료: `artifacts/sources/*.html`, `artifacts/sources/*.json`, `artifacts/sources/*.png`

## 결과

| 산출물 | 관찰 결과 | 본문 위치 | 해석 범위 |
|---|---|---|---|
| 첫 설정 변경 | Discord 입력을 별도 마이크로 바꿔 Bluetooth 마이크 조건부터 분리 | `1. Discord 입력을 별도 마이크로 변경` | 통화 시작과 동시에 달라지는 증상 |
| 두 번째 설정 변경 | Discord 출력을 다른 장치로 바꿔 통신용 출력 조건을 분리 | `2. 그대로라면 Discord 출력 장치 확인` | 입력 변경만으로 해결되지 않는 증상 |
| 지원 여부와 선택 | LE Audio 지원을 확인하고, 지원되지 않으면 별도 마이크와 모노 품질 중 선택 | `3. 이어폰 하나로 말하고 들으려면 LE Audio 확인` | Windows 11과 Bluetooth 오디오 장치 |

## 실패와 반례

- 실제 Windows PC, Bluetooth 이어폰, Discord 계정을 조작하지 않았으므로 특정 제품의 성공을 체험값으로 단정하지 않습니다.
- 음질이 통화 시작 전부터 나쁘거나 통화를 끝내도 돌아오지 않으면 HFP 전환 외에 코덱, 드라이버, 무선 간섭, 앱별 출력, 음향 효과를 확인해야 합니다.
- Bluetooth Classic 이어폰의 자체 마이크를 계속 사용하면서 A2DP 스테레오를 유지하는 해결책은 제시하지 않습니다. 두 프로필의 기능 한계가 충돌하기 때문입니다.
- 별도 마이크를 지정해도 앱이 Bluetooth 출력 스트림을 통신용으로 분류하면 HFP가 계속 선택될 수 있습니다.
- Bluetooth 5.2·5.3 같은 버전 표기만으로 LE Audio와 마이크 사용 중 스테레오 지원을 보장하지 않습니다.
- Discord의 2023년 LE Audio 문구는 현재 Windows 지원 조건과 시점이 달라 보조 사례로만 사용합니다.

## 미해결 항목

- 없음. 기기별 지원 여부와 메뉴 차이는 독자가 자신의 Windows 설정과 제조사 사양에서 확인하도록 범위를 명시합니다.

## 출처 스냅숏 SHA-256

| 파일 | SHA-256 |
|---|---|
| `microsoft-bluetooth-classic-audio.html` | `1638def31c070d315bcabb3f7c061bca3fac6538e47da0e971f6c02d6f119ba5` |
| `microsoft-communications-audio-formats.html` | `794948ec9ee9ba9c90a9b846f5c52e9a7e46ba6de47089a16f8466f378e5f04f` |
| `microsoft-le-audio-quality.html` | `30d8578ccdf1a1971983bb5aebd32ecb1ba2d9459321e4d8692d70809bbc83de` |
| `microsoft-check-le-audio.html` | `a276425ddba11f58108de32d2a9058b06c64e262d92b4778f0a260246a26e1bb` |
| `microsoft-check-le-audio-ko.html` | `dcacac4af0506a0cb7dd5a4a5628b2e0f1e31dd80760dba95d8067d1993f4d34` |
| `microsoft-le-audio-quality-ko.html` | `4910b6be76e2f211bc1e0ca8534f85d8792f33a99833d84d587fa313c37521f6` |
| `discord-audio-input.json` | `46be4dc0a68acc4a9a739227f248b3ef4511c477a5e171697633c27e0ddd80db` |
| `discord-audio-quality-drop.json` | `422537a99c7a25d922f6cab2803a182c824ed93a253aeb41ce9ebc5346bdc84d` |
| `discord-input-device.png` | `a71060e7aa858785b2567af4242f6f7ac4c3179fafbf22697ad914627573d212` |
| `microsoft-le-audio-format.png` | `532e44b723ee4db329878cb9c316501c23f9828aeecb8e76bbc72e540152181d` |
