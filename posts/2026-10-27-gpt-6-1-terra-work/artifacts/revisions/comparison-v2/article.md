---
title: "GPT-6.1 Terra vs Claude Opus 5.5, 성능과 가격으로 본 선택"
slug: gpt-6-1-terra-work
date: 2026-10-27
category: "Log"
subcategory: "AI 모델 · 비교"
status: reviewing
format: rich-post-v2
tags: [GPT-6.1 Terra, Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra, AI 모델 비교]
summary: "Terra와 Opus 5.5의 공식 평가·독립 지수·초기 후기·API 비용을 비교해 기존 모델을 유지할 작업과 Terra를 검토할 작업을 나눕니다."
hero_image: assets/terra-opus-comparison-v2.png
published_url: ""
sources:
  - https://openai.com/index/introducing-gpt-6-1-terra/
  - https://developers.openai.com/api/docs/models/gpt-6.1-terra
  - https://platform.claude.com/docs/en/models/opus-5-5/overview
  - https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5
  - https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier
  - https://artificialanalysis.ai/models/gpt-6-1-terra
  - https://artificialanalysis.ai/models/claude-opus-5-5
  - https://artificialanalysis.ai/models/gpt-6-1-sol
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://learn.chatgpt.com/docs/models
---

안녕하세요. dev.log입니다.

OpenAI가 새 작업용 AI인 **GPT-6.1 Terra**를 공개했습니다. 화면 속 자료를 읽고 앱을 조작하거나 글을 쓰는 모델입니다. 이미 클로드나 Sol을 쓰고 있다면, 더 저렴한 Terra로 바꿔도 원하는 결과를 얻을 수 있을지 궁금해집니다.

**화면 기반 반복 업무와 API 비용 절감에는 Terra를 검토할 만하고, 어려운 작업의 해결 능력을 우선한다면 Opus를 유지할 이유가 있습니다.** 독립 종합 평가에서는 Opus가 앞서지만, Terra의 기본 API 단가는 Opus의 4분의 1입니다. 2026년 10월 27일 확인한 공식 자료와 독립 평가, 초기 공개 후기를 나눠 살펴봤습니다.

{{media:terra-lead}}

### Terra의 특징과 Opus를 비교하는 이유

Terra는 OpenAI가 시각적 추론과 컴퓨터 조작, 글쓰기에 초점을 맞춰 소개한 모델입니다. 상품 사진을 카탈로그 항목과 대조하거나, 화면에 있는 정보를 읽어 앱에 입력하는 일을 떠올리면 됩니다. [Terra 모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)

비교할 모델은 **Claude Opus 5.5**입니다. Anthropic은 Opus를 장시간 코딩과 지식 업무용으로 안내합니다. OpenAI의 Terra 발표에도 Opus와 비교한 작업 비용과 과학 연구 평가가 있어, 작업을 맡길 후보로 함께 살펴볼 수 있습니다. OpenAI 안에서의 위치는 Sol 6.1과 Astra를 보조 기준으로 확인하겠습니다. [Opus 모델 문서](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Terra 발표](https://openai.com/index/introducing-gpt-6-1-terra/)

Terra는 일반 Chat에는 제공되지 않습니다. Plus·Pro·Business·Enterprise·Edu의 ChatGPT Work와 Codex에서 이용하며, 웹이나 데스크톱의 Work에서는 Advanced 모델 목록에서 선택합니다. 계정과 관리자 설정에 따라 제공 여부가 달라질 수 있습니다. [ChatGPT 이용 안내](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)

### 공식 평가에서 드러난 화면 작업의 강점

OpenAI가 소개한 평가는 서로 다른 일을 측정합니다. **MMMU-Pro**는 이미지가 포함된 여러 분야의 문제를 이해하는 능력, **Agents’ Last Exam**은 도면을 3D 모형으로 만드는 등 도구를 사용한 전문 업무 수행, **Terminal-Bench-Science 0.1**은 코드를 이용한 과학 연구 작업을 봅니다. 성적은 높을수록 좋고, 과제당 비용은 낮을수록 적은 돈을 쓴 것입니다.

`medium`과 `max`는 모델이 답을 만들기 전에 얼마나 추론할지 조절하는 설정입니다. 같은 이름이라도 모델별 실제 계산량은 다를 수 있습니다. [추론 설정 설명](https://learn.chatgpt.com/docs/models)

아래는 [Terra 발표 본문](https://openai.com/index/introducing-gpt-6-1-terra/)에서 확인한 비교입니다. 그래프에서 읽지 못한 절대 점수는 채우지 않았습니다.

| OpenAI 공개 평가 | 발표에서 확인되는 비교 | 해석할 때의 조건 |
|---|---|---|
| MMMU-Pro · 시각 추론 | Terra가 Sol·Astra에 근접 | 해당 이미지 문제 평가 |
| Agents’ Last Exam · 전문 업무 | Terra medium이 Astra와 대등한 수준 | 발표의 중간 추론 설정 |
| 같은 전문 업무 평가의 비용 | max에서 Terra의 과제당 비용이 Opus의 약 1/9 | 토큰 사용량과 단가를 함께 반영 |
| Terminal-Bench-Science 0.1 | Terra max가 Sol을 앞서고 Opus와 5점 이내 차이 | Opus 대비 추정 비용은 1/5 미만 |

표의 비용 차이는 해당 평가의 과제와 설정에서 사용한 토큰 및 단가를 반영합니다.

Terra의 장점은 화면을 이해하고 도구를 쓰는 일부 업무에서 상위 모델에 가까운 성적을 더 적은 비용으로 제시했다는 점입니다. OpenAI는 동시에 **가장 복잡한 코딩에는 Sol과 Astra가 더 적합하다**고 안내합니다. 시각 작업의 성적과 장시간 코드 작업의 선택은 나눠 볼 필요가 있습니다.

### 독립 종합 평가에서는 Opus 우위

독립 평가 기관인 Artificial Analysis의 **Intelligence Index v4.3.2**는 코딩·문서·추론 등을 포함한 10개 평가를 묶은 지수입니다. 높을수록 이 평가 묶음에서 성적이 좋다는 의미이며, 정답률을 나타내는 백분율은 아닙니다. 아래는 10월 27일 모델별 페이지에 표시된 값입니다.

Opus 행은 Artificial Analysis가 표시한 **default fallback** 평가 구성입니다. 거절이 발생하면 다른 모델로 재시도하는 조건을 포함합니다. [Opus의 평가 조건 설명](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5) 이 표는 공개된 모델·서비스 설정을 비교한 것입니다. 동일한 `max` 표기가 같은 연산량을 보장하지 않으며, 과제당 비용도 해당 지수의 가중 평균입니다.

| 모델 · 추론 설정 | 종합 지수 ↑ | 지수 과제당 비용 ↓ |
|---|---:|---:|
| GPT-6.1 Terra · max | 48 | $0.40 |
| GPT-6.1 Sol · max | 52 | $0.72 |
| GPT-6 Astra · max | 53 | $3.26 |
| Claude Opus 5.5 · max, default fallback | 58 | $5.98 |

[Terra 측정](https://artificialanalysis.ai/models/gpt-6-1-terra), [Sol 측정](https://artificialanalysis.ai/models/gpt-6-1-sol), [Astra 측정](https://artificialanalysis.ai/models/gpt-6-astra), [Opus 측정과 평가 구성](https://artificialanalysis.ai/models/claude-opus-5-5)

이 범위에서는 Opus가 Terra보다 10점 높습니다. Terra는 비용이 크게 낮지만 종합 능력에는 격차가 남습니다. Sol과 비교해도 Terra는 4점 낮고 과제당 비용은 더 적습니다.

코딩을 좁혀 봐도 같은 구분이 필요합니다. [Artificial Analysis의 Terra 출시 분석](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier)에서는 **Coding Agent Index v2.0**이 Terra 48점, Sol 54점이었습니다. 한편 터미널에서 코딩 과제를 푸는 Terminal-Bench 4.0에서는 Terra max가 Sol과 경쟁하는 수준으로 올라왔다고 설명합니다. 특정 코딩 과제의 개선과 여러 코딩 과제를 합친 성적은 다릅니다.

이 분석은 Terra의 종합 지수 대비 비용 효율에서 `low`와 `medium`을 주목했습니다. 무조건 max를 고르는 것보다 맡길 일에 맞는 추론 설정을 함께 봐야 하는 이유입니다. 이 지수들은 한국어 블로그 문체를 직접 평가한 점수는 아닙니다.

### 초기 후기에서 갈린 속도와 사용량

출시 직후 공개 후기에는 빨라졌다는 반응이 있습니다. 한 Reddit 사용자는 평소 Sol에서 오래 기다리던 Codex 작업을 Terra가 더 빠르게 마쳤다고 평가했습니다. 다만 같은 입력과 추론 설정을 통제한 비교 자료는 제시하지 않았습니다. [Terra 속도에 관한 공개 후기](https://www.reddit.com/r/ChatGPT/comments/1xg7rfk/its_my_impression_or_terra_61_is_fing_fast/)

반대 경험도 나왔습니다. 픽셀 스타일 프로젝트 관리 화면을 만든 다른 사용자는 Terra high의 결과가 단순해 max로 올렸지만, Sol medium과 Opus medium의 결과를 더 선호했다고 썼습니다. Terra에서 더 많은 사용량을 소모했다고도 보고했습니다. 서로 다른 추론 설정과 서비스의 사용량 표시를 비교한 사례이므로 API 비용이나 모델 전체의 성능 순위로 환산할 수는 없습니다. [Terra·Sol·Opus 제작 후기](https://www.reddit.com/r/codex/comments/1xgcjjb/gpt_61_terra_on_gpt_plus/)

두 사례는 출시 직후 일부 사용자의 경험입니다. 첫 결과가 나오는 속도와 원하는 결과까지 수정하는 데 드는 시간·사용량은 다르게 느껴질 수 있습니다. 장기 안정성이나 한국어 작업의 만족도는 이 후기만으로 판단하기 어렵습니다.

### 기본 API 단가는 Opus의 4분의 1

API는 프로그램에서 모델을 호출하고 사용량만큼 요금을 내는 방식으로, ChatGPT·Claude의 월 구독료와 별도입니다. 아래는 10월 27일 확인한 표준 텍스트 단가이며, **100만 토큰당 미국 달러**입니다. 토큰은 모델이 글 등을 처리하는 단위로 한국어 글자 수와 일치하지 않습니다.

| 모델 | 기본 입력 | 출력 | 캐시 입력 |
|---|---:|---:|---:|
| GPT-6.1 Terra | $1 | $5 | $0.05 |
| Claude Opus 5.5 | $4 | $20 | $0.20 |
| GPT-6.1 Sol | $2 | $10 | $0.10 |
| GPT-6 Astra | $10 | $50 | $1 |

[Terra 요금](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Opus 요금](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5), [Sol 요금](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra 요금](https://developers.openai.com/api/docs/models/gpt-6-astra)

캐시 입력은 이미 보낸 자료를 다시 사용할 때 적용됩니다. 캐시를 처음 저장하는 비용은 별도입니다. 기본 입력 10만 토큰과 청구 대상 출력 1만 토큰을 쓴다고 가정하면 Terra는 **$0.15**, Opus는 **$0.60**, Sol은 **$0.30**, Astra는 **$1.50**입니다. 입력 단가에 0.1, 출력 단가에 0.01을 곱해 더했습니다. 캐시·도구·모드별 할증·세금은 제외한 계산 예시입니다.

고정한 처리량으로 Terra를 네 번 호출하면 Opus 한 번과 같은 텍스트 비용입니다. 저렴한 모델이 같은 결과를 내기 위해 몇 번 더 수정해야 하는지도 선택에 영향을 줍니다. 실제 재시도에서는 대화가 길어지고 출력량도 바뀌므로, 네 번이라는 값은 위 가정에서만 성립합니다.

또한 Terra는 입력이 **272,000토큰을 넘으면 요청 전체의 입력·캐시 단가가 2배, 출력 단가가 1.5배**가 됩니다. 길게 이어지는 작업에서는 첫 요청의 단가뿐 아니라 마지막 수정까지 쓴 토큰을 확인해야 합니다. [Terra 장문 과금 조건](https://developers.openai.com/api/docs/models/gpt-6.1-terra)

### 지금 쓰는 모델을 바꿀 만할까

공개 평가와 비용을 실제 작업에 대입하면 다음처럼 나눠 볼 수 있습니다.

| 지금 맡기는 일 | 선택 방향 | 판단 근거 |
|---|---|---|
| 화면·이미지 해석 후 반복 입력 | Terra 검토 | 공식 시각·도구 평가와 낮은 단가 |
| 어려운 코드·추론, Opus 결과에 만족 | Opus 유지 | 독립 종합 지수의 격차, 작업 품질 우선 |
| 복잡한 업무와 비용을 함께 고려 | Sol도 비교 | Terra보다 높은 종합·코딩 지수 |
| Astra로 고난도 연구·판단 수행 | 필요한 작업에 유지 | OpenAI가 권장하는 최고 난도 용도 |

Astra의 용도는 [공식 모델 선택 안내](https://learn.chatgpt.com/docs/models)를 기준으로 했습니다. 이 표는 공개 근거를 종합한 작업별 선택이며 직접 실행한 성능 순위가 아닙니다.

같은 품질에 도달할 때까지 수정이 크게 늘어나면 Terra의 비용 절감 효과가 줄어듭니다. 비교할 작업을 고른다면 이미지에서 항목을 읽어 입력하는 업무 한 건처럼 결과를 확인할 수 있는 대상을 정하고, 누락·오입력과 완료까지의 총비용을 함께 보는 편이 좋습니다.

### 참고 자료

- 공식 발표·문서: [Terra 발표](https://openai.com/index/introducing-gpt-6-1-terra/), [Terra API](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Opus API](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Opus 요금](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5), [Sol API](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra API](https://developers.openai.com/api/docs/models/gpt-6-astra), [Work 제공 범위](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)
- 독립 평가: [Terra 출시 분석](https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier), [Terra](https://artificialanalysis.ai/models/gpt-6-1-terra), [Opus](https://artificialanalysis.ai/models/claude-opus-5-5), [Sol](https://artificialanalysis.ai/models/gpt-6-1-sol), [Astra](https://artificialanalysis.ai/models/gpt-6-astra)
- 공개 사용자 경험: [속도 후기](https://www.reddit.com/r/ChatGPT/comments/1xg7rfk/its_my_impression_or_terra_61_is_fing_fast/), [제작 결과와 사용량 후기](https://www.reddit.com/r/codex/comments/1xgcjjb/gpt_61_terra_on_gpt_plus/)
