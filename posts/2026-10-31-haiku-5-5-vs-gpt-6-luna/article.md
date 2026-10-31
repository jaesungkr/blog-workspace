---
format: rich-post-v2
slug: haiku-5-5-vs-gpt-6-luna
status: published
title: Claude Haiku 5.5 vs GPT-6 Luna, 얼마나 쓸 만하고 얼마나 쌀까?
category: Log
subcategory: AI 모델 · 비교
date: 2026-10-31
hero_image: assets/haiku-5-5-official-hero.jpg
tags: ["Claude Haiku 5.5", "GPT-6 Luna", "AI 모델 비교", "API 비용"]
summary: "Claude Haiku 5.5와 GPT-6 Luna의 공개 평가와 API 요금을 비교하고, 평가 조건과 입력 길이에 따라 달라지는 선택 기준을 정리합니다."
published_url: "https://dop3n.tistory.com/entry/Claude-Haiku-55-vs-GPT-6-Luna-%EC%96%BC%EB%A7%88%EB%82%98-%EC%93%B8-%EB%A7%8C%ED%95%98%EA%B3%A0-%EC%96%BC%EB%A7%88%EB%82%98-%EC%8C%80%EA%B9%8C"
sources: ["https://www.anthropic.com/claude-haiku-5-5", "https://www.anthropic.com/claude-haiku-5-5-system-card", "https://developers.openai.com/api/docs/models/gpt-6-luna", "https://platform.claude.com/docs/en/about-claude/pricing", "https://arena.ai/blog/style-control", "https://arena.ai/leaderboard/chat/text"]
---

안녕하세요. dev.log입니다.

Haiku나 Luna처럼 저렴한 AI 모델을 보면 한번 써볼까 싶다가도 망설이게 됩니다. 싸게 썼다가 답변을 고치는 데 시간이 더 들면 곤란하니까요. 또한 가격표에 적힌 ‘100만 토큰당 몇 달러’도 실제로 얼마나 저렴한 건지 쉽게 와닿지도 않습니다.

Claude Haiku 5.5와 GPT-6 Luna를 더 비싼 Sonnet 5.5와 나란히 놓아 보니, 맡길 일을 구분하는 게 중요했습니다. 공개된 코드 수정 평가에서는 상위 모델과 차이가 비교적 작았지만, 여러 단계를 끝까지 처리하는 개발 작업에서는 격차가 컸습니다.

그럼 비용은 어느 정도일까요? **짧은 문서 요약에 쓸 입력·출력량을 가정하면, 1,000번 요청하는 비용이 두 모델 모두 $0.45**입니다. 앱이나 프로그램에서 모델을 호출하고 쓴 만큼 내는 API 요금 기준이며, ChatGPT·Claude의 월 구독료와는 별도입니다.

{{media:haiku-lead}}

### Sonnet과 나란히 놓고 본 실력

Haiku와 Luna는 글을 읽고 답변을 만드는 저비용 모델입니다. 외부 도구를 연결하면 코드도 수정할 수 있습니다. ‘저렴해도 쓸 만하다’는 말만으로는 부족하니, 상위 모델인 Sonnet 5.5를 기준점으로 함께 보겠습니다.

[Anthropic이 공개한 비교표](https://www.anthropic.com/claude-haiku-5-5)에서 세 가지 평가를 골랐습니다.

- **업무 결과물:** 문서·슬라이드·표 등을 만들게 한 뒤, 모델 이름을 가리고 결과물을 비교합니다. GDPval-AA는 이 비교에서 나온 상대 점수라서 만점이 정해진 시험 점수처럼 읽으면 안 됩니다.
- **터미널 작업:** 명령어로 프로그램을 실행하며 여러 단계의 작업을 끝내도록 합니다. Terminal-Bench는 이런 작업을 얼마나 잘 끝냈는지 평가합니다.
- **코드 수정:** 실제 공개 소프트웨어를 수정하는 작업을 맡깁니다. FrontierCode는 수정한 코드의 기능과 품질을 함께 채점합니다.

아래는 추론량을 높인 설정에서 나온 성적입니다. 모두 높을수록 좋고, 같은 행 안에서 비교하면 됩니다.

| 평가하는 일 | Haiku 5.5 | GPT-6 Luna | Sonnet 5.5 |
|---|---:|---:|---:|
| 업무 결과물 · GDPval-AA v2.1 | 1,620점 | 1,437점 | 1,840점 |
| 여러 단계의 명령어 작업 · Terminal-Bench 4.0 | 39.2% | 16.4% | 70.6% |
| 실제 코드 수정 · FrontierCode 1.1 Main | 46.4% | 42.4% | 52.1% |

{{media:haiku-benchmarks}}

코드 수정 평가만 보면 Haiku는 Sonnet보다 5.7%포인트, Luna는 9.7%포인트 낮습니다. 반면 여러 명령을 실행하며 작업을 끝내야 하는 시험에서는 Sonnet이 훨씬 앞섭니다. **작은 수정안을 받아 사람이 확인하는 일과, 복잡한 개발 작업을 통째로 맡기는 일은 다르게 봐야 합니다.** 저렴한 모델을 어디에 써볼지 정할 때 이 차이가 도움이 됩니다.

[시스템 카드](https://www.anthropic.com/claude-haiku-5-5-system-card)에 따르면 업무 평가는 Artificial Analysis, 코드 수정은 Cognition이 수행했고, 터미널 평가는 Anthropic 측정치와 Luna 공개 기록을 비교했습니다. 실행 도구는 모델마다 다르고, Haiku는 Max, 코드 수정의 Sonnet은 xhigh 설정을 썼습니다. 기본 설정에서는 성적과 사용 토큰 수가 달라질 수 있습니다.

### 요약 1,000번에 약 675원?

AI 요금표에서 말하는 토큰은 글을 처리하는 단위입니다. 보내는 문서와 질문은 입력, 모델이 생성하는 내용은 출력으로 계산합니다.

두 모델의 기본 API 단가는 100만 토큰당 **입력 $0.10, 출력 $0.50**으로 같습니다. Sonnet 5.5는 각각 $2와 $10입니다. 같은 토큰 수를 쓴다면 Haiku와 Luna의 기본 요금은 **Sonnet의 20분의 1**인 셈입니다. [Claude 요금표](https://platform.claude.com/docs/en/about-claude/pricing) · [Luna 요금표](https://developers.openai.com/api/docs/models/gpt-6-luna)

조금 더 익숙한 작업으로 바꿔 보겠습니다. 짧은 문서를 보내 요약을 받고, 이때 입력 2천 토큰과 출력 500토큰을 쓴다고 가정하면 아래처럼 계산됩니다. 출력에는 화면에 보이는 답변뿐 아니라 과금되는 추론 토큰까지 포함했습니다.

| 한 번 요청할 때의 사용량 가정 | 100번 요청 | 1,000번 요청 |
|---|---:|---:|
| 짧은 문서 요약 · 입력 2천 + 출력 500토큰 | $0.045 | $0.45 · 약 675원 |
| 더 긴 자료 요약 · 입력 1만 + 출력 1천 토큰 | $0.15 | $1.50 · 약 2,250원 |

원화는 체감하기 쉽도록 **1달러=1,500원으로 가정**했습니다. 실제 요약을 실행해 잰 비용이 아니라, 정해진 사용량을 요금표에 넣어 계산한 예시입니다.

첫 번째 분량으로 하루 30번씩, 30일 동안 요약을 받아도 900회입니다. 이 정도 작업이라면 모델 호출료 자체보다, 결과를 얼마나 손봐야 하는지가 더 신경 쓰일 수 있겠습니다.

계산식도 간단합니다. 첫 줄의 1회 비용은 `(2,000 × $0.10 + 500 × $0.50) ÷ 1,000,000 = $0.00045`입니다. 실제 청구액은 모델별 토큰 수와 추론량·답변 길이·재시도에 따라 달라지며, 여기에는 캐시·일괄 처리 할인과 별도 도구 요금, 세금은 넣지 않았습니다.

### 긴 문서에서 벌어지는 가격 차이

다만 자료를 한꺼번에 많이 넣으면 이야기가 달라집니다. 두 모델의 기본 단가가 같은 건 **입력이 10만 토큰 이하일 때**입니다.

[Haiku 요금표](https://platform.claude.com/docs/en/about-claude/pricing)와 [Luna 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-luna)를 입력 길이에 따라 나눠봤습니다. 아래 금액은 모두 100만 토큰당 달러입니다.

| 요청의 입력 길이 | Haiku 입력 / 출력 | Luna 입력 / 출력 |
|---|---:|---:|
| 10만 토큰 이하 | $0.10 / $0.50 | $0.10 / $0.50 |
| 10만 초과~27만 2천 이하 | $0.50 / $2.50 | $0.10 / $0.50 |
| 27만 2천 초과 | $0.50 / $2.50 | $0.20 / $0.75 |

Haiku는 입력이 10만 토큰을 넘으면 단가가 올라가지만, Luna는 27만 2천 토큰까지 기본 단가를 유지합니다. 여기서 주의할 점은 기준을 넘긴 부분에만 추가 요금이 붙는 게 아니라, 해당 요청의 입력과 출력 전체에 높은 단가가 적용된다는 것입니다.

예를 들어 입력 15만 토큰과 과금 대상 출력 2천 토큰을 쓰는 요청을 1,000번 보내면, Haiku는 $80, Luna는 $16입니다. **같은 토큰 수인데도 다섯 배 차이**가 납니다. 여러 문서나 긴 대화 기록을 묶어서 읽히는 작업이라면 Luna 쪽이 비용을 줄이기 좋습니다.

### 사람들이 고른 답변은?

작업을 얼마나 잘 끝내는지와 대화할 때 어느 답변이 더 마음에 드는지는 조금 다른 이야기입니다. Arena에서는 모델 이름을 가린 두 답변을 보여주고 사람들이 더 나은 쪽에 투표합니다.

기본 화면의 **Style Control**은 답변 길이와 제목·굵은 글씨·목록 같은 형식이 선호도에 미치는 영향을 통계적으로 보정한 지표입니다. 정답 여부만 채점하는 시험은 아닙니다. [Arena의 집계 방식 설명](https://arena.ai/blog/style-control)

[Text Overall 리더보드](https://arena.ai/leaderboard/chat/text)의 2026년 10월 28일 화면에서는 보정을 켜고 끄는 것만으로 두 모델의 순서가 바뀌었습니다.

| Arena 집계 방식 | Haiku 5.5 · High | GPT-6 Luna · Max |
|---|---:|---:|
| 기본 보정 · Style Control | 126위 · 1,425점 | 97위 · 1,441점 |
| 보정 없음 · None | 154위 · 1,401점 | 170위 · 1,389점 |

보정한 점수는 Luna가, 보정하지 않은 점수는 Haiku가 높았습니다. 추론 설정이 다른 두 모델을 여러 언어의 답변으로 비교한 결과이며, 어느 쪽을 더 선호하는지는 집계 조건에 따라 달랐습니다.

### Haiku와 Luna를 고르는 기준

짧은 입력으로 코드 수정이나 업무 보조를 맡긴다면, 공개 평가에서 앞선 **Haiku 5.5부터 후보에 넣어볼 만합니다.** 기본 단가가 같으니 이 구간에서는 가격보다 결과의 차이가 중요합니다.

긴 자료를 한 번에 읽히는 일이 많다면 **Luna의 요금 구조가 더 유리**합니다. 두 모델 모두 작은 일을 여러 번 처리할 때는 비용 부담이 낮습니다. 다만 복잡한 작업에서는 상위 모델과의 성능 차이가 남아 있으니, 평소 반복하던 일 중 범위가 분명한 작업부터 맡겨보기 좋겠습니다.

### 참고 자료

- [Anthropic · Claude Haiku 5.5 소개와 비교 평가](https://www.anthropic.com/claude-haiku-5-5)
- [Anthropic · Haiku 5.5 시스템 카드](https://www.anthropic.com/claude-haiku-5-5-system-card)
- [Claude API · 요금과 긴 입력의 과금 조건](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI API · GPT-6 Luna 모델과 요금](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [Arena · Text Overall 리더보드](https://arena.ai/leaderboard/chat/text)
- [Arena · 답변 길이와 형식 보정의 의미](https://arena.ai/blog/style-control)
