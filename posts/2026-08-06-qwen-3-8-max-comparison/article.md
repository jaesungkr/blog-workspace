---
title: "Qwen3.8-Max 성능 비교, 중국 AI의 추격은 어디까지 왔나"
slug: qwen-3-8-max-comparison
date: 2026-08-06
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
format: rich-post
tags: [Qwen3.8-Max, Qwen3.7-Max, Kimi K3, Qwen, Alibaba Cloud, AI 모델 비교, 오픈웨이트]
summary: "Qwen3.8-Max의 2.4조·950억 활성 구조, 공식표 30개 재계산, Arena 순위, 가격과 공개 가중치 현황을 Qwen3.7-Max·Kimi K3와 비교합니다."
hero_image: assets/screenshots/qwen38-official-hero.webp
published_url: ""
sources:
    - https://qwen.ai/blog?id=qwen3.8
    - https://x.com/Alibaba_Qwen/status/2084100707423289643
    - https://docs.qwencloud.com/developer-guides/getting-started/text-generation-models
    - https://www.alibabacloud.com/help/en/model-studio/model-pricing
    - https://arena.ai/leaderboard
    - https://github.com/MoonshotAI/Kimi-K3
    - https://huggingface.co/Qwen/models
---

안녕하세요. dev.log입니다.

새 AI 모델이 나올 때마다 “가장 강력하다”는 문구와 큰 숫자가 먼저 보입니다. 이때 필요한 질문은 더 단순합니다. 이전 모델보다 얼마나 좋아졌는지, 다른 최상위 모델과 비교하면 어디쯤인지, 오늘 어떤 경로로 쓸 수 있는지를 따로 봐야 합니다.

`Qwen3.8-Max`는 Alibaba Qwen의 최상위 AI 모델입니다. ChatGPT나 Claude처럼 질문에 답하고, 이미지를 읽고, 코딩과 여러 단계의 도구 작업을 맡길 수 있습니다. 설치 없이 확인하려면 [Qwen Studio의 Qwen3.8-Max 직링크](https://chat.qwen.ai/?models=qwen3.8-max)가 가장 짧은 시작점입니다.

Qwen 공식 비교표의 단일 점수 30개는 Codex가 다시 계산했습니다. 공개 선호도 리더보드인 Arena와 공식 Hugging Face 조직도 같은 날 확인했습니다. 모델 답변 품질과 속도를 직접 시험한 사용기는 아니며, 공개 전 가중치의 로컬 실행 조건도 추정하지 않습니다.

{{media:qwen38-official-hero}}

### 2.4조 전체·950억 활성의 뜻

[Qwen 공식 출시 글](https://qwen.ai/blog?id=qwen3.8)은 Qwen3.8-Max를 전체 2.4조, 토큰 처리 때 활성화되는 규모 950억 파라미터의 모델로 소개합니다. 문맥 창은 100만 토큰이고 텍스트와 이미지 입력, 추론, 도구 호출을 지원합니다. 쉽게 말하면 긴 코드 저장소나 여러 문서를 한 작업 안에서 다루면서 계획과 실행을 이어 가도록 만든 최상위 등급입니다.

전체 파라미터와 활성 파라미터는 가리키는 범위가 다릅니다. 전체 2.4조는 모델이 보유한 전체 가중치 규모이고, 950억은 입력 토큰을 처리할 때 실제 계산에 참여하는 규모입니다. 활성 수가 작아도 개인 PC용 모델이 되는 것은 아닙니다. 저장·분산 배치와 실제 계산량은 별도로 따져야 합니다.

세 모델의 공개 사양과 현재 이용 상태를 같은 기준으로 놓으면 차이가 선명해집니다.

| 비교 기준 | Qwen3.8-Max | Qwen3.7-Max | Kimi K3 |
|---|---|---|---|
| 전체·활성 규모 | 2.4조·950억 | 공식 문서에 미표기 | 2.8조·1,040억 |
| 문맥 창 | 100만 토큰 | 100만 토큰 | 1,048,576 토큰 |
| 주요 입력 | 텍스트·이미지 | 텍스트 | 텍스트·이미지 |
| 공개 가중치 | 8월 3일 `다음 주` 공개 예고 | 비공개 | 공개 완료 |
| 가장 쉬운 시작 | Qwen Studio | Model Studio·QwenCloud API | Kimi 웹 |

Qwen3.8-Max의 API 가격은 [Qwen 공식 발표](https://x.com/Alibaba_Qwen/status/2084100707423289643)의 100만 토큰당 입력 2달러·출력 6달러·암시적 캐시 입력 0.25달러 기준입니다. Qwen3.7-Max는 [Alibaba Cloud 싱가포르 가격표](https://www.alibabacloud.com/help/en/model-studio/model-pricing)의 100만 토큰당 입력 2.5달러·출력 7.5달러를 사용했습니다. 지역과 프로모션에 따라 청구액은 달라질 수 있으므로 실제 전환 전에는 계정 콘솔의 단가를 다시 확인해야 합니다.

[Kimi K3 공식 모델 카드](https://github.com/MoonshotAI/Kimi-K3)는 2.8조 전체·1,040억 활성 파라미터와 공개 가중치를 확인할 수 있습니다. Qwen3.8-Max보다 전체 규모가 크다고 품질이 자동으로 높은 것은 아닙니다. 대신 지금 가중치를 내려받아 검토하고 배포해야 한다면, 아직 공개 파일이 없는 Qwen3.8-Max보다 Kimi K3가 먼저 후보가 됩니다.

### 공식 성능표 30개 재계산

Qwen의 공식 표는 Qwen3.8-Max, Qwen3.7-Max, Opus4.8, Fable5, GPT5.6 Sol 등 5개 모델을 비교합니다. 모든 행은 값이 높을수록 좋습니다. 다만 모델별 결측치가 있어 실제 비교 수는 행마다 3~5개이고, 서로 단위가 다르므로 점수를 더하거나 평균내면 안 됩니다.

Codex는 한 셀에 숫자 하나만 있는 30행을 파싱해 같은 행 안에서 순위를 다시 계산했습니다. 두 점수가 함께 적힌 `Agents' Last Exam (Pass / Score)` 한 행은 사후에 유리한 지표를 고르지 않도록 제외했습니다.

공식 출시 글은 별도로 고른 16개 지표를 그래프로 묶었습니다. 그래프에는 Gemini와 Qwen3.7 Plus가 추가되고 멀티모달 지표도 들어가므로, 아래 30행 재계산과 같은 표로 보면 안 됩니다. 이미지는 공식 발표가 강조한 전체 경향을 보여 줍니다. 이어지는 HTML 표는 공식 글의 단일 점수 30행을 따로 재계산한 결과입니다.

{{media:qwen38-official-performance}}

| 공식표 범위 | 행 수 | 1위 | 2위 | 3위 | 4위 |
|---|---:|---:|---:|---:|---:|
| 코딩 에이전트 | 12 | 1 | 6 | 3 | 2 |
| 일반 에이전트 | 8 | 1 | 3 | 2 | 2 |
| 일반 능력 | 10 | 5 | 2 | 2 | 1 |
| 합계 | 30 | 7 | 11 | 7 | 5 |

요약만 보면 비교 대상을 놓치기 쉽습니다. 아래 표는 30개 행 모두에서 Qwen3.8-Max의 값·순위·행별 1위를 보여 줍니다.

**코딩 에이전트 12개**

| 시험 | Qwen3.8-Max | 행 순위 | 행 1위 |
|---|---:|---:|---|
| Terminal Bench 2.1 | 86.6 | 2/5 | GPT5.6 Sol (88.8) |
| SWE-bench Pro | 67.7 | 3/5 | Fable5 (80.0) |
| DeepSWE 1.1 | 56.6 | 4/5 | GPT5.6 Sol (73.0) |
| NL2Repo-Bench | 55.9 | 2/3 | Opus4.8 (69.4) |
| FrontierSWE | 73.5 | 2/4 | Fable5 (88.8) |
| MLS-Bench-Lite | 41.0 | 4/5 | Fable5 (49.9) |
| PaperBench | 93.0 | 1/5 | Qwen3.8-Max (93.0) |
| AndroidBench | 75.1 | 2/5 | Fable5 (84.5) |
| QwenSWEBench | 80.7 | 3/5 | Fable5 (86.3) |
| QwenQoderBench | 58.4 | 3/5 | Fable5 (63.1) |
| QwenReactBench | 1724 | 2/5 | Fable5 (1770) |
| QwenSVGBench | 1713 | 2/5 | GPT5.6 Sol (1758) |

**일반 에이전트 8개**

| 시험 | Qwen3.8-Max | 행 순위 | 행 1위 |
|---|---:|---:|---|
| CoWorkBench | 74.8 | 2/5 | Fable5 (75.9) |
| WorkSpaceBench | 67.7 | 2/5 | Fable5 (68.7) |
| JobBench | 53.4 | 2/5 | Fable5 (57.4) |
| SkillsBench | 70.2 | 3/5 | GPT5.6 Sol (73.5) |
| Automation-Bench | 27.3 | 3/5 | GPT5.6 Sol (29.7) |
| Toolathlon Verified | 72.5 | 4/5 | Fable5 (77.9) |
| WideSearch | 81.9 | 1/4 | Qwen3.8-Max (81.9) |
| HLE w/ tools | 56.2 | 4/5 | Fable5 (64.5) |

**일반 능력 10개**

| 시험 | Qwen3.8-Max | 행 순위 | 행 1위 |
|---|---:|---:|---|
| GPQA Diamond | 92.6 | 2/5 | GPT5.6 Sol (94.1) |
| HLE | 43.6 | 4/5 | Fable5 (53.3) |
| IFBench | 82.8 | 1/5 | Qwen3.8-Max (82.8) |
| $OneMillion-Bench | 52.5 | 3/5 | Fable5 (55.9) |
| HealthBench | 60.2 | 1/4 | Qwen3.8-Max (60.2) |
| PLawBench | 73.2 | 1/5 | Qwen3.8-Max (73.2) |
| PRBench-Legal | 57.6 | 공동 1/5 | Fable5·GPT5.6 Sol·Qwen3.8-Max (57.6) |
| PRBench-Finance | 58.3 | 1/5 | Qwen3.8-Max (58.3) |
| MRCR v2 256K | 92.9 | 2/4 | GPT5.6 Sol (93.8) |
| LongBench v2 | 66.3 | 3/4 | Opus4.8 (69.1) |

가장 뚜렷한 결과는 Qwen3.8-Max가 같은 30행에서 Qwen3.7-Max를 모두 앞섰다는 점입니다. 이전 세대 대비 개선은 공식 표 안에서 일관됩니다. 반면 1위는 7개뿐이고, 코딩 12개에서는 PaperBench 한 항목만 1위입니다. “Qwen 역사상 가장 강한 모델”과 “비교한 최상위 모델을 대부분 이긴 모델”은 같은 결론이 아닙니다.

이 수치는 [Qwen이 구성한 출시 표](https://qwen.ai/blog?id=qwen3.8)를 다시 계산한 결과입니다. 시험마다 하네스·도구·추론 수준이 다르고 Qwen 자체 시험도 포함됩니다. 따라서 30개 순위는 벤더 표의 구조를 더 투명하게 읽는 자료이지, 동일 환경에서 모델을 다시 돌린 독립 벤치마크가 아닙니다.

### Arena 종합 5위

벤더 표와 별도로 [Arena 리더보드](https://arena.ai/leaderboard)를 2026년 8월 6일 확인했습니다. 당시 Text Arena에는 677개 모델이 표시됐습니다. 종합 순위는 Qwen3.8-Max 5위, Kimi K3 Max 13위, Qwen3.7-Max Preview 21위였습니다.

| Arena 항목 | Qwen3.8-Max | Qwen3.7-Max Preview |
|---|---:|---:|
| 종합 | 5위 | 21위 |
| 어려운 질문 | 6위 | 25위 |
| 코딩 | 9위 | 16위 |
| 창작 | 3위 | 33위 |
| 지시 따르기 | 9위 | 25위 |
| 긴 질문 | 5위 | 11위 |

Arena는 사람들이 두 답변을 비교해 선택한 결과를 누적하는 공개 선호도 평가입니다. 실제 사용자가 선호한 방향을 볼 수 있지만, 고정된 코드 시험이나 사실 정확도 평가와는 다릅니다. 순위도 투표가 쌓이면 바뀝니다. Qwen 공식표에서 보인 세대 향상이 독립된 공개 신호에서도 같은 방향으로 나타났다는 정도로 읽는 편이 정확합니다.

### 오픈웨이트는 아직 예고 상태

Qwen은 8월 3일 공식 출시 글에서 Max 등급 모델 최초로 가중치를 공개할 예정이며 `다음 주` 배포한다고 밝혔습니다. 8월 6일 [Qwen 공식 Hugging Face 모델 목록](https://huggingface.co/Qwen/models)을 API로 검색했을 때는 `Qwen3.8` 결과가 0개였습니다.

따라서 지금 Qwen3.8-Max를 오픈웨이트 모델이라고만 부르면 이용 가능 상태를 오해하기 쉽습니다. 정확한 표현은 **공개가 예고된 호스팅 모델**입니다. 실제 파일, 라이선스, 모델 카드, 서빙 엔진 지원이 올라온 뒤에야 다운로드 크기와 필요한 하드웨어를 계산할 수 있습니다.

Kimi K3는 공식 저장소에 가중치와 라이선스가 이미 공개됐습니다. 자체 배포가 첫 조건이면 Kimi K3가 앞섭니다. 웹·API에서 최상위 Qwen 성능을 바로 쓰려면 Qwen3.8-Max가 더 직접적인 후보입니다.

### Qwen3.8-Max 사용법

비개발자와 개발자의 시작점은 분리하는 편이 안전합니다.

| 목적 | 시작 순서 | 필요한 조건 |
|---|---|---|
| 웹에서 먼저 확인 | [Qwen Studio 직링크](https://chat.qwen.ai/?models=qwen3.8-max) 열기 → 상단 모델이 `Qwen3.8-Max`인지 확인 → 정답을 아는 작은 과제 입력 | 실제 제출 때 로그인·이용 한도가 필요할 수 있음 |
| 앱·서비스에 연결 | QwenCloud·Model Studio에서 API Key 생성 → 지역에 맞는 OpenAI 호환 Base URL 설정 → 모델 ID `qwen3.8-max` 호출 | 계정·API Key·유료 사용량 |
| 코딩 에이전트에 연결 | 공식 출시 글의 Claude Code·Codex·Qwen Code 설정에서 같은 모델 ID 사용 | 도구별 설정 파일과 환경변수 |
| 자체 서버에 배포 | 공식 가중치·라이선스·모델 카드 공개 확인 → 파일 크기·지원 엔진·GPU 구성 계산 | 8월 6일 현재 실행 불가 |

첫 시험은 “좋은 웹사이트를 만들어 줘”처럼 판정이 모호한 과제보다 완료 조건이 있는 작업이 낫습니다. 예를 들어 작은 저장소에서 실패하는 테스트 하나를 고치게 하고, 수정 파일·테스트 로그·되돌린 시도까지 확인합니다. 모델이 강해도 하네스와 권한, 중간 검증이 없으면 장시간 작업의 품질을 판단하기 어렵습니다.

API에서 `model not found`가 나오면 무작정 재설치하지 않습니다. API Key와 Base URL이 같은 서비스·지역에서 발급된 조합인지 먼저 확인합니다. 이어서 계정 지역에서 `qwen3.8-max`를 제공하는지 살펴봅니다. 웹 모델 목록에 보이지 않을 때도 캐시 문제로 단정하지 말고 공식 직링크와 계정의 이용 자격을 구분해 봅니다.

### Qwen3.8-Max·Kimi K3 선택 기준

설치 없이 가장 강한 Qwen을 확인하려면 **Qwen Studio에서 Qwen3.8-Max를 먼저 시험하는 것**이 기본 선택입니다. 공식표 30개에서 Qwen3.7-Max를 모두 앞섰고, 현재 Arena 종합 순위도 5위입니다. 새 프로젝트에서 Qwen3.7-Max를 먼저 선택할 이유는 줄었습니다.

운영 중인 시스템은 곧바로 바꾸지 않는 편이 좋습니다. 같은 대표 요청으로 성공률·지연·비용·출력 형식 회귀를 측정한 뒤 전환합니다. 가중치 통제와 자체 배포가 당장 필요하다면 Kimi K3를 검토합니다. Qwen3.8-Max는 실제 공개 파일과 라이선스가 나온 뒤 다시 비교하는 순서가 정확합니다.

Qwen3.8-Max는 이전 Qwen보다 넓게 좋아졌고 최상위권에 들어왔지만, 모든 코딩 시험의 1위는 아닙니다. 선택을 가르는 것은 2.4조라는 숫자보다 호스팅 API를 쓸지, 공개 가중치를 지금 확보해야 하는지입니다.

### 참고 자료

- [Qwen3.8-Max 공식 출시 글](https://qwen.ai/blog?id=qwen3.8)
- [Qwen 공식 출시 발표와 API 가격](https://x.com/Alibaba_Qwen/status/2084100707423289643)
- [QwenCloud 텍스트 모델·문맥·도구 지원 문서](https://docs.qwencloud.com/developer-guides/getting-started/text-generation-models)
- [Alibaba Cloud Model Studio 모델 가격](https://www.alibabacloud.com/help/en/model-studio/model-pricing)
- [Qwen 공식 Hugging Face 모델 목록](https://huggingface.co/Qwen/models)
- [MoonshotAI/Kimi-K3 공식 모델 카드](https://github.com/MoonshotAI/Kimi-K3)
- [Arena 공개 리더보드](https://arena.ai/leaderboard)
