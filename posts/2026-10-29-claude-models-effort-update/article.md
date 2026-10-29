---
title: "Claude 모델 비교와 Effort 설정, 무엇을 고를까?"
slug: claude-models-effort-update
date: 2026-10-29
category: Log
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags:
  - Claude
  - Opus 5.5
  - Sonnet 5.5
  - Haiku 5.5
  - Fable 5.1
  - Effort
summary: "Claude의 최신 모델 4종과 Effort 차이를 정리했습니다. 평소에는 무엇을 쓰고, 답이 아쉬울 때는 어떤 설정을 바꾸면 좋을지 살펴봅니다."
hero_image: assets/official-model-comparison.jpg
published_url: "https://dop3n.tistory.com/entry/Claude-모델-비교-및-Effort"
sources_verified: 2026-10-29
---

안녕하세요. dev.log입니다.

Claude에서 모델을 고르려고 메뉴를 열면 Haiku, Sonnet, Opus처럼 여러 이름이 나옵니다. 하나를 골랐더니 이번에는 Effort를 얼마나 높일지 정해야 하죠. 둘 다 답변을 더 잘하게 만드는 설정 같아서, 어디부터 바꿔야 할지 헷갈립니다.

**모델은 어떤 AI에게 일을 맡길지, Effort는 그 AI가 얼마나 공들여 처리할지를 고르는 설정**이라고 생각하면 쉽습니다. 간단한 문장 수정과 여러 자료를 대조하는 분석에 늘 같은 조합을 쓸 필요는 없습니다.

기존 글을 최신 모델 기준으로 다시 정리했습니다. 이번에는 복잡한 성능 수치보다, 실제로 어떤 상황에서 무엇을 고르면 좋을지에 초점을 맞췄습니다.

{{media:claude-models-official}}

### 지금 Claude 모델은 어떻게 나뉠까?

2026년 10월 29일 기준, 공식 문서가 주력으로 소개하는 모델은 **Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1**입니다. 아래는 공식 설명을 일상적인 작업에 맞춰 풀어본 선택 기준입니다. [공식 모델 비교](https://platform.claude.com/docs/en/models/overview)

| 모델 | 이런 작업에 먼저 고려 | 선택할 때 볼 점 |
| --- | --- | --- |
| **Haiku 5.5** | 짧은 요약, 정보 추출, 반복적인 분류 | 빠른 응답이 중요한 작업 |
| **Sonnet 5.5** | 글 초안, 자료 정리, 일상적인 코딩 | 속도와 답변 품질을 함께 챙길 때 |
| **Opus 5.5** | 조건이 많은 분석, 어려운 버그, 여러 단계의 업무 | 시간이 조금 더 걸려도 판단의 질이 중요할 때 |
| **Fable 5.1** | Opus로도 잘 풀리지 않는 고난도 추론, 오래 이어지는 복잡한 작업 | 가장 어려운 문제를 맡길 추가 선택지 |

가령 이메일 한 문장을 다듬는 일이라면 빠르게 여러 번 주고받는 편이 편합니다. 반대로 서로 다른 문서에서 모순을 찾거나, 여러 파일에 걸친 오류의 원인을 좁혀야 한다면 더 강한 모델을 고려할 만합니다.

Anthropic은 어떤 모델을 쓸지 모르겠다면 대부분의 작업에서 Opus 5.5부터 시작하도록 안내합니다. 다만 **응답 속도를 더 중시한다면 Sonnet 5.5부터 써보는 것도 실용적인 선택**입니다. 모델 이름만 보고 하나를 고정하기보다, 자주 맡기는 일에 맞추면 됩니다.

Fable은 이용 조건도 다릅니다. Pro에서는 별도 사용량 크레딧이 필요하므로, 평소 쓰는 모델을 바꾸기 전에 이 부분도 확인하는 편이 좋습니다. [Fable 이용 안내](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)

### Effort를 높이면 무엇이 달라질까?

Effort는 답변 길이를 정하는 옵션이 아닙니다. 답을 내기까지 얼마나 검토하고 작업할지에 영향을 줍니다. Claude Code에서는 관련 파일을 더 살펴보거나, 테스트와 확인을 더 수행하는 차이로도 나타납니다. [모델과 Effort의 차이](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code)

현재 모델 4종은 모두 다음 5단계를 지원합니다. [공식 Effort 문서](https://platform.claude.com/docs/en/build-with-claude/effort)

| Effort | 이렇게 이해하면 편합니다 | 고려할 작업 |
| --- | --- | --- |
| **Low** | 빠르게 초안을 받고 직접 다듬기 | 짧은 질문, 표현 수정, 간단한 분류 |
| **Medium** | 속도와 꼼꼼함 사이의 균형 | 범위가 분명한 일상 업무와 코딩 |
| **High** | 조건과 예외를 더 살피기 | 까다로운 분석, 원인 찾기, 검증이 중요한 작업 |
| **Extra high · xhigh** | 길고 복잡한 작업을 더 깊게 진행하기 | 여러 단계로 이어지는 코딩·자동화 |
| **Max** | 가장 어려운 문제에 최대한 공들이기 | 충분히 시간을 들여 풀어야 하는 고난도 작업 |

#### 같은 앱을 만들면 얼마나 달라질까?

Claude 개발자 블로그에는 **같은 Opus 5.5로 운동 기록 앱을 Effort별로 만들어본 예시**가 있습니다. 2026년 9월 25일 공개된 글로, 세부 기능을 길게 지정하지 않고 개인용 운동 기록 앱을 만들어 달라고 요청했습니다. [공식 비교 예시](https://claude.dev/blog/spending-your-effort/)

| Effort | 앱을 만드는 데 걸린 시간 |
| --- | --- |
| **Low** | 1분 30초 |
| **Medium** | 4분 |
| **High** | 11분 |
| **Max** | 67분 |

Low에서는 운동을 기록하는 화면과 간단한 그래프를 만들었습니다. 강도를 높일수록 세부 기능이 늘었으며, 원문은 Max 결과에 운동 기록을 색으로 보여주는 히트맵도 포함됐다고 소개합니다. 같은 요청을 받아도 Claude가 스스로 정하고 구현하는 범위가 달라진 것입니다.

{{media:effort-app-low}}

{{media:effort-app-max}}

**빠르게 기본 틀을 받아 함께 고칠 때는 Low, 한 번에 더 많은 부분을 맡길 때는 높은 Effort**가 어울린다는 차이를 보여줍니다. 표의 시간은 이 앱을 만든 개별 실행 기록이며, 모든 작업의 평균 속도를 뜻하지는 않습니다. 이 예시에는 xhigh 결과가 공개되지 않았습니다.

높일수록 기다리는 시간과 사용량이 늘 수 있습니다. 그렇다고 **Max가 언제나 가장 좋은 선택은 아닙니다.** 간단한 요청까지 과하게 검토할 수 있고, 더 들인 시간만큼 결과가 좋아지지 않을 수도 있습니다. Claude Code 공식 문서도 Max를 널리 적용하기 전에 실제 작업에서 확인하라고 안내합니다. [Claude Code Effort 안내](https://code.claude.com/docs/en/model-config#choose-an-effort-level)

우선 기본값으로 쓰다가, 답변이 너무 성급하거나 검토가 부족할 때 높이는 편이 이해하기 쉽습니다.

### 답이 아쉬우면 모델부터 바꿀까, Effort부터 높일까?

여기서부터 두 설정의 차이가 조금 더 분명해집니다.

**필요한 자료를 충분히 읽고도 판단을 잘못한다면, 더 강한 모델을 먼저 고려할 만합니다.** 반대로 관련 파일이나 확인 과정을 건너뛴 채 일을 끝낸다면 Effort를 높여 다시 맡겨볼 수 있습니다. Anthropic도 Claude Code의 선택 기준으로 이 구분을 제시합니다. [공식 선택 가이드](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code)

예를 들어 코드를 고쳤다고 하는데 테스트를 한 번도 실행하지 않았다면, 우선 테스트를 요청하고 실행할 수 있는 환경인지 확인합니다. 그 조건이 갖춰졌는데도 검증을 자꾸 생략한다면 Effort를 올려볼 차례입니다. 관련 코드를 다 읽고 테스트까지 했는데 핵심 원인을 계속 놓친다면 모델을 바꿔보는 쪽이 낫겠습니다.

한 번에 둘 다 바꾸기보다는 **같은 요청에서 하나씩 바꿔봐야** 무엇이 도움이 됐는지 알기 쉽습니다.

### Claude 대화창에서는 어디서 바꿀까?

전송 버튼 옆의 **모델 이름**을 누르면 모델을 바꿀 수 있습니다. 같은 메뉴에서 **Effort**를 선택하면 강도도 조절할 수 있고, 추가 모델은 **More models**에서 확인합니다. 처음에는 메뉴에 **Default**로 표시된 값부터 시작하면 됩니다. 변경한 설정은 다음 답변부터 적용됩니다. [Claude 설정 안내](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)

{{media:claude-effort-official}}

예전 글처럼 Thinking을 끄면 된다고 생각하기 쉬운데, 현재 Claude 대화창에서는 위 네 모델 모두 Thinking을 끌 수 없습니다. **더 빠르고 가볍게 쓰고 싶을 때는 Effort를 낮추는 방향**으로 접근하면 됩니다.

### Claude Code와 API는 기본값이 같지 않을 수 있습니다

Claude Code를 쓴다면 `/model`로 모델을 고르고, `/effort`로 강도를 조절할 수 있습니다. 현재 **Opus 5.5·Sonnet 5.5·Haiku 5.5의 Claude Code 기본값은 Medium**입니다. [Claude Code 설정](https://code.claude.com/docs/en/model-config#choose-an-effort-level)

여기서 헷갈리기 쉬운 모델이 Sonnet 5.5입니다. Claude Code에서는 Medium이 기본이지만, 개발자가 API로 직접 호출할 때 값을 지정하지 않으면 High가 적용됩니다. Opus 5.5와 Haiku 5.5는 API에서도 Medium이 기본입니다. [API Effort 기본값](https://platform.claude.com/docs/en/build-with-claude/effort)

또한 **서로 다른 모델의 Medium이 똑같은 생각량을 뜻하지는 않습니다.** Effort 기준은 모델별로 조정됩니다. 예전 모델에서 High를 썼다고 새 모델에서도 그대로 높일 필요는 없습니다. [모델별 Effort 차이](https://code.claude.com/docs/en/model-config#choose-an-effort-level)

### 결국, 평소에는 기본값부터

매번 설정을 고민할 필요는 없습니다. **평소에는 자주 쓰는 모델의 기본값으로 시작하고, 결과가 아쉬운 이유에 따라 하나씩 바꾸면 됩니다.** 답을 빨리 받아가며 다듬을 일인지, 시간을 들여서라도 정확히 풀어야 할 일인지가 먼저입니다.

모델을 올리는 것과 Effort를 높이는 것의 차이만 알아도, 모든 요청을 무조건 가장 높은 설정으로 처리할 이유는 없어집니다.

### 참고자료

- [Claude 개발자 블로그 — 같은 작업에서 Effort 비교](https://claude.dev/blog/spending-your-effort/)
- [Anthropic — 최신 Claude 모델 비교](https://platform.claude.com/docs/en/models/overview)
- [Claude Help Center — 모델·Effort·Thinking 설정](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- [Claude Platform — Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Claude Code — 모델 설정](https://code.claude.com/docs/en/model-config)
- [Anthropic — Claude Code에서 모델과 Effort 고르기](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code)
- [Claude Help Center — Fable 이용 조건](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
