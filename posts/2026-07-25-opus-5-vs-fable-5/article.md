---
title: "Opus 5 vs Fable 5 - 클로드 모델 비교"
slug: opus-5-vs-fable-5
date: 2026-07-25
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
tags: [Claude, Opus 5, Fable 5, Claude Code, AI 모델 비교, Anthropic]
summary: "Claude Opus 5와 Fable 5의 가격·벤치마크·실사용 테스트를 비교하고, 반값 단가가 실제 작업비로 이어지는 조건과 작업별 선택 기준을 정리합니다."
hero_image: assets/opus-5-vs-fable-5-hero.png
published_url: ""
sources:
    - https://www.anthropic.com/news/claude-opus-5
    - https://www.anthropic.com/claude-opus-5-system-card
    - https://www.anthropic.com/news/claude-fable-5-mythos-5
    - https://platform.claude.com/docs/en/about-claude/models/overview
    - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
    - https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
    - https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
    - https://artificialanalysis.ai/articles/opus-5
    - https://artificialanalysis.ai/models/claude-opus-5
    - https://artificialanalysis.ai/models/claude-fable-5
    - https://www.youtube.com/watch?v=2J3uX8iRNng
    - https://www.youtube.com/watch?v=yKu03nBC9yY
    - https://www.youtube.com/watch?v=Vh1v2VSroes
---

안녕하세요. dev.log입니다.

지난달까지만 해도 Claude에서 가장 어려운 작업은 Fable 5에 맡기는 것이 자연스러웠습니다. 그런데 [2026년 7월 24일 출시된 Opus 5](https://www.anthropic.com/news/claude-opus-5)가 여러 코딩·지식 노동 벤치마크에서 Fable 5를 앞서면서 선택 기준이 다시 바뀌었습니다. 결론부터 말씀드리면 **대부분의 Claude Code와 API 작업은 Opus 5로 시작하는 편이 합리적입니다.** 다만 Fable 5가 사라진 것은 아닙니다. 긴 계획 수립, 사실 지식의 폭, 간결한 대화처럼 Fable이 더 잘 맞는 구간이 남아 있습니다.

이번 비교에서는 Anthropic 발표와 시스템 카드, Artificial Analysis 평가뿐 아니라 공개된 실사용 테스트 3건의 비용·시간·결과도 함께 살폈습니다. 특히 한 테스트의 전체 토큰을 세션 수로 다시 나눠, ‘토큰 단가가 절반’이라는 말이 실제 작업비에도 그대로 적용되는지 계산했습니다. dev.log에서 두 모델의 API를 같은 조건으로 재실행한 테스트는 아니며, 공개된 원시 수치를 다시 계산하고 서로 다른 자료를 교차 검토한 결과입니다.

### 1. 두 모델의 자리

[이전 Fable 5와 Opus 4.8 비교](https://dop3n.tistory.com/entry/Fable-5-vs-Opus-48-%ED%81%B4%EB%A1%9C%EB%93%9C-%EB%AA%A8%EB%8D%B8-%EB%B9%84%EA%B5%90)에서는 Opus로 충분한 작업은 Opus에 두고, 장시간 자율 작업만 Fable로 올리는 전략을 권했습니다. Opus 5가 나오면서 이 승격선이 더 높아졌습니다.

Anthropic은 여전히 Fable 5를 ‘일반 공개 모델 중 최고 성능’, Opus 5를 ‘복잡한 에이전틱 코딩과 기업 업무용’으로 구분합니다. 에이전틱 작업은 모델이 답만 쓰는 것이 아니라 계획을 세우고, 도구를 사용하고, 결과를 검증하며 여러 단계를 스스로 진행하는 작업입니다.

두 모델의 기본 사양은 비슷하지만 운영 조건에는 큰 차이가 있습니다.

| 항목 | Opus 5 | Fable 5 |
|---|---:|---:|
| 공식 역할 | 복잡한 코딩·기업 업무 | 최고 난도 장시간 에이전트 |
| API 입력 단가 | $5 / 100만 토큰 | $10 / 100만 토큰 |
| API 출력 단가 | $25 / 100만 토큰 | $50 / 100만 토큰 |
| 컨텍스트 | 100만 토큰 | 100만 토큰 |
| 최대 출력 | 12만 8천 토큰 | 12만 8천 토큰 |
| 비교 지연시간 | 보통 | 느림 |
| 신뢰도 높은 지식 기준일 | 2026년 5월 | 2026년 1월 |
| API 데이터 보존 | ZDR 적용 가능 | 30일 보존 의무 |

가격과 사양은 [Claude 모델 공식 비교표](https://platform.claude.com/docs/en/about-claude/models/overview), 데이터 보존 조건은 [Claude API 데이터 보존 문서](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) 기준입니다. ZDR은 API 응답이 끝난 뒤 프롬프트와 응답을 저장하지 않는 ‘제로 데이터 보존’을 뜻합니다.

**스펙만 놓고 보면 Opus 5는 Fable 5의 절반 가격으로 같은 크기의 작업 공간을 제공합니다.** Fable 5의 30일 보존 의무가 계약에 맞지 않는 조직이라면 성능 비교를 시작하기도 전에 Opus 5로 결정됩니다.

### 2. 벤치마크를 읽는 순서

이번 세대에서는 모델명만 비교하면 중요한 변수를 놓칩니다. 두 모델 모두 `effort`라는 사고량 조절 장치를 사용합니다. `low`, `medium`, `high`, `xhigh`, `max`로 올릴수록 더 많은 토큰과 시간을 써서 문제를 깊게 풉니다. Opus 5의 기본값은 `high`입니다.

실제 결과가 만들어지는 흐름은 다음과 같습니다.

> 프롬프트 → 모델과 effort → Claude Code 같은 실행 도구 → 계획·도구 사용·검증 반복 → 결과물 → 테스트 또는 평가자

같은 모델이라도 effort와 실행 도구가 달라지면 결과가 달라집니다. 성공 조건을 자세히 적으면 검증을 오래 반복할 수 있고, 멈춤 조건이 모호하면 이미 완성한 결과를 계속 고치기도 합니다. 그래서 아래 표는 ‘모델의 절대 순위’가 아니라 **특정 설정과 평가 도구에서 관찰한 결과**로 읽어야 합니다.

표에 나오는 Frontier-Bench는 터미널에서 긴 코딩 작업을 수행하는 능력, BrowseComp는 웹에서 필요한 근거를 찾는 능력, OSWorld는 실제 컴퓨터 화면을 조작하는 능력을 봅니다. GDPval-AA는 문서·슬라이드·스프레드시트처럼 직업 현장에서 만드는 결과물을 비교해 Elo 점수로 환산합니다. 수치와 Elo 모두 높을수록 좋습니다.

### 3. 공식 벤치마크의 엇갈린 승부

아래는 [Claude Opus 5 시스템 카드](https://www.anthropic.com/claude-opus-5-system-card)의 대표 결과입니다. 별도 표기가 없는 Opus 5 수치는 `max` effort에서 기본 샘플링 설정으로 5회 평균을 낸 값입니다.

| 평가 항목 | Opus 5 | Fable 5 | 관찰 결과 |
|---|---:|---:|---|
| SWE-bench Pro | 79.2% | **80.0%** | Fable 근소 우위 |
| DeepSWE v1.1 | 68.8% | **69.7%** | Fable 근소 우위 |
| Frontier-Bench v0.1 | **43.3%** | 33.7% | Opus 우위 |
| BrowseComp | **90.8%** | 87.4% | Opus 우위 |
| HLE, 도구 사용 | **64.7%** | 63.9% | 사실상 동률 |
| OSWorld 2.0 | **70.6%** | 66.1% | Opus 우위 |
| GDPval-AA v2 | **1861 Elo** | 1747 Elo | Opus 우위 |
| AutomationBench | **26.0%** | 17.4% | Opus 우위 |

표를 보면 ‘Opus 5가 모든 항목에서 Fable 5를 이겼다’는 표현은 정확하지 않습니다. 잘 정의된 소프트웨어 수정 과제인 SWE-bench Pro와 DeepSWE에서는 Fable 5가 근소하게 앞섭니다. 반면 터미널에서 여러 단계를 진행하는 코딩, 컴퓨터 조작, 검색, 업무 자동화에서는 Opus 5가 우위를 보였습니다.

독립 평가에 가까운 자료에서도 전체 차이는 작았습니다. Artificial Analysis의 9개 평가 종합 지수에서 Opus 5 `max`는 61점, Fable 5 `max`는 60점으로 사실상 동률이었습니다. 다만 작업당 평균비용은 Opus 5가 $2.03, Fable 5가 $2.75로 Opus가 26% 낮았습니다. 이 기관은 Anthropic의 출시 전 평가를 지원했고 두 모델의 안전 거부에는 Opus 4.8 폴백을 사용했으므로, 완전히 독립된 블라인드 검증으로 보기는 어렵습니다. [Artificial Analysis의 Opus 5 평가](https://artificialanalysis.ai/articles/opus-5)도 이 조건을 함께 밝히고 있습니다.

**벤치마크 결론은 ‘Fable급 지능을 절반 단가에 샀다’에 가깝지, 모든 문제에서 Fable을 압도했다는 뜻은 아닙니다.** Artificial Analysis의 사실 지식 평가에서는 Fable 5가 여전히 앞섰고, `max` 설정의 평가 전체에서 [Opus 5는 1억 개](https://artificialanalysis.ai/models/claude-opus-5), [Fable 5는 8,700만 개](https://artificialanalysis.ai/models/claude-fable-5)의 출력 토큰을 사용했습니다. Opus 5의 응답이 더 장황해질 수 있다는 신호입니다.

### 4. 반값이라는 말의 계산법

API 단가가 절반이어도 작업비가 항상 절반이 되지는 않습니다. 실제 청구액에는 입력과 출력뿐 아니라 프롬프트 캐시, 도구 호출, 실패 후 재시도까지 들어갑니다.

> 실제 작업비 = 입력 토큰 × 입력 단가 + 출력 토큰 × 출력 단가 + 캐시 비용 + 도구 비용

입력과 출력의 비율이 두 모델에서 같다고 단순화하면 손익분기점은 명확합니다.

- Opus 5가 Fable 5보다 토큰을 1.5배 쓰면 작업비는 Fable의 약 75%입니다.
- 토큰을 정확히 2배 쓰면 작업비가 같습니다.
- 토큰을 2배 넘게 쓰면 Fable 5보다 비싸질 수 있습니다.

여기서는 [Nate Herk가 진행한 Opus 5와 Fable 5 테스트](https://www.youtube.com/watch?v=2J3uX8iRNng)의 공개 수치를 다시 계산했습니다. 영상은 Opus 5를 10회, Fable 5를 8회 실행해 원시 합계만으로는 공정한 비교가 아닙니다. 공개된 출력 토큰을 실행 횟수로 나누면 다음과 같습니다.

| 재계산 항목 | Opus 5 | Fable 5 |
|---|---:|---:|
| 실행 횟수 | 10회 | 8회 |
| 전체 출력 토큰 | 약 200만 | 약 83만 2천 |
| 1회당 출력 토큰 | 약 20만 | 약 10만 4천 |
| 출력만 계산한 1회 비용 | 약 $5.00 | 약 $5.20 |
| 평균 실행 시간 | 약 63분 | 약 25분 |

Opus 5는 한 번에 Fable 5의 약 1.92배 출력 토큰을 썼습니다. 절반 단가의 이점이 거의 사라졌지만, 출력 비용만 보면 여전히 약 3.8% 저렴합니다. 반대로 평균 실행 시간은 약 2.52배였습니다.

이 계산은 영상의 전체 청구액을 복원한 값이 아닙니다. 입력·캐시·도구 비용을 제외한 출력 토큰 비교이고, 과제도 완전히 같은 수로 실행하지 않았습니다. 그래도 **Opus 5가 과도하게 검증하면 반값 할인 폭을 거의 모두 소모할 수 있다는 경계선**은 확인할 수 있습니다.

### 5. 각 실사용 테스트의 공통점

출시 당일 공개된 세 실사용 테스트는 같은 모델을 비교했지만 결론의 강도는 달랐습니다. 반복 횟수와 블라인드 채점이 부족한 초기 테스트라서 방향성 자료로만 사용했습니다.

| 공개 테스트 | 조건 | 관찰 결과 | 중요한 한계 |
|---|---|---|---|
| [Nate Herk](https://www.youtube.com/watch?v=2J3uX8iRNng) | Claude Code에서 코딩·영상·웹·리서치 등 다수 작업 | 코딩 검증은 Opus, 일부 창작·오케스트레이션은 Fable | Opus 10회, Fable 8회로 실행 수 불일치 |
| [Duncan Rogoff](https://www.youtube.com/watch?v=yKu03nBC9yY) | 한 프롬프트로 랜딩 페이지·이메일·영상 광고 제작 | Opus가 13% 저렴, 결과별 승자는 혼합 | 단 1회, 품질 평가는 제작자 취향 |
| [Alex Finn](https://www.youtube.com/watch?v=Vh1v2VSroes) | 자체 제작 코딩·에이전트 과제 5개 | 대부분 Opus 우세, 구조물 과제는 Fable 우세 | 공개 직후 테스트, 반복·블라인드 채점 없음 |

첫 번째 영상의 코드베이스 버그 찾기 두 건이 특히 흥미롭습니다. 한 과제에서는 Fable 5가 11분과 $5.30으로 더 깔끔한 수정안을 냈고, Opus 5는 13분과 $4.22를 썼습니다. 다른 과제에서는 Opus 5가 4개 테스트를 모두 통과해 93/95점을 받았지만 Fable 5는 2개만 통과해 66/95점에 그쳤습니다. 이때도 Opus가 $6.50으로 Fable의 $8.73보다 쌌지만, 시간은 20분으로 Fable의 12분보다 길었습니다.

두 번째 영상에서는 Opus 5가 $5.16과 7분 43초, Fable 5가 $5.93과 6분 20초를 기록했습니다. Opus가 약 13% 저렴했지만 약 22% 느렸습니다. 제작자는 랜딩 페이지와 영상 광고에서는 Opus를, 짧고 직접적인 콜드 이메일에서는 Fable을 선호했습니다. **비용·속도·품질의 승자가 한 모델로 모이지 않은 사례**입니다.

세 번째 영상의 자체 벤치마크에서는 3D 롤러코스터, 웹사이트 복제, 디버깅에서 Opus가 좋은 평가를 받았습니다. 다만 문서 찾기 과제에서 Fable 5가 보안 분류기에 막혀 중단됐습니다. 이것은 순수 모델 능력보다는 ‘Fable 5와 안전 분류기를 합친 실제 제품’의 실패입니다. 연구용 모델 비교에는 잡음이지만, 작업 완주가 중요한 실무에서는 무시할 수 없는 결과입니다.

### 6. Opus 5의 과잉 검증

세 영상에서 반복해서 나타난 Opus 5의 특징은 스스로 확인하고 고치는 습관입니다. 버그를 표면적으로 가리지 않고 원인을 찾거나, 결과를 브라우저에서 다시 열어 확인하는 상황에서는 강점입니다. 반대로 이미 성공한 결과를 계속 다듬거나 불필요한 하위 에이전트를 호출하면 시간과 토큰을 씁니다.

Anthropic도 [Opus 5 프롬프팅 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)에서 이전 모델용 ‘최종 검증을 반드시 수행하라’ 같은 지시를 제거하라고 권합니다. Opus 5는 지시하지 않아도 검증하므로, 같은 내용을 다시 요구하면 과잉 검증이 생길 수 있기 때문입니다. 기본 응답과 작성 문서가 길고, 작업 중 진행 상황을 자주 설명한다는 특성도 공식 문서에 적혀 있습니다.

실무에서는 다음처럼 범위와 멈춤 조건을 함께 주는 편이 좋습니다.

```text
요청한 범위만 처리하세요.
성공 조건은 테스트 A, B, C의 통과입니다.
세 테스트가 통과하면 추가 개선 없이 멈추세요.
검증은 한 번만 실행하고, 최종 보고는 10줄 이내로 작성하세요.
```

**Opus 5의 비용을 줄이는 첫 단계는 모델을 바꾸는 것이 아니라 중복 검증 지시를 지우는 일입니다.** 잘 정의된 반복 작업은 `low`나 `medium`부터 평가하고, 대규모 리팩터링과 긴 에이전트 작업만 `xhigh`나 `max`로 올리는 편이 안전합니다.

### 7. Fable 5가 남는 이유

공식 라인업에서 Fable 5가 여전히 최상위인 이유도 있습니다. SWE-bench Pro와 DeepSWE처럼 정교한 소프트웨어 수정에서는 근소하게 앞섰고, Artificial Analysis의 사실 지식 평가에서도 우위를 유지했습니다. 실사용 영상에서는 복잡한 계획을 주고받을 때 Fable이 더 집중력 있고 간결하다는 평가가 나왔습니다.

따라서 다음 조건이라면 Fable 5를 시험할 이유가 있습니다.

- 한 번의 실패 비용이 토큰비보다 훨씬 큰 최고 난도 작업
- 여러 팀과 시스템을 묶는 장기 계획·오케스트레이션
- 넓은 사실 지식과 차분한 대화형 탐색이 중요한 작업
- 내부 평가에서 Opus 5가 두 번 이상 실패한 과제

대신 제약도 분명합니다. Fable 5는 프롬프트와 응답을 30일 보존해야 하므로 ZDR 환경에서 사용할 수 없습니다. 안전 분류기는 정상적인 보안·생명과학 요청도 막을 수 있습니다. Anthropic은 [Fable 5 출시 당시](https://www.anthropic.com/news/claude-fable-5-mythos-5) 분류기가 전체 세션의 5% 미만에서 작동한다고 밝혔지만, 업무 영역에 따라 비율은 달라질 수 있습니다.

Opus 5에도 안전 분류기가 있지만 Anthropic은 Fable 5보다 개입 빈도가 약 85% 낮을 것으로 예상합니다. API에서는 거부가 오류 코드가 아니라 HTTP 200과 `stop_reason: "refusal"`로 돌아올 수 있습니다. 자동화에 넣을 때는 일반 오류와 별도로 거부·폴백 횟수를 기록해야 합니다. 자세한 응답 구조는 [공식 거부와 폴백 문서](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)에서 확인할 수 있습니다.

### 8. 작업별 선택표

두 모델 중 하나를 기본값으로 정해야 한다면 Opus 5가 맞습니다. 예외만 Fable 5로 올리면 됩니다.

| 작업 | 시작 모델 | 이유 |
|---|---|---|
| 일상 Claude Code·버그 수정 | **Opus 5 `high`** | 검증·도구 사용과 비용의 균형 |
| 대규모 리팩터링·브라우저 조작 | **Opus 5 `high~xhigh`** | Frontier-Bench·OSWorld 우위 |
| 반복 자동화·지식 노동 | **Opus 5 `medium~high`** | GDPval-AA·AutomationBench 우위 |
| 최고 난도 계획·브레인스토밍 | Fable 5도 병행 평가 | 집중력·사실 지식의 예외 가능성 |
| 짧은 카피·대화형 탐색 | 두 모델 블라인드 비교 | 공개 실사용 결과가 엇갈림 |
| ZDR가 필요한 코드·문서 | **Opus 5** | Fable 5는 30일 보존 의무 |
| 보안·생명과학 자동화 | **Opus 5 우선** | Fable 분류기 오탐·폴백 위험 |

새 프로젝트라면 Opus 5 `high`에서 시작하고, 같은 실무 과제 20개 정도를 성공률·수정 횟수·총토큰·완료시간으로 기록하는 것을 권합니다. Opus가 두 번 이상 실패하거나 계획 품질이 부족한 과제만 Fable 5로 올리면 됩니다. 반대로 Opus가 성공하지만 토큰을 지나치게 쓴다면 먼저 effort와 멈춤 조건을 낮춰야 합니다.

### 9. 최종 판단

Opus 5는 Fable 5의 단순 하위 모델이 아닙니다. 코딩 에이전트, 컴퓨터 사용, 지식 노동, 업무 자동화에서는 더 좋은 결과를 내면서 작업당 비용도 낮출 수 있는 새로운 기본값입니다. 다만 더 자주 검증하고 더 많이 말하는 성향 때문에, 프롬프트가 모호하면 절반 단가를 긴 실행 시간과 추가 토큰으로 되돌려 줄 수 있습니다.

한 문장으로 정리하면 **Opus 5는 기본 실행 모델이고, Fable 5는 실제 작업 로그로 필요성이 증명됐을 때만 올리는 최고 난도 모델**입니다. ‘가장 똑똑한 모델’을 고르는 것보다, 성공 조건을 만족한 뒤 제때 멈추는 모델을 고르는 편이 비용과 결과 모두에 더 중요합니다.

### 참고 자료

- [Introducing Claude Opus 5 - Anthropic](https://www.anthropic.com/news/claude-opus-5)
- [Claude Opus 5 System Card - Anthropic](https://www.anthropic.com/claude-opus-5-system-card)
- [Claude 모델 비교표 - Anthropic](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Prompting Claude Opus 5 - Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- [Claude API 데이터 보존 - Anthropic](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)
- [Claude API 거부와 폴백 - Anthropic](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)
- [Introducing Claude Fable 5 and Mythos 5 - Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Claude Opus 5 Intelligence, Performance & Price Analysis - Artificial Analysis](https://artificialanalysis.ai/articles/opus-5)
- [Claude Opus 5 - Artificial Analysis](https://artificialanalysis.ai/models/claude-opus-5)
- [Claude Fable 5 - Artificial Analysis](https://artificialanalysis.ai/models/claude-fable-5)
- [Claude Opus 5 vs Fable 5 - Nate Herk](https://www.youtube.com/watch?v=2J3uX8iRNng)
- [Claude Opus 5 vs Fable 5 - Duncan Rogoff](https://www.youtube.com/watch?v=yKu03nBC9yY)
- [Claude Opus 5 vs Fable 5 - Alex Finn](https://www.youtube.com/watch?v=Vh1v2VSroes)
