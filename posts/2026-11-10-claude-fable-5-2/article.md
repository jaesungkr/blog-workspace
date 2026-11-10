---
title: "Fable 5.2 vs Fable 5.1 vs Opus 5.5 - 클로드 모델 비교"
slug: claude-fable-5-2
date: 2026-11-10
category: "Log"
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags: [Claude Fable 5.2, Claude Fable 5.1, Claude Opus 5.5, Claude Code, AI 모델 비교]
summary: "Fable 5.2를 Fable 5.1·Opus 5.5와 비교합니다. 코딩 성능, 추론 설정별 비용, 20% 낮아진 API 단가, 요금제와 이전 조건으로 각 모델의 쓰임새를 살펴봅니다."
hero_image: assets/fable-52-official-hero.jpg
published_url: "https://dop3n.tistory.com/entry/Fable-52-vs-Fable-51-vs-Opus-55-%ED%81%B4%EB%A1%9C%EB%93%9C-%EB%AA%A8%EB%8D%B8-%EB%B9%84%EA%B5%90"
sources:
  - https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/
  - https://www.anthropic.com/research/formalizing-fermats-last-theorem
  - https://www.anthropic.com/claude-fable-and-mythos-5-2
  - https://platform.claude.com/docs/en/models/fable-5-1/overview
  - https://platform.claude.com/docs/en/models/fable-5-2/migration-guide
  - https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
  - https://artificialanalysis.ai/models/claude-fable-5-1
  - https://platform.claude.com/docs/en/models/fable-5-2/overview
  - https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
  - https://www.anthropic.com/research/claude-electronics-design
  - https://artificialanalysis.ai/leaderboards/models
  - https://artificialanalysis.ai/models/claude-fable-5-2
  - https://www.vals.ai/benchmarks/vals_index
  - https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
---

안녕하세요. dev.log입니다.

오랜만에 Fable의 새 버전이 나왔습니다. **Fable 5.2**는 2026년 11월 9일 공개됐고, 9월 1일에 나왔던 5.1 이후 두 달 만입니다. 긴 코드 수정이나 자료 조사를 맡길 때는 답의 품질만큼 기다리는 시간과 비용도 신경 쓰입니다. 이번에는 코딩 성능이 좋아지면서 프로그램에서 모델을 호출해 쓰는 API의 기본 단가도 20% 내려갔습니다. [5.2 발표](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [5.1 출시 정보](https://platform.claude.com/docs/en/models/fable-5-1/overview)

Fable 5.1을 쓰던 분이라면 반가운 변화입니다. 그런데 Opus 5.5로도 일을 잘 처리하고 있다면, 입력·출력 단가가 2배인 Fable이 필요한지도 궁금해집니다. **평소 문서·코드 작업은 Opus 5.5에서 시작하고, 추론을 더 시켜도 해결하지 못하는 오래 걸리는 작업에 Fable 5.2를 쓰는 편이 합리적입니다.** Anthropic의 선택 지침도 이 방향이며, 공개 평가에서 어디까지 뒷받침되는지 살펴봤습니다. 자료는 11월 10일 확인 기준입니다. [모델 선택 지침](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)

{{media:lead}}

### Fable 5.1에서 달라진 점

Fable은 여러 시간 동안 도구를 사용하며 코드를 고치거나, 자료 조사부터 문서·스프레드시트 완성까지 이어 가는 상위 모델입니다. Opus 5.5도 문서·코드·도구 작업을 맡길 수 있는 범용 상위 모델입니다. 여기서 에이전트 작업은 AI가 도구를 실행하고 결과를 확인하며 다음 행동을 이어 가는 방식을 말합니다. [Fable의 용도](https://platform.claude.com/docs/en/models/fable-5-2/overview)

5.1에서 5.2로 바뀌며 개선된 부분은 **복잡한 과제를 해결하는 성능과 처리 효율**입니다. 추론 강도는 답을 내기 전에 얼마나 많은 계산을 할지 정하는 옵션이며, medium은 중간 강도입니다. 공식 발표에 따르면 기본 출력 생성 속도는 최대 30% 빨라졌고, 같은 medium 설정에서 어려운 작업을 더 적은 토큰으로 처리했습니다. 토큰은 글과 자료를 잘게 나눈 처리 단위입니다.

텍스트·이미지를 받아 텍스트를 출력하는 방식, 한 번에 다루는 문맥 100만 토큰, 최대 출력 12만 8천 토큰은 그대로입니다. 지식 기준일도 두 모델 모두 2026년 6월입니다. 문맥 크기는 한 요청에 함께 참고할 수 있는 자료의 양을 뜻합니다. [5.1·5.2 사양 비교](https://platform.claude.com/docs/en/models/fable-5-1/overview)

함께 발표된 **Mythos 5.2**는 Fable과 같은 기반 모델을 사용합니다. Fable에는 사이버보안과 생물학 분야의 악용을 막는 안전장치가 적용돼 있고, Mythos는 검증 프로그램을 통과한 조직에 제공됩니다. 공식 성능표의 취약점 탐지·단백질 설계 행은 Mythos 결과이므로, 아래에서는 Fable로 공개된 평가를 비교했습니다. [모델과 접근 조건](https://platform.claude.com/docs/en/models/fable-5-2/overview)

### Fable 5.1·Opus 5.5와 코딩 성능 비교

코딩 모델은 짧은 함수를 한 번에 작성하는 능력과 큰 프로젝트를 끝까지 수정하는 능력을 함께 봐야 합니다. Anthropic의 **FrontierCode 2.0**은 모델이 만든 코드 변경을 오픈소스 프로젝트 관리자가 받아들일 만한지 평가합니다. **FrontierSWE v2**도 여러 단계를 거치는 소프트웨어 개발 작업을 다룹니다.

아래는 Anthropic이 발표한 비교입니다. 점수가 높을수록 좋으며, 별도 표시가 없는 값은 각 모델에서 가능한 가장 높은 추론 설정을 사용했습니다. 제조사가 다르면 같은 설정 이름도 실제 계산량은 다릅니다.

| 공식 평가 | Fable 5.2 | Fable 5.1 | Opus 5.5 |
|---|---:|---:|---:|
| 코드 변경 · FrontierCode 2.0 | 49.1% | 32.4% | 45.5% |
| 개발 과제 · FrontierSWE v2 | 69.9% | 56.3% | 62.3% |
| 업무 자동화 · AutomationBench | 51.4% | 31.4% | 42.5% |
| 차트 읽기 · Chartography | 73.4% | 44.8% | 64.4% |

FrontierCode의 Fable 두 모델은 xhigh 설정입니다. Chartography는 도구 없이 측정했습니다. 자동화는 여러 업무 도구를 사용해 과제를 처리하는 평가이고, 차트 읽기는 그림 속 수치와 관계를 해석하는 평가입니다. 아래 화면은 공식 표의 코딩·업무 자동화 부분입니다. [공식 비교표와 측정 조건](https://www.anthropic.com/claude-fable-and-mythos-5-2)

{{media:benchmarks}}

이전 Fable과의 차이가 특히 큽니다. FrontierCode에서 16.7%p, FrontierSWE에서 13.6%p 올라갔습니다. %p는 두 비율의 차이인 퍼센트포인트입니다. Opus 5.5와의 차이는 각각 3.6%p와 7.6%p입니다. 두 코딩 평가 모두 5.1에서의 개선 폭이 Opus와의 격차보다 큽니다.

다만 업무 자동화에서는 같은 공식 표에 있는 Gemini 4 Carbon이 53.9%로 Fable보다 높았습니다. 평가마다 문제와 실행 조건이 다르므로, 한 모델이 모든 업무에서 가장 좋다고 묶기보다는 어떤 종류의 과제를 해결했는지를 봐야 합니다.

### 페르마의 마지막 정리를 약 30시간에 형식화

긴 작업을 여러 에이전트가 나눠 맡는 능력은 수학 실험에서도 드러났습니다. 페르마의 마지막 정리는 1995년에 증명됐고, 이번 실험은 그 증명을 컴퓨터가 단계마다 검사할 수 있는 Lean 코드로 옮기는 **형식화**를 다뤘습니다. Anthropic은 Fable 5.2 초기 버전의 에이전트 1,000개가 이 작업을 **28.7시간, 약 30시간**에 완료했다고 보고했습니다. [실험 상세](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/)

에이전트들은 인터넷이 차단된 환경에서 작업했습니다. 연구진은 Lean과 수학 라이브러리 Mathlib, 증명할 명제 60개, 증명 경로의 짧은 개요와 정의, 이전 실험에서 증명한 보조정리 47개를 제공했습니다. 에이전트들은 이 자료를 바탕으로 일을 나누고 결과를 공유했으며, 연구자가 증명 방향을 계속 지휘하지는 않았습니다. [제공 자료와 실행 환경](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/)

앞선 실험에서는 Fable 5.1과 비슷한 수준의 내부 연구 모델을 사용하는 수십 개 에이전트가 연구자의 도움과 전용 협업 도구를 이용해 11일 만에 형식화를 마쳤습니다. 인원과 도구가 달랐으므로 완료 시간도 이 조건과 함께 봐야 합니다. [이전 실험](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

이번에 같은 1,000개 에이전트 구성으로 실행한 Opus 5.5는 18시간에 진행률 26%였고, 30시간까지도 추가 진전이 거의 없었습니다. Fable과 Opus는 각각 한 번 실행했으며, 모두 18시간 시점의 저장 상태에서 재개해 12시간을 더 작업했습니다. [Fable·Opus 비교 조건](https://www.anthropic.com/claude-fable-and-mythos-5-2)

{{media:fermat}}

### 설계한 회로가 실제 기기로 이어진 사례

이번 발표에서 눈길을 끄는 사례는 전자기기 설계입니다. Anthropic은 회로 설계 회사 Diode와 함께 Fable 5.2에 스피커폰, 음성 비서 허브, 휴대용 가상 반려동물을 만들도록 했습니다. AI는 부품을 고르고 회로와 외장을 설계했으며 기기 안에서 실행되는 소프트웨어도 작성했습니다. 실제 회로기판 제작과 조립은 Diode의 엔지니어가 맡았습니다. [전자기기 설계 연구](https://www.anthropic.com/research/claude-electronics-design)

{{media:electronics}}

전자기기는 회로도만 맞는다고 완성되지 않습니다. 부품이 케이스 안에 들어가야 하고, 조립할 순서도 가능해야 하며, 공장이 생산할 수 있는 모양이어야 합니다. 연구 기록에서 Fable은 스피커폰 기판을 그대로 내리면 스위치가 케이스에 걸린다는 점을 확인하고, 기판을 기울여 넣는 방법을 조립 안내에 반영했습니다. 설계 파일의 숫자를 실제 제작 순서와 연결한 사례입니다.

{{media:electronics-design}}

완성된 세 기기는 회로를 수정하지 않고 동작했다고 연구진은 설명합니다. 다만 초기 시제품이라 장기간 사용했을 때의 내구성이나 상용 인증 통과 여부는 아직 확인되지 않았습니다. AI가 여러 제약을 함께 다루며 실제 작동하는 시제품까지 설계했다는 데 의미가 있습니다. [설계 과정과 남은 한계](https://www.anthropic.com/research/claude-electronics-design)

### 추론 설정을 올리면 무엇이 달라질까

외부 평가 기관인 **Artificial Analysis**도 Fable을 측정했습니다. 이곳의 **Intelligence Index v5.0.1**은 코딩, 문서 업무, 추론 등을 다루는 9개 평가를 합친 지수입니다. 점수가 높을수록 이 평가 묶음에서 성능이 좋다는 뜻입니다. 아래 값은 정답률을 나타내는 백분율이 아닙니다. [평가 구성](https://artificialanalysis.ai/models/claude-fable-5-2)

11월 10일 리더보드에서 Fable 5.2는 max 설정으로 가장 높은 지수를 기록했습니다. Fable의 중간 설정인 medium, 높은 설정인 high도 함께 놓으면 성능을 더 얻기 위해 얼마나 기다리고 지출했는지 보입니다.

| 독립 평가 · 모델과 설정 | 종합 지수 | 과제당 비용 | 과제당 시간 |
|---|---:|---:|---:|
| Fable 5.1 · max | 49 | $12.99 | 22.5분 |
| Fable 5.2 · medium | 56 | $3.80 | 8.3분 |
| Fable 5.2 · high | 62 | $9.08 | 17.7분 |
| Fable 5.2 · max | 65 | $26.54 | 46.4분 |
| Opus 5.5 · medium | 48 | $2.45 | 7.2분 |
| Opus 5.5 · max | 59 | $10.04 | 25.2분 |

Fable 결과에는 기본 fallback 구성이 포함돼 있습니다. Fallback은 안전장치가 제한한 요청을 지정된 다른 Opus 모델로 넘기는 대체 처리입니다. 비용은 입력·캐시·추론·답변 토큰을 반영해 평가별 비중으로 계산한 과제당 평균입니다. 시간도 해당 평가의 평균이며, 일상적인 채팅 한 번의 대기시간과는 구분해야 합니다. [Artificial Analysis 리더보드](https://artificialanalysis.ai/leaderboards/models) · [Fable 5.1의 같은 지수 버전 결과](https://artificialanalysis.ai/models/claude-fable-5-1)

Fable 5.1 max와 비교하면 5.2의 high는 지수가 더 높으면서 과제당 비용과 시간이 모두 줄었습니다. 같은 max끼리는 5.2의 지수가 높지만 비용과 시간도 늘었습니다. 필요한 성능에 도달하는 설정을 기준으로 비교하면 5.2의 효율 개선이 잘 드러납니다.

여기서는 Fable high가 Opus max보다 높은 지수를 기록하면서 평균 비용과 시간도 낮았습니다. 반면 Fable을 high에서 max로 올리면 지수는 3점 오르고 비용은 약 2.9배, 시간은 약 2.6배가 됩니다. Opus도 medium에서는 $2.45와 7.2분으로 더 가볍게 실행됐습니다. 같은 표 안에서도 Opus medium은 비용과 시간을 아끼고, Fable high는 더 높은 지수를 얻는 선택으로 나뉩니다.

평가가 바뀌면 비용의 순서도 바뀝니다. 금융·코딩·법률·세무 과제를 묶은 **Vals Index 2.2**에서는 Fable 5.2가 71.31%, Opus 5.5가 70.14%였습니다. 표시된 테스트당 비용은 각각 $17.94와 $24.77이었습니다. 이 평가에서는 Fable이 더 적은 비용으로 조금 높은 점수를 냈습니다. AA와 Vals는 과제 구성과 실행 조건이 달라 각각의 표 안에서 비교해야 합니다. [Vals Index, 11월 9일 갱신](https://www.vals.ai/benchmarks/vals_index)

설정을 고를 때는 이용 환경부터 나누면 됩니다. **Claude 앱과 Claude Code는 기본 medium**, **직접 API를 호출할 때는 기본 high**입니다. API 문서는 high에서 성능 개선의 상당 부분을 얻을 수 있다고 설명합니다. 오래 걸리는 코딩·에이전트 과제에서 추가 개선이 확인되면 xhigh로 올리고, max는 시간과 토큰 사용량보다 최대 성능이 중요한 드문 작업에 남겨 두도록 권합니다. [추론 설정 권장값](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)

또 하나 달라진 동작이 있습니다. 5.2에서는 medium 이상으로 설정한 뒤 프롬프트에 “생각하지 말고 바로 답해 줘”라고 적어도 추론을 줄이지 않을 수 있습니다. 쉬운 요청에서 지연과 비용을 줄이려면 effort 자체를 낮춰야 합니다. 다만 low·medium에서는 긴 과제 도중 남은 일만 정리하고 멈추는 사례가 더 자주 나타났다고 공식 문서가 설명합니다. 반복적으로 이런 문제가 생기는 작업은 설정을 올릴 이유가 됩니다. [추론과 중도 종료 동작](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)

### API 단가는 20% 인하

API 요금은 처리한 토큰 양으로 계산합니다. 입력은 모델에 보낸 내용, 출력은 추론과 답변을 생성한 양에 해당합니다. Claude나 ChatGPT의 월 구독료와는 별도입니다.

Fable 5.2의 기본 API 요금은 Fable 5.1보다 입력과 출력 모두 20% 낮아졌습니다. 아래는 미국 달러 기준 100만 토큰당 가격입니다. [Fable 5.2 요금](https://platform.claude.com/docs/en/models/fable-5-2/overview) · [Fable 5.1 발표 요금](https://www.anthropic.com/claude-fable-and-mythos-5-1)

| API 모드 | 입력 100만 토큰 | 출력 100만 토큰 |
|---|---:|---:|
| Fable 5.1 · 일반 | $10 | $50 |
| Fable 5.2 · 일반 | $8 | $40 |
| Fable 5.2 · fast | $16 | $80 |
| Opus 5.5 · 일반 | $4 | $20 |

입력 10만 토큰과 출력 1만 토큰을 쓴다고 가정해 계산하면 Fable 5.1은 $1.50, Fable 5.2는 $1.20, Fable 5.2 fast는 $2.40, Opus 5.5는 $0.60입니다. 캐시·도구·재시도 비용을 빼고 같은 처리량으로 계산한 예시입니다. 실제 작업에서는 모델이 사용하는 토큰 양이 달라집니다.

공식 코딩 비용 그래프도 그 차이를 보여 줍니다. FrontierCode에서 Fable high는 Opus max와 비슷한 점수에 도달하면서 과제당 비용은 약 절반이었습니다. 기본 토큰 단가로는 Fable이 더 비싸도, 특정 과제를 끝내는 데 사용한 양까지 포함하면 비용이 낮아질 수 있습니다.

{{media:coding-cost}}

추가 비용을 내고 출력 속도를 높이는 fast 모드도 생겼습니다. 토큰 생성 속도를 최대 2.5배 높이는 대신 단가는 일반 모드의 2배입니다. 이 수치는 토큰을 만들어 내는 속도이므로, 검색이나 도구 실행까지 포함한 전체 작업 시간이 같은 비율로 줄어드는지는 작업에 따라 달라집니다. [출력 속도와 fast 모드](https://www.anthropic.com/claude-fable-and-mythos-5-2)

### 내 요금제에서 Fable 5.2를 쓰려면

Fable 5.2는 Claude의 유료 요금제에서 사용할 수 있습니다. 웹·모바일·데스크톱 앱에서는 모델 선택 메뉴에서 **Fable 5.2**를 고르면 됩니다. Claude Code는 **2.1.321 이상**, Cowork는 최신 Claude Desktop이 필요합니다. Team·Enterprise에서는 조직 소유자가 허용한 모델을 이용할 수 있으므로, 메뉴에 보이지 않으면 관리자에게 Fable 5.2 활성화 여부를 확인해야 합니다. 프로그램에서 직접 호출할 때의 API 모델 이름은 `claude-fable-5-2`입니다. [이용 경로와 버전](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)

요금제에서 사용할 수 있다는 것과 추가 비용 없이 포함된다는 것은 구분해야 합니다. 평소 적용되는 조건은 다음과 같습니다.

| 이용 중인 요금제 | Fable 사용 비용과 한도 |
|---|---|
| Max·Ultra, Team 프리미엄 좌석 | 주간 사용 한도의 최대 50%까지 포함. 한도 이후에는 사용량 크레딧으로 계속 이용 가능 |
| Pro·Team 표준 좌석 | 기본적으로 별도 사용량 크레딧으로 과금. 아래 출시 혜택 기간에는 예외 적용 |
| Enterprise | 계약·좌석 유형에 따라 포함 여부와 과금 방식이 다름 |
| Claude API | 구독 한도와 별개로 API 사용량에 따라 과금 |

사용량 크레딧은 구독에 포함된 한도 밖의 이용료를 내는 방식입니다. Fable은 다른 Claude 모델보다 주간 한도를 빨리 소모합니다. 현재 잔여량과 크레딧 사용 여부는 Claude의 **Settings → Usage**에서 확인할 수 있습니다. [요금제별 기본 조건](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)

출시 혜택도 있습니다. Pro와 Team 표준 좌석에는 11월 9일부터 11월 16일 오후 11시 59분(미국 태평양 시간)까지 기존 주간 사용 한도 중 최대 50%를 Fable에 쓸 수 있습니다. 사용량 초기화 혜택에는 구독 시작 시점 등 별도 조건이 있으므로, 자신의 요금제에서 확인해야 합니다. Free 플랜은 대상에 포함되지 않습니다. 기간이 끝나거나 50%를 모두 쓰면, 사용량 크레딧을 켠 계정은 해당 크레딧으로 과금됩니다. [출시 혜택과 적용 조건](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers)

{{media:availability}}

회사 자료를 다룬다면 보관 조건도 확인해야 합니다. Fable 5.2는 기본적으로 안전 모니터링을 위해 30일 데이터 보관이 필요하며, 데이터를 보관하지 않는 ZDR 적용에는 Anthropic의 별도 승인이 필요합니다. 사내 규정상 보관이 허용되지 않는 자료라면 승인된 사용 환경부터 확인해야 합니다. [모델별 데이터 보관 조건](https://platform.claude.com/docs/en/models/fable-5-2/overview)

### Fable 5.1 API에서 옮길 때 확인할 것

Claude 앱이나 Claude Code에서 모델을 선택하는 사용자와, 직접 API 요청을 만드는 개발자는 이전 과정이 다릅니다. 5.2에서는 모델이 이미 만든 추론 내용 앞의 system·tools·과거 메시지를 바꿨는지 검사하는 규칙이 모든 계정에 적용됩니다. 예전 메시지를 편집한 뒤 그 추론 내용을 다시 보내면 기본 동작에서 400 오류가 날 수 있습니다. 5.1에서 오래된 계정으로 동작하던 코드도 여기에 걸릴 수 있습니다. [5.1에서 바뀐 API 검사](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)

직접 연동한 코드는 대화 앞부분을 수정하지 않고 새 메시지만 덧붙이는지 확인해야 합니다. 반면 Claude 앱·Claude Code·Claude Agent SDK가 요청을 만들어 주는 경우에는 이 검사 변경에 따로 대응할 필요가 없습니다. 또한 5.2에서 Opus 5.5나 Fable 5.1로 대화 중 전환하면 5.2의 내부 추론 내용은 이어받지 못합니다. 대화 기록을 가공하거나 모델을 번갈아 쓰는 서비스라면 [공식 이전 가이드](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide)를 먼저 확인하는 편이 좋습니다.

### Fable 5.2와 Opus 5.5의 쓰임새

**기존 Fable 5.1로 긴 작업을 맡기고 있었다면 5.2로 옮길 이유가 분명해졌습니다.** 문맥 크기와 입출력 형식은 유지하면서 공식 코딩 점수는 올랐고 단가는 내려갔습니다. 독립 평가에서도 5.2 high가 5.1 max보다 높은 지수를 더 적은 비용과 시간으로 얻었습니다. 직접 만든 API 연동은 앞서 설명한 호환성 조건도 확인해야 합니다.

Opus 5.5를 쓰고 있다면 작업의 난도가 선택을 가릅니다. 짧은 문서 정리나 평소 코드 수정은 기본 단가와 낮은 추론 설정의 비용이 작은 Opus에서 시작할 만합니다. 여러 파일을 바꾸는 대규모 수정, 긴 조사와 계산을 거쳐 결과물을 완성하는 일처럼 Opus의 추론 강도를 높여도 해결이 어려운 과제에는 Fable 5.2가 더 설득력 있습니다. 공개된 코딩·에이전트 평가가 이 선택을 뒷받침합니다.

### 참고 자료

- [Anthropic: Claude Fable 5.2·Mythos 5.2 공식 발표와 평가표](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [Claude Platform: 모델 사양·가격·데이터 보관](https://platform.claude.com/docs/en/models/fable-5-2/overview)
- [Claude Platform: Fable 5.1 사양](https://platform.claude.com/docs/en/models/fable-5-1/overview) · [5.2 이전 가이드](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide)
- [Claude Platform: 5.2의 동작 변화와 대체 처리](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)
- [Anthropic: 페르마 정리 형식화의 제공 자료와 협업 구성](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/)
- [Anthropic: 실제 전자기기를 설계한 연구와 한계](https://www.anthropic.com/research/claude-electronics-design)
- [Claude Help Center: 요금제별 Fable 이용 조건](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- [Claude Help Center: 출시 혜택과 대상 요금제](https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers)
- [Artificial Analysis: 모델 리더보드](https://artificialanalysis.ai/leaderboards/models) · [Fable 5.2의 평가 구성](https://artificialanalysis.ai/models/claude-fable-5-2) · [Fable 5.1의 현재 평가](https://artificialanalysis.ai/models/claude-fable-5-1)
- [Vals AI: Vals Index의 성능과 테스트당 비용](https://www.vals.ai/benchmarks/vals_index)
