---
title: "GPT-6.1 Terra, 화면을 읽고 앱 작업을 돕는 AI"
slug: gpt-6-1-terra-work
date: 2026-10-27
category: "Log"
subcategory: "AI 모델 · 비교"
status: reviewing
format: rich-post-v2
tags: [GPT-6.1 Terra, ChatGPT Work, Codex, AI 모델]
summary: "GPT-6.1 Terra의 ChatGPT Work 제공 범위와 화면 작업 활용법, API 비용의 의미를 공식 문서로 확인합니다."
hero_image: assets/terra-visual-action-v1.png
published_url: ""
sources:
  - https://learn.chatgpt.com/docs/whats-new/october-26-30-2026
  - https://developers.openai.com/api/docs/changelog
  - https://openai.com/index/introducing-gpt-6-1-terra/
  - https://developers.openai.com/api/docs/models/gpt-6.1-terra
---

안녕하세요. dev.log입니다.

ChatGPT에서 이미지 속 내용을 읽게 한 뒤, 그 내용을 다른 앱에 옮기는 일까지 맡기고 싶을 때가 있습니다. GPT-6.1 Terra는 이런 화면 이해와 컴퓨터 작업을 함께 처리하도록 소개된 OpenAI의 AI 모델입니다. 사용할 곳을 찾는다면 **ChatGPT Work와 Codex**를 확인해야 합니다. 일반 Chat에는 제공되지 않습니다. [OpenAI의 이번 주 업데이트](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)가 이 차이를 명시하고 있습니다.

{{media:terra-lead}}

### Terra를 선택할 수 있는 곳

공식 모델명은 **GPT-6.1 Terra**입니다. 개발자가 프로그램에서 호출할 때 쓰는 이름은 `gpt-6.1-terra`이며, [API 변경 기록](https://developers.openai.com/api/docs/changelog)에 2026년 10월 26일 출시가 올라와 있습니다. ChatGPT라는 서비스 이름과 그 안에서 선택하는 모델 이름을 구분하면 제공 범위를 읽기 편합니다.

[ChatGPT 공식 안내](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)에 따르면 Plus, Pro, Business, Enterprise, Edu에서 ChatGPT Work와 Codex를 통해 사용할 수 있습니다. 데스크톱 앱이나 웹의 ChatGPT Work에서 Advanced의 모델 목록을 열어 선택하며, 모바일 Work도 지원합니다. 기업 계정은 워크스페이스의 모델 제공 여부와 관리자 설정에 영향을 받습니다.

따라서 일반 Chat에서 이름이 보이지 않는다면 먼저 Work를 보고 있는지 확인하는 편이 좋습니다. 브라우저와 컴퓨터를 조작하는 기능에는 각각 별도 설정과 접근 요건이 있습니다. 앱 작업을 맡기려면 해당 도구가 접근할 수 있는 환경을 준비해야 합니다.

### 이미지 설명에서 앱 작업으로

OpenAI가 [출시 글](https://openai.com/index/introducing-gpt-6-1-terra/)에서 강조한 변화는 시각적 추론, 컴퓨터 조작, 자연스러운 글쓰기입니다. 시각적 추론은 이미지에 무엇이 있는지 알아보는 데서 더 나아가, 배치와 관계를 읽고 작업에 필요한 판단을 하는 능력을 뜻합니다.

예를 들어 공급업체의 상품 사진을 카탈로그와 대조한 뒤 해당 항목을 찾아 수정하는 일이 여기에 해당합니다. [공식 사용 안내](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)는 캠페인 이미지의 잘림이나 글자 배치를 확인하고 수정 작업을 정리하는 예도 듭니다. 화면에서 얻은 정보가 다음 앱 작업의 입력으로 이어지는 셈입니다.

다만 사진을 읽는 능력과 외부 서비스에서 변경을 끝내는 능력은 나눠서 판단해야 합니다. dev.log의 글 작성 흐름에 대입하면 원고를 다듬는 일, 미리보기에서 이미지를 확인하는 일, 로그인한 티스토리 편집기에 글을 넣는 일은 각각 다른 조건을 요구합니다. 아래 표는 작업을 맡기기 전에 필요한 조건을 나눈 판단표입니다.

| 맡길 작업 | 준비할 자료·환경 | 완료를 확인할 대상 |
|---|---|---|
| 원고 다듬기 | 원고와 보존할 사실·출처 | 수정 원고의 사실과 문체 |
| 이미지 배치 검토 | 실제 미리보기 또는 화면 이미지 | 글자 잘림과 본문에서의 크기 |
| 티스토리 편집기 입력 | 로그인과 브라우저 접근 권한 | 편집기에 반영된 글과 첨부 이미지 |

원고가 완성됐어도 편집기에 접근하지 못하면 게시 작업은 남습니다. 이처럼 결과물과 실행 환경을 분리해 두면 ‘화면 작업을 지원한다’는 설명을 실제로 맡길 수 있는 일로 바꿀 수 있습니다.

### API 요금과 ChatGPT 사용 한도

[API 모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)의 표준 텍스트 요금은 입력 100만 토큰당 1달러, 출력 100만 토큰당 5달러입니다. 토큰은 모델이 글을 처리할 때 쓰는 단위이며 한국어 글자 수와 일치하지 않습니다. 이 수치는 프로그램에서 API를 호출할 때의 요금으로, ChatGPT 월 구독료와는 별개입니다.

단순 계산으로 입력 1만 토큰과 출력 2천 토큰을 사용하면 텍스트 요금은 0.02달러입니다. 입력 요금 0.01달러에 출력 요금 0.01달러를 더한 값입니다. 이는 캐시와 도구 요금 등을 제외한 표준 텍스트 계산 예시이며, 실제 청구액은 측정하지 않았습니다. 긴 입력이나 다른 처리 모드에는 별도 요금 조건이 적용되므로 예상 비용을 잡을 때는 문서의 조건까지 확인해야 합니다.

ChatGPT Work와 Codex에 대해서는 [OpenAI가 같은 사용 한도로 더 많은 작업을 처리할 수 있다고 설명](https://openai.com/index/introducing-gpt-6-1-terra/)합니다. 실제 처리 가능한 작업량은 작업 내용과 사용 한도에 따라 달라집니다.

### 성능 평가의 범위와 미지원 입출력

출시 글에는 화면 조작과 코딩 평가 결과가 실려 있습니다. 이 결과는 OpenAI가 공개한 평가 조건에서 나온 수치입니다. 개별 한국어 원고의 품질이나 특정 웹사이트에서의 작업 성공률을 그대로 알려 주지는 않습니다. OpenAI도 [가장 복잡한 코딩 작업에는 GPT-6.1 Sol과 GPT-6 Astra를 더 적합한 선택으로 안내](https://openai.com/index/introducing-gpt-6-1-terra/)합니다.

입출력 방식에도 구분이 필요합니다. [API 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)에 표시된 기본 입출력은 텍스트 입출력과 이미지 입력입니다. 네이티브 오디오·비디오 입출력은 지원하지 않습니다. 출시 글의 ‘영상 편집’ 활용 예시는 컴퓨터 도구를 사용하는 작업 맥락으로 읽어야 합니다. 모델 자체가 영상 파일을 직접 입출력하는 지원 항목과는 다릅니다.

### 참고 자료

- [OpenAI: GPT-6.1 Terra 출시 발표](https://openai.com/index/introducing-gpt-6-1-terra/)
- [ChatGPT: 2026년 10월 26~30일 업데이트](https://learn.chatgpt.com/docs/whats-new/october-26-30-2026)
- [OpenAI API: GPT-6.1 Terra 모델 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)
- [OpenAI API: 변경 기록](https://developers.openai.com/api/docs/changelog)
