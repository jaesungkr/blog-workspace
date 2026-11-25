---
title: "NariQ란? Qwen3.8-27B를 10GB로 줄인 방법과 실제 실행 조건"
slug: nariq-qwen-27b
date: 2026-11-25
category: "Log"
subcategory: "AI 모델 · 비교"
status: published
format: rich-post-v2
tags: [NariQ, Qwen3.8-27B, 로컬 AI, 양자화, VRAM]
summary: "3비트 언어 모델 파일 10.12GB와 전체 문맥 실행 메모리 약 30GB의 차이를 개발팀의 실행 조건과 코딩 평가로 살펴봅니다."
hero_image: assets/nariq-memory.png
published_url: "https://dop3n.tistory.com/entry/NariQ%EB%9E%80-Qwen38-27B%EB%A5%BC-10GB%EB%A1%9C-%EC%A4%84%EC%9D%B8-%EB%B0%A9%EB%B2%95%EA%B3%BC-%EC%8B%A4%EC%A0%9C-%EC%8B%A4%ED%96%89-%EC%A1%B0%EA%B1%B4"
sources:
  - https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
  - https://arxiv.org/abs/2611.26157
  - https://vals-ai.com/benchmarks/terminal-bench-2-1
  - https://github.com/nari-labs/nari-llama.cpp
  - https://news.hada.io/topic?id=37749
---

안녕하세요. dev.log입니다.

ChatGPT에 질문하면 답변은 OpenAI 서버에서 만들어집니다. AI 모델을 내려받아 내 컴퓨터에서 직접 답변을 만들 수도 있습니다. 이때는 모델 파일을 저장할 공간과, 답변을 만드는 동안 쓸 메모리가 모두 내 컴퓨터에 있어야 합니다. 모델 파일이 작아지면 저장 공간을 덜 차지하고, 실행할 때 그래픽카드 메모리에도 그만큼 여유가 생깁니다.

NariQ는 이런 모델 파일을 줄이는 압축 기술입니다. 개발팀은 Qwen3.8-27B의 언어 모델 파일을 53.8GB에서 10.12GB로 줄였습니다. 다만 AI가 앞서 읽은 코드나 작업 기록을 참고하면서 답하려면 메모리가 더 필요합니다. [개발팀 자료](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)에 따르면 이미지 입력을 켜고 모델이 한 번에 참고할 수 있는 분량을 최대로 늘렸을 때, 그래픽카드 메모리가 약 30GB 필요할 것으로 추산됩니다. 파일은 10GB쯤인데 실행할 때는 왜 그보다 더 많은 메모리가 필요한지부터 살펴보겠습니다.

{{media:lead}}

### 10.12GB 파일을 실행하는 데 30GB가 드는 이유

코딩 에이전트가 테스트 실패를 고치는 상황을 생각해 보겠습니다. 에이전트는 소스 파일을 읽고, 코드를 수정하고, 테스트를 실행합니다. 다음에 어느 부분을 고칠지 정할 때는 처음 받은 요청뿐 아니라 방금 읽은 코드와 오류 메시지도 참고합니다. 모델이 한 번에 참고할 수 있는 기록의 범위를 **문맥 길이**라고 합니다.

이전 기록을 매번 처음부터 다시 계산하면 답변이 느려집니다. 그래서 모델은 앞선 토큰에서 계산한 키와 값(Key와 Value)을 메모리에 보관하고, 다음 토큰을 생성할 때 다시 사용합니다. 이 저장 공간이 **KV 캐시**입니다. NariQ v1은 언어 모델의 가중치를 압축했습니다. KV 캐시와 계산 중간값에는 여전히 16비트 형식인 BF16을 씁니다. [모델 카드의 메모리 관련 설명](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#known-limits-and-future-work)

KV 캐시가 차지하는 용량은 모델 구조로 계산해 볼 수 있습니다. Qwen3.8-27B에서 전체 문맥을 참조하는 어텐션 층은 16개입니다. 이 층들이 토큰 하나의 키와 값을 저장하는 데 총 64KiB가 듭니다. **한 세션이 131,072토큰을 담으면 이 캐시만 8GiB, 262,144토큰을 담으면 16GiB**입니다. 여기에 모델 가중치와 계산용 메모리가 필요하고, 개발팀의 실행 예제는 이미지 입력을 처리하는 0.93GB짜리 프로젝터도 함께 올립니다. 10.12GB는 내려받는 언어 모델 파일의 크기이고, 약 30GB는 이 구성을 모두 올렸을 때의 추산치입니다. [Qwen3.8-27B 모델 구조](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#model-overview) · [개발팀의 메모리 표](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)

### 코딩 에이전트의 작업 기록으로 양자화를 보정하는 법

가중치는 모델이 학습 과정에서 얻은 수치입니다. 양자화는 이 수치를 더 적은 비트로 근사해 저장합니다. NariQ에서 ‘3비트’는 언어 모델의 가중치 하나당 평균을 뜻합니다. 정해진 파일 크기 안에서 어느 부분의 정밀도를 더 살릴지는 압축 후 모델의 예측이 얼마나 달라지는지에 따라 정했습니다. [NariQ 기술 보고서 2절](https://arxiv.org/html/2611.26157v1#S2)

개발팀은 BF16 원본 모델이 오픈소스 저장소에서 코딩 과제를 수행한 기록으로 그 차이를 살폈습니다. 예를 들어 테스트가 긴 오류 로그를 출력했다면, 원본과 압축 모델 양쪽에 같은 로그를 보여줍니다. 그런 다음 **모델이 직접 답변이나 도구 호출을 작성한 위치에서** 다음 토큰에 매긴 확률을 비교합니다. 오류 로그는 다음 행동을 고르는 데 필요한 문맥으로 남고, 보정은 그 로그를 읽은 모델이 무엇을 쓸지에 초점을 맞춥니다. 개발팀은 이 예측이 압축에 민감한 부분에 더 많은 비트를 배정했습니다. [기술 보고서의 보정 방법](https://arxiv.org/html/2611.26157v1#S2)

### 3비트·2.5비트·2비트의 파일 크기와 코딩 성능

개발팀은 로컬에서 실행한 Qwen3.8-27B를 Claude Code CLI에 연결해 평가했습니다. 답변을 생성하고 다음 행동을 고른 모델은 Qwen이고, Claude Code는 모델이 도구를 사용해 과제를 진행하도록 연결한 프로그램입니다. 네 버전 모두 문맥 길이를 262,144토큰으로 맞췄습니다. [NariQ 모델 카드의 평가 조건](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

| 모델 | 언어 모델 파일 | DeepSWE v1.1 | Terminal-Bench 2.1 |
|---|---:|---:|---:|
| BF16 원본 | 53.8GB | 39.8% | 62.6% |
| NariQ 3비트 | 10.12GB | 41.0% | 63.8% |
| NariQ 2.5비트 | 8.44GB | 41.9% | 60.2% |
| NariQ 2비트 | 6.75GB | 28.6% | 52.4% |

DeepSWE 수치는 코드 수정 과제 113개를 세 차례 평가해, 새 테스트와 기존 테스트를 모두 통과한 과제의 비율을 평균 낸 값입니다. Terminal-Bench는 터미널 과제 82개를 세 번씩 시도한 성공률입니다. 표에는 개발팀이 최신 모델 카드에 공개한 결과를 사용했습니다. [개발팀의 평가표](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

3비트 파일은 원본 크기의 약 19%였고, 두 평가의 성공률은 원본과 비슷했습니다. 2.5비트는 여기서 1.68GB를 더 줄였습니다. 3비트와 비교하면 DeepSWE 점수는 0.9%포인트 높았고 Terminal-Bench는 3.6%포인트 낮았습니다. 2비트까지 줄였을 때는 두 평가 모두 원본보다 10%포인트 이상 낮아졌습니다. [NariQ 모델 카드](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

#### Claude·GPT·Gemini는 같은 터미널 과제를 얼마나 풀었을까

Vals AI는 Terminal-Bench 2.1의 89개 과제로 여러 모델을 평가했습니다. 아래 네 모델은 모두 `Terminus 2`를 통해 터미널을 사용했습니다. 점수는 한 번의 시도에서 과제에 딸린 테스트를 모두 통과한 비율(`pass@1`)입니다. GPT의 87.27%는 **GPT-6 Astra**의 기록이며, 이 평가표에 GPT-6.2 Astra의 결과는 없습니다. [Vals AI 평가표와 채점 방법](https://vals-ai.com/benchmarks/terminal-bench-2-1)

| 모델 | Terminal-Bench 2.1 성공률 |
|---|---:|
| Claude Opus 5.5 | 87.64% |
| GPT-6 Astra | 87.27% |
| Gemini 3.8 Flash | 81.27% |
| Qwen 3.8 27B | 58.43% |

두 표를 이어 주는 모델은 **NariQ의 바탕이 된 Qwen3.8-27B**입니다. 이 모델은 Vals AI에서 58.43%를 기록했고, Nari Labs가 Claude Code로 82개 과제를 세 번씩 평가했을 때는 BF16 원본이 62.6%, NariQ 3비트가 63.8%였습니다. 같은 Terminal-Bench 2.1이라도 과제 구성과 실행 도구가 달라 두 표의 점수 차이를 모델 간 성능 차이로 환산하기는 어렵습니다. 압축 후 성능이 얼마나 유지됐는지는 같은 조건에서 얻은 **원본 62.6%와 3비트 63.8%**를 비교하면 알 수 있습니다. [Vals AI 평가표](https://vals-ai.com/benchmarks/terminal-bench-2-1) · [Nari Labs 모델 카드](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

### 내 장비에서 NariQ를 열려면

2026년 11월 25일 기준, 세 압축 파일을 실행하려면 **Nari Labs가 수정한 전용 `llama.cpp`**가 필요합니다. 파일 확장자는 로컬 모델에 흔히 쓰이는 `.gguf`이지만, 일반 `llama.cpp`와 Ollama, LM Studio는 NariQ가 가중치를 저장하는 형식을 아직 읽지 못합니다. Hugging Face 상단의 자동 실행 예시에 붙은 `:BF16`은 BF16 버전을 지정합니다. 3비트 압축본을 쓰려면 모델 카드 본문의 **Quickstart**에서 `Qwen3.8-27B-NariQ-3.0bpw.gguf`를 전용 `llama-server`로 여는 예제를 보면 됩니다. [공식 Quickstart](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart) · [Nari Labs의 llama.cpp](https://github.com/nari-labs/nari-llama.cpp)

Mac에서는 Apple의 Metal을 실험적으로 지원합니다. 개발팀은 통합 메모리 18GB인 M3 Pro에서 3비트 모델이 **초당 약 3.8토큰**을 생성했다고 보고했습니다. 이 수치는 해당 Mac의 생성 속도입니다. AMD GPU에는 Linux의 ROCm용 실험 브랜치가 공개돼 있으며, RX 7900 XTX와 RX 9070 XT의 검증 결과는 아직 나오지 않았습니다. [모델 카드의 하드웨어 지원 현황](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#known-limits-and-future-work)

### 24GB GPU라면 문맥 길이를 어디에 맞출까

24GB GPU에서 3비트를 쓰는 개발팀의 수동 실행 예제는 `-c 131072`로 시작합니다. `-c`는 한 세션에서 쓸 수 있는 토큰 수를 정하는 옵션입니다. 이 설정은 메모리 여유가 작아서 같은 그래픽카드가 화면 출력도 맡는다면 값을 조금 낮춰야 할 수 있습니다. 이미지 프로젝터를 포함한 개발팀 추산으로는 2.5비트를 고르면 약 160K, 2비트를 고르면 약 184K까지 문맥을 늘릴 수 있습니다. [24GB GPU의 문맥 길이 비교](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)

따라서 24GB에서 13만 토큰 안팎으로 코딩 작업을 이어갈 계획이라면, 공개 평가에서 원본과 비슷한 성적을 낸 3비트가 자연스러운 출발점입니다. **262K 전체가 필요한 경우에는 가장 작은 2비트도 약 27GB를 씁니다.** 3비트로 그 길이를 모두 쓰려는 독자에게 개발팀이 안내하는 사양은 VRAM 32GB 이상입니다. [모델 카드의 전체 문맥 실행 조건](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)

### 참고 링크

- 모델 파일과 최신 평가 결과를 공개한 [Nari Labs 모델 카드](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)
- 양자화와 보정 방법을 설명한 [NariQ 기술 보고서](https://arxiv.org/abs/2611.26157)
- 운영체제별 실행 방법을 담은 [NariQ 전용 llama.cpp 저장소](https://github.com/nari-labs/nari-llama.cpp)
- 이 글의 출발점이 된 [GeekNews 소개 글](https://news.hada.io/topic?id=37749)
