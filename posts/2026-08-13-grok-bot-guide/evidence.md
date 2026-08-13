# 근거 지도: Grok Bot 사용법, 일론 머스크의 애착 에이전트

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Grok Bot은 전용 클라우드 컴퓨터에서 앱·웹사이트를 조작하고 완료된 작업을 가져오는 초기 베타 제품이다. | 공식·Codex 화면 관찰 | 확인 | `https://x.ai/bot`, `https://x.ai/news/introducing-grok-bot`, 2026-08-13 DOM·화면 캡처 | 독립 성공률 검증 아님 |
| C02 | 일반 Grok 대화, Grok Automations, Grok Bot은 각각 단발 답변, 일정·이메일 조건 실행, UI를 통한 다단계 작업에 초점이 다르다. | 공식 문서 비교 | 확인 | Grok 제품 페이지, Automations 출시 글, Bot 출시 글 | 기능 경계는 베타 업데이트로 바뀔 수 있음 |
| C03 | 공식 활용 사례 페이지에는 56개 사례와 9개 분류가 표시된다. | Codex 화면 관찰 | 확인 | `https://x.ai/bot/use-cases`, 2026-08-13 DOM | 현재 페이지의 사례 수일 뿐 사용 가능 앱 전체가 아님 |
| C04 | 공식 사례는 영업·마케팅·지원·채용·재무·제품·엔지니어링·개인 업무를 포함한다. | 공식·Codex 화면 관찰 | 확인 | use cases 전체 DOM | 벤더가 제시한 가능 사례이며 성능 증거 아님 |
| C05 | 전송·캠페인 조정·예약 같은 외부 영향 행동은 공식 예시에서 승인 단계와 함께 설명된다. | 공식·Codex 화면 관찰 | 확인 | Sales Outbound, Paid Media, Travel Coordinator, Inbox Manager 사례 | 모든 행동의 기본 승인 정책을 뜻하지 않음 |
| C06 | 현재 이용 대상은 Cursor Ultra, SuperGrok Heavy, Cursor Premium Teams 구독자다. | 공식 FAQ·출시 글 | 확인 | `https://x.ai/bot`, 2026-08-13 FAQ | 지역·계정별 제공 여부와 이후 변경 가능 |
| C07 | 지원 표면은 macOS Apple Silicon·Intel, Windows 10·11 x64, iOS이며 Android는 Coming soon이다. | 공식 다운로드 UI | 확인 | `https://x.ai/bot`, More downloads 모달 | 2026-08-13 상태 |
| C08 | Bot은 로그인이 필요하면 Computer 화면에서 사용자에게 로그인을 요청할 수 있고, 한 번 따라온 절차를 Routine으로 저장할 수 있다. | 공식 제품 페이지 | 확인 | works where you work, show a Bot how it’s done 카드 | 실제 앱에서 재현하지 않음 |
| C09 | 여러 Bot은 협업·인계할 수 있지만 한 사용자 단위의 지속형 클라우드 컴퓨터, 파일, 브라우저 로그인을 공유한다. | 공식 FAQ | 확인 | Do Bots share one computer? 답변 | 팀·엔터프라이즈 격리 정책 전체는 확인하지 않음 |
| C10 | 가격 표는 Cursor Ultra 월 $200, Cursor Premium Teams 좌석당 월 $120이며 포함 사용량 이후 추가 토큰 비용 가능성을 안내한다. | 공식 가격·FAQ | 확인 | `https://x.ai/bot`, 2026-08-13 | 세금·환율·지역·프로모션 미포함, 변경 가능 |
| C11 | 공식 페이지는 암호화, 학습 제외 선택, 민감 행동의 Auto Review를 보안 수단으로 안내한다. | 벤더 주장 | 확인 | Bot privacy FAQ | 설정별 기본값과 독립 보안 검증은 확인하지 않음 |
| C12 | 공개된 가입 화면 캡처에는 카드 등록이 필요한 7일 무료 체험, 전체 기능, 제한된 사용량, 별도 구독 전 미청구 조건이 표시된다. | 제3자 공개 카드의 가입 화면 캡처 + 공식 로그인 진입 관찰 | 부분 확인 | `artifacts/sources/web/instagram-reference-free-trial.png`, `artifacts/sources/web/grok-bot-onboarding-login.png`, `https://www.instagram.com/p/Db-PtJSGjiu/`, `https://cursor.com/bot/onboarding?product=grok-bot`, 2026-08-14 | 로그인 이후 원본 trial 화면을 독립 재현하지 못했고 계정·지역별 제공 차이 가능 |
| C13 | ‘애착 에이전트’는 공식 명칭이 아니며 공식 출시 글은 일론 머스크 개인 사용을 말하지 않는다. | 공식 원문 부재 경계 | 확인 | 제품 페이지·출시 글의 명칭과 본문 | 별칭의 유통 경로 전체를 검증한 것은 아님 |
| C14 | Grok Bot onboarding URL은 Cursor 로그인 화면을 열며 이메일 입력, Google·GitHub·Apple 로그인, SuperGrok Heavy의 Grok 계정 연결 선택지를 보여 준다. | 공식 로그인 화면·Codex 관찰 | 확인 | `artifacts/sources/web/grok-bot-onboarding-login.png`, `https://cursor.com/bot/onboarding?product=grok-bot`, 2026-08-14 | 로그인 이후 trial·결제 화면은 확인하지 않음 |

## 직접 검증 설계

- 질문: 처음 쓰는 독자가 공식 페이지에서 Grok Bot의 정체, 이용 조건, 맡길 일, 승인 경계를 찾을 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: macOS, Codex 인앱 브라우저, 1280×720, 2026-08-13
- 입력: `https://x.ai/bot`, `/bot/use-cases`, `/news/introducing-grok-bot`, Grok Bot onboarding 로그인 진입, 사용자 지정 참고 카드
- 전처리 또는 표현: 화면 DOM을 읽고 공식 UI를 1280×720 PNG로 캡처
- 비교·판정 규칙: 같은 주장을 제품 페이지, 출시 글, 활용 사례·FAQ 중 가능한 두 표면에서 대조. 7일 체험은 제3자 공개 카드의 가입 화면 문구와 공식 onboarding 로그인 진입을 구분해 기록
- 성공 기준: 본문의 모든 강한 주장에 공식 화면 또는 원문 근거가 있고 앱 실행 여부를 정확히 밝힘
- 반복 횟수와 표본 크기: 공식 페이지 3개, FAQ 7개 중 관련 6개, 활용 사례 56개 목록 관찰
- 보존할 원자료: `artifacts/sources/web/*.png`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 제품 첫 화면 | 초기 베타, 전용 컴퓨터, 도구 로그인, macOS 다운로드 확인 | `artifacts/sources/web/grok-bot-landing-hero.png` | 공식 기능 소개 |
| E02 | 활용 사례 첫 화면·전체 DOM | 56개 사례, 9개 분류와 대표 역할 확인 | `artifacts/sources/web/grok-bot-use-cases-featured.png` | 벤더 제시 사례 |
| E03 | 작동 방식 카드 | 로그인 요청, workflow 시연, Routine 학습 설명 확인 | `artifacts/sources/web/grok-bot-workflow-cards.png` | UI 데모 설명 |
| E04 | Sales Outbound 사례 모달 | 초안 생성 뒤 사람이 전송을 승인하는 예시 확인 | `artifacts/sources/web/grok-bot-launch-sales-outbound-modal.png` | 영업 사례 한 건 |
| E05 | Grok Bot onboarding URL | Cursor 로그인과 이메일·Google·GitHub·Apple·Grok 연결 선택지 확인 | `artifacts/sources/web/grok-bot-onboarding-login.png` | 로그인 진입만 확인, trial 화면 미확인 |

## 실패와 반례

- 실패한 입력: 없음. 공개 페이지는 로그인 없이 열렸습니다.
- 예상과 달랐던 결과: 사용자 표현의 `X에서 쓰는 Bot`과 달리 시작 위치는 X 앱이 아니라 별도 Grok Bot 앱·제품 페이지였습니다.
- 일반화하면 안 되는 범위: 공개 제품 데모만으로 앱 내부 세부 클릭, 외부 서비스 연결 성공률, 장기 실행 안정성, 실제 토큰 비용을 단정하지 않습니다.

## 미해결 항목

- 실제 앱과 계정 연결 검증은 글의 약속에서 제외하고 첫 화면과 마지막 한계에 명시합니다.
- 7일 체험은 계정·지역별 차이를 확인하지 못했으므로 가입 화면에서 종료일·청구 조건을 재확인하도록 본문에 적습니다.

## 출처 메모

- `x.ai/bot`: 제품 정체, 작동 방식, 가격, 기기, 이용 대상, 공유 컴퓨터·보안 FAQ.
- `x.ai/news/introducing-grok-bot`: 2026-08-11 출시일, 초기 베타, 내부 사용 사례, 이용 대상.
- `x.ai/bot/use-cases`: 역할별 활용 범위와 승인 문구. 사례는 벤더 제안이지 독립 검증이 아닙니다.
- `x.ai/news/grok-automations`: Bot과 혼동하기 쉬운 일정·이메일 트리거형 자동화의 공식 범위.
