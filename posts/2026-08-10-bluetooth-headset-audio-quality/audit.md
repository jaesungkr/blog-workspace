# 최종 감사: 게임·디스코드에서 블루투스 이어폰 음질이 나빠질 때 해결법

## 구조와 독자

- [x] 제목 앞부분이 실제 검색 의도에서 시작합니다.
- [x] 제목과 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤 익숙한 증상과 첫 해결 방향이 나옵니다.
- [x] 첫 해결을 먼저 제시하고 A2DP·HFP 원리는 뒤에서 설명합니다.
- [x] 별도 마이크라는 기본 선택과 LE Audio 예외를 분리합니다.
- [x] 특정 기기 직접 테스트가 아닌 source-based 범위를 밝힙니다.

## 근거와 독창성

- [x] Microsoft·Discord 공식 문서 원본과 해시를 보존했습니다.
- [x] Windows 10의 분리 장치와 Windows 11의 통합 입출력을 구분했습니다.
- [x] Bluetooth Classic과 LE Audio의 지원 조건을 섞지 않았습니다.
- [x] Discord 2023년 문서는 현재 Windows LE Audio 근거가 아닌 보조 사례로 제한했습니다.
- [x] Codex가 만든 3단계 진단 순서를 사용자의 경험으로 표현하지 않았습니다.
- [x] 실제 기기 실험이 없다는 한계가 보입니다.

## 문장과 형식

- [x] 본문 존대어가 일관됩니다.
- [x] em dash 대신 하이픈을 사용했습니다.
- [x] 과장된 해결 보장과 불필요한 재설치 절차를 넣지 않았습니다.
- [x] 기술 용어를 처음 나올 때 풀어 설명했습니다.
- [x] 표는 A2DP·HFP 차이를 한눈에 보여 주는 한 곳에만 썼습니다.

## 제목·문체 폴리싱

- 비교 표본: `vercel-deployment-guide`(ready), `koreaconnect-public-data-api`(ready), `github-stacked-pull-requests`(ready), `wsl-containers-without-docker-desktop`(ready), `ccshare-manycode-guide`(ready)
- 대체 기준: 다섯 글 모두 같은 `Log > 개발 · 디지털`의 최근 완성 글이므로 대체 표본을 쓰지 않았습니다.
- 보호한 불변값: 확인일 2026-08-10, Windows 11 24H2·빌드 26100.4484 조건, A2DP·HFP 동작, Discord 메뉴 경로, 공식 링크, 실제 기기 테스트가 없다는 한계를 유지했습니다.
- 제목 수정: 반복되던 `검색어 - 설명` 틀을 줄이고, 검색 상황과 해결 약속을 한 문장으로 연결했습니다.
- 소제목 수정: `Windows 11에서 Hands-Free가 따로 안 보이는 이유`를 ``Stereo`와 `Hands-Free`가 하나로 합쳐진 Windows 11`로 바꿔 화면 차이를 바로 드러냈습니다. `별도 마이크가 가장 빠른 해결`은 독립 검수 뒤 `별도 마이크로 첫 원인을 가르는 방법`으로 낮춰 썼습니다.
- 문단 연결 수정: Windows 10의 분리 장치 안내에서 Windows 11 통합 입출력으로 이어지는 대조를 앞세우고, Discord 입력 변경 뒤 게임 자체가 마이크를 다시 열 수 있는 예외로 연결했습니다.
- 긴 문장 수정: LE Audio 조건을 운영체제·빌드와 하드웨어·드라이버 조건 두 문장으로 나눴습니다.
- 남은 문체·근거 위험: 특정 제품에서 같은 설정이 성공한다고 보장할 수 없으므로 공식 문서 기반 한계와 화면 차이를 유지했습니다.

## 독립 source 검수와 수정

| 회차 | 발견한 문제 | 반영한 수정 | 재검증 |
|---|---|---|---|
| 1 | HFP 전환을 블루투스 마이크 사용으로만 좁혀 통신용 출력 스트림 조건을 해결 절차에서 누락 | 도입·30초 진단·Discord 절·brief·evidence를 두 조건 분리 흐름으로 고치고, 별도 마이크를 해결 보장이 아닌 첫 테스트로 변경 | 문체 분석·bundle 검사 뒤 독립 재검수에서 두 조건 확인 |
| 1 | 근거가 없는 2.4GHz USB 동글 헤드셋 구매 대안 | 선택표에서 해당 행 삭제 | 본문과 evidence의 대안 범위 대조 통과 |
| 1 | LE Audio 메뉴의 한국어 표기와 영문 스크린샷 설명 불일치 | `LE 오디오`, `스테레오(채널 2개)`로 맞추고 영문 공식 화면임을 본문에 명시, 한국어 문서 스냅숏 2개 보존 | 스냅숏 해시와 UI 라벨 독립 재검수 통과 |
| 2 | Windows 11 통합 입출력 설명과 증상표 두 곳이 다시 마이크 조건만으로 축약됨 | 두 곳 모두 `앱의 입력 장치와 통신용 출력`을 확인하도록 일치시킴 | `/root/source_review` 독립 source 검수 최종 `pass` |

## 미디어 판단

- 생성형 리드: `1장`, source pass 뒤 생성 완료·독립 검증 대기
- 공식 UI 스크린샷: `2장`, Discord 입력 장치와 Windows LE Audio 스테레오 형식
- 인포그래픽: `없음`, A2DP·HFP 관계는 본문 표로 충분함
- 배제한 화면: Windows 기본 소리 화면, 장치 관리자, 레거시 제어판은 첫 해결에 불필요하거나 환경별 차이가 큼

### 생성형 대표 이미지 후보

- 후보: `assets/bluetooth-audio-profile-switch.png` (`1672 x 941`, SHA-256 `8e95c10c1ed5ec8534f4aae0fd09aa68551fa440ad6b3a400a1c02e336e0ba2a`)
- 배치: 표준 인사와 문제 제기 뒤, 본문 첫 소제목 앞
- 대체 텍스트: 두 개의 넓은 음향 리본이 무선 이어폰에서 나와 좁은 통로를 지나 하나로 압축되는 장면
- 인식 단서: 무선 이어폰 한 쌍에서 나온 두 개의 넓은 음향 리본이 좁은 금속 통로를 지나 하나의 가는 리본으로 줄어드는 모습
- 최종 프롬프트: `Korean Tistory technology hero for an editorial article. A pair of unbranded realistic true-wireless earbuds rests on pale sandblasted aluminum. Two broad woven acoustic ribbons, one cobalt blue and one warm amber, flow out from the earbuds and compress through a narrow brushed-metal collar into one thin muted ribbon. Use this tactile physical metaphor for high-quality stereo audio switching to constrained call audio. Wide 16:9 composition, left-center focal subject, soft daylight, restrained enterprise campaign palette, generous negative space. No text, logos, UI, arrows, neon, circuit-board motifs, or brand resemblance.`
- 생성 직후 육안 확인: 풀사이즈에서 이어폰·리본·금속 통로의 접촉과 재질이 자연스럽고 문자·로고·UI가 없습니다. 축소했을 때도 `두 갈래의 넓은 리본 → 좁은 통로 → 한 갈래` 관계가 남습니다. 작은 이어폰 그릴 표현은 독립 검수에서 결함 여부를 다시 확인합니다.
- 독립 검수 1차: `/root/hero_review`가 콘셉트·구도·썸네일 인식은 통과로 보았지만, 아래쪽 이어버드 스템 끝의 검은 글리프와 금색 구멍을 국소 생성 흔적으로 판정해 `targeted_edit`를 요청했습니다.
- 국소 편집: 두 흔적만 주변과 같은 무광 은색 표면으로 복원하고 구도·리본·조명·그림자는 유지했습니다. 초안은 `artifacts/captures/generated/bluetooth-audio-profile-switch-v1.png`에 보존했습니다.
- 독립 재검수: `/root/hero_review`가 최종 SHA-256 `8e95c10c1ed5ec8534f4aae0fd09aa68551fa440ad6b3a400a1c02e336e0ba2a`를 확인했습니다. 풀사이즈에서 두 흔적이 사라졌고, `360 x 202`·`220 x 124` 썸네일에서도 이어폰과 두 색 리본의 압축 관계가 유지돼 최종 `pass`를 받았습니다.

### 게이밍 장면 대표 이미지 v2 후보

- 사용자 피드백: 기존 이미지는 원리 은유가 강해 게임·Discord 검색 독자가 기대하는 장면이 바로 보이지 않음
- 후보: `assets/bluetooth-gaming-voice-chat-hero-v2.png` (`1672 x 941`, SHA-256 `15fe8b7f4d4fc3dc45eca765c6b016825495836f0913961edc04872f76633b41`)
- 배치: 표준 인사와 문제 제기 뒤, 본문 첫 소제목 앞
- 대체 텍스트: 게임 화면과 음성 채팅 참가자 표시가 보이는 PC 책상 앞에 무선 이어폰과 마이크가 놓인 모습
- 인식 단서: 전경의 무선 이어폰, 멀티플레이 게임 화면 가장자리의 음성 참가자 원형 표시, 기계식 키보드와 데스크톱 마이크
- 최종 프롬프트: `Use case: ads-marketing. Asset type: wide 16:9 hero image for a Korean technology troubleshooting article. Create a convincing editorial photograph of a real home PC gaming session where Bluetooth earbuds and voice chat are immediately recognizable. Place a pair of unbranded true-wireless earbuds in an open charging case as the sharp foreground subject. In the background, show a coherent multiplayer action game with a small brand-neutral vertical voice-chat participant strip made of circular portraits and subtle activity rings, plus a compact mechanical keyboard, mouse, partial controller, and small desktop microphone. Use a low desk-level three-quarter view, controlled asymmetry, plausible muted indigo monitor light and soft warm desk-lamp edge light, graphite and charcoal materials, believable microtexture and contact shadows. No logos, trademarks, brand names, readable text, watermark, fake storefront, floating panels, RGB rainbow, cyberpunk neon, pseudo-writing, duplicated peripherals, or resemblance to a specific commercial earbud design.`
- 생성 방식: OpenAI 내장 이미지 생성, 신규 방향으로 생성해 기존 후보를 덮어쓰지 않음
- 생성 직후 육안 확인: 무선 이어폰이 전경의 첫 초점이고, 게임 화면·참가자 원형 표시·마이크·키보드가 한 장면에서 읽힙니다. 로고와 읽을 수 있는 문자는 없습니다. 이어버드·충전 케이스 형상, 게임 화면 인물, 주변 기기의 세부 결함과 썸네일 주제 인식은 독립 검수에 넘깁니다.
- 독립 검수: `/root/hero_review`가 원본과 `360 x 202`·`220 x 124` 썸네일을 확인했습니다. 전경 이어폰과 게임 화면·원형 음성 참가자 표시·마이크가 함께 남아 검색 주제가 즉시 읽히고, 로고·문자·특정 앱 복제나 차단할 생성 결함이 없어 최종 `pass`를 받았습니다.
- 최종 선택: 사용자 피드백을 반영해 v2를 대표 이미지로 채택하고, 기존 물리적 은유 후보는 번들에 보존하되 게시 미디어에서는 제외했습니다.

## 문장 밀도 재편집

- 사용자 피드백: 설명은 빠지면 안 되지만 같은 결론을 여러 문단에서 되풀이하는 글은 읽기 어렵습니다.
- 수정 전 진단: `107개` 문장, 평균 `34.4자`, `50자 초과 20개`. 별도 마이크·통신용 출력·게임 음성 채팅 확인이 해결 절과 마지막 표·결론에서 반복됐습니다.
- 구조 수정: Windows 11의 통합 장치 설명을 A2DP·HFP 원리 절에 합치고, 해결 순서를 `증상 확인 -> 원리 -> Discord 입력 -> 가능한 선택 -> LE Audio -> 증상표`로 정리했습니다.
- 문장 수정: 한 문장에는 한 판단만 남기고, 출처 소개와 한계 문장은 해당 판단 옆에 붙였습니다. 마지막 문단의 해결 순서 반복은 삭제하고 기술적 한계만 남겼습니다.
- 보호한 내용: HFP 전환의 두 조건, 8kHz·16kHz, Windows 11 통합 입출력, Discord 입력 경로, LE Audio의 Windows·하드웨어 조건, 공식 링크와 실제 기기 테스트 한계는 유지했습니다.
- 현재 상태: source-level 재검증 대기
- 독립 검수 1차: 실제 기기 미측정 한계가 공개 본문에서 빠졌고, LE Audio 지원과 마이크 중 스테레오 조건이 합쳐졌으며, 세 진단 문장이 근거보다 단정적이어서 `revision_required`
- 수정: 미측정 한계를 한 문장으로 복원하고, LE Audio와 스테레오 지원을 분리했으며, 진단을 `설명하기 어렵습니다`·`가능성이 큽니다`·`다시 비교하세요`로 한정
- 재검증: `/root/concise_review` 독립 검수 `pass`. 실기기 미측정 한계, LE Audio 지원과 마이크 중 스테레오 조건의 분리, 진단 표현의 근거 범위를 확인했습니다.

## 현재 상태

- 원고 상태: `reviewing`
- source-level 독립 검수: `/root/expert_structure_review` 최종 `pass`
- source freeze: 새 정보 구조의 article·brief·evidence hash로 `artifacts/qa-v2/source-pass.json` 갱신 완료
- 대표 이미지 경로 변경 후 source freeze 재검증: `/root/source_review`가 본문 body·brief·evidence 동일성을 확인해 새 경로로 기록 갱신
- 대표 이미지 독립 검수: 사용자 요청으로 게이밍 장면 v2를 새로 생성, `/root/hero_review` 최종 `pass`
- 로컬 미디어·반응형 preflight: v2 checker `pass`, light/dark 로컬 렌더 완료
- `1280 x 900`: 문서 가로 넘침 없음, 본문·표·대표 이미지·공식 화면이 콘텐츠 폭 안에 표시됨
- `360 x 800`: 문서 전체 가로 넘침 없음, 본문 폭 `320px`, 대표 이미지는 폭에 맞춰 축소됨
- 모바일 표: 각 `620px` 너비를 표 내부에서만 가로 스크롤하며 본문 순서를 해치지 않음
- Discord 공식 화면: `640px` 내부 폭과 `320px` 보이는 영역, `INPUT DEVICE` 라벨이 첫 화면에서 읽힘
- Microsoft 공식 화면: `720px` 내부 폭과 `320px` 보이는 영역, 가로 스크롤 뒤 `2 channels` 값을 읽을 수 있음을 확인함
- 다크 모드: 배경 `rgb(30, 31, 33)`, 본문 `rgb(245, 245, 247)`, 링크와 캡션의 대비 및 이미지 경계 이상 없음
- 게이밍 대표 이미지 v2 교체 preflight: light/dark `1280 x 900`에서 `916px`, `360 x 800`에서 `320 x 181px`로 표시되고 문서 가로 넘침이 없었습니다. 썸네일에서도 이어폰·게임 화면·음성 참가자·마이크가 남으며 캡션 대비가 유지됩니다.
- Tistory CDN URL: 사용자 제공 URL 3개를 stable media ID에 연결 완료
- 원격 미디어 기준선: `/root`가 3개 파일의 HTTP 200, PNG 형식, 크기와 프레임을 기록해 `pass`
- 이전 final light/dark 페이지 QA: 본문 재편집으로 무효화하고 새 후보를 다시 캡처함
- 최종 페이지 확인: 원격 이미지 3장 로딩·가독성, 단일 H1, 고유 TOC, 문서 가로 넘침 없음, 캡션 결합, 목록 간격, 표·미디어 내부 스크롤, 다크 대비와 이미지 배경을 모두 통과
- 최종 fragment 확인: H1 `0`, 미해결 placeholder `0`, 로컬 경로 `0`
- 이전 source pass: `/root/concise_review`의 `pass` 기록은 이번 정보 구조 재편집으로 무효화됨
- 이전 최종 페이지 QA: TOC 6개 후보의 기록은 이번 재편집으로 무효화됨
- 현재 source pass·최종 페이지 QA: 새 정보 구조 기준으로 모두 재생성 완료

## 정보 구조 재리팩터링

- 사용자 피드백: 목차만 봐도 정보가 많아 보이고, 무엇부터 해야 하는지 바로 알기 어려웠습니다.
- 제목 수정: `이유와 해결 순서`를 덜어 내고 검색 상황과 해결 약속만 남겼습니다.
- 구조 수정: 소제목을 `6개`에서 `3개`로 줄이고 `Discord 입력 -> Discord 출력 -> LE Audio 지원` 순서로 바꿨습니다.
- 첫 화면 수정: Discord 입력 장치에서 별도 마이크를 고르라는 답과 메뉴 이름을 대표 이미지보다 먼저 배치했습니다.
- 제거한 반복: 별도 증상 확인 절, 선택지 표, 마지막 증상표를 삭제하고 필요한 분기만 각 해결 단계에 붙였습니다.
- 보호한 내용: HFP 전환의 입력·출력 조건, 8kHz·16kHz 모노, Windows 11 통합 장치, Discord 메뉴 경로, LE Audio의 빌드·하드웨어·드라이버 조건, 실기기 미측정 한계를 유지했습니다.
- 수정 전 분석: 소제목 `6개`, 문장 `81개`, 평균 `27.8자`, 50자 초과 `5개`.
- 수정 후 분석: 소제목 `3개`, 문장 `76개`, 평균 `25.9자`, 50자 초과 `4개`.

| 구간 | 주 역할 | 보조 역할 |
|---|---|---|
| 도입 | 진단·첫 행동 | 근거 범위 |
| Discord 입력 변경 | 행동 | 성공 확인·게임 예외 |
| Discord 출력 확인 | 행동 | 통신용 출력 조건 |
| LE Audio 확인 | 행동 | 지원 조건·메커니즘·기술적 한계 |

- 독립 source 검수 1차: 소제목 `두 곳만 더 확인`이 실제 분기를 숨기고, 중요한 선택 기준이 글 끝에 묻혀 있어 `revision_required`
- 수정: 목차 자체를 `입력 변경 -> 출력 확인 -> LE Audio 확인` 순서로 바꾸고, 별도 마이크가 없을 때의 두 선택을 도입부로 이동
- 독립 source 재검수: `/root/expert_structure_review`가 제목·목차의 행동 순서와 필수 기술 조건을 대조해 `pass`
- 새 final light/dark 페이지 QA: `/root/final_page_review`가 `1280 x 900`·`360 x 800` 두 테마에서 즉시 행동 문장, TOC 3개, 번호형 제목 래핑, 절차 목록, 표·이미지 내부 스크롤과 다크 대비를 확인해 `pass`
