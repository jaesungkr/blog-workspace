---
title: "GPT-6.1 Sol vs Claude Opus 5.5 - 새 GPT 모델의 성능과 가격"
slug: gpt-6-1-sol-vs-opus-5-5
date: 2026-09-30
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
format: rich-post-v2
tags: [GPT-6.1 Sol, Claude Opus 5.5, GPT-6 Astra, Claude Fable 5.1, AI 모델 비교]
summary: "GPT-6.1 Sol을 Opus 5.5와 비교하고, Astra·Fable 5.1을 포함한 독립 평가와 API 비용으로 새 모델의 위치를 살펴봅니다."
hero_image: assets/gpt-6-1-sol-vs-opus-5-5-hero-v1.png
published_url: ""
sources:
  - https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/
  - https://developers.openai.com/api/docs/models/gpt-6.1-sol
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://www.anthropic.com/claude-opus-5-5
  - https://www.anthropic.com/claude-fable-and-mythos-5-1
  - https://artificialanalysis.ai/leaderboards/models
  - https://artificialanalysis.ai/models/claude-opus-5-5
---


안녕하세요. dev.log입니다.

OpenAI가 새 GPT 모델인 **GPT-6.1 Sol**을 공개했습니다. 기존 Sol을 개선한 모델로, 글쓰기와 자료 분석부터 코딩, 도구를 활용한 업무까지 맡길 수 있습니다. 새 모델이 나온 만큼, 이전보다 얼마나 좋아졌고 지금 쓰는 클로드와 비교하면 어느 정도인지 궁금해집니다.

**Sol은 문서 분석과 업무 자동화에서 성능과 비용을 함께 따져 볼 만한 모델입니다.** OpenAI가 공개한 일부 업무 평가에서는 Opus 5.5를 앞서면서 비용도 낮췄습니다. 다만 여러 분야를 묶은 독립 종합 평가에서는 Opus가 더 높은 점수를 받았으므로, 어떤 작업을 맡길지에 따라 선택이 달라집니다.

{{media:sol-opus-hero}}

### GPT-6.1 Sol의 특징과 이용 방법

OpenAI는 [2026년 9월 29일 DevDay](https://openai.com/index/devday-2026-recap/)에 GPT-6.1 Sol을 발표했습니다. 기존 GPT-6 Sol을 개선하면서 코딩·컴퓨터 조작·전문 업무에서 더 비싼 GPT-6 Astra에 가까운 성능을 목표로 한 모델입니다. 출시 안내에 따르면 Plus·Pro·Business·Enterprise·Edu 사용자는 ChatGPT Work와 Codex의 모델 선택 화면에서 Sol 6.1을 선택할 수 있습니다. 일반 Chat에는 아직 제공되지 않으며, API에서는 `gpt-6.1-sol`이라는 식별자로 호출합니다. [OpenAI 출시 안내](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

클로드와 비교할 때는 **Opus 5.5**를 중심으로 보는 것이 좋겠습니다. Anthropic이 9월 22일 출시한 모델로, 코드 작업과 문서 작성 등 대부분의 업무에서 Fable 5.1 수준의 성능을 제공한다고 설명합니다. OpenAI의 Sol 출시 자료에도 Opus와 직접 비교한 결과가 있습니다. 여기에 OpenAI의 상위 모델인 Astra와 Claude의 다른 고성능 모델인 Fable 5.1을 함께 놓으면, 새 Sol의 수준과 가격을 더 넓게 가늠할 수 있습니다. [Anthropic Opus 5.5 발표](https://www.anthropic.com/claude-opus-5-5)

### Opus와 비교한 업무 성능

OpenAI의 출시 자료에서 먼저 눈에 띄는 것은 문서 분석 성능입니다. 표·차트·작은 주석을 읽고 질문에 답하는 **GDP.pdf** 평가에서는, 추론에 사용할 자원의 양을 정하는 설정을 바꿔 가며 두 모델을 비교했습니다. OpenAI에 따르면 Sol 6.1은 평가한 설정 전반에서 Opus 5.5보다 높은 점수를 기록했고, 과제당 비용은 절반 미만이었습니다. 이때 Opus는 안전장치 등이 작동하면 다른 모델로 작업을 넘기는 **fallback(대체 처리)**을 포함한 구성입니다.

문서를 읽는 데서 더 나아가, 여러 업무용 도구를 연결해 작업을 끝내는 **AutomationBench 1.0.6**에서도 Sol이 앞섰습니다. 중간 추론 수준인 medium 설정에서 Opus보다 점수가 2.2%p 높았고, 과제당 비용은 약 3분의 1이었습니다. %p는 두 비율의 차이를 나타내는 퍼센트포인트입니다. 다만 두 결과 모두 OpenAI가 발표한 특정 업무 평가입니다. 같은 페이지에 제시된 Fable 5.1 비용에는 약 40%의 과제에서 발생한 fallback 비용이 빠져 있으므로, 표시된 금액만으로 네 모델의 비용 순위를 정하기는 어렵습니다. [OpenAI 전문 업무 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

코딩에서는 Opus보다 Astra와의 비교가 더 분명합니다. 실제 코드베이스에서 긴 소프트웨어 개발 과제를 수행하는 **DeepSWE v1.1**에서 Sol은 Astra와 같은 수준의 점수를 약 5분의 1 비용으로 달성했다고 OpenAI가 보고했습니다. 반면 Opus 출시 자료의 코딩 비교표에 들어 있는 모델은 이전 버전인 GPT-5.6 Sol입니다. 이 표를 새 Sol 6.1의 결과처럼 읽으면 두 모델의 코딩 성능을 잘못 비교하게 됩니다. 현재 자료로는 Sol과 Opus 중 어느 쪽이 코딩 전반에서 우세한지까지 판단하기 어렵습니다. [OpenAI 코딩 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/), [Anthropic 비교표](https://www.anthropic.com/claude-opus-5-5)

### 독립 종합 평가에서 본 네 모델의 수준

앞의 결과는 문서 분석과 자동화 같은 개별 업무를 보여 줍니다. 여러 분야를 함께 평가하면 순위는 어떻게 달라질까요? 독립 평가 기관인 Artificial Analysis의 **Intelligence Index v4.3.2**는 문서 업무·코딩·추론 등을 포함한 10개 평가를 묶은 종합 지수입니다. 점수가 높을수록 이 평가 묶음에서 성능이 좋다는 뜻이며, 업무 성공률이나 정답률을 나타내는 백분율과는 다릅니다. [평가 구성](https://artificialanalysis.ai/models/claude-opus-5-5)

아래 표는 2026년 9월 30일 리더보드에서 확인한 정수 표시값입니다. medium은 중간, max는 최대 추론 설정을 뜻합니다. Claude 결과에는 리더보드에 표시된 fallback 구성이 포함되어 있습니다. 제조사마다 추론 설정을 구현하는 방식이 달라서, 설정 이름이 같다고 실제 계산량까지 같지는 않습니다. [Artificial Analysis 리더보드](https://artificialanalysis.ai/leaderboards/models)

모바일에서는 표를 좌우로 밀어 모든 열을 확인하세요.

| 모델 | medium 지수 | max 지수 | max 과제당 비용 |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | 48 | 52 | $0.72 |
| Claude Opus 5.5 | 51 | 58 | $5.98 |
| GPT-6 Astra | 50 | 53 | $3.26 |
| Claude Fable 5.1 | 49 | 53 | $7.63 |

종합 지수에서는 Opus가 가장 높았습니다. Sol은 Astra와 Fable에 가까운 점수를 훨씬 낮은 비용으로 얻었지만, Opus의 최대 추론 성능과는 차이가 남아 있습니다. 표의 과제당 비용은 이 평가 묶음의 평균값이므로, 실제 문서 한 건이나 코드 수정 한 번에 들 요금은 별도로 계산해야 합니다.

난도가 높은 작업에서는 모델의 역할도 달라집니다. OpenAI는 가장 어려운 과학 연구에 여전히 Astra를 권장합니다. 문서와 자동화 평가에서 Sol이 좋은 결과를 얻었다고 해서, 어려운 연구 과제까지 상위 모델과 같은 수준으로 해결한다고 볼 수는 없습니다. [OpenAI 과학 연구 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

### 같은 처리량으로 비교한 API 비용

평가에 나온 과제당 비용은 모델이 사용한 토큰 수와 작업 방식까지 반영한 값입니다. 기본 요금 자체가 얼마나 다른지 보려면, 같은 양을 처리한다고 가정해 비교하는 편이 이해하기 쉽습니다.

API는 프로그램에서 모델을 호출하고 처리한 양만큼 요금을 내는 방식입니다. 그 처리량을 세는 단위가 **토큰**이며, 입력은 모델에 보낸 자료와 지시, 출력은 모델이 생성한 내용에 해당합니다. 아래 단가는 100만 토큰 기준으로, GPT는 Standard, Claude는 일반 API 요금을 사용했습니다. [Sol 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Opus 요금](https://www.anthropic.com/claude-opus-5-5), [Astra 요금](https://developers.openai.com/api/docs/models/gpt-6-astra), [Fable 요금](https://www.anthropic.com/claude-fable-and-mythos-5-1)

마지막 열은 입력 10만 토큰과 출력 1만 토큰을 처리한다고 가정한 계산입니다. 입력 단가에 0.1을, 출력 단가에 0.01을 곱해 더했으며, 캐시·도구 비용·재시도·모드별 할증은 제외했습니다. 실제 모델을 실행해 측정한 비용은 아닙니다.

모바일에서는 표를 좌우로 밀어 모든 열을 확인하세요.

| 모델 | 입력 / 100만 토큰 | 출력 / 100만 토큰 | 가정한 처리량의 비용 |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | $2 | $10 | $0.30 |
| Claude Opus 5.5 | $4 | $20 | $0.60 |
| GPT-6 Astra | $10 | $50 | $1.50 |
| Claude Fable 5.1 | $10 | $50 | $1.50 |

같은 처리량이라면 Sol의 기본 요금은 Opus의 절반입니다. 다만 같은 일을 맡겨도 모델마다 사용하는 토큰 수가 다르므로, 실제 작업 비용이 항상 절반이 되는 것은 아닙니다.

같은 자료를 반복해서 보내는 경우에는 이전에 처리한 입력을 재사용하는 **캐시**가 비용을 줄여 줍니다. Sol의 캐시 입력은 100만 토큰당 $0.10, Opus의 캐시 읽기는 $0.20이며, 캐시를 처음 저장하는 비용과 적용 조건은 별도로 확인해야 합니다. 긴 자료를 한 번에 보내는 경우에도 주의할 조건이 있습니다. Sol은 입력이 27만 2천 토큰을 넘으면 전체 요청의 입력·캐시 단가가 2배, 출력 단가가 1.5배로 올라갑니다. 모델이 받아들일 수 있는 길이의 자료라도 기본 요금보다 더 비싸질 수 있다는 뜻입니다. [Sol 상세 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Opus 상세 요금](https://www.anthropic.com/claude-opus-5-5)

이 요금표는 ChatGPT나 Claude의 월 구독료와는 별개입니다. 구독을 바꾸려는 경우에는 API 단가보다 실제 이용할 서비스의 사용 한도와 필요한 기능을 먼저 확인하는 것이 좋겠습니다.

### 클로드 대신 쓸지 판단하는 방법

문서 분석이나 업무 자동화를 API로 반복한다면, Sol의 낮은 단가가 실제로 비용을 줄여 주는지 시험해 볼 만합니다. 반면 어려운 문제의 해결 가능성을 더 중요하게 본다면 종합 평가에서 앞선 Opus도 함께 비교할 이유가 있습니다. Fable 5.1을 이미 사용 중이라면, 더 비싼 요금만큼 현재 작업에서 더 나은 결과를 얻고 있는지 확인해 보세요.

직접 비교할 때는 **평소 자주 맡기는 작업 한 건을 두 모델에 같은 조건으로 요청하는 것**부터 시작하면 됩니다. 문서라면 표의 수치와 각주를 제대로 반영했는지, 코드라면 요구한 동작을 구현하면서 기존 기능도 유지했는지를 확인하세요. 첫 답변만 보고 결정하기보다는, 필요한 수정을 모두 마칠 때까지 걸린 시간과 총비용을 비교하는 편이 실제 선택에 도움이 됩니다. 지금 쓰는 Opus의 결과에 만족한다면 유지하되, 수정이 많았던 작업부터 Sol에도 맡겨 보는 것이 좋겠습니다.

### 참고 자료

- [OpenAI: GPT-6.1 Sol 출시 안내와 업무별 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)
- [OpenAI API: GPT-6.1 Sol 사양과 상세 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [Anthropic: Claude Opus 5.5 발표와 평가 조건](https://www.anthropic.com/claude-opus-5-5)
- [Anthropic: Claude Fable 5.1 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [OpenAI API: GPT-6 Astra 요금](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [Artificial Analysis: 독립 모델 평가 리더보드](https://artificialanalysis.ai/leaderboards/models)
- [Artificial Analysis: Intelligence Index 평가 구성](https://artificialanalysis.ai/models/claude-opus-5-5)
