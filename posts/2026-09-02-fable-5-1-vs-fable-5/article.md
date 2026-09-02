---
title: "Fable 5.1 vs Fable 5 - 클로드 모델 비교"
slug: fable-5-1-vs-fable-5
date: 2026-09-02
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
format: rich-post-v2
tags: [Claude, Fable 5.1, Fable 5, Claude Code, AI 모델 비교, Anthropic]
summary: "Claude Fable 5.1과 Fable 5의 공식 벤치마크, 캐시 가격, 외부 평가 작업비, API 호환성을 비교하고 기존 사용자의 이전 기준을 정리합니다."
hero_image: assets/fable-5-1-vs-fable-5-hero.png
published_url: ""
sources:
  - https://www.anthropic.com/claude/fable
  - https://platform.claude.com/docs/en/models/fable-5-1/overview
  - https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
  - https://platform.claude.com/docs/en/models/fable-5-1/migration-guide
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
  - https://www.anthropic.com/news/claude-fable-5-mythos-5
  - https://artificialanalysis.ai/articles/claude-fable-5-1
---

안녕하세요. dev.log입니다.

Fable 5를 쓰고 있는데 모델 선택기에 Fable 5.1이 생겼다면 바로 바꿔도 될까요? Anthropic이 2026년 9월 1일 공개한 Fable 5.1은 입력·출력 기본 단가를 유지한 채 장시간 코딩·연구·문서 작업을 강화한 후속 모델입니다. **기존 Fable 5 사용자는 호환성만 확인되면 5.1로 옮길 이유가 충분합니다.** 캐시 읽기가 75% 싸졌어도 전체 작업비가 같은 폭으로 줄어들지는 않습니다. 외부 평가의 `max` 설정에서는 Fable 5.1이 더 많은 출력 토큰을 써서 오히려 과제당 비용이 20% 높았습니다.

[기존 Opus 5와 Fable 5 비교](https://dop3n.tistory.com/entry/Opus-5-vs-Fable-5-%ED%81%B4%EB%A1%9C%EB%93%9C-%EB%AA%A8%EB%8D%B8-%EB%B9%84%EA%B5%90)에서는 일상 작업을 Opus 5에서 시작하고, 최고 난도 장시간 작업만 Fable 5로 올리는 전략을 권했습니다. 이번 수치를 대조해 봐도 일상 작업과 최고 난도 작업을 가르는 선택 기준은 같습니다. 달라진 것은 승격 뒤 선택입니다. 이제 기존 Fable 5 자리는 Fable 5.1이 맡는 편이 합리적입니다.

{{media:fable-5-1-vs-fable-5-hero}}

### 같은 기본 단가, 캐시 읽기는 4분의 1

Fable 5.1은 Fable 5를 잇는 Mythos급 모델입니다. 두 모델 모두 몇 시간 동안 계획을 세우고 도구를 쓰는 에이전트 작업에 맞춰져 있습니다. 100만 토큰 컨텍스트 창과 최대 12만 8천 토큰 출력, 항상 켜지는 adaptive thinking도 같습니다. Adaptive thinking은 모델이 요청 난도에 맞춰 내부 사고량을 조절하고, 사용자는 `effort`로 그 깊이를 정합니다.

기본 사양표에서 달라지는 항목은 캐시 읽기 가격과 지식 기준일입니다.

| 항목 | Fable 5.1 | Fable 5 | 실제 차이 |
|---|---:|---:|---|
| API 입력 | $10 / 100만 토큰 | $10 / 100만 토큰 | 같음 |
| API 출력 | $50 / 100만 토큰 | $50 / 100만 토큰 | 같음 |
| 5분 캐시 쓰기 | $12.50 / 100만 토큰 | $12.50 / 100만 토큰 | 같음 |
| 캐시 읽기 | **$0.25 / 100만 토큰** | $1 / 100만 토큰 | 5.1이 75% 저렴 |
| 컨텍스트 | 100만 토큰 | 100만 토큰 | 같음 |
| 최대 출력 | 12만 8천 토큰 | 12만 8천 토큰 | 같음 |
| 신뢰도 높은 지식 기준일 | 2026년 6월 | 2026년 1월 | 5.1이 5개월 최신 |

가격은 [Claude 공식 가격표](https://platform.claude.com/docs/en/about-claude/pricing), Fable 5.1 사양은 [모델 문서](https://platform.claude.com/docs/en/models/fable-5-1/overview)를 기준으로 했습니다. 캐시는 코드베이스, 도구 설명, 대화 앞부분처럼 매 요청에서 반복되는 긴 입력을 다시 계산하지 않도록 저장하는 기능입니다. 따라서 한 번 묻고 끝나는 대화보다 같은 문맥을 여러 차례 읽는 에이전트에서 가격 차이가 커집니다.

[Anthropic 공식 Fable 페이지](https://www.anthropic.com/claude/fable)에 따르면 Fable 계열은 안전 모니터링을 위해 기본적으로 30일 데이터 보존을 요구합니다. Enterprise Frontier Safeguards 적용 대상 조직은 데이터를 자체 클라우드에 저장하며, 사람의 검토가 필요하면 기본적으로 Anthropic이 아니라 해당 조직이 직접 담당합니다. Anthropic은 EFS 제공 전까지 해당 조직이 Fable 5.1을 zero data retention으로 사용할 수 있다고 안내합니다. 대부분의 Claude 애플리케이션은 분류기 개입 시 자동 폴백하지만, API 고객은 Fallback API를 직접 구성해야 합니다. 민감한 업무라면 성능보다 조직의 보존 정책과 폴백 처리부터 확인해야 합니다.

### Anthropic 표의 일곱 평가군 모두 Fable 5.1 우위

[Anthropic의 공개 비교표](https://www.anthropic.com/claude/fable)는 Fable 5.1과 Fable 5를 일곱 평가군에 나란히 놓았습니다. Terminal-Bench-Science는 과학 연구 과제를, Terminal-Bench 4.0은 터미널 기반 코딩·공학 과제를 봅니다. OSWorld는 컴퓨터 조작을 평가합니다. GDPval-AA v2는 실제 업무 결과물을 블라인드로 비교한 Elo 평점입니다. Humanity's Last Exam은 여러 학문 분야의 어려운 추론 문제이고, AutomationBench와 CursorBench는 각각 업무 자동화와 코딩 에이전트 성능을 평가합니다. 모두 높을수록 좋습니다.

| Anthropic 공개 평가 | Fable 5.1 | Fable 5 | 차이 |
|---|---:|---:|---:|
| Terminal-Bench-Science 0.1 | **52.6%** | 24.7% | +27.9%p |
| Terminal-Bench 4.0 | **55.8%** | 42.0% | +13.8%p |
| GDPval-AA v2 | **1,853 Elo** | 1,723 Elo | +130 Elo |
| OSWorld 2.0 partial | **77.9%** | 72.9% | +5.0%p |
| OSWorld 2.0 strict | **41.7%** | 36.1% | +5.6%p |
| Humanity's Last Exam, 도구 없음 | **60.9%** | 57.8% | +3.1%p |
| Humanity's Last Exam, 도구 사용 | **65.0%** | 63.8% | +1.2%p |
| AutomationBench | **31.4%** | 17.1% | +14.3%p |
| CursorBench 3.2.0 | **73.4%** | 70.5% | +2.9%p |

표의 아홉 결과 행에서 Fable 5.1이 모두 앞섰습니다. 가장 큰 변화는 과학 연구와 업무 자동화처럼 여러 도구와 단계를 이어 가는 과제에서 나왔습니다. 반면 HLE 도구 사용과 CursorBench의 차이는 작습니다. `.1` 업데이트가 모든 작업을 같은 폭으로 개선했다는 뜻은 아닙니다.

숫자의 범위는 표 아래 각주가 정합니다. Terminal-Bench-Science의 모델별 표준오차는 ±3.5~4.5%p입니다. OSWorld에서는 Fable 5와 Opus 5를 2026년 8월 작업 세트로 다시 실행했습니다. 생산 안전장치가 개입한 일부 과제는 0점 또는 Opus 폴백으로 처리됐습니다. 이 표는 Anthropic의 실제 제품 구성을 보여 주며, 독립된 동일 환경 재현까지 뜻하지는 않습니다.

### 외부 평가의 66점과 20% 높은 과제당 비용

외부 평가에서는 성능과 비용의 방향이 갈렸습니다. [Artificial Analysis](https://artificialanalysis.ai/articles/claude-fable-5-1)는 여러 추론·지식·코딩 과제를 묶은 Intelligence Index에서 Fable 5.1 `max`를 66점, Fable 5 `max`를 62점으로 측정했습니다. 5.1이 4점 높았지만 과제당 평균비용은 $3.76으로, Fable 5의 $3.14보다 20% 높았습니다.

| Artificial Analysis 측정 | Fable 5.1 max | Fable 5 max |
|---|---:|---:|
| Intelligence Index | **66** | 62 |
| 지수 과제당 비용 | $3.76 | **$3.14** |
| 상대 출력 토큰 | 약 **1.7배** | 1배 |

기본 단가는 같고 캐시 읽기는 더 싼데 작업비가 오른 이유는 출력량입니다. Fable 5.1 `max`가 같은 평가 묶음에서 약 1.7배의 출력 토큰을 사용했습니다. 캐시 인하로 과제당 약 $1.40을 아꼈지만, 늘어난 출력 비용이 그 절감분을 넘었습니다.

Fable 5.1은 `xhigh`부터 확인할 만합니다. 같은 기관의 측정에서 65점으로 `max`보다 1점 낮았고, 과제당 비용은 $2.72로 $1.04 적었습니다. 대표 과제를 `xhigh`로 먼저 돌린 뒤 성공률 차이가 확인된 작업만 `max`로 올리면 됩니다.

출시 전 협업과 폴백 조건은 이 외부 평가의 독립성 범위를 좁힙니다. Artificial Analysis는 Anthropic의 출시 전 평가를 지원했고, 안전 요청을 Opus 4.8 또는 Opus 5로 넘기는 기본 폴백이 지수 출력 토큰의 약 4%를 처리했습니다. 수치는 Fable 5.1 단독 가중치보다 실제 API 구성에 가깝게 읽어야 합니다.

{{media:fable-5-1-upgrade-card}}

### 반복해서 읽을수록 커지는 캐시 할인

캐시 가격이 전체 청구액에 미치는 폭을 보기 위해 공식 단가에 두 토큰 구조를 대입했습니다. 계산은 Codex가 수행했습니다. 두 경우 모두 20만 토큰을 5분 캐시에 한 번 쓰고, 비캐시 입력 10만 토큰과 출력 10만 토큰을 사용한다고 가정했습니다. 차이는 같은 캐시를 다시 읽은 양뿐입니다.

| 구조 예시 | 캐시 읽기 | Fable 5 | Fable 5.1 | 절감률 |
|---|---:|---:|---:|---:|
| 짧은 반복 세션 | 400만 토큰 | $12.50 | **$9.50** | 24.0% |
| 긴 에이전트 세션 | 1,000만 토큰 | $18.50 | **$11.00** | 40.5% |

캐시 읽기가 400만 토큰이면 전체 비용은 24.0% 줄고, 1,000만 토큰이면 40.5% 줄었습니다. 입력과 출력 단가가 바뀐 것이 아니라 반복해서 읽는 문맥의 비중이 커졌기 때문입니다. 긴 코드베이스와 도구 설명을 여러 차례 재사용하는 세션일수록 Fable 5.1의 가격 구조가 유리합니다.

이 값은 두 모델의 도구 호출과 출력 토큰을 같게 고정한 구조 예시입니다. 실제 Claude Code 청구서를 재현하지 않았습니다. 앞선 외부 평가처럼 Fable 5.1이 더 많은 출력을 만들면 절감 폭은 줄거나 사라질 수 있습니다. 비용을 비교할 때에는 API 로그의 `cache_read_input_tokens`, `output_tokens`, 전체 turn 수를 함께 기록해야 합니다.

### Fable 5.1 전환 전 세 가지 호환성 점검

API 통합은 모델 ID만 `claude-fable-5-1`로 바꾸면 끝나지 않을 수 있습니다. [공식 변경점 문서](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)는 세 가지 중단 가능성을 명시합니다.

1. **강제 도구 호출을 제거합니다.** `tool_choice`의 `any` 또는 특정 `tool` 지정은 400 오류를 냅니다. 기본값인 `auto`를 유지하고 JSON 형식은 strict tool use나 structured outputs로 강제해야 합니다.
2. **모델을 낮출 때 thinking 블록을 정리합니다.** Fable 5.1은 이전 모델의 thinking 블록을 읽지만, Fable 5와 Opus 5는 Fable 5.1의 블록을 읽지 못합니다. 5.1에서 이전 모델로 전환하면 해당 추론 문맥이 빠질 수 있습니다.
3. **대화 기록을 append-only로 다룹니다.** 앞선 system·tools 설정이나 이전 메시지를 수정하면 이후 thinking 블록이 다른 대화에 묶인 것으로 판단돼 오류가 나거나 제거될 수 있습니다. 일시 지시는 중간 system message로 추가하고, 문맥 축약은 서버 측 compaction을 사용하는 편이 안전합니다.

Claude Code에서는 Fable 5.1을 쓰려면 [2.1.250 이상](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)이 필요합니다. 자체 에이전트에서는 병렬 도구 호출도 확인해야 합니다. Fable 5.1은 Fable 5가 여러 독립 도구를 묶어 호출하던 상황에서 한 턴에 하나씩 부르는 경우가 있습니다. 여러 대상을 명시하지 않으면 turn 수와 대기시간이 늘어날 수 있습니다.

작은 파일 수정에서 전체 파일을 다시 쓰는 성향과 긴 문장도 공식 문서에 기록돼 있습니다. 마이그레이션 회귀 테스트에는 정답률만 넣지 말고 변경 파일 수, diff 크기, 도구 호출 수, 출력 토큰을 함께 넣어야 합니다.

### 작업별 시작 모델

기존 Fable 5 통합이라면 호환성 검사를 통과한 뒤 Fable 5.1로 옮기는 것이 기본 선택입니다. 공식 표의 모든 결과 행이 같은 방향이고, 같은 캐시를 반복해서 읽는 긴 에이전트에서는 가격 구조도 유리합니다. 이 글에서 확인한 장시간 에이전트 지표만 놓고 보면 Fable 5를 계속 둘 이유는 성능보다 롤백과 회귀 확인에 가깝습니다.

| 작업 상황 | 시작 선택 | 이유 |
|---|---|---|
| 기존 Fable 5 장시간 에이전트 | **Fable 5.1 xhigh** | 성능 상승과 캐시 절감을 함께 확인하기 좋음 |
| 최고 난도 과학·코딩 과제 | Fable 5.1 xhigh 후 max | 외부 지수의 추가 1점이 비용 차이를 정당화하는지 평가 |
| 긴 코드베이스·도구 설명 반복 | **Fable 5.1** | 캐시 읽기 $0.25/100만 토큰 |
| 일상 Claude Code·기업 업무 | **Opus 5부터** | Anthropic도 대부분의 작업에 Opus 5를 먼저 권장 |
| 기존 대화 기록을 수정하는 자체 API | 단계적 이전 | thinking 블록 결합과 도구 호출 회귀 검사 필요 |
| Fable 5와 동일 동작이 필요한 운영 환경 | Fable 5를 잠시 롤백용으로 유지 | 새 동작의 diff 크기와 턴 수 증가를 확인할 때까지만 유지 |

새 프로젝트는 Opus 5에서 시작합니다. Anthropic도 대부분의 작업에는 Opus 5를 먼저 쓰고, 높은 effort의 Opus 5로 해결하기 어려운 장시간 추론 작업에 Fable 5.1을 권합니다. 기존 Fable 5 사용자는 대표 과제를 Fable 5.1 `xhigh`로 옮겨 성공률·캐시 읽기·출력 토큰을 기록해 보세요. `max`는 추가 성공률이 비용 차이를 정당화하는 과제에만 사용하면 됩니다.

### 참고 자료

- [Claude Fable 5.1 공식 페이지 - Anthropic](https://www.anthropic.com/claude/fable)
- [Claude Fable 5.1 모델 사양 - Claude Platform Docs](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- [Claude Fable 5.1 변경점 - Claude Platform Docs](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)
- [Claude Fable 5.1 마이그레이션 가이드 - Claude Platform Docs](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)
- [Claude 모델 가격표 - Claude Platform Docs](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Fable 모델의 플랜·Claude Code 최소 버전 - Anthropic Help Center](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- [Claude Fable 5 and Claude Mythos 5 - Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Claude Fable 5.1 출시 평가 - Artificial Analysis](https://artificialanalysis.ai/articles/claude-fable-5-1)
