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
legacy_anchors:
  "3비트25비트2비트의-파일-크기와-코딩-성능": "10GB로 줄여도 코딩 성능은 비슷할까"
  "코딩-에이전트의-작업-기록으로-양자화를-보정하는-법": "3비트는 모델이 학습한 수치인 가중치 하나를 저장하는 데 평균 3비트를 썼다는 뜻입니다."
  "1012gb-파일을-실행하는-데-30gb가-드는-이유": "내 컴퓨터에서 어떤 파일을 고르면 될까"
  "24gb-gpu라면-문맥-길이를-어디에-맞출까": "내 컴퓨터에서 어떤 파일을 고르면 될까"
  "내-장비에서-nariq를-열려면": "파일을 열 수 있는 실행 프로그램"
---

안녕하세요. dev.log입니다.

ChatGPT에 질문하면 답변은 OpenAI 서버에서 만들어집니다. AI 모델을 내려받아 내 컴퓨터에서 직접 답변을 만들 수도 있습니다. 이때는 모델 파일을 저장할 공간과, 답변을 만드는 동안 쓸 메모리가 모두 내 컴퓨터에 있어야 합니다. 모델 파일이 작아지면 저장 공간을 덜 차지하고, 실행할 때 그래픽카드 메모리에도 그만큼 여유가 생깁니다.

NariQ는 이런 모델 파일을 줄이는 압축 기술입니다. 개발팀은 Qwen3.8-27B의 언어 모델 파일을 53.8GB에서 10.12GB로 줄였습니다. 다만 AI가 앞서 읽은 코드나 작업 기록을 참고하면서 답하려면 메모리가 더 필요합니다. [개발팀 자료](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)에 따르면 이미지 입력을 켜고 모델이 한 번에 참고할 수 있는 분량을 최대로 늘렸을 때, 그래픽카드 메모리가 약 30GB 필요할 것으로 추산됩니다. 코딩 평가에서 압축 전후 성능이 얼마나 달라졌는지 먼저 보고, 그래픽카드 메모리에 맞춰 어떤 파일을 고르면 좋을지 살펴보겠습니다.

{{media:lead}}

### 10GB로 줄여도 코딩 성능은 비슷할까

코딩에 쓸 파일을 고른다면 **3비트가 첫 선택**입니다. Nari Labs의 두 코딩 평가에서 10.12GB짜리 3비트 모델은 53.8GB 원본과 비슷한 비율로 과제를 끝냈습니다. **2.5비트**는 3비트보다 1.68GB 작습니다. 코드 수정 성적은 비슷했고 터미널 과제 성공률은 3.6%포인트 낮았습니다. **2비트**는 파일이 6.75GB까지 작아지는 대신 두 평가 모두 원본보다 10%포인트 이상 낮았습니다. [Nari Labs 평가표](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

개발팀은 원본과 세 압축 모델을 각각 자기 장비에서 실행하고, 모두 같은 Claude Code CLI에 연결했습니다. 코드를 읽고 다음 행동을 정한 것은 Qwen이고, Claude Code는 파일을 열거나 테스트를 실행할 수 있게 해 주는 프로그램입니다. 네 모델 모두 문맥 길이를 262,144토큰으로 맞추고 추론을 켠 상태에서 `max` 설정으로 평가했습니다. [개발팀의 실행 조건](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

| 모델 | 언어 모델 파일 | DeepSWE v1.1 | Terminal-Bench 2.1 |
|---|---:|---:|---:|
| BF16 원본 | 53.8GB | 39.8% | 62.6% |
| NariQ 3비트 | 10.12GB | 41.0% | 63.8% |
| NariQ 2.5비트 | 8.44GB | 41.9% | 60.2% |
| NariQ 2비트 | 6.75GB | 28.6% | 52.4% |

DeepSWE는 코드 수정 과제 113개를 세 차례 실행해, 새 테스트와 기존 테스트를 모두 통과한 과제의 비율을 평균 냈습니다. Terminal-Bench는 터미널 과제 82개를 각각 세 번씩 시도한 성공률입니다.

3비트는 모델이 학습한 수치인 가중치 하나를 저장하는 데 평균 3비트를 썼다는 뜻입니다. 개발팀은 원본과 압축 모델에 같은 코드와 오류 메시지를 보여 준 뒤, 답변을 쓰거나 도구를 호출할 때 두 모델이 다음에 어떤 내용을 출력할 가능성이 높은지 비교했습니다. 압축했을 때 예측이 크게 달라지는 부분에는 더 많은 비트를 남겼습니다. [NariQ 기술 보고서 2절](https://arxiv.org/html/2611.26157v1#S2)

#### 다른 모델과 비교한 Vals AI의 터미널 평가

Qwen3.8-27B 자체가 다른 모델에 비해 터미널 과제를 얼마나 잘 푸는지는 Vals AI의 평가에서 볼 수 있습니다. 아래 네 모델은 모두 `Terminus 2`로 터미널을 사용했습니다. 89개 과제를 대상으로 첫 시도에 과제의 테스트를 모두 통과한 비율을 집계했습니다. [Vals AI 평가표와 채점 방법](https://www.vals.ai/benchmarks/terminal-bench-2-1)

| 모델 | Terminal-Bench 2.1 성공률 |
|---|---:|
| Claude Opus 5.5 | 87.64% |
| GPT-6 Astra | 87.27% |
| Gemini 3.8 Flash | 81.27% |
| Qwen 3.8 27B | 58.43% |

87.27%는 GPT-6 Astra의 기록이며, 이 표에는 GPT-6.2 Astra의 결과가 없습니다. Qwen의 58.43%도 Vals AI의 과제와 도구로 얻은 점수입니다. **압축의 영향**을 보려면 첫 표에서 같은 도구로 같은 82개 터미널 과제를 푼 BF16 원본(62.6%)과 3비트(63.8%)를 비교하면 됩니다.

### 내 컴퓨터에서 어떤 파일을 고르면 될까

**24GB 그래픽카드에서 코딩에 쓴다면 3비트 파일과 약 13만 토큰으로 시작할 만합니다.** 파일 크기 10.12GB는 내려받을 언어 모델이 디스크에서 차지하는 용량입니다. 실행할 때는 그래픽카드 메모리에 모델을 올리고, 앞서 읽은 코드와 오류 메시지를 이어서 참고할 공간도 확보해야 합니다. 한 번에 참고할 수 있는 분량을 **문맥 길이**라고 합니다. 개발팀이 추산한 **약 30GB**는 3비트 모델에 이미지 입력을 켜고 문맥을 최대 길이인 약 26만 토큰까지 늘렸을 때의 메모리입니다. [모델 카드의 실행 예제와 메모리 표](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)

- **24GB에서 코딩 성능을 우선할 때**는 개발팀의 3비트 예제처럼 `-c 131072`로 시작합니다. `-c`는 한 세션의 문맥 길이입니다. 이 설정에서는 여유 메모리가 작아 같은 그래픽카드가 모니터 출력도 맡는다면 값을 조금 낮춰야 할 수 있습니다.
- **24GB에서 더 긴 코드를 한 번에 읽혀야 할 때**는 2.5비트를 고려할 만합니다. 이미지 입력을 포함한 개발팀 추산으로는 약 16만 토큰까지 담을 수 있습니다. 2비트는 약 18만 4천 토큰까지 들어가지만, 앞의 두 코딩 평가에서 모두 성공률이 낮아졌습니다.
- **3비트로 262,144토큰을 모두 쓸 때** 개발팀이 안내하는 사양은 그래픽카드 메모리 32GB 이상입니다. 이미지 입력까지 포함하면 가장 작은 2비트 파일도 이 문맥 길이에서는 약 27GB가 필요합니다. [문맥 길이별 메모리 안내](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart)

#### 파일을 열 수 있는 실행 프로그램

2026년 11월 25일 기준, 세 압축 파일을 열려면 **Nari Labs가 수정한 전용 `llama.cpp`**가 필요합니다. 파일 확장자는 `.gguf`이지만 일반 `llama.cpp`, Ollama, LM Studio는 당시 NariQ의 저장 형식을 지원하지 않았습니다. Hugging Face 페이지 상단 자동 실행 예시의 `:BF16`은 원본을 지정합니다. 3비트를 받으려면 모델 카드 본문의 **Quickstart**에서 `Qwen3.8-27B-NariQ-3.0bpw.gguf`를 전용 `llama-server`로 여는 예제를 확인하세요. [공식 Quickstart](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#quickstart) · [Nari Labs의 llama.cpp](https://github.com/nari-labs/nari-llama.cpp)

Mac에서는 Apple의 Metal을 실험적으로 지원합니다. 개발팀은 통합 메모리 18GB인 M3 Pro에서 3비트 모델의 생성 속도를 초당 약 3.8토큰으로 측정했습니다. AMD GPU용으로는 Linux에서 ROCm을 쓰는 실험 브랜치가 공개됐으며, 당시 RX 7900 XTX와 RX 9070 XT의 검증 결과는 나오지 않았습니다. [모델 카드의 하드웨어 지원 현황](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF#known-limits-and-future-work)

### 참고 링크

- 모델 파일과 최신 평가 결과를 공개한 [Nari Labs 모델 카드](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)
- 양자화와 보정 방법을 설명한 [NariQ 기술 보고서](https://arxiv.org/abs/2611.26157)
- 운영체제별 실행 방법을 담은 [NariQ 전용 llama.cpp 저장소](https://github.com/nari-labs/nari-llama.cpp)
- 이 글의 출발점이 된 [GeekNews 소개 글](https://news.hada.io/topic?id=37749)
