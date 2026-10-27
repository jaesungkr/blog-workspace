---
title: "GPT-6.1 Terra vs Sol vs GPT-6 Astra, 성능과 비용 비교"
slug: gpt-6-1-terra-work
date: 2026-10-27
category: "Log"
subcategory: "AI 모델 · 비교"
status: reviewing
format: rich-post-v2
tags: [GPT-6.1 Terra, GPT-6.1 Sol, GPT-6 Astra, AI 모델 비교]
summary: "Terra·Sol·Astra의 화면 작업, 코딩·문서 평가와 API 비용을 비교하고 작업별 선택 기준을 정리합니다."
hero_image: assets/terra-sol-astra-comparison-v2.png
published_url: ""
sources:
  - https://openai.com/index/introducing-gpt-6-1-terra/
  - https://openai.com/index/introducing-gpt-6-1-sol/
  - https://learn.chatgpt.com/docs/models
  - https://learn.chatgpt.com/docs/whats-new/october-26-30-2026
  - https://developers.openai.com/api/docs/models/gpt-6.1-terra
  - https://developers.openai.com/api/docs/models/gpt-6.1-sol
  - https://developers.openai.com/api/docs/models/gpt-6-astra
---

안녕하세요. dev.log입니다.

ChatGPT Work에서 화면 속 자료를 읽거나 코드를 고칠 때, 새로 나온 Terra와 기존 Sol·Astra 중 무엇을 골라야 할까요? 세 모델 모두 OpenAI의 작업용 AI지만, 잘 맞는 일과 사용 비용에는 차이가 있습니다. **이미지와 화면을 다루는 반복 업무에는 Terra, 복잡한 코딩과 문서 작업을 비용까지 고려해 맡길 때는 Sol, 가장 어려운 추론과 연구에는 Astra**를 우선 후보로 볼 수 있습니다. [OpenAI의 모델 선택 안내](https://learn.chatgpt.com/docs/models)를 작업별로 풀어 쓴 구분입니다.

2026년 10월 27일 확인한 공식 발표와 API 문서를 기준으로 비교했습니다. Terra의 화면 이해 능력이 상위 모델에 얼마나 가까워졌는지, 낮은 API 단가가 실제 선택에서 어떤 차이를 만드는지가 이번 비교의 초점입니다.

{{media:terra-lead}}

### Terra·Sol·Astra의 역할 차이

비교 대상은 **GPT-6.1 Terra, GPT-6.1 Sol, GPT-6 Astra**입니다. OpenAI는 세 모델을 ChatGPT Work와 Codex의 선택지로 함께 안내합니다. 같은 서비스 안에서 작업 성격에 맞춰 고를 수 있고, Terra 출시 발표도 Sol·Astra와의 성능 및 비용 차이를 직접 다룹니다. [공식 모델 안내](https://learn.chatgpt.com/docs/models), [Terra 발표](https://openai.com/index/introducing-gpt-6-1-terra/)

먼저 공식 권장 용도를 나누면 다음과 같습니다. 이는 뒤에서 살펴볼 평가와 비용을 읽기 위한 비교 지도입니다.

| 모델 | 먼저 고려할 작업 | 선택할 때 볼 점 |
|---|---|---|
| GPT-6.1 Terra | 이미지·화면 해석, 글 초안, 앱 입력 | 처리량과 낮은 호출 비용 |
| GPT-6.1 Sol | 코드 수정, 여러 자료를 엮는 문서, 긴 업무 | 복잡한 작업의 성능과 비용 균형 |
| GPT-6 Astra | 어려운 연구, 복잡한 판단, 여러 단계를 잇는 작업 | 비용보다 결과의 완성도가 중요한지 |

Terra는 일반 Chat에는 제공되지 않습니다. [이번 주 업데이트](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)에 따르면 Plus·Pro·Business·Enterprise·Edu의 Work와 Codex에서 사용할 수 있습니다. 웹이나 데스크톱의 Work에서 Advanced 모델 목록을 확인하면 됩니다. 실제 선택지는 계정·관리자 설정에 따라 달라질 수 있습니다.

### 화면을 읽고 조작할 때의 Terra

Terra의 특징은 이미지 속 배치와 내용을 이해한 뒤 앱 작업으로 이어 가는 능력입니다. 예를 들면 상품 사진을 카탈로그 항목과 대조하거나, 도면을 읽고 제작 도구를 조작하는 일입니다. OpenAI는 제안서 작성과 문장 수정도 Terra의 용도로 소개합니다. [Terra 모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)

공개 평가에서 볼 항목은 두 가지입니다. **MMMU-Pro**는 여러 분야의 이미지와 문제를 함께 이해하는 능력을, **Agents’ Last Exam**은 도구를 써서 전문 업무를 마치는 능력을 평가합니다. 후자에는 도면을 3D 모형으로 만들거나 영상을 장면별로 검토하는 과제가 포함됩니다. 모두 평가 성적이 높을수록 좋습니다.

[Terra 출시 발표](https://openai.com/index/introducing-gpt-6-1-terra/)가 설명한 상위 모델과의 비교는 아래와 같습니다. 세 모델을 직접 실행해 얻은 결과가 아니라 OpenAI의 평가 설명을 정리한 표입니다.

| OpenAI 공개 평가 | 발표에서 확인되는 비교 | 적용 범위 |
|---|---|---|
| MMMU-Pro · 시각 추론 | Terra가 Sol·Astra에 근접 | 이미지 문제 평가 |
| Agents’ Last Exam · 전문 업무 | Terra medium이 Astra와 대등한 수준 | 발표의 해당 추론 설정·업무 과제 |

여기서 `medium`은 답을 내기 전에 얼마나 추론할지 조절하는 설정입니다. OpenAI는 모델마다 같은 이름의 추론 설정이 정확히 대응하지 않는다고 설명합니다. 따라서 이 표의 ‘근접’이나 ‘대등’을 모든 작업에서 같은 능력을 낸다는 의미로 넓힐 수는 없습니다. [추론 설정 안내](https://learn.chatgpt.com/docs/models)

Terra가 매력적인 지점은 **화면 기반 작업에서 상위 모델에 가까운 성적과 낮은 단가를 함께 제시했다는 것**입니다. 다만 이 평가에는 특정 한국어 블로그의 문체 선호나 티스토리 게시 성공률이 별도 항목으로 제시돼 있지 않습니다. 그런 작업까지 우열을 정하려면 해당 결과물이 필요합니다.

### 복잡한 코드와 문서에서는 Sol·Astra

Sol은 여러 코드 파일과 자료를 오가며 오래 걸리는 일을 맡길 때 살펴볼 모델입니다. OpenAI는 Sol의 코딩·업무 능력이 여러 평가에서 Astra에 가까워졌다고 설명합니다. 실제 코드 저장소에서 긴 소프트웨어 과제를 푸는 **DeepSWE v1.1**, 표와 각주가 있는 PDF를 읽고 전문 질문에 답하는 **GDP.pdf**가 대표적인 비교 항목입니다. [Sol 출시 발표](https://openai.com/index/introducing-gpt-6-1-sol/)

아래는 Sol 발표의 평가 설명입니다. 앞 절의 Terra 평가와 별개로 읽어야 합니다.

| OpenAI 공개 평가 | Sol과 Astra의 비교 | 판단에 유용한 작업 |
|---|---|---|
| DeepSWE v1.1 | Sol이 Astra와 대등, 과제 비용은 약 1/5 | 실제 저장소의 복잡한 코드 수정 |
| GDP.pdf | Sol이 Astra에 근접, 과제 비용은 약 1/5 | 복잡한 PDF에서 근거를 찾아 답하기 |

Sol은 이런 작업에서 Astra보다 비용을 줄일 수 있는 선택지입니다. 그렇지만 모든 어려운 문제에서 Astra와 같다는 결론은 아닙니다. OpenAI는 가장 까다로운 과학 연구에 Astra를 권하며, [Astra 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-astra)도 복잡한 추론·코딩·연구·문서 제작을 주요 용도로 제시합니다.

Terra 출시 글 역시 **가장 복잡한 코딩에는 Sol과 Astra가 더 적합하다**고 명시합니다. 이미지와 화면 처리 성적이 높아졌다는 이유로 장시간 코드 작업까지 Terra가 대체한다고 판단하기는 어렵습니다. [Terra의 코딩 평가 설명](https://openai.com/index/introducing-gpt-6-1-terra/)

화면 조작 평가인 OSWorld를 한 표로 합치는 것도 피했습니다. Terra 발표는 **2.1**, Sol 발표는 **2.0의 offline partial reward**를 사용합니다. 버전과 채점 조건이 달라 두 발표의 수치를 가져와 Terra·Sol·Astra의 공통 순위를 만들 수 없습니다. 위 비교표들은 각 발표 안에서 확인되는 관계만 담았습니다. [Terra 평가](https://openai.com/index/introducing-gpt-6-1-terra/), [Sol 평가 조건](https://openai.com/index/introducing-gpt-6-1-sol/)

### 긴 자료를 받는 범위는 세 모델 모두 동일

API 사양에서 세 모델의 컨텍스트는 **1,050,000토큰**, 최대 출력은 **128,000토큰**으로 같습니다. 컨텍스트는 한 번에 참고하는 대화와 자료의 범위이고, 토큰은 글 등을 모델이 처리하는 단위입니다. 한국어 글자 수와는 일치하지 않습니다. [Terra 사양](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Sol 사양](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra 사양](https://developers.openai.com/api/docs/models/gpt-6-astra)

입출력 형식도 텍스트 입출력과 이미지 입력으로 같습니다. 세 API 모델 모두 네이티브 오디오·비디오 입출력은 지원하지 않습니다. 도구를 이용한 영상 편집 사례와 모델 자체가 받는 입력 형식은 구분해야 합니다.

따라서 ‘더 긴 자료를 넣을 수 있는가’만으로는 세 모델의 차이를 찾기 어렵습니다. 문서에서 어떤 근거를 빠뜨렸는지, 여러 조건을 끝까지 지켰는지처럼 **넣은 자료로 무엇을 해냈는지**를 봐야 합니다. API의 이 사양은 Work에서 첨부할 수 있는 파일 수나 크기를 그대로 뜻하지도 않습니다.

### API 단가는 Terra 1, Sol 2, Astra 10

API는 프로그램에서 모델을 호출하고 사용량만큼 요금을 내는 방식입니다. ChatGPT 월 구독료와 별도이며, 아래는 2026년 10월 27일 확인한 표준 텍스트 요금입니다. 모두 **100만 토큰당 미국 달러**입니다.

| 표준 API 요금 | GPT-6.1 Terra | GPT-6.1 Sol | GPT-6 Astra |
|---|---:|---:|---:|
| 기본 입력 | $1 | $2 | $10 |
| 출력 | $5 | $10 | $50 |
| 캐시 입력 | $0.05 | $0.10 | $1 |

[Terra 가격](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Sol 가격](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra 가격](https://developers.openai.com/api/docs/models/gpt-6-astra)

캐시 입력은 이미 보낸 자료를 재사용할 때 적용되는 항목입니다. 기본 입출력 단가에서 Terra는 Sol의 절반, Astra의 10분의 1입니다. 캐시 입력 단가는 Astra와 20배 차이가 나지만, 캐시를 처음 저장하는 비용은 별도로 따져야 합니다.

단가 차이를 같은 처리량에 대입해 보겠습니다. 세 모델 모두 기본 입력 10만 토큰과 청구 대상 출력 1만 토큰을 쓴다고 가정하면 Terra는 **$0.15**, Sol은 **$0.30**, Astra는 **$1.50**입니다. 계산식은 `입력 토큰 × 입력 단가 + 출력 토큰 × 출력 단가`이며, 단가는 토큰당 값으로 환산했습니다. 캐시·외부 도구·다른 처리 모드·세금은 제외한 계산 예시입니다.

이 조건에서 Terra를 두 번 호출하면 Sol 한 번과 같은 텍스트 비용입니다. Terra를 열 번 호출하면 Astra 한 번과 같습니다. 따라서 낮은 단가가 유리한지는 원하는 결과까지 몇 번 시도했는지에 따라서도 달라집니다. 실제 재시도는 입력과 출력 길이까지 바뀌므로 이 횟수는 고정 처리량에서의 계산 기준입니다.

입력이 **272,000토큰을 넘는 요청**은 세 모델 모두 요청 전체의 입력·캐시 단가가 2배, 출력 단가가 1.5배가 됩니다. API를 연결해 쓰는 경우에는 기본 단가 외에 실제 토큰 사용량과 재시도 비용을 함께 봐야 합니다. Work에서는 자신의 요금제 사용 한도를 확인해야 하며, API 단가 비율을 Work의 작업 가능 횟수로 환산할 수는 없습니다.

### 어떤 작업에 무엇을 고를까

화면을 읽어 내용을 옮기거나 짧은 글을 다듬는 반복 업무에는 Terra부터 고려할 만합니다. 복잡한 코드나 여러 문서를 함께 다루면서 비용도 줄이고 싶다면 Sol이 더 넓은 출발점입니다. 어려운 연구나 판단을 맡겨 완성도를 우선하려면 Astra가 맞습니다. 공식 권장 용도와 위 평가를 종합한 선택이며, 같은 과제를 세 모델에 실행한 실측 순위는 아닙니다.

| 작업 상황 | 우선 후보 | 장점과 감수할 점 |
|---|---|---|
| 상품·차트·화면을 읽고 앱에 입력 | Terra | 낮은 단가와 시각 작업 강점, 복잡한 추론 우위는 별도 확인 |
| 여러 파일의 코드 수정·문서 작성 | Sol | Astra에 가까운 공개 평가와 낮은 비용, 최고 난도에는 격차 가능 |
| 난도가 높은 연구·복합 판단 | Astra | OpenAI의 최상위 작업 모델, 세 모델 중 높은 API 단가 |

Terra는 화면을 이해하고 반복 업무를 처리할 때 비용을 줄일 후보입니다. **복잡한 작업까지 폭넓게 맡길 기본 후보는 Sol, 시각 업무와 처리량을 우선하면 Terra, 가장 어려운 일에는 Astra**라는 구분이 이번 공식 자료와 잘 맞습니다.

### 참고 자료

- [OpenAI: GPT-6.1 Terra 발표와 평가 설명](https://openai.com/index/introducing-gpt-6-1-terra/)
- [OpenAI: GPT-6.1 Sol 발표와 평가 조건](https://openai.com/index/introducing-gpt-6-1-sol/)
- [ChatGPT: 모델별 권장 작업과 추론 설정](https://learn.chatgpt.com/docs/models)
- [ChatGPT: Terra 제공 범위](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)
- API 사양·가격: [Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra)
