---
title: "Kimi K3란? 중국 AI 모델의 특징·성능과 현실적인 사용법"
slug: kimi-k3-guide
date: 2026-07-30
category: "Log"
subcategory: "AI 모델 · 비교"
status: ready
format: rich-post
tags: [Kimi K3, Moonshot AI, 오픈웨이트, MoE, AI 코딩, Kimi Code, AI 모델 비교]
summary: "Kimi K3가 어떤 AI인지부터 2.8조 파라미터 구조, 코딩 성능, 오픈웨이트의 의미와 웹·Kimi Code·API·자체 배포 중 현실적인 사용 방법까지 쉽게 설명합니다."
hero_image: assets/screenshots/kimi-k3-official-hero.webp
published_url: ""
sources:
    - https://www.moonshot.ai/about
    - https://www.kimi.com/blog/kimi-k3
    - https://github.com/MoonshotAI/Kimi-K3
    - https://huggingface.co/moonshotai/Kimi-K3
    - https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
    - https://platform.kimi.ai/docs/pricing/chat-k3
---

안녕하세요. dev.log입니다.

최근 AI 소식을 보다 보면 `Kimi K3`라는 이름이 자주 보입니다. Kimi K3는 [중국 AI 기업 Moonshot AI](https://www.moonshot.ai/about)가 만든 AI 모델입니다. ChatGPT나 Claude처럼 질문에 답하고, 긴 문서를 읽거나 이미지를 이해하고 코드를 작성하는 일까지 맡길 수 있습니다. 이름이 낯선 만큼 무엇이 특별한지, 일반 사용자는 어디에서 써야 하는지부터 막막할 수 있습니다.

처음 접한다면 Kimi 웹사이트에서 평소 하던 질문이나 문서 요약을 맡겨보는 것이 가장 쉽습니다. 개발자는 Kimi Code나 API로 활용 범위를 넓힐 수 있습니다. 반면 모델을 직접 내려받아 운영하는 일은 대규모 서버가 필요한 별도 프로젝트입니다.

이 글은 Kimi K3를 직접 실행한 사용기가 아닙니다. Moonshot AI의 공식 발표·모델 카드·API 문서를 확인했습니다. 공개된 코딩 평가 9개와 Hugging Face의 모델 파일 크기는 Codex가 다시 계산했습니다.

{{media:kimi-k3-official-hero}}

### Kimi K3란? 질문·이미지·코딩을 함께 다루는 AI

[Moonshot AI의 공식 모델 카드](https://github.com/MoonshotAI/Kimi-K3)는 Kimi K3를 네이티브 멀티모달 에이전트 모델로 소개합니다. 텍스트와 이미지를 한 모델에서 처리하고, 문맥 창은 1,048,576토큰입니다. 긴 저장소 탐색, 도구 호출, 조사와 문서 작업처럼 여러 단계를 이어 가는 과제를 겨냥했습니다.

핵심 구조는 **MoE(Mixture of Experts)**입니다. MoE는 모든 질문에 모델 전체를 한꺼번에 쓰지 않고, 입력 토큰마다 필요한 전문가 묶음을 골라 계산하는 방식입니다. Kimi K3에는 896개 전문가가 있고 토큰마다 16개를 선택합니다. 공유 전문가 2개를 더해 공식 표에 적힌 활성 파라미터는 1,040억 개입니다.

| 공식 사양 | 값 | 읽는 방법 |
|---|---:|---|
| 전체 파라미터 | 2.8조 | 저장하고 관리해야 하는 전체 모델 규모 |
| 활성 파라미터 | 1,040억 | 토큰 처리 때 실제로 활성화되는 계산 규모 |
| 전문가 선택 | 896개 중 16개 | 입력마다 일부 전문가만 통과 |
| 문맥 길이 | 1,048,576토큰 | 한 요청에서 유지할 수 있는 최대 문맥 |
| 양자화 | MXFP4 가중치·MXFP8 활성값 | 낮은 정밀도를 학습 단계부터 반영 |

전체 파라미터와 활성 파라미터는 서로 다른 질문에 답합니다. 2.8조는 모델을 보관하고 분산 배치하는 부담에 가깝고, 1,040억은 한 토큰을 계산할 때의 비용을 이해하는 단서입니다. 따라서 “일부만 활성화되니 가벼운 모델”이라고 읽으면 안 됩니다. 계산을 아껴도 전체 가중치는 여전히 준비해 두어야 합니다.

Moonshot AI는 Kimi Delta Attention과 Attention Residuals를 함께 적용했다고 설명합니다. 전자는 긴 문맥에서 주의 계산을 효율화합니다. 후자는 층이 깊어질 때 앞선 표현을 모두 똑같이 누적하지 않고 필요한 표현을 골라 가져옵니다. 이는 벤더가 밝힌 설계 목적이며, 독립적으로 효율을 재현한 결과는 아닙니다.

### Kimi K3 공식 코딩 평가 9개 모두 3위 안

모델 발표 자료의 막대그래프에서는 Kimi K3가 파란색으로 강조됩니다. 행마다 순위를 다시 계산하자 그림이 조금 달라졌습니다.

계산 전에 9개 이름을 용도별로 묶었습니다. 저장소 변경 과제는 DeepSWE·FrontierSWE·SWE-Marathon, 명령행 작업은 Terminal-Bench 2.1, 프로그램 작성은 ProgramBench입니다. PostTrainBench·MLS-Bench-Lite·SciCode는 모델 학습과 과학 연구에 가까운 코딩을 다루고, Kimi Code Bench 2.0은 Moonshot AI의 사내 종합 평가입니다. 이 분류는 [공식 README의 평가 설명](https://github.com/MoonshotAI/Kimi-K3#3-evaluation-results)을 독자가 읽기 쉽게 묶은 것입니다.

판정은 단순합니다. **같은 벤치마크 행 안에서만 높은 점수 순으로 모델의 위치를 셌습니다.** 척도가 다른 행의 절대 점수를 더하거나 평균내지 않았습니다. 이 규칙으로 코딩 영역 9개를 세었더니 Kimi K3는 1위 2개, 2위 6개, 3위 1개였습니다.

| Kimi K3 위치 | 벤치마크 수 | 해당 항목 |
|---|---:|---|
| 1위 | 2개 | ProgramBench, SWE-Marathon |
| 2위 | 6개 | Terminal-Bench 2.1, FrontierSWE, PostTrainBench, MLS-Bench-Lite, SciCode, Kimi Code Bench 2.0 |
| 3위 | 1개 | DeepSWE |

K3가 코딩에서 항상 1위는 아니었습니다. 그래도 9개 모두 3위 안에 들었으므로 공식 표 안에서는 상위권을 꾸준히 유지했습니다. **한두 개 최고점보다 여러 코딩 과제에서 순위가 크게 흔들리지 않은 점이 Kimi K3의 더 정확한 강점입니다.**

재계산에는 발표 시점의 공식 숫자를 그대로 사용했습니다. [공식 평가표의 주석](https://github.com/MoonshotAI/Kimi-K3#3-evaluation-results)을 보면 모델별 하네스가 다릅니다. Claude Fable 5에는 fallback이 포함될 수 있고, GPT-5.6 Sol에는 cyberguard가 작동한 항목이 있습니다. `Kimi Code Bench 2.0`은 Moonshot AI의 사내 벤치마크입니다. 그러므로 2·6·1이라는 분포는 **벤더 표를 읽기 쉽게 다시 정리한 결과**이며 독립 성능 검증으로 볼 수 없습니다.

[Moonshot AI의 공식 출시 글](https://www.kimi.com/blog/kimi-k3#limitations)은 Kimi K3의 전체 성능이 Claude Fable 5와 GPT-5.6 Sol보다 아직 뒤처진다고 적었습니다. 화려한 출시 문구와 이 한계 문장을 함께 읽어야 “최상위 모델을 전부 넘어섰다”는 과장을 피할 수 있습니다.

### 오픈웨이트지만 직접 설치 파일만 1.56TB

오픈웨이트는 모델 가중치를 내려받아 연구·배포·수정할 수 있다는 뜻입니다. 무료 웹 서비스나 개인용 로컬 모델과 같은 말은 아닙니다. [Kimi K3 License](https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE)는 소프트웨어와 가중치의 사용·복제·수정·배포를 허용하지만, 일정 규모 이상의 Model as a Service 사업자와 대형 상용 서비스에는 별도 조건을 둡니다.

[공식 Hugging Face 저장소](https://huggingface.co/moonshotai/Kimi-K3)가 2026년 7월 30일 반환한 파일 메타데이터를 합산했습니다. `model-00001`부터 `model-00096`까지 safetensors 샤드는 96개이며 총 1,560,936,091,448바이트였습니다. 십진 단위로 약 1.561TB, 이진 단위로 약 1.420TiB입니다.

| 확인 항목 | 재계산 결과 | 해석 제한 |
|---|---:|---|
| 모델 샤드 | 96개 | 설정·토크나이저 파일은 제외 |
| 샤드 합계 | 1.561TB | 네트워크 전송·저장 용량 기준 |
| 이진 단위 | 1.420TiB | 실제 추론 메모리 측정값이 아님 |

이 수치는 공개 저장소의 파일 크기 합계입니다. GPU 메모리, KV 캐시, 런타임 버퍼, 병렬화 오버헤드까지 재지는 않았습니다. 그래도 개인용 GPU 한두 장으로 간단히 내려받아 돌릴 규모가 아니라는 점은 분명합니다. [공식 발표](https://www.kimi.com/blog/kimi-k3#architecture-and-infrastructure) 역시 Kimi K3 배포에 64개 이상 가속기를 묶은 supernode 구성을 권장합니다.

Kimi K3의 공개 가중치는 개인 PC 설치 편의보다 **대규모 연구·추론 사업자가 모델을 직접 검토하고 배치할 선택권**에 더 큰 의미가 있습니다. 로컬 실행이 목적이라면 모델 품질만큼 저장 용량, 가속기 토폴로지, 서빙 엔진 지원을 먼저 확인해야 합니다.

### Kimi K3 사용법: 웹·Kimi Code·API·자체 배포

사용 경로는 네 가지로 나뉩니다. 같은 모델이라도 필요한 준비와 검증 항목이 다릅니다.

| 목적 | 먼저 선택할 경로 | 확인할 것 |
|---|---|---|
| 긴 문서 조사·일반 작업 | Kimi.com 또는 Kimi Work | 한국어 품질, 출처 추적, 결과 수정 비용 |
| 저장소 단위 코딩 | Kimi Code | 긴 세션 안정성, diff 품질, 권한 범위 |
| 제품 기능에 연결 | Kimi API | reasoning history 보존, 도구 호출, 비용·지연 |
| 가중치 통제·사내 배포 | vLLM·SGLang 등 자체 서빙 | 1.56TB 파일, 64+ 가속기 구성, 라이선스 |

일반 사용자는 웹에서 실제 문서 한 건을 넣어 보는 것이 가장 짧은 경로입니다. 코딩이 목적이면 Kimi Code에서 작은 저장소와 명확한 테스트를 먼저 주는 편이 낫습니다. 둘 다 만족한 뒤 API로 옮기면 모델의 가능성과 제품 통합 문제를 분리해서 볼 수 있습니다.

API 통합에는 Kimi K3 특유의 주의점이 있습니다. [공식 모델 사용법](https://github.com/MoonshotAI/Kimi-K3#6-model-usage)에 따르면 이 모델은 항상 추론하며 `reasoning_effort`를 `low`, `high`, `max`로 조절합니다. 여러 차례 대화하거나 도구를 호출했다면 API가 돌려준 assistant 메시지를 통째로 다음 요청에 전달해야 합니다. `reasoning_content`와 `tool_calls`도 빠뜨리면 안 됩니다. 공식 문서는 중간 기록을 잘라낼 때 모델 품질이 크게 흔들릴 수 있다고 경고합니다.

이 글의 독자에게 자체 배포는 가장 늦게 검토할 경로입니다. 공개 가중치라고 해서 API보다 싸다고 단정할 수 없습니다. 저장·네트워크·가속기·운영 인력까지 포함한 총비용을 계산해야 합니다. 그 전에 가중치가 필요한 이유가 데이터 통제인지 커스텀 추론인지부터 분명히 해야 합니다.

### Kimi K3를 쓰기 전에 알아둘 공식 한계 세 가지

[공식 출시 글의 `Limitations`](https://www.kimi.com/blog/kimi-k3#limitations)에는 실제 운영에서 중요한 내용이 세 가지 적혀 있습니다.

첫째, **추론 기록에 민감합니다.** 호환되지 않는 하네스가 이전 reasoning history를 온전히 돌려주지 않으면 생성 품질이 불안정해질 수 있습니다. 진행 중인 세션에서 다른 모델을 K3로 바꿀 때도 같은 문제가 생길 수 있습니다. 기존 에이전트의 모델 이름만 교체하기보다 호환성이 검증된 Kimi Code부터 확인해야 하는 이유입니다.

둘째, **필요 이상으로 선제 행동할 수 있습니다.** K3는 긴 과제와 어려운 문제를 오래 밀고 나가도록 학습됐습니다. 작은 모호함을 만났을 때 사용자를 대신해 예상 밖의 결정을 내릴 수 있습니다. 시스템 프롬프트나 `AGENTS.md`에는 허용 범위·확인 시점·금지 행동을 구체적으로 적어야 합니다.

셋째, **벤치마크와 체감 품질은 같지 않습니다.** Moonshot AI는 K3가 전체적으로 경쟁력 있지만 Claude Fable 5와 GPT-5.6 Sol보다 사용자 경험에서 눈에 띄는 격차가 있다고 밝혔습니다. 코딩 점수 몇 개만 보고 설명의 자연스러움, 편집 부담, 장시간 세션의 예측 가능성까지 결론 내릴 수는 없습니다.

세 한계는 테스트 계획을 바로 바꿉니다. 모델 전환 없이 새 세션에서 시작하고, 도구 권한을 좁혀야 합니다. 최종 결과와 함께 중간 diff, 되돌리기 횟수도 기록해야 합니다.

### 처음이라면 Kimi 웹에서 대표 과제 하나부터

Kimi K3의 기술적 의미는 분명합니다. 2.8조 규모의 네이티브 멀티모달 MoE 모델이 가중치까지 공개됐고, 공식 코딩표를 다시 세어도 9개 항목 모두 3위 안에 들었습니다. 동시에 자체 배포 파일만 1.56TB이며, 모델을 바꾸는 순간 바로 안정적인 에이전트가 되는 것도 아닙니다.

가장 현실적인 기본 선택은 **웹이나 Kimi Code에서 대표 과제 하나를 끝까지 수행해 보는 것**입니다. 출처를 다시 찾을 수 있는지, 코딩 diff가 작고 검토 가능한지, 예상 밖의 행동을 권한 규칙으로 막을 수 있는지를 살펴봅니다. 이 세 가지가 통과하면 API를 붙입니다. 가중치 통제가 정말 필요한 조직만 그다음에 자체 배포 비용을 계산하는 순서가 좋습니다.

### 참고 자료

- [Moonshot AI 회사 소개](https://www.moonshot.ai/about)
- [Kimi K3 공식 발표](https://www.kimi.com/blog/kimi-k3)
- [MoonshotAI/Kimi-K3 공식 GitHub 저장소와 기술 요약](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi K3 공식 Hugging Face 모델 저장소](https://huggingface.co/moonshotai/Kimi-K3)
- [Kimi K3 API 빠른 시작](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart)
- [Kimi K3 API 가격 문서](https://platform.kimi.ai/docs/pricing/chat-k3)
