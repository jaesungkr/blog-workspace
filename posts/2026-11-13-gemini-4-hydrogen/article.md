---
title: "Gemini 4 Hydrogen vs Claude Sonnet 5.5 vs GPT-6.1 Terra - AI 모델 비교"
slug: gemini-4-hydrogen
date: 2026-11-13
category: "Log"
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags: [Gemini 4 Hydrogen, Gemini 3.8 Flash, Gemini 4 Argon, Gemini 4 Carbon, AI 모델 비교]
summary: "Gemini 4 Hydrogen을 Claude Sonnet 5.5·GPT-6.1 Terra와 비교합니다. Flash·Argon 사용자들의 공개 테스트, 독립 평가 비용과 Arena 순위까지 살펴봅니다."
hero_image: assets/lead.png
published_url: "https://dop3n.tistory.com/entry/Gemini-4-Hydrogen-%EB%B9%84%EA%B5%90-Claude-Sonnet-55%C2%B7GPT-61-Terra%EC%99%80-%EC%84%B1%EB%8A%A5%C2%B7%EA%B0%80%EA%B2%A9-%EC%B0%A8%EC%9D%B4"
sources:
  - https://artificialanalysis.ai/models/claude-sonnet-5-5
  - https://artificialanalysis.ai/models/gpt-6-1-terra
  - https://artificialanalysis.ai/models/gemini-4-argon
  - https://github.com/gnana70/gemini-4-hydrogen-tests/blob/main/README.md
  - https://news.ycombinator.com/item?id=50471431
  - https://www.reddit.com/r/GeminiAI/comments/1xukz84/my_test_with_gemini_4_hydrogen_compared_to_gemini/
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
  - https://deepmind.google/models/model-cards/gemini-4-hydrogen/
  - https://support.google.com/gemini/answer/18648722?hl=en
  - https://artificialanalysis.ai/models/gemini-4-hydrogen-high
  - https://artificialanalysis.ai/models/gemini-4-hydrogen
  - https://arena.ai/leaderboard/agent
  - https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity
---

안녕하세요. dev.log입니다.

구글이 11월 12일 신규 AI 모델 **Gemini 4 Hydrogen**을 공개했습니다. 일상적인 개발과 업무를 빠르게 처리하는 데 초점을 맞춘 모델입니다. 기존 Flash·Argon은 물론, Claude와 GPT를 쓰던 사람에게도 얼마나 쓸 만한 선택지가 될지 궁금해집니다.

Hydrogen은 코딩 성능뿐 아니라 작업을 끝내는 속도와 비용에서도 눈여겨볼 모델입니다. **Claude Sonnet 5.5·GPT-6.1 Terra**와 성능·가격을 비교하고, 기존 Flash·Argon에서 무엇이 달라졌는지도 살펴봤습니다.

{{media:lead}}

### Flash와 Argon을 쓰던 사람이라면

Hydrogen은 코드를 작성하고, 도구를 실행하고, 그 결과를 확인하며 다음 작업을 이어가는 모델입니다. 이런 방식을 에이전트 작업이라고 부릅니다. 예를 들어 “로그인 오류를 고쳐줘”라는 요청을 받으면 관련 파일을 찾고 수정한 뒤 테스트까지 진행하는 식입니다.

구글은 Gemini 3.8 Flash와 비교해 Hydrogen의 기본 high 설정이 작업을 2.5배 빠르게 끝냈다고 발표했습니다. 명령어를 이용해 개발 작업을 수행하는 **Terminal-Bench 4.1**의 점수는 18.2%에서 57.0%로 올랐습니다. 이 수치는 구글이 공개한 평가 조건에서 나온 결과입니다. [공식 성능 설명](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

Reddit에는 Flash와 Hydrogen을 모두 앱의 high 설정으로 실행하고 두 대화 링크를 공개한 글이 올라왔습니다. 작성자는 Hydrogen의 속도와 결과를 더 좋게 평가했습니다. [Flash·Hydrogen 비교 글](https://www.reddit.com/r/GeminiAI/comments/1xukz84/my_test_with_gemini_4_hydrogen_compared_to_gemini/)

좀 더 구체적인 사례로는 테스트 코드와 결과를 공개한 [개인 테스트 저장소](https://github.com/gnana70/gemini-4-hydrogen-tests/blob/main/README.md)가 있습니다. 계산기 구현 과제를 각 모델에 5회씩 맡겼고, 세 모델 모두 5회 성공했습니다. 작성자가 보고한 시간의 중앙값은 Hydrogen 41초, Flash 3.9분, Argon 1.9분이었습니다. 반면 주문 정보에서 정해진 값을 뽑아내는 단순 추출에서는 Flash가 9초, Hydrogen이 15초였습니다.

이 사례가 흥미로운 건 모든 작업에서 새 모델이 이겼다고 끝내지 않는다는 점입니다. **여러 단계를 거치는 코드 작업과 짧은 정보 추출은 선택 기준이 다를 수 있습니다.** 다만 소수 과제를 실행한 개인 테스트이며, 제가 코드를 재실행한 결과는 아닙니다. 공개 조건과 원본을 함께 볼 수 있는 초기 참고 사례로 읽는 편이 맞습니다.

### Sonnet 5.5·Terra와 코딩 성능 비교

다른 회사 모델과 비교하면 강점과 약점이 더 잘 보입니다. 아래는 구글 모델카드의 비교 결과입니다. 모두 높은 점수가 좋으며, 독립 평가가 아니라 구글이 공개한 수치입니다.

| 구글 공개 평가 | Hydrogen | Sonnet 5.5 | GPT-6.1 Terra |
|---|---:|---:|---:|
| SWE-sweep · 버그 수정 | 13.5% | 3.1% | 5.8% |
| Terminal-Bench 4.1 · 터미널 개발 작업 | 57.0% | 63.9% | 미공개 |
| AutomationBench-AA · 업무 자동화 | 76.1% | 71.8% | 60.2% |
| OSWorld-2.1 · PC 화면 조작, 오프라인 평가 | 77.6% | 83.9% | 74.2% |

Hydrogen은 버그 수정과 업무 자동화에서 앞서지만, 터미널 작업과 PC 화면 조작에서는 Sonnet 5.5가 더 높은 점수를 받았습니다. “코딩에 좋다”는 말도 어떤 일을 시키느냐에 따라 달라지는 셈입니다. 사용한 도구와 실행 설정도 결과에 영향을 줍니다. [구글 모델카드](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)

{{media:benchmarks}}

실제 결과물을 보고 싶다면 Hacker News에 올라온 이미지→HTML 비교가 참고할 만합니다. 한 사용자가 같은 디자인을 바탕으로 만든 [Hydrogen 결과](https://html.non.io/lcars-gemini-4-hydrogen)와 [Sonnet 5.5 결과](https://html.non.io/lcars-sonnet-5.5/)를 공개했습니다. 작성자는 Hydrogen의 복잡한 화면 구성 처리에 좋은 평가를 남겼습니다. 다만 한 디자인에 대한 개인 평가이므로, UI 제작 전반의 우열로 확대해서 읽지는 않았습니다. [원문 댓글](https://news.ycombinator.com/item?id=50471431)

### 독립 평가에서는 성능과 비용이 어떻게 갈릴까

Hydrogen API에는 low·medium·high·xhigh 네 가지 추론 설정이 있습니다. 답을 내기 전에 얼마나 깊게 계산할지 정하는 옵션이며, 기본값은 high입니다. 같은 모델이라도 설정에 따라 기다리는 시간과 비용이 달라집니다.

독립 평가 업체 Artificial Analysis는 코딩·업무·지식 등 여러 시험을 묶은 **Intelligence Index**와 작업당 시간·비용을 공개합니다. 11월 13일 확인한 수치입니다.

| 모델·추론 설정 | 종합 점수 | 평가 작업당 시간 | 평가 작업당 비용 |
|---|---:|---:|---:|
| Hydrogen high | 51 | 7.9분 | $1.87 |
| Hydrogen xhigh | 54 | 13.7분 | $3.16 |
| Sonnet 5.5 max · 기본 fallback | 55 | 34.1분 | $10.02 |
| GPT-6.1 Terra max | 51 | 14.6분 | $0.96 |
| Argon high | 50 | 30.0분 | $4.97 |

같은 평가 묶음이지만 추론 설정은 서로 다릅니다. 시간과 비용은 평가 작업의 가중 평균이며, 일반 채팅 한 번의 대기 시간이나 요금이 아닙니다. [Hydrogen high](https://artificialanalysis.ai/models/gemini-4-hydrogen-high) · [xhigh](https://artificialanalysis.ai/models/gemini-4-hydrogen) · [Sonnet](https://artificialanalysis.ai/models/claude-sonnet-5-5) · [Terra](https://artificialanalysis.ai/models/gpt-6-1-terra) · [Argon](https://artificialanalysis.ai/models/gemini-4-argon)

이 표에서는 **Hydrogen high가 Terra max와 같은 51점을 받으면서 더 빨리 끝났지만, 비용은 Terra가 더 낮았습니다.** Sonnet max는 55점으로 가장 높았고, 시간과 비용도 가장 컸습니다. Hydrogen xhigh는 54점까지 올라가지만 high보다 작업당 비용이 약 69%, 시간이 약 73% 늘어났습니다.

표의 작업당 비용은 Terra가 가장 낮고, Hydrogen high는 처리 시간이 가장 짧습니다. Hydrogen의 장점은 이 속도와 성능의 균형에 있습니다. 반복 작업을 빠르게 끝내려면 high부터, 어려운 작업의 결과가 부족하면 xhigh를 비교해보는 순서가 자연스럽습니다.

{{media:thinking}}

### Arena에서는 어느 정도일까

실제 사용자와 일을 이어갈 때도 좋은 결과를 내는지 궁금해집니다. **Agent Arena**는 작업 성공 신호, 사용자 반응, 수정 요청을 따르는 정도 등을 실제 에이전트 세션에서 집계합니다. 웹사이트 결과물을 나란히 비교하는 WebDev 순위와는 평가 방식이 다릅니다.

11월 13일 확인한 페이지에는 11월 11일 기준이라는 날짜가 표시돼 있었고, Hydrogen high는 5위였습니다. 비교할 만한 Gemini 모델과 이전 글에서 다룬 Fable·Astra를 함께 정리했습니다.

| Agent Arena 전체 순위 | 모델·설정 | 집계 세션 |
|---|---|---:|
| 1위 | Fable 5.2 Max | 7,841 |
| 3위 | Carbon High | 61,473 |
| 5위 | Hydrogen High | 6,465 |
| 7위 | GPT-6 Astra Max | 15,664 |
| 11위 | Argon High | 54,066 |

Hydrogen에는 **Preliminary**, 즉 초기 결과 표시가 붙어 있습니다. 모델마다 맡은 작업과 설정, 표본 수가 달라서 이 표로 동일한 업무의 처리 속도를 계산하기는 어렵습니다. 현재 표에서 Hydrogen은 Argon보다 위에 있지만, 집계 세션은 훨씬 적습니다. [Agent Arena](https://arena.ai/leaderboard/agent)

### API 가격과 실제 작업비

API는 앱 구독과 별도로, 프로그램에서 모델을 호출하고 처리량에 따라 비용을 내는 방식입니다. Hydrogen의 표준 단가는 입력 100만 토큰당 **$1.50**, 출력 100만 토큰당 **$7.50**입니다. 토큰은 글과 자료를 모델이 처리하는 단위입니다. 구글은 100만 토큰 문맥 범위 전체에 같은 단가를 적용한다고 밝혔습니다. [공식 가격](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

같은 양의 토큰을 처리할 때의 차이도 보겠습니다. 아래 경쟁 모델 단가는 Artificial Analysis에 표시된 표준 단가 기준입니다. 앱 구독료와는 별개입니다.

| 모델 | 입력 100만 토큰 | 출력 100만 토큰 | 입력 10만 + 과금 대상 출력 1만 토큰 가정 |
|---|---:|---:|---:|
| Hydrogen | $1.50 | $7.50 | $0.225 |
| Sonnet 5.5 | $2.00 | $10.00 | $0.300 |
| GPT-6.1 Terra | $1.00 | $5.00 | $0.150 |

캐시 할인과 별도 도구 요금을 제외한 계산입니다. 같은 토큰 사용량이라면 Hydrogen은 Sonnet보다 저렴하고 Terra보다 비쌉니다. 하지만 실제 작업에서는 모델마다 생각하는 길이와 재시도 횟수가 다릅니다. 그래서 앞의 평가 작업비는 이 단가 비율과 일치하지 않습니다.

### 무료 계정에서 쓰는 방법

개인 Google 계정 기준으로 무료 이용자는 **Auto**를 켰을 때 질문에 따라 Hydrogen으로 연결됩니다. 대부분의 가벼운 질문에는 Flash-Lite가 쓰이고, 더 많은 추론이 필요하면 Hydrogen이 선택될 수 있습니다. Auto를 끄면 Flash-Lite만 사용합니다.

| 이용 환경 | Hydrogen 접근 방식 |
|---|---|
| Gemini 무료 계정 | Auto가 질문에 따라 선택 |
| Google AI Plus·Pro·Ultra | 채팅에서 Hydrogen 직접 선택 가능 |
| Google Antigravity | 유료 Pro·Ultra에 제공 |

어떤 모델이 답했는지는 응답 아래 메뉴의 **응답 세부정보(See response details)**에서 확인할 수 있습니다. 회사·학교 계정은 Workspace 계약에 따라 제공 범위가 달라집니다. [Gemini 앱 도움말](https://support.google.com/gemini/answer/18648722?hl=en) · [Antigravity 제공 조건](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)

앱의 추론 설정은 Low·Medium·High이고, API의 xhigh와 구분해야 합니다. 모델 이름이 같아도 앱과 API의 설정·사용량 한도는 다릅니다.

### Carbon과 나눠서 일하는 방식

개발용 도구 Antigravity에는 **Orchestrator**도 함께 추가됐습니다. 한 작업 안에서 Carbon이나 Argon과 Hydrogen을 필요에 따라 바꿔 쓰는 기능입니다.

구글이 제시한 예에서는 Carbon이 먼저 파일 사이의 관계를 파악하고 수정 계획을 세웁니다. Hydrogen이 코드를 고치고 테스트를 실행하다 막히면, Carbon이 다시 상황을 보고 계획을 수정합니다. 처음 요청을 한 번 분류해서 모델을 정하는 방식보다 작업 도중 생기는 문제에 대응하기 쉽도록 설계했습니다. [Orchestrator 설명](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)

예를 들어 게임의 저장 기능을 고칠 때, 저장 구조와 기존 데이터 호환성은 깊게 검토하고 반복적인 파일 수정은 빠르게 처리하는 식으로 역할을 나눌 수 있습니다. 게임 사례는 역할 분담을 설명하기 위한 가상 예시입니다. Pro에는 Argon 조합, Ultra에는 Carbon과 Argon 조합이 제공됩니다.

### 빠르게 일할 모델을 고른다면

공개된 자료에서는 각 모델을 고를 이유가 꽤 분명합니다. **Hydrogen high는 반복 작업의 대기 시간을 줄이는 쪽**, Sonnet 5.5는 터미널 개발과 PC 조작의 공개 성능, Terra는 낮은 API 단가와 독립 평가 작업비가 눈에 띕니다. 기존 Flash도 개인 테스트의 단순 추출에서는 더 빠른 결과를 냈습니다.

Hydrogen은 Flash보다 개선된 코딩 성능과 Argon보다 짧은 평가 시간을 보여줬습니다. **속도가 중요한 반복 작업에는 Hydrogen high가 눈에 띄고**, 비용이나 터미널 작업의 성공률을 우선하면 Terra와 Sonnet의 강점도 분명합니다.

### 참고 자료

- [Google: Gemini 4 Hydrogen 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
- [Google DeepMind: 모델카드](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)
- [Google: Gemini 앱 모델과 이용 조건](https://support.google.com/gemini/answer/18648722?hl=en)
- [Google Antigravity: Hydrogen과 Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)
- [Artificial Analysis: high](https://artificialanalysis.ai/models/gemini-4-hydrogen-high) · [xhigh](https://artificialanalysis.ai/models/gemini-4-hydrogen)
- [Agent Arena](https://arena.ai/leaderboard/agent)
