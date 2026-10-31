---
format: rich-post-v2
slug: anatomy-ai-skill
status: published
title: 설명이 움직이는 AI 스킬, Anatomy
category: Log
subcategory: AI 개념 · 실전
date: 2026-10-31
hero_image: assets/anatomy-pen-lead.png
tags: ["Anatomy", "AI 스킬", "Claude Code", "인터랙티브 일러스트"]
summary: "Anatomy는 Claude Code와 Codex 등에 기계의 구조와 움직임을 설명하는 그림을 만드는 방법을 알려 주는 AI 스킬입니다. 볼펜 예시와 공식 커뮤니티 작품으로 활용법을 살펴봅니다."
published_url: "https://dop3n.tistory.com/entry/%EC%84%A4%EB%AA%85%EC%9D%B4-%EC%9B%80%EC%A7%81%EC%9D%B4%EB%8A%94-AI-%EC%8A%A4%ED%82%AC-Anatomy"
sources: ["https://github.com/wheresryan22/anatomy", "https://github.com/wheresryan22/anatomy/blob/main/SKILL.md", "https://skills.wheresryan.sh/anatomy/community", "https://patents.google.com/patent/US5263786A/en"]
---

안녕하세요. dev.log입니다.

오늘 소개할 **Anatomy는 직접 눌러 보고 움직여 볼 수 있는 설명 그림을 만드는 AI 스킬**입니다. 볼펜 버튼을 누르면 안쪽 부품이 어떻게 움직이는지, 커피 머신에서 커피가 어떤 과정을 거쳐 내려오는지 같은 내용을 눈으로 보여 줄 수 있습니다.

사용 방법도 간단합니다. Claude Code나 Codex에 스킬을 추가한 뒤, 설명하고 싶은 대상을 말하면 됩니다. AI가 그림과 동작을 함께 만들어 주기 때문에, 완성된 페이지에서는 버튼을 누르거나 부품을 펼쳐 보며 구조를 살펴볼 수 있습니다. 이번 글에서는 한국어로 만든 볼펜 예시와 공식 커뮤니티의 작품들을 함께 소개하겠습니다. [공식 저장소](https://github.com/wheresryan22/anatomy)

{{media:anatomy-pen-lead}}

### 볼펜 버튼 아래에서 벌어지는 일

볼펜 심이 고정되는 원리는 [공식 커뮤니티의 클릭 볼펜 작품](https://skills.wheresryan.sh/anatomy/community/nader0913/click-pen)에서도 다루고 있습니다. 제작 요청도 “클릭 볼펜의 작동 원리를 설명해 달라”는 짧은 문장입니다.

아래 그림은 같은 원리를 한국어로 설명하기 위해 Codex가 Anatomy의 공개 제작 지침을 적용해 만든 예시입니다. 심을 잡아 두었다가 놓아주는 부품의 움직임에 초점을 맞췄습니다. 이 부품은 회전하는 걸쇠 역할을 하며, **회전 캠**이라고 부릅니다.

{{media:anatomy-pen-states}}

처음에는 심이 안에 들어 있습니다. 버튼을 누르면 심과 내부 부품이 내려가면서 스프링을 누릅니다. 손을 뗀 뒤에는 회전 캠이 걸리는 위치가 바뀌어 심이 나온 상태를 유지합니다. 버튼을 한 번 더 누르면 걸림이 풀리면서 스프링이 심을 안으로 되돌립니다. 이 고정과 해제 원리는 [회전 캠 볼펜 특허의 설명](https://patents.google.com/patent/US5263786A/en)에서도 확인할 수 있습니다.

안쪽을 더 자세히 보고 싶을 때는 분해 보기를 켜면 됩니다. 몸통과 버튼, 스프링이 펼쳐져 각 부품의 위치를 구분하기 쉬워집니다. 이 예시는 작동 순서를 설명하기 위해 모양과 움직임을 단순화했습니다.

### Claude Code에 추가하고 짧게 요청하기

이런 설명 그림은 파일을 읽고 프로그램을 실행할 수 있는 Claude Code나 Codex에서 만들 수 있습니다. 해당 도구에 Anatomy 저장소 주소를 주고, 설치부터 요청할 수 있습니다.

> https://github.com/wheresryan22/anatomy 이 저장소의 설치 안내를 확인하고, 지금 프로젝트에 Anatomy 스킬을 추가해 줘.

공식 설치 안내에는 Claude Code와 Codex에서 스킬을 추가하는 방법이 나와 있습니다. 지금 작업 중인 프로젝트에만 설치할 수도 있습니다. 설치가 끝나면 스킬 목록에 Anatomy가 보이는지 확인하고, Claude Code에서는 `/anatomy`, Codex에서는 `$anatomy`로 불러옵니다. [설치·호출 안내](https://github.com/wheresryan22/anatomy#quick-start)

스킬을 불렀다면 설명하고 싶은 물건과 궁금한 점을 적어 줍니다. 볼펜을 한국어로 설명해 달라는 요청은 이 정도로 시작할 수 있습니다.

> Anatomy로 볼펜의 작동 원리를 한국어로 보여 줘.

결과는 브라우저에서 열 수 있는 HTML 페이지로 받을 수 있습니다. 블로그에 정지 이미지로 넣을 때는 누르기 전과 후를 나란히 보여 주고, 직접 조작하게 하려면 작동하는 페이지를 함께 제공하면 됩니다.

### 다마고치 안쪽부터 커피가 내려오는 과정까지

볼펜 외에 어떤 물건을 설명할 수 있을까요? [공식 커뮤니티](https://skills.wheresryan.sh/anatomy/community)에는 56개 작품과 각각의 제작 요청이 공개되어 있습니다. 만들고 싶은 그림과 비슷한 작품을 찾으면 어떤 식으로 요청했는지도 함께 볼 수 있습니다.

[@pixelyokai의 다마고치](https://skills.wheresryan.sh/anatomy/community/pixelyokai/tamagotchi-teardown)는 장난감 안에 들어 있는 부품을 펼쳐 보여 줍니다. 겉모습과 비교해 가며 작은 화면과 버튼 뒤에 무엇이 들어 있는지 살펴볼 수 있습니다.

{{media:anatomy-tamagotchi}}

커피를 내리는 과정은 [@entity의 레버식 에스프레소 머신](https://skills.wheresryan.sh/anatomy/community/entity/lever-espresso-machine)에서 볼 수 있습니다. 레버를 당겼다 놓을 때 스프링과 피스톤이 어떻게 커피를 추출하는지 보여 줍니다. 카페에서 보던 손동작을 기계 안쪽의 움직임과 연결해 볼 수 있습니다.

{{media:anatomy-espresso}}

수업에서 스프링이 하는 일을 설명하거나 제품 문서에서 버튼을 누른 뒤의 변화를 보여 줄 때, 이런 그림을 곁들이면 부품과 움직임을 함께 짚어 줄 수 있습니다. 블로그에서 물건의 작동 원리를 소개할 때도 같은 방식으로 활용할 수 있습니다. 정보를 상자와 화살표로 한눈에 정리하고 싶다면 [앞서 소개한 diagram-design](https://dop3n.tistory.com/161)을, 물건 속 부품이 어떻게 움직이는지 보여 주고 싶다면 Anatomy를 고르면 됩니다.
