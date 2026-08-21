---
title: "중국 AI가 만만치 않은 이유 - 딥시크 이후 넓어진 경쟁"
slug: china-ai-rewrites-the-race
date: 2026-08-21
category: "Trends"
subcategory: "AI 뉴스 · 테크 · 산업"
status: ready
format: rich-post-v2
tags: [중국 AI, 딥시크, Kimi K3, Qwen, 오픈웨이트, AI 산업]
summary: "중국 AI의 경쟁력을 최신 모델 점수 하나가 아니라 성능·비용·개발 생태계의 세 축으로 확인합니다. 미국의 우위와 중국 모델의 한계까지 함께 짚습니다."
hero_image: assets/china-ai-logo-roster-hero-v7.png
published_url: ""
sources:
  - https://www.joongang.co.kr/article/25453502
  - https://hai.stanford.edu/ai-index/2026-ai-index-report
  - https://hai.stanford.edu/assets/files/hai-digichina-issue-brief-beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-policy-implications.pdf
  - https://artificialanalysis.ai/models/kimi-k3/
  - https://artificialanalysis.ai/models/qwen3-8-max
  - https://artificialanalysis.ai/models/glm-5-2/
  - https://artificialanalysis.ai/models/deepseek-v4-pro
  - https://artificialanalysis.ai/models/claude-fable-5/
  - https://artificialanalysis.ai/models/gpt-5-6-sol-medium/
  - https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
---

안녕하세요. dev.log입니다.

AI 시장을 볼 때 ChatGPT, Claude, Gemini만 떠올려도 큰 문제가 없던 시기가 있었습니다. 그런데 [중앙일보는 8월 15일](https://www.joongang.co.kr/article/25453502) 중국 모델 4개가 AI 종합 평가 톱10에 들었고, 일부 모델의 출력 단가는 미국 선두 모델의 약 10분의 1이라고 보도했습니다.

같은 시점의 공개 자료를 다시 묶으니 더 현실적인 결론이 나왔습니다. **중국 AI를 값싼 모방품으로 보고 비교 대상에서 빼는 판단은 이미 위험합니다.** 딥시크 한 곳을 넘어 여러 연구소가 성능, 가격, 배포 방식에서 미국 선두권을 압박하고 있기 때문입니다.

{{media:china-ai-race-hero}}

### 톱10보다 중요한 세 가지 신호

순위표는 빠르게 바뀝니다. 평가 문제나 추론 강도가 달라지면 같은 모델의 점수도 움직입니다. 중국 AI가 실제 경쟁자인지 보려면 최고점 하나보다 다음 세 질문이 더 유용합니다.

1. 서로 다른 중국 개발사의 모델이 미국 선두권 성능에 반복해서 가까워지고 있는가?
2. 비슷한 능력을 훨씬 낮은 가격에 제공하는 모델이 여럿인가?
3. 공개된 가중치가 다운로드와 파생 모델로 이어져 개발자 생태계를 넓히고 있는가?

2026년 8월 21일에 확인한 자료에서는 세 항목이 모두 충족됐습니다. 중국의 전면 역전까지 증명된 것은 아닙니다. 미국은 투자와 데이터센터, 최상위 모델 수에서 여전히 앞서 있습니다. 보안과 검열 문제도 실제 도입 단계에서 따로 확인해야 합니다.

{{media:china-ai-three-signals}}

### 네 연구소가 동시에 선두권에 진입

[Artificial Analysis Intelligence Index v4.1.1](https://artificialanalysis.ai/)은 독립 평가 지수입니다. 수학, 코딩, 과학, 도구 사용 등 9개 평가를 묶습니다. Kimi K3는 60점, Qwen3.8 Max는 58점을 기록했습니다. GLM-5.2와 DeepSeek V4 Pro 0813은 각각 53점이었습니다. 같은 평가의 미국 모델 Claude Fable 5는 62점이었습니다.

| 개발사·모델 (추론 설정) | 지수 점수 | 입력·출력 100만 토큰 가격 | 공개 방식 |
|---|---:|---:|---|
| Moonshot AI · Kimi K3 (max) | 60 | 3달러 · 15달러 | 오픈웨이트 |
| Alibaba · Qwen3.8 Max (default) | 58 | 2달러 · 6달러 | 폐쇄형 |
| Z AI · GLM-5.2 (max) | 53 | 1.40달러 · 4.40달러 | 오픈웨이트 |
| DeepSeek · V4 Pro 0813 (max) | 53 | 1.32달러 · 3.96달러 | 오픈웨이트 |
| Anthropic · Claude Fable 5 (max·Opus 4.8 fallback) | 62 | 10달러 · 50달러 | 폐쇄형 |
| OpenAI · GPT-5.6 Sol (medium) | 56 | 5달러 · 30달러 | 폐쇄형 |

이 표는 2026년 8월 21일의 같은 지수 버전과 평가 묶음으로 모은 스냅샷입니다. `max`와 `medium`, `default`는 평가 때 사용한 추론 강도를 가리킵니다. `fallback`은 Fable 5가 필요할 때 Opus 4.8로 작업을 넘기는 설정입니다. 추론 강도와 fallback 사용 여부가 달라 통제된 일대일 실험은 아닙니다. 점수는 높을수록 좋지만 설정 차이까지 성능 차이로 단정할 수 없습니다.

중국 쪽에는 [Kimi K3](https://artificialanalysis.ai/models/kimi-k3/)와 [Qwen3.8 Max](https://artificialanalysis.ai/models/qwen3-8-max)가 있습니다. [GLM-5.2](https://artificialanalysis.ai/models/glm-5-2/)와 [DeepSeek V4 Pro](https://artificialanalysis.ai/models/deepseek-v4-pro)도 함께 놓았습니다. 네 모델은 [Claude Fable 5](https://artificialanalysis.ai/models/claude-fable-5/) 점수의 85.5~96.8% 구간에 들어왔습니다. 설정 차이를 감안해도 네 개발사가 동시에 상위 점수대에 나타났다는 관찰은 남습니다. 딥시크 하나가 사라지면 끝날 흐름으로 보기 어려운 이유입니다.

[Stanford HAI와 DigiChina의 2025년 12월 보고서](https://hai.stanford.edu/assets/files/hai-digichina-issue-brief-beyond-deepseek-chinas-diverse-open-weight-ai-ecosystem-policy-implications.pdf)는 당시 강력한 모델을 공개하는 중국 조직이 12곳을 넘는다고 정리했습니다. Alibaba는 여러 크기와 형태의 Qwen 계열을 운영했습니다. Moonshot AI와 Z AI, DeepSeek도 각자의 주력 모델을 내놓았습니다. 2026년 8월 점수표에 이 네 곳이 다시 나타났습니다. 이제 중국 AI를 한 회사의 성패만으로 설명하기 어렵습니다.

### 낮은 가격이 바꾸는 모델 선택표

중앙일보가 가격 비교에 사용한 [Claude Fable 5](https://artificialanalysis.ai/models/claude-fable-5/)는 이 표에서 62점으로 가장 높습니다. 출력 가격도 100만 토큰당 50달러로 매우 비쌉니다. 이 모델을 기준으로 Qwen3.8 Max, GLM-5.2, DeepSeek V4 Pro의 출력 가격은 7.9~12%, Kimi K3는 30%입니다.

두 번째 미국 비교점인 [GPT-5.6 Sol medium](https://artificialanalysis.ai/models/gpt-5-6-sol-medium/)은 56점, 출력 30달러입니다. 이를 기준으로 Qwen3.8 Max·GLM-5.2·DeepSeek V4 Pro는 13.2~20%, Kimi K3는 50%입니다. ‘10분의 1’은 고가의 Fable 5와 일부 중국 모델을 짝지었을 때 나오는 값이며, 미국과 중국 모델 전체의 고정 가격 차이가 아닙니다.

가격이 낮아질수록 최고 점수만으로 모델을 고르기 어려워집니다. 고객 문의 분류, 문서 요약, 코드 초안은 모델을 많이 호출합니다. 이런 작업에서는 2~3점의 성능 차이보다 월간 비용과 자체 운영 가능성이 더 중요할 수 있습니다. 최고 모델 하나가 시장 전체를 가져가기 어려운 이유입니다.

토큰 단가가 낮아도 실제 작업이 저렴하다는 보장은 없습니다. 답변이 길어지거나 실패 후 재시도가 늘면 총비용이 커집니다. 캐시 할인, 서버 운영비, 보안 검토와 사람의 재검수도 빠져 있습니다. 실제 도입에서는 같은 업무 입력으로 정확도와 완수 비용을 함께 재야 합니다.

### 오픈웨이트가 넓힌 개발자 생태계

오픈웨이트 모델은 학습이 끝난 가중치를 내려받아 자체 서버에서 실행하거나 목적에 맞게 추가 학습할 수 있습니다. API 제공사의 정책과 가격에만 의존하지 않고 제품 안에 모델을 넣을 여지가 생깁니다. 학습 데이터와 개발 과정까지 모두 공개하는 완전한 오픈소스와는 범위가 다릅니다.

확산 지표에서도 변화가 보입니다. Stanford 보고서는 2024년 8월부터 2025년 8월까지 Hugging Face 다운로드를 지역별로 나눴습니다. 중국 개발자 모델의 비중은 17.1%로 미국 개발자의 15.8%를 근소하게 앞섰습니다. 2025년 9월 새로 올라온 파인튜닝·파생 모델 중 중국 기반 모델의 비중은 63%였습니다.

다운로드는 실제 매출이나 기업 도입과 다릅니다. 이 수치는 2025년 공개 생태계의 스냅샷이므로 2026년 현재 점유율로 읽어서도 안 됩니다. 당시 개발자가 중국 모델을 내려받고 그 위에 새 모델을 만들기 시작했다는 확산 신호로 범위를 한정할 수 있습니다.

### 미국의 자본·인프라 우위

중국 AI의 추격 속도를 인정해도 미국을 넘어섰다고 결론 내릴 근거는 부족합니다. [Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)은 2026년 3월 두 나라의 최상위 모델 성능 차이를 2.7%로 봤습니다. 반면 미국의 2025년 민간 AI 투자는 2,859억 달러로 중국의 124억 달러보다 23배 이상 많았습니다. 미국이 더 많은 최상위 모델과 데이터센터를 보유했다는 점도 함께 적었습니다.

평가 방법을 바꾸면 격차도 달라집니다. 미국 NIST 산하 CAISI는 [DeepSeek V4 평가](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)에서 미국 프런티어보다 약 8개월 뒤라고 판단했습니다. DeepSeek가 고른 공개 벤치마크에서는 비슷해 보였지만, CAISI가 결과를 보기 전에 확정한 평가 묶음에서는 차이가 나타났습니다. Stanford의 2.7%와 NIST의 8개월은 서로 다른 모델과 평가를 본 결과이므로 하나만 골라 전체 진실처럼 쓰기 어렵습니다.

### 민감한 데이터를 맡기기 전 검증

오픈웨이트도 공개 범위와 안전성을 자동으로 보장하지 않습니다. [CAISI의 2025년 DeepSeek 평가](https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks)는 보안 취약성과 검열 위험을 지적했습니다. 모든 중국 모델에 그대로 적용할 결과는 아닙니다. 기업이 모델의 국적이나 가격만 보고 개인정보와 내부 문서를 맡겨서는 안 된다는 경고로는 충분합니다.

### 중국 모델을 비교표에 넣을 때

한국 기업과 개발자는 미국 모델만 넣던 비교표에 중국 선두 모델도 포함할 필요가 있습니다. 실제 한국어 업무로 성능과 총비용을 다시 재는 것이 먼저입니다. 민감한 데이터를 다룬다면 라이선스와 학습 데이터 설명을 읽고, 제공 지역과 로그 보관 조건도 확인해야 합니다. 검열과 보안 평가는 가중치 공개 여부와 별개의 항목입니다.

### 한국 AI가 먼저 증명할 현장

모델을 만드는 쪽의 과제도 선명합니다. [중앙일보 기사](https://www.joongang.co.kr/article/25453502)에서 인용한 전문가들은 한국의 제조업 기반을 살린 피지컬 AI, 온디바이스 AI와 산업 특화 모델을 후보로 들었습니다. 미국과 같은 자본 규모로 정면 대결하거나 중국과 토큰 가격만 겨루기 어려운 만큼, 실제 제조·산업 현장에서 더 정확하고 안전하게 끝낸 업무 기록이 필요합니다.

중국 AI는 아직 약점이 많고 미국의 기반도 두껍습니다. 그럼에도 성능, 가격, 개발자 확산이 여러 회사에서 동시에 움직인다는 사실은 가볍게 볼 수 없습니다. 앞으로의 모델 선택은 미국 선두만 확인하는 일에서 끝나지 않을 것입니다. 중국 모델을 실제 후보로 놓고 같은 조건에서 비교해야 하는 시점이 이미 왔습니다.
