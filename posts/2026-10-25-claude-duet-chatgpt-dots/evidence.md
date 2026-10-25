# Claude Duet과 ChatGPT Dots, AI에게 계속 업무를 맡기는 방법

확인일: 2026-10-25 Asia/Seoul. 조사 주체: Codex. 실제 제품 계정·화면·작업 실행을 검증하지 않았습니다. 웹 도구로 공식 원문을 열어 문장을 확인했고, 검색 요약은 사실 확정에 사용하지 않았습니다.

| 주장 | 원문·근거 | 상태와 한계 |
|---|---|---|
| Duet 10월 21일 연구 프리뷰 | https://claude.com/resources/articles/claude-duet / https://support.claude.com/en/articles/12138966-release-notes | 날짜가 일치합니다. 미국 Pro·Max 대기 명단입니다. |
| Duet 별도 모바일 앱, 웹, Claude 계정 재사용 | https://claude.com/product/claude-duet / https://claude.com/resources/articles/claude-duet | 기존 기억·스킬·연결 앱을 가져옵니다. Claude Code 작업 인계는 문서에서 미확인입니다. |
| Duet 시작·Tasks·Make | https://support.claude.com/en/articles/17631495-get-started-with-claude-duet | 대기 명단 이메일·계정 일치 필요. Tasks는 진행, Make는 완성 파일입니다. |
| Duet 확인 주기·부재 중 실행 | https://claude.com/resources/articles/claude-duet | 자체 클라우드 VM·브라우저, 기기가 켜져 있을 필요 없음. every few hours. 정확한 SLA는 없습니다. |
| Duet 보호·승인 | https://claude.com/resources/articles/claude-duet-safety-privacy-and-security | 10월 23일 후속. 행동 심사·민감정보 검사·인증정보 분리·외부 침투 시험은 회사 설명입니다. 검사 누락·오탐도 명시합니다. 세부 승인 면제는 변화 중이므로 매번 승인이라는 절대 표현을 피했습니다. |
| Duet 앱 해제·메모리 | 같은 안전 문서 | 새 접근만 중단. 이전 정보는 메모리 초기화가 필요합니다. 일괄 정지 UI는 미확인입니다. |
| Duet 비용과 조건 | 시작 도움말의 Pricing and usage limits | 추가 요금 없이 Pro·Max 기존 한도, 백그라운드 포함, 5시간·주간 한도. 초대 시 한도 초기화 1회는 11월 30일까지이나 본문에서는 기간 의존성이 큰 부차 정보를 제외했습니다. |
| Microsoft 365 상충 | 제품 페이지 로고 / 시작 도움말 Limitations | 제품 페이지에는 로고가 있으나 도움말은 Microsoft 365 isn't available yet라고 명시합니다. 문장으로 된 제한을 우선하고 충돌 자체를 본문에 공개했습니다. |
| Claude Code 관계 | https://claude.com/product/claude-code | 버그 수정·테스트·개발 작업 제품. Duet이 Code의 기능이라는 설명은 하지 않습니다. |
| 기존 Claude 예약·부재 중 실행 | Claude 릴리스 노트 7월 7일 | 기존 제품에도 자동화가 있음을 분명히 했습니다. |
| Dots 소개일 | https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026 / https://learn.chatgpt.com/docs/whats-new/devday-2026 | 첫 링크는 주간 범위만 명시. 별도 DevDay 원문에 September 29, 2026 명시. 소개일을 근거 없이 9월 28일로 고정하지 않았습니다. |
| Dots의 현재 정체·접근 조건 | https://learn.chatgpt.com/docs/dots | OpenAI의 ChatGPT 개인 에이전트. Pro 100/200/500, over 18, EEA/UK/Switzerland 제외. Business Premium worldwide, Enterprise worldwide/off by default. 단계적 배포입니다. 한국은 지역 조건상 포함이라는 해석이며 계정 활성화 보장은 없습니다. |
| Dots 대화·Work·Codex 한도 | https://learn.chatgpt.com/docs/dots#access | 대화는 ChatGPT 한도에 미포함. 시작/관리한 Work·Codex 작업은 해당 제품 한도에 포함. deeper work allowance·첫 달 expanded limits 안내만 있고 정량 수치는 없습니다. 과금 0 또는 무제한으로 단정하지 않습니다. |
| 설정·사건 감시 | https://learn.chatgpt.com/docs/dots/getting-started | 이메일·캘린더·파일 앱 플러그인 연결. 연락수단과 앱·컴퓨터 연결은 별개. 서비스가 지원하는 이벤트만 가능. 설정 확인을 요청합니다. |
| 지속 작업·위임·예약 | https://learn.chatgpt.com/docs/dots/tasks-and-memory | 멈춤·재개 시점 판단, Work·Codex 작업 위임, 사건/일정 기반 작업. 반복 일정은 저장·확인 필요. 연결만으로 감시 시작하지 않습니다. |
| 로컬과 클라우드 | https://learn.chatgpt.com/docs/dots/computers-and-apps | 클라우드는 기기 꺼져도 작업, 로컬은 온라인+ChatGPT 앱 필요, Codex cloud 환경 사전 구성. 브라우저 Take over 가능. |
| 승인·중단 | https://learn.chatgpt.com/docs/dots/controls | 지시·권한·규칙·기본 안전 요건 자동 심사. 범위 내 향후 행동 허용 가능. Pause=main, Activity=delegated, Scheduled=recurring. 완료된 행동은 되돌리지 않음. |
| 후속 업데이트 | https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026 / https://learn.chatgpt.com/docs/whats-new | 10월 9일 모바일 생성·플러그인, 목록 최신 10월12~16일 위젯·Shortcuts. 공개 전체에 후속 업데이트가 없다는 단정은 하지 않습니다. |
| 사례 구분 | Duet 발표의 Mya 사례 / Dots 개요 Ways to work with your dot | 전자는 회사가 소개한 초기 사용자 사례입니다. 회의 준비 요청은 가상 시나리오로 명시했습니다. Dots 출시 자료·코드 후속 조사는 공식 활용 예시입니다. |

## 원문 보관과 접근 한계

- learn.chatgpt.com은 .md 원문을 직접 내려받아 artifacts/sources에 보관했습니다. HTML 원문도 웹 도구로 열었습니다.
- Claude 원문은 웹 도구에서 본문을 읽었지만 별도 urllib 보관 요청은 403을 받았습니다. fetch-receipt.json은 그 실패를 그대로 보존합니다. 403을 제품 미출시 또는 원문 열람 실패로 확대하지 않습니다.
- 1Password는 coming soon으로 남아 있으므로 현재 기능 목록에 넣지 않았습니다.
- 독립 안전성 비교·계정별 활성화·실제 작업 성능·지연·백그라운드 정량 비용은 확인하지 못했습니다.

## 독자 판단 체계

질문·예약·책임의 차이를 작업 시작 조건, 후속 확인, 허용 행동, 결과 검토로 나눴습니다. 우열이나 구독 전환은 제안하지 않습니다. 한국 독자에게는 현재 대상 계정 여부를 첫 도입 조건으로 둡니다.

## 미디어 관련 주장

| ID | 메시지 | 근거 | 제한 |
|---|---|---|---|
| C-duet-screen | Tasks에서 Ready for review·Needs input·Working 상태를 구분합니다. | https://claude.com/resources/articles/claude-duet-safety-privacy-and-security 의 작업 목록 이미지 | Anthropic이 공개한 예시이며 실제 작성자 계정을 사용한 결과가 아닙니다. 원본에서 왼쪽 Tasks 화면만 잘랐습니다. |
| C-dots-screen | Dots가 대화 사이에 업무를 이어가고 무엇을 지켜보며 언제 알릴지 사용자에게 요청합니다. | https://learn.chatgpt.com/docs/dots#how-dots-work 의 대화 예시 | OpenAI가 만든 소개용 예시를 인앱 브라우저로 캡처했습니다. 실제 계정 대화가 아닙니다. |

## 후속 이용 조건 재확인

2026-10-25(한국 시간)에 Codex가 Duet 발표·시작 도움말, Dots 개요의 Access와 사용량, ChatGPT 최신 업데이트 원문을 다시 열었습니다. 미국 Pro·Max 대기 명단 연구 프리뷰와 Dots 적격 요금제·지역·배포 방식, 두 제품의 사용량 안내는 본문과 일치했습니다. 확인한 업데이트 목록의 최신 항목은 10월 12~16일입니다. 별도 계정의 접근 가능 여부를 검증한 것은 아닙니다.
