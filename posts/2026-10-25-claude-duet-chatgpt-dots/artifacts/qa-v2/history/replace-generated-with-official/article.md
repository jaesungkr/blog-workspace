---
title: "Claude Duet과 ChatGPT Dots, AI에게 계속 업무를 맡기는 방법"
slug: claude-duet-chatgpt-dots
date: 2026-10-25
category: "Log"
subcategory: "AI 개념 · 실전"
status: reviewing
format: rich-post-v2
tags: [Claude Duet, ChatGPT Dots, AI 에이전트, 업무 자동화]
summary: "회의 준비를 예로 들어 Duet과 Dots의 지속적인 업무 위임, 승인과 중단, 한국 이용 조건과 사용량을 공식 문서로 비교합니다."
hero_image: assets/claude-duet-chatgpt-dots-hero-v2.png
published_url: ""
sources:
  - https://claude.com/resources/articles/claude-duet
  - https://claude.com/product/claude-duet
  - https://support.claude.com/en/articles/17631495-get-started-with-claude-duet
  - https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
  - https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026
  - https://learn.chatgpt.com/docs/whats-new/devday-2026
  - https://learn.chatgpt.com/docs/whats-new
  - https://learn.chatgpt.com/docs/dots
  - https://learn.chatgpt.com/docs/dots/getting-started
  - https://learn.chatgpt.com/docs/dots/tasks-and-memory
  - https://learn.chatgpt.com/docs/dots/controls
  - https://learn.chatgpt.com/docs/dots/computers-and-apps
---

안녕하세요. dev.log입니다.

내일 회의를 준비하려면 지난 회의록을 읽고, 메일에 들어온 수정 요청과 바뀐 일정을 대조해야 합니다. AI에게 자료를 정리해 달라고 한 뒤에도 새로운 메일이 오면 다시 확인을 요청하게 됩니다. 이때 “회의 전까지 변경 사항을 계속 확인하고, 결정할 일이 생기면 알려줘”라고 맡길 수 있다면 사용자가 직접 챙기는 일은 어떻게 달라질까요?

Claude Duet은 연결된 업무 앱을 살피고 자료와 다음 행동을 준비하는 Anthropic의 별도 앱입니다. ChatGPT Dots는 ChatGPT 안에서 만드는 개인 에이전트로, 계속 맡겨둔 일을 관리하며 필요한 작업을 ChatGPT Work나 Codex에 나눠 맡길 수 있습니다. 여기서 **에이전트**란 요청을 읽고 필요한 자료와 도구를 골라 여러 단계를 수행하는 AI를 뜻합니다. 두 제품은 그 작업을 대화 사이에도 이어가도록 설계됐습니다. [Duet 제품 소개](https://claude.com/product/claude-duet), [Dots 소개](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026)

정보 확인 기준일은 **2026년 10월 25일**입니다. Duet은 미국에서 대기 명단을 통해 제공하는 연구 프리뷰이고, Dots는 대상 계정에 점진적으로 배포되고 있습니다.

{{media:duet-dots-hero}}

### Claude Duet은 어디에서 무엇을 하나요?

Anthropic은 10월 21일 Duet의 연구 프리뷰를 발표했습니다. iOS·Android에서는 기존 Claude 앱과 분리된 앱을 쓰고, 컴퓨터에서는 claude.ai에서 이용합니다. 기존 Claude 계정의 메모리, 스킬, 연결된 앱을 가져옵니다. 메모리는 이전에 공유한 정보를 기억해두는 기능이며, 스킬은 특정 업무를 수행하는 지침입니다. [공식 발표](https://claude.com/resources/articles/claude-duet)

시작하려면 [제품 페이지](https://claude.com/product/claude-duet)의 대기 명단에 Claude 계정 이메일로 신청하고 초대를 받아야 합니다. 이후 메일·캘린더처럼 필요한 앱을 연결하고, 텍스트를 입력하거나 음성으로 일을 요청합니다. 예를 들어 회의 상대 회사의 사전 자료를 부탁하면, Duet이 사용할 앱과 작업 단계를 정하고 클라우드 컴퓨터에서 자료를 준비합니다. 앱을 닫아도 작업은 이어집니다. 진행 상황은 **Tasks**, 완성된 파일은 **Make** 탭에서 확인하며, 완료되거나 판단이 필요하면 주 대화에 메시지를 보냅니다. [시작 안내](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)

Duet은 아침에 주요 업무를 요약하고, 낮에도 연결된 계정을 확인합니다. 사용자가 화면을 열어 기다리지 않아도 서버에서 처리하는 일을 **백그라운드 작업**이라고 합니다. Duet은 계정을 몇 시간 간격으로 확인하므로, 확인 사이에 들어온 긴급한 소식은 다음 확인까지 놓칠 수 있습니다. [공식 발표](https://claude.com/resources/articles/claude-duet)

[Claude Code](https://claude.com/product/claude-code)는 코드 수정·테스트 등 개발 작업을 맡기는 제품입니다. Duet은 메일과 일정 등 여러 업무를 살피는 용도이며, 공개 문서에는 기존 Claude Code 작업을 이어받는 기능이 명시돼 있지 않습니다.

### ChatGPT Dots는 ChatGPT 안에서 만드는 개인 에이전트

OpenAI의 Dots는 [9월 28일~10월 2일 업데이트](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026)와 **9월 29일자 DevDay 자료**에서 소개됐습니다. 사용자는 자신의 dot에 이름을 붙이고, “프로젝트 일정과 미응답 사항을 관리해줘”처럼 지속적인 책임을 맡깁니다. dot은 연결된 앱에서 자료를 찾고, 파일을 만들거나 일을 나눠 수행한 뒤 결과와 결정 요청을 가져옵니다. [DevDay 발표](https://learn.chatgpt.com/docs/whats-new/devday-2026)

Dots는 ChatGPT 안의 기능입니다. 모바일 앱·데스크톱 앱·데스크톱 웹에서 dots를 열고 이름과 외형을 정한 뒤 필요한 플러그인을 연결합니다. 플러그인은 외부 서비스의 자료와 기능을 쓰게 해주는 연결 수단입니다. **대화할 Slack 채널, 자료를 읽을 앱, 개인 컴퓨터는 각각 따로 연결합니다.** [설정 안내](https://learn.chatgpt.com/docs/dots/getting-started)

ChatGPT Work는 조사·분석·파일 제작 같은 작업을, Codex는 소프트웨어 개발을 맡기는 제품입니다. dot은 필요할 때 이들에 작업을 맡기고 후속 지시를 내릴 수 있습니다. 클라우드 작업은 사용자의 컴퓨터가 꺼져 있어도 진행됩니다. 로컬 파일이나 기존 로컬 Codex 작업을 사용하려면 개인 컴퓨터를 연결하고 ChatGPT 앱을 켜둬야 합니다. 클라우드 개발에는 저장소와 설정을 갖춘 Codex 환경이 필요합니다. [작업과 메모리](https://learn.chatgpt.com/docs/dots/tasks-and-memory), [컴퓨터 연결](https://learn.chatgpt.com/docs/dots/computers-and-apps)

10월 9일에는 모바일 앱에서 dot을 만들고 플러그인을 연결하는 기능이 소개됐고, 최신 업데이트 목록의 10월 12~16일 항목에는 iOS 위젯·Shortcuts 진입 기능이 실렸습니다. [10월 9일 업데이트](https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026), [최신 업데이트](https://learn.chatgpt.com/docs/whats-new)

### “내일 회의 준비를 도와줘”를 맡기는 세 가지 방식

다음은 차이를 설명하기 위한 가상 상황입니다. 일반 대화에서는 회의록과 메일을 주고 쟁점을 정리해 달라고 요청할 수 있습니다. 이후의 변경 사항을 계속 확인하려면 별도의 후속 요청이나 자동화 설정이 필요합니다. 기존 Claude에도 예약 작업이 있고 ChatGPT Work도 일정에 따른 실행을 지원합니다. [Claude 릴리스 노트](https://support.claude.com/en/articles/12138966-release-notes), [ChatGPT 기능 구분](https://learn.chatgpt.com/docs/dots)

예약 작업에는 “내일 오전 8시에 회의 자료를 정리해줘”처럼 실행 시간을 지정합니다. 지속적인 업무 위임에는 “회의까지 안건과 미응답 사항을 관리하고, 내 결정이 필요한 변화만 알려줘”처럼 관리할 대상과 판단 조건을 줍니다. AI가 먼저 필요한 소식을 전하는 **선제적 알림**도 이 조건에 맞춰 이해하면 됩니다.

Duet에는 캘린더와 관련 메일을 연결하고 회의 전 자료를 요청할 수 있습니다. Anthropic은 Duet이 고객 통화를 앞두고 자료를 준비하고, 비행 일정과 가깝다는 점을 발견해 시간 변경을 제안한 사례를 소개했습니다. 이는 회사가 제시한 초기 사용자 사례입니다. [발표 속 활용 사례](https://claude.com/resources/articles/claude-duet)

Dots에는 “내일 회의까지 안건과 미응답 사항을 관리하고, 한국 시간 오전 8시에 자료를 정리해줘. 결정이 필요하면 ChatGPT에서 알려줘”라고 맡길 수 있습니다. 연결된 서비스가 지원하면 “지정한 Slack 채널에 새 버그 보고가 올라올 때 조사해줘”처럼 사건을 계기로 실행하도록 요청할 수도 있습니다. 채널을 연결한 다음에는 무엇을 감시하도록 설정했는지 확인해야 합니다. [시작 안내](https://learn.chatgpt.com/docs/dots/getting-started)

공식 문서의 ‘상시 실행’은 대화 사이에도 업무를 이어가는 방식입니다. Duet은 주기적으로 계정을 확인하고, Dots는 필요할 때 멈췄다가 다시 작업할 시점을 정합니다. Dots의 정확한 확인 간격은 해당 문서에 공개돼 있지 않습니다. 두 문서는 중단 없는 추론을 약속하지 않습니다. [Duet 실행 방식](https://claude.com/resources/articles/claude-duet), [Dots 실행 방식](https://learn.chatgpt.com/docs/dots/tasks-and-memory)

### Duet과 Dots의 작업 방식 비교

공식 문서에서 확인한 기능과 제공 조건은 다음과 같습니다. 휴대폰에서는 표를 좌우로 밀어 두 제품의 내용을 모두 확인할 수 있습니다.

| 항목 | Claude Duet | ChatGPT Dots |
|---|---|---|
| 제품의 성격 | 별도 모바일 앱·웹 경험 | ChatGPT 안의 개인 에이전트 |
| 작업을 시작하는 계기 | 사용자 요청·아침 요약·주기적 계정 확인 | 사용자 요청·일정·지원되는 사건·후속 판단 |
| 지속 작업 | 클라우드에서 처리하며 몇 시간 간격으로 계정 확인 | 클라우드에서 후속 작업을 관리하고 Work·Codex에 위임 |
| 앱 연결 | Claude 계정의 커넥터·스킬 등을 사용 | 플러그인·연락 수단·개인 컴퓨터를 구분해 연결 |
| 알림 | 완료되거나 판단이 필요할 때 알림 | 정한 조건과 연락 수단에 따라 결과·결정 요청 전달 |
| 승인 | 전송·결제·서명·삭제 전에 승인하도록 설계 | 지시·권한·규칙을 자동 심사해 실행·승인·사용자 처리 결정 |
| 이용 단계 | 미국 Pro·Max 대상 대기 명단 연구 프리뷰 | 적격 계정에 점진적 배포 |
| 사용량 | 백그라운드 확인도 Claude 한도에 포함 | 대화와 위임한 Work·Codex 작업의 계산이 다름 |

표의 근거: [Duet 발표](https://claude.com/resources/articles/claude-duet), [Dots 작업 문서](https://learn.chatgpt.com/docs/dots/tasks-and-memory), [Dots 승인 문서](https://learn.chatgpt.com/docs/dots/controls)

### 맡긴 일을 확인하고 멈추는 방법

Duet은 전송·결제·서명·삭제 전에 내용을 보여주고 승인을 기다리도록 설계됐습니다. Tasks에서 진행 방향을 바꿀 수 있고, 연결된 앱을 해제하면 이후 접근이 중단됩니다. 이미 기억한 정보는 별도 메모리 초기화가 필요합니다. 전체 작업을 한 번에 멈추는 구체적인 조작법은 확인한 문서에 없습니다. [안전·개인정보 후속 설명](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)

Dots는 외부 계정이나 정보 공유에 영향을 주는 행동을 자동 심사합니다. 기존 지시와 권한에 따라 바로 수행하거나, 승인을 요청하거나, 사용자에게 단계를 넘깁니다. 특정 범위의 향후 행동도 지시로 허용할 수 있습니다. 고객 메시지는 항상 확인받도록 하는 등의 **Custom rules**를 추가할 수 있지만, 이 규칙도 실수 가능성이 있으며 기본 안전 요건을 해제하지 못합니다. [통제 문서](https://learn.chatgpt.com/docs/dots/controls)

Dots의 진행 상황은 데스크톱 프로필의 **Activity**, 예약 작업은 **Scheduled**에서 봅니다. **Pause**는 현재 주 작업을 멈춥니다. 따로 맡긴 작업은 Activity에서, 향후 예약 실행은 Scheduled에서 각각 중단해야 합니다. 중단해도 이미 보낸 메시지나 완료된 변경은 되돌아오지 않습니다. 클라우드 브라우저는 **Take over**로 직접 조작할 수 있지만, Duet 프리뷰는 브라우저 보기와 제어권 인수를 지원하지 않습니다. [Dots 통제](https://learn.chatgpt.com/docs/dots/controls), [Dots 브라우저](https://learn.chatgpt.com/docs/dots/computers-and-apps), [Duet 제한](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)

Anthropic은 10월 23일 별도 안전 설명에서 행동 심사, 민감정보 검사, 인증정보 분리와 외부 침투 테스트를 설명했습니다. 같은 문서는 보호 장치의 누락과 오탐 가능성도 인정합니다. 이 설명은 회사가 공개한 설계와 평가입니다. 이번 조사에서는 두 제품의 안전성을 비교한 독립 검증 자료를 확보하지 못했습니다. [Duet 안전 설명](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)

### 한국에서의 이용 조건과 사용량

Duet은 현재 미국 Claude 계정의 Pro·Max 가입자가 초대를 받아야 이용할 수 있습니다. 한국 계정은 대상에 포함되지 않고 Team·Enterprise도 아직 지원하지 않습니다. 프리뷰에는 추가 요금이 없으며, 아침 요약과 계정 확인도 기존 5시간·주간 사용량에 반영됩니다. [최신 도움말](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)

Dots는 18세 초과 Pro 100·200·500 사용자 중 유럽경제지역·영국·스위스 밖의 사용자를 대상으로 합니다. 한국은 이 지역 제한상 대상에 들어가지만, 실제 계정 활성화는 점진적 배포에 달려 있습니다. Business Premium·Enterprise는 전 세계 배포 대상으로 안내되며 Enterprise는 관리자가 켜야 합니다. Plus는 대상 목록에 없습니다. 모바일 앱·데스크톱 앱·데스크톱 웹을 지원하고 모바일 웹은 지원하지 않습니다. [현재 이용 조건](https://learn.chatgpt.com/docs/dots#access)

dot과의 대화는 ChatGPT 사용량 한도에 포함되지 않지만, 위임한 Work·Codex 작업에는 해당 제품 한도가 적용됩니다. 더 깊은 작업의 허용량과 출시 첫 달 확대 한도를 안내하지만, 정확한 수치와 확인 1회당 소모량은 공개하지 않았습니다. 구체적인 비용 계산에는 계정에 적용된 최신 한도가 필요합니다. [사용량 안내](https://learn.chatgpt.com/docs/dots#access)

### 회의 준비부터 개발 후속 점검까지

Duet은 회사 조사 자료와 일정 확인을, Dots는 회의 자료 준비와 후속 관리를 공식 예시로 제시합니다. 관련 메일·캘린더·문서를 연결하고 최종 안건과 공유할 내용을 검토하도록 요청할 수 있습니다. [Duet 업무 예시](https://claude.com/product/claude-duet), [Dots 소개 업데이트](https://learn.chatgpt.com/docs/whats-new/september-28-october-2-2026)

**프로젝트 변경 추적**은 출시 채널·기획서·발표 자료를 연결해 변경에 맞춘 문구와 슬라이드를 준비하는 Dots의 공식 예시입니다. **개발 후속 점검**도 피드백 출처와 코드 프로젝트를 연결해 문제를 조사하고 코드 리뷰용 수정안을 준비하는 사례가 있습니다. 병합 여부는 사람이 판단합니다. [Dots 활용 예시](https://learn.chatgpt.com/docs/dots)

메일·일정·청구서처럼 여러 업무 앱을 살피는 책임은 Duet의 공개 사례와 잘 맞습니다. Work·Codex에 업무를 나눠 맡기고 기존 로컬 Codex 작업도 이어가려는 개발자에게는 Dots의 위임 방식이 구체적으로 문서화돼 있습니다. 다만 Duet 제품 페이지의 Microsoft 365 로고와 달리 도움말은 아직 미지원이라고 명시하므로, 실제 연결 가능 여부는 도움말 조건으로 판단해야 합니다. [Duet 제품 페이지](https://claude.com/product/claude-duet), [현재 연결 제한](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)

지속적인 업무 위임에서는 요청에 관리 대상과 기간, 알림 조건, 허용할 행동을 함께 담게 됩니다. 사용자는 결과물을 검토하는 일에 더해, AI가 언제 다시 확인하고 어디까지 행동할지 정합니다. 한국에서 사용하려면 두 제품의 차이와 함께, 내 계정으로 지금 이용할 수 있는지도 확인해야 합니다.
