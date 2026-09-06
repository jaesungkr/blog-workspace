---
title: "GPT-6 Astra vs. Fable 5.1 - AI 모델 비교"
slug: gpt-6-astra-vs-fable-5-1
date: 2026-09-06
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
format: rich-post-v2
tags: [GPT-6, Astra, Fable 5.1, Claude, AI 모델 비교]
summary: "GPT-6 Astra와 Claude Fable 5.1의 공식 벤치마크 9종과 외부 평가, 작업 기능, API 비용을 비교합니다."
hero_image: assets/gpt-6-astra-vs-fable-5-1-hero.png
published_url: ""
sources:
  - https://openai.com/index/gpt-6-astra/
  - https://www.anthropic.com/claude-fable-and-mythos-5-1
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://platform.claude.com/docs/en/models/fable-5-1/overview
  - https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/context-windows
  - https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://artificialanalysis.ai/models/claude-fable-5-1
  - https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2
  - https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra
---

안녕하세요. dev.log입니다.

클로드의 최신 모델 **Fable 5.1**이 공개된 지 이틀 만에 OpenAI가 **GPT-6 Astra**를 선보였습니다. 코드를 수정하고 문서를 만드는 AI를 고르는 입장에서는, 세대가 바뀐 GPT가 최신 클로드보다 얼마나 나아졌는지 궁금할 만합니다. OpenAI가 제시한 코딩·과학 평가에서는 Astra가 앞선 항목이 많지만, 외부 기관의 종합 평가에서는 Fable 5.1이 더 높은 점수를 받았습니다. [Fable 출시 안내](https://www.anthropic.com/claude/fable), [Astra 출시 평가](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)

**코딩과 데이터 분석에 쓸 새 모델을 찾는다면 Astra를 먼저 시험할 만합니다.** 다만 긴 프로젝트의 종합적인 수행 능력을 우선하거나 Claude에 작업 환경을 갖춰 놓았다면 Fable 5.1을 함께 비교할 이유가 충분합니다. 판단의 근거가 된 벤치마크와 요금은 **2026년 9월 6일 확인한 자료**를 기준으로 합니다.

{{media:astra-fable-hero}}

### GPT-6 Astra와 Fable 5.1의 등장

Astra는 OpenAI가 복잡한 추론, 코딩, 컴퓨터 조작, 조사와 문서 작성에 내놓은 상위 모델입니다. 질문에 답하는 데서 작업이 끝나지 않습니다. 앱에서 도구를 연결하면 파일을 읽고 코드를 실행하며 결과물을 만들 수 있습니다. 이런 여러 단계의 실행을 에이전트 작업이라고 부릅니다. [Astra 모델 안내](https://developers.openai.com/api/docs/models/gpt-6-astra)

{{media:openai-astra-launch}}

Fable 5.1은 Anthropic이 긴 코딩 작업과 여러 단계의 조사, 문서·표·슬라이드 작성을 강화한 모델입니다. 공식 문서는 일반적인 업무에서 Opus 5로 시작하고, 더 많은 추론이 필요하거나 기존 모델의 결과가 부족할 때 Fable 5.1을 사용하도록 안내합니다. 최고 사양 모델을 모든 짧은 질문에 쓸 필요는 없다는 뜻입니다. [Fable 모델 안내](https://platform.claude.com/docs/en/models/fable-5-1/overview)

{{media:anthropic-fable-launch}}

발표 화면에는 Mythos 5.1도 함께 등장합니다. Anthropic은 Fable과 Mythos가 같은 기반 모델을 쓰지만 안전장치와 접근 대상이 다르다고 설명합니다. 아래 비교 대상은 일반적으로 제공되는 **Fable 5.1**입니다. [Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)

### 공식 벤치마크 9종 비교

벤치마크는 모델에 정해진 과제를 주고 결과를 채점하는 평가입니다. 코딩 항목은 코드 수정과 터미널 작업을, 과학 항목은 연구 문제 해결을, 업무 항목은 여러 단계를 거치는 작업을 살펴봅니다. 아래 표는 **OpenAI 발표표에 두 모델의 수치가 모두 있는 주요 지표 9종**을 추렸습니다. 제조사가 제시한 비교이며, 각 지표는 높을수록 좋습니다. 서로 다른 행의 점수를 합쳐 총점으로 쓰지는 않습니다. [OpenAI 성능 비교표](https://openai.com/index/gpt-6-astra/)

| 평가 항목 | GPT-6 Astra | Fable 5.1 |
| --- | --- | --- |
| Terminal-Bench 4.0 · 터미널 작업 | **57.9%** | 55.8% |
| DeepSWE v1.1 · 소프트웨어 개발 | **74.1%** | 67.4% |
| FrontierCode 1.1 Extended · 코딩 | **64.5%** | 63.6% |
| AutomationBench · 업무 자동화 | **41.4%** | 31.4% |
| Terminal-Bench Science 0.1 · 과학 연구 작업 | **64.6%** | 52.6% |
| FrontierMath Tier 4 v2 · 고난도 수학 | **97.6%** | 87.8% |
| GPQA Diamond · 대학원 수준 과학 | **96.0%** | 93.7% |
| Humanity’s Last Exam · 도구 사용 | 57.2% | **65.0%** |
| ARC-AGI-2 · 추상 추론 | **95.0%** | 90.0% |

굵은 숫자는 해당 행에서 더 높은 값입니다. OpenAI는 추론 강도별 결과 중 최고점을 제시했으며, 연구 환경과 API(프로그램에서 모델을 호출하는 방식)에서 얻은 결과가 실제 ChatGPT와 다를 수 있다고 밝힙니다. 같은 시간과 비용을 쓴 비교라는 뜻은 아닙니다. FrontierCode의 Astra에는 저장소 지침을 따르고 불필요한 테스트를 줄이라는 개발자 지시가 적용되었습니다.

Astra의 강점은 과학 연구 작업과 수학에서 두드러집니다. 반면 여러 분야의 고난도 질문을 다루는 Humanity’s Last Exam에서는 Fable이 앞섭니다. Terminal-Bench나 FrontierCode처럼 차이가 작은 행까지 같은 무게로 세어 승수를 매기면, 실제 작업에서 기대할 차이를 과장하기 쉽습니다.

{{media:openai-astra-science}}

그래프는 과학 연구 작업의 해결률과 추정 API 비용을 함께 보여 줍니다. 왼쪽 위에 가까울수록 적은 비용으로 높은 해결률을 얻은 설정입니다. 모델 하나에도 점이 여러 개 있는 이유는 추론 강도를 바꿔 평가했기 때문입니다. Anthropic은 이 평가의 모델별 표준오차가 약 ±3.5~4.5점이라고 설명합니다. 작은 점수 차이를 확정적인 성능 차이로 읽지 않아야 합니다. [Fable 평가 조건](https://www.anthropic.com/claude-fable-and-mythos-5-1)

비교표에서 뺀 항목도 있습니다. OpenAI의 ARC-AGI-3 결과에는 Fable 5.1 수치가 없고, OSWorld 2.0은 양사 자료에서 과제 구성과 채점 조건이 달라 그대로 붙여 비교하기 어렵습니다. BenchCAD 역시 Claude 측 평가에 수정 사항이 있다는 주석이 있어 위 표에서 제외했습니다. 빈칸을 다른 버전 점수로 채우는 것보다 비교 가능한 범위를 남기는 편이 정확합니다. [OpenAI 평가 주석](https://openai.com/index/gpt-6-astra/), [Anthropic 평가 조건](https://www.anthropic.com/claude/fable)

### 외부 평가에서는 왜 순위가 달라질까?

Artificial Analysis는 모델을 직접 실행해 평가하는 외부 기관입니다. 이곳의 **Intelligence Index v4.2**는 코딩·추론·문서 이해·업무 수행을 합친 지수입니다. **Coding Agent Index**는 Codex나 Claude Code처럼 파일 편집과 도구 실행 환경까지 포함한 별도 평가입니다. 두 지수는 척도가 다르므로 같은 점수판으로 읽으면 안 됩니다.

문서 이해 지표인 **GDP.pdf**도 함께 볼 만합니다. 여러 PDF의 본문·표·각주에 흩어진 근거를 종합하는 평가이며, 필요한 채점 조건을 전부 충족한 과제만 성공으로 셉니다. 아래 표에서 성능 값은 높을수록, 비용은 낮을수록 좋습니다. [v4.2 평가 방식](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2)

| Artificial Analysis 평가 | GPT-6 Astra | Fable 5.1 |
| --- | --- | --- |
| Intelligence Index v4.2 · 종합 지수 | 55 | **57** |
| GDP.pdf · 모든 조건을 충족한 비율 | **33.2%** | 26.2% |
| Coding Agent Index · 9월 3일 발표 | Codex 67점 | Claude Code **70점** |
| v4.2 과제당 가중평균 비용 | **$2.57** | $6.12 |

종합 지수와 비용은 [Astra](https://artificialanalysis.ai/models/gpt-6-astra)·[Fable 5.1](https://artificialanalysis.ai/models/claude-fable-5-1)의 최신 모델 페이지, GDP.pdf는 [9월 4일 발표](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2), 코딩 지수는 [9월 3일 발표](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)에 따른 값입니다. 종합 평가는 두 모델 모두 추론을 많이 허용하는 `max` 설정이며, Fable에는 안전장치가 개입한 요청을 다른 Claude 모델로 보내는 기본 대체 처리 조건이 포함됩니다. 같은 `max`라는 이름이 동등한 연산량을 뜻하지는 않습니다.

**종합 점수는 Fable이 높아도 문서 평가의 모든 항목에서 앞서는 것은 아닙니다.** GDP.pdf에서는 Astra가 더 높은 값을 기록했습니다. 반대로 OpenAI 발표표의 개별 코딩 지표에서 Astra가 앞섰다고 해서 Claude Code까지 포함한 외부 평가에서도 같은 순서가 나오는 것은 아닙니다. 과제, 도구 환경, 추론 설정과 채점 기준이 달라지면 결과도 달라집니다.

평가 시점도 맞춰야 합니다. Intelligence Index는 **9월 4일 v4.2로 개편**되면서 업무·문서 과제와 가중치가 바뀌었습니다. OpenAI 출시 페이지에 남아 있는 v4.1.1 수치와 현재 모델 페이지 수치를 한 표에 섞지 않았습니다. 지수 하락을 며칠 사이의 모델 성능 저하로 해석해서도 안 됩니다. [평가 개편 안내](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2)

과제당 비용은 입력·캐시·추론·답변 비용을 평가별로 가중평균한 값입니다. 이 결과는 Astra의 비용 효율을 함께 검토할 근거가 되지만, 앱 구독료나 내 보고서 한 건의 견적은 아닙니다. 실제로 내보내는 답변과 추론의 양이 다르면 총비용도 달라집니다.

### 긴 작업에서 달라지는 기능

두 모델은 글과 이미지를 읽고 텍스트를 생성하며, 많은 문서를 한 번에 다룰 수 있습니다. 토큰은 AI가 글을 나누어 처리하는 단위이고, 컨텍스트 창은 입력 자료와 생성할 답변을 포함해 한 번에 다룰 수 있는 범위입니다. 다음은 앱의 업로드 한도와 구분되는 모델/API 사양입니다. [Astra 사양](https://developers.openai.com/api/docs/models/gpt-6-astra), [Fable 사양](https://platform.claude.com/docs/en/models/fable-5-1/overview)

| 모델/API 사양 | GPT-6 Astra | Fable 5.1 |
| --- | --- | --- |
| 컨텍스트 창 | 105만 토큰 | 100만 토큰 |
| 최대 출력 | 12만 8천 토큰 | 12만 8천 토큰 |
| 입력 → 출력 | 글·이미지 → 글 | 글·이미지 → 글 |
| API 모델 ID | `gpt-6-astra` | `claude-fable-5-1` |

자료가 많아지면 용량만큼 작업을 이어 가는 방식도 중요해집니다. Astra API는 외부 도구가 실행되는 동안 독립적인 작업을 진행하는 비동기 도구 호출과, 작업 도중 새 지시를 반영하는 기능을 제공합니다. 예를 들어 조사 중 보고서의 대상 독자가 달라져도 진행 중인 작업에 수정 지시를 전달하는 방식입니다. [Astra 사용 가이드](https://developers.openai.com/api/docs/guides/latest-model)

Fable 5.1에는 대화 중 추론 강도를 바꾸면서 이미 처리한 입력을 재사용하는 캐시를 유지하는 기능과, 도구 호출 사이에 진행 상황을 텍스트로 받는 기능이 있습니다. 두 기능은 베타입니다. 기본 표시 설정에서는 진행 안내가 비어 있을 수 있으므로 개발자가 표시 옵션을 설정해야 합니다. [Fable 변경 사항](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)

이 기능들은 API 통합 방식에 따라 달라집니다. 채팅 앱에서 바로 같은 동작을 기대하기보다는, 현재 쓰는 앱이 지시 변경과 진행 표시를 지원하는지 확인하는 것이 좋습니다. 또한 100만 토큰을 넣을 수 있다는 사양이 그 안의 조건을 빠짐없이 기억한다는 보장은 아닙니다.

### 같은 기본 요금, 다른 실제 비용

두 모델의 일반 입력과 출력 단가는 같습니다. 차이가 나는 부분은 캐시와 장문 입력입니다. 캐시는 반복해서 보내는 자료를 재사용하는 기능으로, 처음 저장할 때와 다시 읽을 때의 요금이 다릅니다. 아래 표는 할인이나 별도 처리 모드를 적용하지 않은 **API 표준 요금**이며, 월 구독료와 구분됩니다.

| 100만 토큰당 표준 단가 | GPT-6 Astra | Fable 5.1 |
| --- | --- | --- |
| 일반 입력 | $10 | $10 |
| 출력 | $50 | $50 |
| 캐시 읽기 | $1 | **$0.25** |
| 캐시 쓰기 | $12.50 | $12.50 · 5분 기준 |

[Astra 가격 문서](https://developers.openai.com/api/docs/models/gpt-6-astra)와 [Claude 가격표](https://platform.claude.com/docs/en/about-claude/pricing)에 따른 값입니다. Fable의 1시간 캐시 쓰기는 $20이므로 모든 보존 옵션의 가격이 같다는 뜻은 아닙니다.

Astra는 **입력이 27만 2천 토큰을 넘으면 해당 요청 전체**에 입력·캐시 단가 2배, 출력 단가 1.5배를 적용합니다. 초과분에만 붙는 요금이 아닙니다. Fable 5.1은 100만 토큰 컨텍스트에서도 장문 할증 없이 표준 단가를 적용합니다. [Astra 장문 요금](https://developers.openai.com/api/docs/models/gpt-6-astra), [Claude 장문 요금](https://platform.claude.com/docs/en/build-with-claude/context-windows)

이 차이를 확인하기 위해 두 모델에 같은 토큰 수를 넣는 가상 요청을 계산했습니다. **실제 모델 실행 결과가 아닌 단가 계산**이며, 출력에는 과금되는 추론 토큰도 포함한다고 가정했습니다. 도구 비용·세금·할인은 제외했습니다.

| 가정한 요청 1회 | GPT-6 Astra | Fable 5.1 |
| --- | --- | --- |
| 새 입력 10만 + 출력 1만 토큰 | $1.50 | $1.50 |
| 캐시 읽기 10만 + 새 입력 1만 + 출력 1만 | $0.70 | $0.625 |
| 새 입력 30만 + 출력 1만 토큰 | $6.75 | $3.50 |

캐시 행은 이미 저장된 자료에 적중한 후속 요청만 계산해 최초 저장 비용을 제외했습니다. 마지막 행의 Astra 비용은 장문 요금을 적용한 `0.3 × $20 + 0.01 × $75`입니다. 같은 문서라도 모델별 토큰 수와 출력량은 달라질 수 있습니다.

캐시 읽기 단가가 낮아도 과제당 총비용이 더 높을 수 있습니다. 재사용한 입력을 싸게 읽어도, 과제를 끝내는 동안 추론과 답변을 더 많이 생성하면 전체 비용은 늘어납니다. 반복 자료의 양뿐 아니라 실제 출력량까지 함께 확인해야 하는 이유입니다.

### 어떤 모델부터 써 볼까?

개별 벤치마크와 비용을 실제 선택에 적용하면 다음과 같이 시험 순서를 정할 수 있습니다. 이미 쓰는 앱, 반복해서 보내는 자료의 양, 결과물을 고치는 데 드는 시간을 함께 고려한 제안입니다.

| 주로 맡길 작업 | 먼저 시험할 모델 | 확인할 부분 |
| --- | --- | --- |
| 코드 수정·데이터 분석 | GPT-6 Astra | 기존 테스트 통과와 작업 비용 |
| 여러 단계의 긴 프로젝트 | Fable 5.1도 함께 비교 | 요구 사항 누락과 결과물 완성도 |
| 많은 PDF에서 근거를 종합 | GPT-6 Astra | 원문 위치와 예외 조건의 정확성 |
| 긴 자료를 반복해서 입력 | Fable 5.1 | 캐시 적중과 전체 청구액 |
| 한국어 보고서·블로그 문장 | 같은 원문으로 두 모델 비교 | 실제로 고쳐야 하는 문장과 수정 시간 |

한국어 문체는 위 성능표가 직접 평가한 항목이 아닙니다. 종합 점수만으로 한국어 글쓰기의 승자를 정하기는 어렵습니다. 평소 자주 고치는 문서 한 편을 같은 자료와 요구 사항으로 작성하게 하고, 결과에서 빠진 내용과 수정 시간을 비교하는 것이 더 직접적입니다.

접근 경로와 과금도 확인해야 합니다. Astra는 API에서 `gpt-6-astra`로 지정합니다. Fable 5.1은 Claude의 모델 선택 메뉴나 API의 `claude-fable-5-1`로 선택하며, Claude Code에서는 2.1.255 이상이 필요합니다. **Claude Pro의 Fable 5.1은 구독에 포함된 사용량 대신 별도 사용 크레딧으로 과금됩니다.** Max에는 플랜 사용량이 적용되지만 Fable용 주간 한도가 따로 있습니다. [Astra 모델 안내](https://developers.openai.com/api/docs/models/gpt-6-astra), [Fable 플랜별 이용 조건](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)

이미 Codex나 Claude Code에 자료와 도구를 연결해 두었다면 그 환경에서 먼저 비교하세요. 같은 저장소 상태와 완료 조건을 맞춘 뒤, 모델이 제출한 결과를 실제 테스트와 원문으로 확인해야 합니다. 새 모델로 바꿀 이유는 순위표의 한 칸보다 내가 맡기는 작업에서 드러납니다.

### 참고 자료

- [GPT-6 Astra 공식 발표와 벤치마크 - OpenAI](https://openai.com/index/gpt-6-astra/)
- [Fable 5.1·Mythos 5.1 발표 - Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [GPT-6 Astra 사양·가격](https://developers.openai.com/api/docs/models/gpt-6-astra) · [사용 가이드](https://developers.openai.com/api/docs/guides/latest-model)
- [Fable 5.1 사양](https://platform.claude.com/docs/en/models/fable-5-1/overview) · [변경 사항](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)
- [Claude 가격표](https://platform.claude.com/docs/en/about-claude/pricing) · [장문 요금](https://platform.claude.com/docs/en/build-with-claude/context-windows) · [플랜별 이용 조건](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- [Astra 외부 평가](https://artificialanalysis.ai/models/gpt-6-astra) · [Fable 5.1 외부 평가](https://artificialanalysis.ai/models/claude-fable-5-1)
- [Intelligence Index v4.2 개편과 문서 평가](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2)
- [Astra 코딩 에이전트 평가 발표](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)
