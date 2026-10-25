---
title: "Kimi K3.1 Pro란? 문서·코딩 AI의 장점과 Opus 5.5 비교"
slug: kimi-k3-1-pro-strengths-vs-opus-5-5
date: 2026-10-25
category: "Log"
subcategory: "AI 모델 · 비교"
status: reviewing
format: rich-post-v2
tags: [Kimi, Kimi K3.1 Pro, Moonshot AI, Opus 5.5, AI 모델 비교]
summary: "Kimi를 처음 접하는 독자를 위해 이용 화면과 문서·코딩·3D 제작 기능을 소개하고, Opus 5.5 대비 공개 평가와 API 비용을 비교합니다."
hero_image: assets/kimi-home.jpg
published_url: ""
sources:
  - https://www.kimi.com/en/blog/kimi-k3-1-pro
  - https://www.kimi.com/en/blog/
  - https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart
  - https://platform.kimi.ai/docs/pricing/chat
  - https://www.kimi.com/en/products/kimi-work
  - https://www.kimi.com/code/en
  - https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks
  - https://platform.claude.com/docs/en/about-claude/pricing
---

안녕하세요. dev.log입니다.

PDF 자료를 읽고 발표자료까지 만들어 줄 AI를 찾고 있다면, Kimi도 살펴볼 만합니다. Kimi는 중국 Moonshot AI가 만든 AI 서비스로, 질문에 답하고 파일을 읽으며 문서·슬라이드·코드 같은 결과물을 만드는 기능을 제공합니다. 10월 24일 공식 연구 목록에 등장한 **Kimi K3.1 Pro**는 이 서비스에서 쓰는 새 AI 모델입니다. [Kimi Code 소개](https://www.kimi.com/code/en), [공식 공개 목록](https://www.kimi.com/en/blog/)

Kimi는 긴 자료를 읽고 여러 단계의 작업을 수행해 문서와 3D 결과물을 만듭니다. 공개 평가에서도 업무 과제와 코딩 성적이 눈에 띄며, 익숙한 비교 대상인 Claude Opus 5.5와의 격차는 평가 항목에 따라 달라집니다.

{{media:kimi-home}}

### Kimi 웹에서 질문하고 파일 넣기

[Kimi 웹](https://www.kimi.com/)의 가운데 입력창에 질문을 적으면 됩니다. 자료를 읽히려면 입력창 왼쪽 아래의 `+`를 누른 뒤 `添加文件与图片`를 선택합니다. ‘파일과 이미지 추가’라는 뜻이며, 옆에 표시된 `从电脑中上传`는 컴퓨터에서 올린다는 뜻입니다. 로그인이나 이용 권한 안내가 나타나면 먼저 해당 계정에서 사용할 수 있는 범위를 확인해야 합니다.

{{media:kimi-attach}}

첫 화면 아래에는 `PPT`, `文档`, `表格`, `深度研究`, `3D Make`가 있습니다. 각각 발표자료, 문서, 표, 심층 조사, 3D 제작으로 들어가는 메뉴입니다. 화면을 확인한 10월 25일에는 입력창 오른쪽에 `K3.1 Pro 进阶`가 표시됐습니다. 중국어로 표시되는 메뉴는 위의 이름을 기준으로 찾으면 됩니다.

처음에는 보고서 하나에서 필요한 내용을 뽑아 문서로 정리하는 작업을 떠올리면 이해하기 쉽습니다. 다음은 요청을 구성하는 예시입니다.

> 첨부한 보고서에서 사업별 매출과 전년 대비 변화를 찾아 한국어 표로 정리해 주세요. 숫자마다 근거 페이지를 붙이고, 확인되지 않는 항목은 비워 두세요. 마지막에는 회의에서 설명할 수 있도록 주요 변화 세 가지를 적어 주세요.

실제 보고서의 수치를 옮길 때는 원문 페이지와 대조해야 합니다. 이전 [AI PDF 요약 검증 글](https://dop3n.tistory.com/entry/ai-pdf-summary-verification)에서도 다룬 것처럼, 표와 각주의 조건까지 확인해야 숫자의 의미를 보존할 수 있습니다.

### 긴 자료를 읽고 결과물을 만드는 방식

K3.1 Pro는 텍스트와 이미지를 입력받고, 한 번의 요청에서 긴 자료를 다루도록 설계됐습니다. 국제 API 문서에 명시된 컨텍스트 길이는 1,048,576토큰입니다. 컨텍스트는 모델이 한 번에 참고하는 자료와 대화의 범위이고, 토큰은 텍스트 등을 모델이 처리하는 단위입니다. 이 범위 안에서 긴 보고서와 여러 자료를 함께 입력할 수 있습니다. 자료 속 근거를 정확하게 찾는 능력은 아래의 업무 평가에서 따로 살펴보겠습니다. 웹에서 첨부할 수 있는 파일 수와 크기는 별도 서비스 제한을 따릅니다. [Kimi API 모델 안내](https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart)

문서를 다루는 기능은 웹과 데스크톱에서 구분됩니다. **Kimi Work**는 허용한 로컬 폴더를 읽고, 브라우저에서 자료를 조사하며, 결과를 Word·PDF·Excel·PPT 형식으로 내보내는 데스크톱 앱입니다. 여러 역할의 AI가 일을 나눠 수행하는 Agent Swarm도 제공합니다. 이렇게 모은 자료로 비교표와 발표자료를 만드는 작업까지 이어 갈 수 있습니다. 로컬 파일을 수정하거나 코드를 실행할 때는 `Ask before acting` 설정으로 사전 승인을 요구할 수 있습니다. [Kimi Work 안내](https://www.kimi.com/en/products/kimi-work)

개발자를 위한 **Kimi Code**는 코드 파일을 읽고 수정한 다음 테스트와 빌드 명령을 실행하는 도구입니다. 명령어를 입력하는 터미널의 CLI, 데스크톱 앱, 코드 편집기 확장에서 사용할 수 있습니다. K3.1 Pro를 선택하는 경로는 공식 발표 기준 `/model` 명령입니다. [Kimi Code](https://www.kimi.com/code/en), [모델 이용 경로](https://www.kimi.com/en/blog/kimi-k3-1-pro#availability)

### 글과 이미지로 시작하는 3D 제작

Kimi에서 특히 눈에 띄는 화면은 **3D Make**입니다. [3D Make 페이지](https://www.kimi.com/make3d)를 열면 입력창에 제작 요청을 적거나 아래의 템플릿을 고를 수 있습니다. 화면에는 건축물, 게임 장면 등 서로 다른 예시가 제시되어 있습니다. 건축물의 모형이나 게임에서 쓸 장면을 만들려는 사람을 위한 작업 공간입니다.

{{media:kimi-3d}}

Moonshot은 글·스케치·참고 이미지로 형태를 지정하고, 모델을 미리 보거나 수정하며, 3D 프린팅용 파일이나 영상으로 내보내는 기능을 소개합니다. 발표에 실린 제작 사례에는 Blender나 CAD 프로그램의 스크립트를 작성하고 실행하는 작업도 포함됩니다. 이는 Moonshot이 공개한 기능과 사례이며, 위 화면은 제작을 시작하는 화면입니다. [3D 제작 설명](https://www.kimi.com/en/blog/kimi-k3-1-pro#_3d-modeling-and-design)

3D 형태를 얼마나 비슷하게 재현하는지도 공개 자료에서 비교할 수 있습니다. BenchCAD는 여러 방향에서 본 물체의 이미지를 주고 CAD 코드로 형태를 복원하게 하는 평가입니다. 이 점수는 완성된 형태가 정답과 겹치는 비율인 Voxel IoU(%)를 나타내며, 높을수록 좋습니다. Moonshot이 공개한 도구 사용 조건에서 Kimi는 92.7%, Opus는 96.2%였습니다.

이 비교에서 Kimi는 도구를 사용해 3D 형태를 복원하는 능력을 보여줍니다. Moonshot은 공개 모델을 전체 데이터 중 1,000개 표본으로 평가했고, Opus 수치는 Anthropic 보고서에서 가져왔습니다. 설계 도면의 치수 정확도나 실제 출력물의 내구성은 이 점수에 포함되지 않습니다. [BenchCAD 평가 조건](https://www.kimi.com/en/blog/kimi-k3-1-pro#coding-benchmarks)

### Opus와 비교하면 어느 정도일까

모델 수준은 여러 과제를 묶은 종합 평가와 특정 업무 평가로 나누어 보겠습니다. 종합 평가에서는 폭넓은 문제 해결 능력을 보고, 업무 평가에서는 문서 작성이나 코드 수정처럼 정해진 작업을 얼마나 잘 마치는지 확인합니다. 서로 다른 평가의 점수는 같은 척도로 환산할 수 없습니다.

**Artificial Analysis의 출시 분석**에서는 종합 지능 지수와 업무 평가인 GDPval-AA를 확인할 수 있습니다. GDPval-AA는 실제 업무 결과물을 서로 비교해 점수를 매깁니다. Elo는 결과물 간 대결에서 추정한 상대 점수이며, 정답률을 뜻하지 않습니다. 두 지표 모두 높을수록 좋습니다. [독립 평가 원문](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks)

| 독립 평가 | Kimi K3.1 Pro | Claude Opus 5.5 |
|---|---:|---:|
| 종합 지능 지수 | 55 | 58 |
| GDPval-AA 업무 평가, Elo | 1,846 | 1,866 |

Kimi는 `max`, Opus의 종합 지수는 `max with fallback` 설정입니다. fallback은 일부 요청에서 다른 모델로 전환될 수 있는 구성이므로, 이 표는 공개된 서비스 설정의 비교로 읽어야 합니다. 한국어 보고서 문체를 따로 채점한 수치는 이 출시 분석에 제시되지 않았습니다.

{{media:aa-intelligence}}

업무별 강점은 Moonshot의 발표에서 더 구체적으로 보입니다. Terminal-Bench 4.0은 터미널에서 코드와 도구를 다뤄 주어진 과제를 해결하는 평가입니다. OfficeQA Pro v2는 여러 재무 문서에서 필요한 근거를 찾고 계산하는 능력을 평가합니다. 아래는 **Moonshot 발표에 실린 비교 수치**이며, 두 항목 모두 높을수록 좋습니다.

| Moonshot 발표의 업무별 평가 | Kimi K3.1 Pro | Claude Opus 5.5 |
|---|---:|---:|
| Terminal-Bench 4.0 | 65.7% | 66.4% |
| OfficeQA Pro v2 | 64.4 | 62.2 |

Kimi는 이 코딩 평가에서 Opus와 0.7%포인트 차이를 보였고, 문서 기반 재무 분석 평가에서는 더 높은 점수를 받았습니다. Moonshot은 Kimi를 주로 최대 추론 설정으로 평가했으며, Terminal-Bench의 다른 모델 점수는 발표문이나 공개 순위표의 최대값을 사용했습니다. OfficeQA에서는 PDF를 이미지로 제공하고 도구를 사용하게 했습니다. **자료에서 근거를 찾아 계산하고 작업을 완료하는 능력**이 Kimi의 장점으로 드러나는 대목입니다. [발표 수치와 평가 각주](https://www.kimi.com/en/blog/kimi-k3-1-pro#agentic-benchmarks)

독립 분석에서는 Terminal-Bench 점수가 67%로 보고되어 있습니다. Moonshot 발표문의 65.7%와 출처를 구분해 표시했습니다. 종합 능력에서는 Opus가 앞서고, 일부 업무 과제에서는 Kimi가 가까운 성적이나 더 높은 수치를 보인다고 정리할 수 있습니다.

### 일반형과 고속형의 API 비용

개발자가 프로그램에서 모델을 호출할 때 쓰는 **일반형 K3.1 Pro의 기본 입출력 단가는 Opus의 절반**입니다. 아래는 2026년 10월 25일 확인한 국제 API 가격으로, 모두 100만 토큰당 미국 달러입니다. 입력은 모델에 보내는 자료, 출력은 모델이 생성하는 내용입니다. 캐시 입력은 앞서 보낸 같은 자료를 재사용할 때 적용됩니다. [Kimi 공식 가격](https://platform.kimi.ai/docs/pricing/chat), [Claude 공식 가격](https://platform.claude.com/docs/en/about-claude/pricing)

| 모델 | 기본 입력 | 출력 | 캐시 입력 |
|---|---:|---:|---:|
| Kimi K3.1 Pro | $2 | $10 | $0.20 |
| Kimi K3.1 Pro Highspeed | $4 | $20 | $0.20 |
| Claude Opus 5.5 | $4 | $20 | $0.20 |

{{media:kimi-pricing}}

예를 들어 기본 입력 10만 토큰과 청구 대상 출력 1만 토큰을 처리한다고 가정하면 일반형 Kimi는 **$0.30**, Opus는 **$0.60**입니다. 단가에 같은 처리량을 곱한 계산 예시이며, 캐시 저장·검색·외부 도구·세금은 제외했습니다. 추론 과정에서 생성하는 토큰과 재시도 횟수가 달라지면 실제 작업비도 달라집니다.

Highspeed는 Moonshot이 일반형보다 2~3배 빠르다고 소개하는 별도 모델이며, 기본 입출력 단가는 Opus와 같습니다. 캐시 입력 단가도 세 모델이 같습니다. 따라서 긴 자료를 새로 처리하는 비중이 큰지, 같은 자료를 반복해서 읽는지에 따라 비용 차이가 달라집니다. 캐시를 처음 저장하는 비용도 별도로 계산해야 합니다.

이 표는 개발자용 종량제 API 요금입니다. Kimi 웹·앱의 멤버십과 Kimi Code 이용권은 별도 상품입니다. 또한 전체 모델 파일인 가중치는 공식 발표 기준 **11월 4일까지 공개할 예정**입니다. 10월 25일에는 공개 서비스와 API로 이용하는 단계입니다. [과금 상품 구분](https://platform.kimi.ai/docs/pricing/chat#concepts), [제공 현황](https://www.kimi.com/en/blog/kimi-k3-1-pro#availability)

Kimi K3.1 Pro는 문서의 근거를 모아 결과물을 만들고, 코드나 3D 제작 도구를 사용하는 작업에서 주목할 만한 모델입니다. Opus와 비교하면 종합 평가에는 격차가 남아 있고, 업무 과제에서는 경쟁력 있는 수치를 보여줍니다. 여기에 일반형의 낮은 API 입출력 단가가 더해집니다.

### 참고 자료

- [Moonshot: Kimi K3.1 Pro 발표와 평가 조건](https://www.kimi.com/en/blog/kimi-k3-1-pro)
- [Kimi API: 모델 기능과 이용 안내](https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart)
- [Kimi Work: 로컬 파일과 결과물 제작](https://www.kimi.com/en/products/kimi-work)
- [Kimi Code: 코딩 도구 안내](https://www.kimi.com/code/en)
- [Kimi 국제 API 가격](https://platform.kimi.ai/docs/pricing/chat), [Claude API 가격](https://platform.claude.com/docs/en/about-claude/pricing)
- [Artificial Analysis: K3.1 Pro 출시 독립 평가](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks)
