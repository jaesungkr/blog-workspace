---
title: "AI 추론 레벨 비교"
slug: codex-claude-reasoning-effort
date: 2026-11-02
category: "Log"
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags: [Codex, Claude, 추론 노력, Effort, Sonnet 5.5, Opus 5.5, GPT-6.1 Sol]
summary: "Sonnet max와 Opus high의 점수·비용, Codex의 단계별 차이, 추론 레벨을 높일 때를 공개 평가로 비교합니다."
hero_image: assets/sonnet-terminal-bench.png
published_url: "https://dop3n.tistory.com/entry/AI-%EC%B6%94%EB%A1%A0-%EB%A0%88%EB%B2%A8-%EB%B9%84%EA%B5%90"
sources_verified: 2026-11-02
sources:
  - https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-claude-opus-5-5-high
  - https://cognition.com/frontiercode
  - https://www.anthropic.com/claude-sonnet-5-5
  - https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol
  - https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-1-sol-xhigh
  - https://claude.dev/blog/spending-your-effort/
  - https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - https://learn.chatgpt.com/docs/models
---

안녕하세요. dev.log입니다.

Codex나 Claude에서 모델을 고르고 나면 추론 레벨도 고민하게 됩니다. AI가 한 요청을 얼마나 깊게 검토할지 조절하는 설정인데, low부터 max까지 놓여 있으니 어디에 맞춰야 할지 애매합니다. 더 오래 생각하면 답도 좋아질 것 같은데, 매번 max로 두는 게 좋을까요?

Sonnet을 max로 쓰는 것과 Opus를 high로 쓰는 것 중 어느 쪽이 나을지도 궁금합니다. 설정 이름만으로는 선뜻 고르기 어렵습니다. 공개된 평가에서 점수와 비용을 함께 보면 이 차이에 조금 더 감을 잡을 수 있습니다.

### Sonnet max vs Opus high

독립 평가기관 Artificial Analysis(AA)의 결과에서는 **Sonnet 5.5 max가 Opus 5.5 high보다 종합 점수가 높았고, 비용은 약 2.9배 들었습니다.**

AA는 업무·코딩·과학·일반 지식 평가를 종합 지수로 묶습니다. 지수는 높을수록 좋고, 아래 비용은 각 평가 작업에 가중치를 적용한 API 비용입니다.

| AA v5.0 비교 | Sonnet 5.5 max | Opus 5.5 high |
| --- | ---: | ---: |
| 종합 지수 | 54 | 52 |
| 작업당 가중 비용 | $10.02 | $3.46 |

[AA v5.0 직접 비교](https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-claude-opus-5-5-high) · Default Fallback · 2026년 11월 2일 확인.

토큰 단가는 Sonnet이 더 낮은데 작업 비용은 왜 더 높았을까요? AA가 집계한 Sonnet max의 가중 출력 토큰은 Opus high의 약 4.75배였습니다. 단가가 낮아도 사용하는 양이 많아지면, 한 작업에 드는 비용은 더 커질 수 있습니다.

코딩 평가로 좁혀 보면 결과는 조금씩 다릅니다. 실제 저장소의 코드 수정 능력을 보는 **FrontierCode 2.0**에서는 Sonnet max가 41.0%, Opus high가 34.5%를 기록했습니다. 기능과 코드 품질을 합친 점수로는 Sonnet 쪽이 앞섰습니다. [Cognition 평가](https://cognition.com/frontiercode)

**CursorBench 4.0**에서는 두 설정이 55.5%와 56.0%로 비슷했습니다. Cursor도 이 정도의 작은 차이는 통계적으로 유의미하지 않을 수 있다고 설명합니다. 어떤 작업을 맡기느냐에 따라 추가 비용으로 얻는 차이가 달라질 수 있습니다. [Cursor 평가](https://cursor.com/en-US/cursorbench)

노력 단계가 바뀔 때 점수와 비용이 어떻게 움직이는지는 아래 공식 그래프에서도 볼 수 있습니다. 터미널 작업을 평가한 결과로, 각 점이 하나의 노력 단계입니다. 위로 갈수록 점수가 높고 오른쪽으로 갈수록 비용이 큽니다. [Anthropic 발표](https://www.anthropic.com/claude-sonnet-5-5)

{{media:sonnet-terminal-bench}}

### Codex 단계별 차이

AA는 Codex에서 선택할 수 있는 **GPT-6.1 Sol**도 노력 단계별로 평가했습니다. **high에서 max로 올렸을 때 종합 지수는 5점 높아졌고, 비용은 약 2.15배 들었습니다.**

{{media:sol-effort}}

low부터 max까지 전체를 보면 지수는 35에서 55로 높아졌고, 작업당 가중 비용은 $0.16에서 $1.27로 늘었습니다. 점수와 비용이 같은 비율로 오르지는 않습니다. 마지막 몇 점을 더 얻기 위해 얼마를 더 쓸 것인지가 선택에 들어갑니다. [low 결과](https://artificialanalysis.ai/models/gpt-6-1-sol-low), [medium·xhigh 비교](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-1-sol-xhigh), [high·max 비교](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol)

이 결과를 보고 Codex의 설정을 바꿀 때는 모델 이름도 함께 확인하는 게 좋습니다. Power 슬라이더는 모델과 노력을 묶어 바꿀 수 있기 때문입니다. 위 비교처럼 노력만 바꿨을 때의 차이를 보려면 같은 모델을 유지해야 합니다.

Max와 Ultra도 작업 방식이 다릅니다. Max는 한 작업의 추론을 늘리고, Ultra는 여러 보조 에이전트로 일을 나눕니다. [Codex 모델·노력 안내](https://learn.chatgpt.com/docs/models?surface=app)

### 추론 레벨을 높일 때

**평소에는 기본값으로 시작하고, 빠뜨린 조건이나 해결하지 못한 오류가 있을 때 한 단계 올리는 쪽을 권합니다.** 이미 원하는 결과를 얻었다면 더 높은 설정으로 다시 돌릴 필요는 적습니다.

기다리는 시간의 차이는 Claude Code 엔지니어 Thariq의 운동 앱 제작 사례에서 잘 드러납니다. Opus 5.5로 앱 하나를 만들게 했을 때 low는 1.5분, high는 11분, max는 67분이 걸렸습니다. 이 사례에서는 높은 설정이 더 많은 기능까지 추가했습니다. 시간 차이에는 모델이 추가로 수행한 작업도 들어 있는 것입니다. [Spending your effort](https://claude.dev/blog/spending-your-effort/)

그래서 노력을 올릴 때는 무엇을 더 해결해 주길 원하는지도 함께 정해두는 편이 좋습니다.

- **작은 수정·정리:** 기본값으로 시작하고, 요청한 조건을 충족했는지 확인합니다.
- **반복되는 오류·여러 파일이 얽힌 버그:** 한 단계 높여 오류 재현과 회귀 테스트를 요청합니다. 앞서 실패한 테스트를 해결하는지가 기준입니다.
- **실패 비용이 큰 작업:** 높은 노력을 고려하되, 완료 조건과 수정 범위를 먼저 적습니다. 추가 시간이 필요한 검증에 쓰이도록 하는 것입니다.

단계를 바꾼 효과가 궁금하다면 **같은 모델·같은 입력·같은 도구**로, 같은 초기 상태에서 비교하면 됩니다. 같은 오류가 사라졌는지, 재수정이 줄었는지를 보면 추가 시간을 쓴 보람이 있었는지 판단하기 쉽습니다.

---

**자료와 비교 조건**

**같은 Opus에서 노력만 올린 결과**

Anthropic은 Opus 5.5로 내부 SWE-bench Pro 478개 문제를 비교했습니다. high에서 xhigh로 올리면 해결률은 1.4%p, 시도당 비용은 약 2.5배 늘었습니다.

| Opus 5.5 노력 | 해결률 | 시도당 API 비용 |
| --- | ---: | ---: |
| low | 87.4% | $0.11 |
| medium | 92.8% | $0.21 |
| high | 95.3% | $0.29 |
| xhigh | 96.7% | $0.74 |

low·medium·high는 각각 2회, xhigh는 1회 실행했습니다. 응답당 한도는 16,384토큰이며 xhigh의 두 시도가 한도에 걸렸습니다. 공개 순위표와 문제 구성이 다릅니다. 비용 배수는 반올림 전 값으로 계산한 공식 설명입니다. [Anthropic 최적화 문서](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)

**수치를 읽을 때 구분할 조건**

- **AA:** 2026년 10월 27일 개편된 Intelligence Index v5.0을 사용했습니다. 9개 평가를 묶으며 분야별 가중치를 적용합니다. 지수의 오차 범위는 비교 페이지에 제시되지 않았습니다. [평가 방법](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
- **Default Fallback:** 안전 분류기가 요청을 거절하면 대체 모델로 넘길 수 있는 설정입니다. 구독 사용량과 API 비용도 별도입니다. [Fallback 안내](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), [구독 사용량 안내](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- **코딩 평가:** Terminal-Bench 4.0은 66개 작업을 5회씩, FrontierCode 2.0은 132개 작업을 평가했습니다. CursorBench는 Cursor의 제품용 환경을 씁니다. 문제와 실행 환경이 달라 기관별 점수를 합산하지 않았습니다. [시스템 카드](https://assets.claude.com/870c8f525702625d2c62fc6dd04c857e3250bec1.pdf), [FrontierCode 방법](https://cognition.com/blog/frontier-code-2.0)
- **버전 차이:** 9월의 FrontierCode 1.1에서는 Opus high가 앞섰습니다. 2.0은 문제와 수정 범위의 평가 기준을 바꾼 시험이므로, 두 버전을 같은 시험의 재측정처럼 비교하지 않았습니다. [이전 발표](https://www.anthropic.com/claude-sonnet-5-5), [2.0 변경 사항](https://cognition.com/blog/frontier-code-2.0)
- **체감 사례:** Thariq의 다른 내부 평가에서는 선형계획법 프로그램 제작 문제를 Opus low가 0/5회, high가 5/5회 해결했습니다. high는 임의의 문제를 만들고 별도 풀이와 대조해 오류를 수정했습니다. Terminal-Bench 3.0의 한 문제에서 얻은 결과입니다. [실험 원문](https://claude.dev/blog/spending-your-effort/)
- **설정 이름:** Sonnet 5.5·Opus 5.5는 low부터 max까지 지원합니다. Claude Code의 두 모델 기본값은 medium이며 Sonnet API는 high입니다. 이 글의 max는 Max 구독 요금제와 구분합니다. 모델·제품마다 같은 이름이 같은 계산량을 뜻하지는 않습니다. [Claude API](https://platform.claude.com/docs/en/build-with-claude/effort), [Claude Code](https://code.claude.com/docs/en/model-config), [Codex](https://learn.chatgpt.com/docs/models)
