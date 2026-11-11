---
title: "Fable 5.2 vs GPT-6 Astra - 클로드 GPT 모델 비교"
slug: fable-5-2-vs-gpt-6-astra
date: 2026-11-11
category: "Log"
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags: [Fable 5.2, GPT-6 Astra, Claude, GPT, Arena, AI 모델 비교]
summary: "최상위 GPT와 클로드를 공식 벤치마크, Arena, 실제 평가 비용으로 비교했습니다. Fable의 성능 우위와 추론 설정에 따라 달라지는 비용을 함께 살펴봅니다."
hero_image: assets/fable-5-2-vs-gpt-6-astra-hero-v1.png
published_url: "https://dop3n.tistory.com/entry/Fable-52-vs-GPT-6-Astra-클로드-GPT-모델-비교"
sources:
  - https://www.anthropic.com/claude-fable-and-mythos-5-2
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://artificialanalysis.ai/models/claude-fable-5-2
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://arena.ai/leaderboard
---

안녕하세요. dev.log입니다.

[지난 글](https://dop3n.tistory.com/175)에서는 Fable 5.2를 이전 Fable, Opus와 비교했습니다. 클로드 안에서 고를 때는 도움이 되지만, GPT를 쓰는 입장에서는 다른 질문이 먼저 떠오릅니다. “그래서 Astra보다 좋은가요? 지금 쓰는 GPT에서 넘어갈 만한가요?”

공개된 평가를 보면 Fable 5.2의 성능은 꽤 인상적입니다. 독립 평가에서 Astra보다 높은 점수를 받았고, Arena의 웹 개발 평가에서도 앞서 있습니다. 다만 최고 성능을 내도록 설정했을 때 드는 비용까지 보면 선택이 조금 달라집니다. Fable은 토큰 단가가 더 저렴한데, 같은 평가에서 작업 하나에 쓴 돈은 Astra보다 훨씬 많았습니다.

자료는 2026년 11월 11일 기준입니다.

{{media:lead}}

### 지금 비교할 모델은 Astra와 Fable 5.2

GPT-6 Astra는 OpenAI가 어려운 작업에 권하는 고성능 추론 모델입니다. 더 최근에 나온 GPT-6.1 Sol도 있지만, 이번 글은 출시 순서보다 각 회사의 최고 난도 작업용 모델에 초점을 맞췄습니다. 클로드에서는 11월 9일 공개된 Fable 5.2를 골랐습니다. 함께 발표된 Mythos 5.2는 검증된 조직에 제공되는 모델이라 일반 이용자의 선택지에서 제외했습니다.

둘 다 긴 문서나 코드 저장소를 다룰 수 있고, 답을 내기 전에 얼마나 오래 추론할지 설정할 수 있습니다. 아래에서 등장하는 medium·high·max·xhigh는 그 설정을 가리킵니다. 회사마다 이름과 구현이 달라서, 같은 이름이라고 같은 시간이나 비용을 쓰지는 않습니다.

| 항목 | Claude Fable 5.2 | GPT-6 Astra |
|---|---:|---:|
| 표준 API 입력 단가 / 100만 토큰 | $8 | $10 |
| 표준 API 출력 단가 / 100만 토큰 | $40 | $50 |
| 한 번에 다룰 수 있는 컨텍스트 | 100만 토큰 | 105만 토큰 |
| 최대 출력 | 12만 8천 토큰 | 12만 8천 토큰 |

출처: [Claude 공식 문서](https://platform.claude.com/docs/en/models/fable-5-2/overview), [OpenAI 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-astra). 컨텍스트에는 입력과 모델이 생성하는 내용이 함께 들어갑니다. Astra는 입력이 27만 2천 토큰을 넘으면 요청 전체에 할증이 적용되므로, 긴 자료를 넣을 때는 아래 가격 설명도 함께 보셔야 합니다.

### 코딩과 업무 평가에서 앞선 Fable

먼저 Anthropic이 발표한 비교표입니다. 서로 다른 회사의 출시 자료에서 숫자를 하나씩 가져오면 평가 버전과 조건이 엇갈릴 수 있어, 같은 표 안에서 두 모델을 비교했습니다.

| 평가 | 무엇을 보는지 | Fable 5.2 | Astra |
|---|---|---:|---:|
| FrontierCode 2.0 | 어려운 코딩 문제 | 49.1% | 42.8% |
| FrontierSWE v2 | 소프트웨어 엔지니어링 작업 | 69.9% | 65.5% |
| AutomationBench | 업무 자동화 | 51.4% | 41.4% |

세 항목 모두 높은 점수가 좋습니다. Fable의 FrontierCode 결과는 xhigh이며, 나머지는 별도 표기가 없는 각 모델의 최고 추론 설정입니다. **Anthropic이 공개한 결과**라는 점은 감안해야 합니다. [공식 발표 및 평가 설명](https://www.anthropic.com/claude-fable-and-mythos-5-2)

이런 평가가 눈길을 끄는 이유는 맡기는 일의 크기가 달라지고 있기 때문입니다. 함수 하나를 고치는 요청보다 여러 파일의 관계를 파악하고 수정한 뒤 테스트까지 이어가는 작업에서, 중간에 놓치는 조건이 적은 모델이 필요합니다. 이 표는 그런 작업을 맡길 후보로 Fable을 먼저 살펴볼 이유를 줍니다. 개인 프로젝트에서 어느 쪽이 더 잘 고칠지는 사용하는 도구와 저장소에 따라 달라집니다.

{{media:benchmarks}}

### Arena 웹 개발 1위, 다른 분야는 아직 미등재

정답이 정해진 문제를 얼마나 잘 푸는지와, 사람이 두 결과물을 놓고 무엇을 고르는지는 조금 다릅니다. Arena는 모델 이름을 가린 상태에서 결과를 비교하는 평가로 알려져 있습니다. 이번에는 그중 웹사이트를 만드는 **WebDev** 순위를 먼저 확인했습니다.

| Arena WebDev Overall | 모델·설정 | 점수 | 투표 수 |
|---|---|---:|---:|
| 1위 | Fable 5.2 xHigh | 1836 ±22 | 994 |
| 2위 | Opus 5.5 Max | 1814 ±12 | 4,187 |
| 5위 | GPT-6 Astra Max | 1764 ±9 | 8,425 |

2026년 11월 11일 확인한 화면 기준입니다. 점수 뒤의 ±는 리더보드가 표시한 불확실성 범위입니다. Fable은 Astra보다 높은 점수를 받았지만, 투표는 아직 약 1천 건으로 Astra보다 적습니다. 특히 1위와 2위는 표시된 범위가 겹칩니다. 신작의 초반 결과인 만큼 순위와 표본 수를 함께 보는 편이 좋겠습니다. [Arena WebDev](https://arena.ai/leaderboard/code/webdev)

예를 들어 “동네 카페의 예약 페이지를 만들어 줘”라고 했을 때, 완성된 화면과 동작이 어느 쪽에서 더 마음에 드는지 궁금하다면 이 결과가 참고가 됩니다. 기존 서비스의 복잡한 버그를 고치는 능력까지 이 순위 하나로 설명하기는 어렵습니다.

다른 분야도 확인했습니다. Text는 일반 텍스트 응답, Agent는 에이전트 작업을 별도로 평가합니다.

| 분야 | Fable 5.2 | GPT-6 Astra Max |
|---|---|---|
| Text Overall | 아직 등재되지 않음 | 41위, 1474 ±6, 18,315표 |
| Agent Overall | 아직 등재되지 않음 | 5위, Net Improvement 14.24 ±2.03%, 15,520세션 |

Text 페이지의 표시일은 11월 9일, Agent는 11월 8일입니다. Agent의 Net Improvement는 여러 실제 세션 신호를 종합해 기준 대비 기여를 추정한 값입니다. 성공률과는 다릅니다. [Agent 평가 방식](https://arena.ai/blog/agent-arena-methodology) 이 두 분야에서는 아직 Fable 5.2와 Astra의 직접 순위 비교를 할 수 없습니다. 따라서 현재 Arena가 보여 주는 Fable의 우위는 **WebDev에 한정해 읽어야 합니다.** [Text](https://arena.ai/leaderboard/chat/text) · [Agent](https://arena.ai/leaderboard/agent)

### 최고 성능에 따라붙는 추론 비용

제조사 밖의 평가도 보겠습니다. Artificial Analysis의 Intelligence Index는 여러 시험을 묶어 모델 성능을 보여 주는 지표입니다. 같은 v5.0.1에서 두 모델을 비교하면 Fable의 높은 점수와 함께, 추론 설정의 영향이 드러납니다.

| 모델·설정 | 종합 점수 | 평가 작업당 비용 | 평가 작업당 시간 |
|---|---:|---:|---:|
| GPT-6 Astra max | 57 | $6.24 | 23.0분 |
| Fable 5.2 medium | 56 | $3.80 | 7.9분 |
| Fable 5.2 high | 62 | $9.08 | 17.5분 |
| Fable 5.2 max | 65 | $26.54 | 44.4분 |

Fable은 모두 **Default Fallback** 구성의 결과입니다. 안전장치가 제한한 요청을 지정된 다른 모델로 넘기는 기본 대체 처리 설정이 포함돼 있습니다. 점수는 높을수록 좋고, 시간·비용은 낮을수록 부담이 적습니다. 비용은 평가에서 사용한 입력·캐시·추론·답변 토큰 등을 반영한 가중 평균입니다. 여러 단계가 필요한 평가 작업을 집계한 값이라 일상 대화의 요금이나 응답 시간과는 구분해서 봐야 합니다. 서로 다른 설정으로 얻을 수 있는 성능·비용 조합을 비교한 표입니다. [Astra](https://artificialanalysis.ai/models/gpt-6-astra) · [Fable medium](https://artificialanalysis.ai/models/claude-fable-5-2-medium) · [high](https://artificialanalysis.ai/models/claude-fable-5-2-high) · [max](https://artificialanalysis.ai/models/claude-fable-5-2)

Fable max는 65점으로 Astra max의 57점보다 높지만, 평가 작업당 비용은 약 4.25배였습니다. 시간을 더 쓰더라도 어려운 문제를 풀어내는 것이 중요한 작업에서는 고려할 만합니다. 반대로 같은 작업을 수백 번 반복해야 한다면 점수 차이만큼 비용 차이도 크게 느껴질 겁니다.

눈에 들어오는 설정은 **Fable high**입니다. 이 평가에서는 Astra max보다 점수가 높고 걸린 시간도 짧았습니다. 비용은 $9.08로 더 들었지만, Fable max의 $26.54보다는 훨씬 낮았습니다. Fable로 어려운 작업을 시작한다면 high부터 사용하고, 해결되지 않는 작업에서 max를 검토하는 쪽이 합리적입니다.

### API 단가는 저렴한데, 왜 작업비는 비쌀까요?

표준 API 단가는 Fable이 Astra보다 입력·출력 모두 20% 낮습니다. 같은 양을 사용한다고 가정하면 계산은 간단합니다.

- 입력 10만 토큰, 출력 1만 토큰을 쓴 경우
- Fable 5.2: 입력 $0.80 + 출력 $0.40 = **$1.20**
- Astra: 입력 $1.00 + 출력 $0.50 = **$1.50**

캐시와 추가 도구 비용을 제외한 예시이며, 출력에는 과금되는 추론 토큰도 포함해야 합니다. 실제로 두 모델에 같은 요청을 해도 소비하는 토큰 수는 달라집니다. Fable이 더 오래 추론하며 토큰을 많이 쓰면 낮은 단가의 이점이 줄어듭니다. 앞의 Artificial Analysis 결과가 바로 이 차이를 보여 줍니다.

긴 문서 작업은 Astra의 가격 조건도 확인해야 합니다. **입력이 27만 2천 토큰을 넘으면 해당 요청 전체의 입력·캐시 단가는 2배, 출력은 1.5배**가 됩니다. 자료를 한꺼번에 많이 넣는 작업이라면 표준 단가만으로 예산을 잡지 않는 것이 좋습니다. [OpenAI 가격 조건](https://developers.openai.com/api/docs/models/gpt-6-astra)

ChatGPT나 Claude 앱을 구독해서 쓰는 분에게는 별도의 문제가 있습니다. 위 숫자는 API 가격이므로 월 구독료와 직접 비교할 수 없습니다. 특히 Fable은 플랜별 포함량과 추가 사용 조건이 다릅니다. Pro 이용자는 11월 16일 미국 태평양 시간까지의 출시 혜택이 끝나면 별도 사용 크레딧으로 이용하게 됩니다. [Fable 플랜별 안내](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan) · [출시 혜택](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers)

### 지금 하나를 고른다면

최고 성능의 모델을 새로 고르는 상황이라면, 이번 자료에서는 **Fable 5.2를 먼저 살펴볼 이유가 더 많습니다.** 공식 코딩·업무 평가와 독립 종합 평가가 같은 방향을 가리키고, Arena WebDev에서도 좋은 출발을 했습니다. API로 어려운 작업을 맡긴다면 high부터 시작하는 것을 권합니다.

최고 추론 설정을 반복해서 사용하는 작업에서는 **Astra의 낮은 평가 비용**이 장점입니다. Fable high는 Astra max보다 높은 점수와 짧은 처리 시간을 보여 줬지만, 작업당 비용은 더 들었습니다. 자동화할 작업이 많다면 성능 점수와 함께 이 차이를 예산에 반영하는 편이 좋겠습니다.

웹 화면을 만드는 일을 많이 한다면 Fable이 우선 후보입니다. 반면 일반 대화나 에이전트 작업의 Arena 순위를 보고 결정하려던 분이라면 Fable 5.2의 결과가 추가된 뒤 다시 비교하는 편이 좋겠습니다. 이번에 확인한 자료만 놓고 보면, Fable의 매력은 분명 높은 성능에 있습니다. 그 성능을 매번 max로 꺼내 쓸 필요가 있는지는 따로 따져볼 만합니다.

### 참고 자료

- [Anthropic: Claude Fable and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [Claude Fable 5.2 공식 모델 문서](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [OpenAI: GPT-6 Astra](https://openai.com/index/gpt-6-astra/), [모델·가격 문서](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [Claude Fable 플랜 안내](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan), [출시 혜택](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers)
- [Arena WebDev](https://arena.ai/leaderboard/code/webdev), [Text](https://arena.ai/leaderboard/chat/text), [Agent](https://arena.ai/leaderboard/agent)
- Artificial Analysis: [Astra max](https://artificialanalysis.ai/models/gpt-6-astra), [Fable medium](https://artificialanalysis.ai/models/claude-fable-5-2-medium), [high](https://artificialanalysis.ai/models/claude-fable-5-2-high), [max](https://artificialanalysis.ai/models/claude-fable-5-2)
