---
title: "GPT-6.1 Sol vs Claude Opus 5.5 - 새 GPT 모델의 성능과 가격"
slug: gpt-6-1-sol-vs-opus-5-5
date: 2026-09-30
category: "Log"
subcategory: "AI 모델 · 비교"
status: reviewing
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

Claude에 PDF 분석이나 코드 수정을 맡기던 분이라면, 새 GPT 모델이 나왔을 때 궁금한 것은 하나입니다. 지금 쓰는 클로드와 비교해 볼 만한 수준일까요? GPT-6.1 Sol은 자료를 읽고 코드를 수정하며, 도구를 사용해 여러 단계의 업무를 처리하는 OpenAI의 새 모델입니다. **문서 분석과 반복 업무에 Sol을 비교 후보로 추가할 이유는 생겼지만, Opus 5.5에서 곧바로 갈아탈 근거까지 확보된 것은 아닙니다.**

출시 자료에서는 일부 업무에서 Sol이 Opus를 앞섰고, 독립 종합 평가에서는 Opus가 더 높은 점수를 받았습니다. PDF 질문의 정확도와 여러 분야를 묶은 종합 점수가 서로 다른 판단 근거를 주기 때문입니다.

{{media:sol-opus-hero}}

### 새 Sol은 어디서 쓸 수 있을까?

OpenAI는 [2026년 9월 29일 DevDay](https://openai.com/index/devday-2026-recap/)에 GPT-6.1 Sol을 발표했습니다. 기존 GPT-6 Sol을 개선한 모델이며, 코딩·컴퓨터 조작·전문 업무에서 더 비싼 GPT-6 Astra에 가까운 성능을 목표로 합니다. 출시 안내에 따르면 Plus·Pro·Business·Enterprise·Edu 사용자는 ChatGPT Work와 Codex에서 이용할 수 있습니다. 일반 Chat에는 아직 제공되지 않습니다. Work 또는 Codex의 모델 선택 화면에서 Sol 6.1을 선택해 사용합니다. API 식별자는 `gpt-6.1-sol`입니다. [OpenAI 출시 안내](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

Claude Opus 5.5는 Anthropic이 9월 22일 출시한 모델로, 코드 작업과 문서 작성 등 대부분의 업무에서 Fable 5.1 수준을 제공한다고 설명합니다. 기존 Claude 사용자가 새 Sol을 검토할 때 자연스럽게 비교할 상대입니다. Astra는 OpenAI의 상위 모델이고, Fable 5.1은 Claude의 또 다른 고성능 모델입니다. 두 모델도 Sol의 수준을 가늠할 비교 대상에 포함했습니다. [Anthropic Opus 5.5 발표](https://www.anthropic.com/claude-opus-5-5)

### Opus와 비교한 업무 성능

출시 자료에서 눈에 띄는 부분은 PDF 분석입니다. 표·차트·작은 주석까지 읽고 질문에 답하는 **GDP.pdf**에서는 추론 설정을 바꿔 가며 비교했습니다. 추론 설정은 답변을 만들기 전에 얼마나 많은 추론 자원을 사용할지 정하는 설정입니다. OpenAI에 따르면 Sol 6.1은 평가한 설정 전반에서 Opus 5.5보다 높은 점수를 기록했고, 과제당 비용은 절반 미만이었습니다. 여기서 Opus는 안전장치 등이 작동하면 다른 모델로 작업을 넘기는 대체 처리, 즉 **fallback**을 포함한 구성입니다.

여러 업무용 도구를 연결해 작업을 끝내는 **AutomationBench 1.0.6**에서는 Sol의 중간 추론 수준인 medium 설정이 Opus보다 2.2%p 높았고, 과제당 비용은 약 3분의 1이었습니다. 퍼센트포인트(%p)는 두 비율의 차이를 나타냅니다. 두 결과는 **OpenAI가 발표한 특정 업무 평가**입니다. 같은 페이지의 Fable 5.1 비용에는 약 40%의 과제에서 발생한 fallback 비용이 빠졌다는 주석도 있어, 표시된 비용만으로 네 모델을 나란히 순위 매기면 비교 조건을 놓치게 됩니다. [OpenAI 전문 업무 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

코딩에서도 Sol이 발전했다는 근거는 있습니다. 실제 코드베이스의 긴 소프트웨어 개발 과제를 다루는 **DeepSWE v1.1**에서는 Astra와 같은 수준의 점수를 약 5분의 1 비용으로 달성했다고 OpenAI가 보고했습니다. 이 결과가 Opus와의 코딩 전반 우열을 증명하지는 않습니다. Opus 출시 때의 코딩 표에는 GPT-5.6 Sol이 들어 있으므로, 그 점수를 새 Sol 6.1의 성능으로 가져와 비교해서는 안 됩니다. [OpenAI 코딩 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/), [Anthropic 비교표](https://www.anthropic.com/claude-opus-5-5)

### 독립 종합 평가에서는 Opus 우위

PDF 질문에 잘 답하는 모델이 글쓰기, 과학 문제, 코딩에서도 항상 앞서는 것은 아닙니다. 여러 영역을 묶은 결과를 보기 위해 독립 평가 기관인 Artificial Analysis의 **Intelligence Index v4.3.2**를 확인했습니다. 문서 업무·코딩·추론 등을 포함한 10개 평가의 종합 지수이며, 점수가 높을수록 이 평가 묶음에서 성능이 좋습니다. 업무 성공률이나 정답률을 그대로 나타내는 백분율은 아닙니다. [평가 구성](https://artificialanalysis.ai/models/claude-opus-5-5)

아래는 2026년 9월 30일 확인한 정수 표시값입니다. medium은 중간, max는 최대 추론 설정입니다. Claude 결과에는 리더보드에 표시된 fallback 구성이 포함되어 있으며, 제조사가 다른 모델에서 같은 설정명을 사용해도 계산량이 같지는 않습니다. [Artificial Analysis 리더보드](https://artificialanalysis.ai/leaderboards/models)

모바일에서는 표를 좌우로 밀어 모든 열을 확인하세요.

| 모델 | medium 지수 | max 지수 | max 과제당 비용 |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | 48 | 52 | $0.72 |
| Claude Opus 5.5 | 51 | 58 | $5.98 |
| GPT-6 Astra | 50 | 53 | $3.26 |
| Claude Fable 5.1 | 49 | 53 | $7.63 |

이 자료에서는 Sol이 Astra와 Fable에 가까운 종합 점수를 낮은 비용으로 얻었고, Opus의 최고 점수와는 차이가 남았습니다. 과제당 비용도 이 평가 묶음의 평균값이므로 내 PDF 한 장이나 코드 수정 한 건의 예상 요금으로 쓰면 안 됩니다.

OpenAI는 가장 어려운 과학 연구에는 여전히 Astra를 권장합니다. 평소 문서 업무의 결과만 보고 모든 난도에서 Sol이 상위 모델을 대체한다고 기대하기는 어렵습니다. [OpenAI 과학 연구 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)

### 같은 양을 처리할 때의 API 비용

API는 프로그램에서 모델을 호출하고 처리한 양만큼 요금을 내는 방식입니다. 토큰은 그 처리량을 세는 단위이며, 입력은 모델에 보낸 자료와 지시, 출력은 모델이 생성한 내용에 해당합니다. 아래 기본 단가는 100만 토큰 기준이며, GPT는 Standard, Claude는 일반 API 요금을 사용했습니다. [Sol 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Opus 요금](https://www.anthropic.com/claude-opus-5-5), [Astra 요금](https://developers.openai.com/api/docs/models/gpt-6-astra), [Fable 요금](https://www.anthropic.com/claude-fable-and-mythos-5-1)

마지막 열은 입력 10만 토큰과 출력 1만 토큰을 처리한다고 가정해 계산한 값입니다. 입력 단가에 0.1을, 출력 단가에 0.01을 곱해 더했습니다. 실제 모델을 실행한 결과가 아니며, 캐시·도구 비용·재시도·모드별 할증은 제외했습니다. 모델마다 같은 작업에 쓰는 토큰 수가 다르므로, 단가 비교와 실제 작업 비용은 구분해야 합니다.

모바일에서는 표를 좌우로 밀어 모든 열을 확인하세요.

| 모델 | 입력 / 100만 토큰 | 출력 / 100만 토큰 | 가정한 처리량의 비용 |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | $2 | $10 | $0.30 |
| Claude Opus 5.5 | $4 | $20 | $0.60 |
| GPT-6 Astra | $10 | $50 | $1.50 |
| Claude Fable 5.1 | $10 | $50 | $1.50 |

같은 자료를 반복해서 보내는 작업에서는 이전에 처리한 입력을 재사용하는 **캐시**도 비용을 바꿉니다. Sol의 캐시 입력은 100만 토큰당 $0.10이고, Opus의 캐시 읽기는 $0.20입니다. 캐시를 처음 저장하는 비용과 적용 조건은 별도로 확인해야 합니다. Sol은 입력이 27만 2천 토큰을 넘는 요청에서 전체 요청의 입력·캐시 단가가 2배, 출력 단가가 1.5배로 올라가므로, 최대 문맥 길이 안에 들어간다고 기본 요금이 유지되는 것은 아닙니다. [Sol 상세 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Opus 상세 요금](https://www.anthropic.com/claude-opus-5-5)

이 단가는 ChatGPT나 Claude의 월 구독료와도 다릅니다. API가 저렴하다는 이유로 같은 구독 금액에서 작업을 몇 배 더 할 수 있다고 계산할 수는 없습니다. 구독을 바꿀 계획이라면 실제 이용 화면의 한도와 필요한 기능을 별도로 확인해야 합니다.

### Claude 사용자라면 무엇부터 비교할까?

이미 Opus로 만든 결과에 만족한다면 계속 사용하되, 최근에 수정이 많았던 PDF 분석이나 코드 작업 한 건을 Sol에도 맡겨 보세요. 문서에서는 표의 수치와 각주를 제대로 반영했는지, 코드에서는 요구한 동작을 구현하고 기존 기능을 유지했는지를 보세요. 같은 자료와 완료 조건을 주고, 첫 답변보다 **수정까지 마친 결과에 걸린 시간과 비용**을 비교해야 전환할 이유가 보입니다.

API로 문서 분석이나 업무 자동화를 반복하는 경우에는 Sol을 먼저 시험할 근거가 비교적 분명합니다. 반대로 비용보다 어려운 문제의 해결 가능성이 중요하다면 Opus도 함께 시험하고, OpenAI 도구를 쓰는 과학 연구 작업에서는 Astra를 남겨 둘 이유가 있습니다. Fable 5.1을 이미 사용 중이라면 종합 점수만으로 더 비싼 요금을 계속 낼 이유를 단정하지 말고, 현재 작업에서 그 비용을 보완할 결과가 나오는지 확인하세요.

### 참고 자료

- [OpenAI: GPT-6.1 Sol 출시 안내와 업무별 평가](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)
- [OpenAI API: GPT-6.1 Sol 사양과 상세 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [Anthropic: Claude Opus 5.5 발표와 평가 조건](https://www.anthropic.com/claude-opus-5-5)
- [Anthropic: Claude Fable 5.1 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [OpenAI API: GPT-6 Astra 요금](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [Artificial Analysis: 독립 모델 평가 리더보드](https://artificialanalysis.ai/leaderboards/models)
- [Artificial Analysis: Intelligence Index 평가 구성](https://artificialanalysis.ai/models/claude-opus-5-5)
