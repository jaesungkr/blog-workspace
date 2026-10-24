# Gemini 4 Argon vs GPT-6 Astra, 내 작업에는 어떤 AI가 맞을까

확인일: 2026-10-25 (Asia/Seoul). 조사와 계산의 주체는 Codex입니다. 두 모델의 직접 성능 실험은 없습니다.

## 주장 지도

| ID | 내용 | 근거 | 성격과 제한 |
|---|---|---|---|
| C01 | Argon은 9월 30일 제한 공개, 10월 13일 일반 유료 앱/API 공개입니다. | S01, S02, S15 | Google 발표. 일반 공개 후 약 2주 평가입니다. |
| C02 | Argon API 입력은 텍스트·이미지·오디오·비디오·PDF, 출력은 텍스트입니다. | S03 | 앱의 전체 지원과 동일하다고 주장하지 않습니다. 이미지 생성 기능으로 혼동하지 않습니다. |
| C16 | Astra는 계정에 제공되면 Work/Codex의 모델 선택기에서 고릅니다. | S16, S17 | 계정·롤아웃·관리자 설정별 접근 차이가 있습니다. |
| C03 | Astra API는 텍스트·이미지 입력과 텍스트 출력, 웹/파일 검색, 코드 실행, 셸, apply patch 등을 지원합니다. | S04 | ChatGPT 전체 서비스의 음성·영상과 구분합니다. |
| C04 | Google 비교표의 DeepSWE는 77.9/74.1, FrontierSWE는 55.0/65.5입니다. | S05, S06 | Argon/Astra 순. 자사 실측과 외부 공개값이 섞인 제조사 비교표입니다. 동일 환경 재측정 표로 표시하지 않습니다. |
| C05 | AA 비교 페이지에서 Argon High/Astra Max 지수는 53/53, AutomationBench-AA 78/68%, GDP.pdf 22/31%입니다. | S07, S08 | 독립 측정. 주로 영어 텍스트 평가이며 한국어 작문·영상 종합 순위가 아닙니다. |
| C06 | Argon 글쓰기·시각화·PDF 속도에 호평이 있습니다. | S09 | dis-interested, Stauce52, Timely_Summer_4135 등의 직접 경험/평가. 대표성은 없습니다. |
| C07 | Astra 복잡한 백엔드, 긴 작업, 반복 감소에 호평이 있습니다. | S10 | sprakes_, DynaBeast, dempsey1200 등. 주로 Sol 6.1과 비교하며 Argon 상대 통제 실험이 아닙니다. GPT 생성 상단 요약은 근거에서 제외했습니다. |
| C08 | Astra 검색/종합 호평과 느림·중간 정지 불만이 있습니다. | S11 | kbrannigan, kingkongjaffa, Topfi 등의 경험. 일반 한도나 확정 속도로 확대하지 않습니다. |
| C09 | Argon 초기 코딩 리뷰는 다른 모델의 계획과 비교해 Astra 심판 점수를 썼습니다. | S12 | 단일 사례, 추론 설정 차이, 모델 심판. 점수를 성능 순위에 넣지 않습니다. 작성자 후속 댓글의 구조 누락 지적만 한정적으로 소개합니다. |
| C10 | Antigravity Pro 사용량 불만과 더 적게 소모됐다는 반응이 함께 있습니다. | S13 | uvuvevue, joshuahtree 등. 숫자를 모든 계정의 한도로 확대하지 않습니다. |
| C11 | Argon 표준 단가는 11월 30일까지 입력 $2/출력 $10, 12월 1일부터 $4/$20입니다. | S14 | 100만 토큰당 미국 달러. thinking 포함, cache/검색/배치 별도입니다. |
| C12 | Astra 입력 $10/출력 $50, 272K 초과 입력 시 전체 요청 입력 2배/출력 1.5배입니다. | S04 | Standard 기준. Fast/Batch/Flex/도구 비용과 구분합니다. |
| C13 | 입력 100K·과금 출력 10K 가정은 Argon $0.30/$0.60, Astra $1.50입니다. | artifacts/compare_costs.py, cost-results.json | Codex 산술 예시. 모델 실행비 관측이 아닙니다. 사고 토큰까지 과금 출력을 같게 가정합니다. |
| C14 | AA 과제당 비용은 $1.99/$3.26, 비율 약 1.6입니다. | S07 | AA 평가의 가중 평균. 독자 업무 비용 예측이나 구독 요금이 아닙니다. |
| C15 | 현 도구 유지, 막혔던 업무를 입력 형식·수정 부담·비용 기준으로 비교하도록 권합니다. | C02-C14 | dev.log의 근거 기반 선택 프레임. 실측 총순위가 아닙니다. |

## 출처

- S01 https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
- S02 https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- S03 https://ai.google.dev/gemini-api/docs/models/gemini-4-argon/
- S04 https://developers.openai.com/api/docs/models/gpt-6-astra
- S05 https://deepmind.google/models/model-cards/gemini-4-argon/
- S06 https://deepmind.google/models/evals-methodology/gemini-4-argon (5쪽 PDF)
- S07 https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-astra
- S08 https://artificialanalysis.ai/methodology/intelligence-benchmarking (v4.3.2)
- S09 https://www.reddit.com/r/GeminiAI/comments/1x1y2a4/people_who_tried_gemini_4_argon/
- S10 https://www.reddit.com/r/codex/comments/1x8a90j/are_you_still_using_astra_and_if_so_why/
- S11 https://news.ycombinator.com/item?id=49571621
- S12 https://www.reddit.com/r/google_antigravity/comments/1x539fq/gemini_4_argon_initial_review/
- S13 https://www.reddit.com/r/google_antigravity/comments/1x73yrd/my_thoughts_about_argon_4_in_antigravity_pro_user/
- S14 https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon
- S15 https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/?hl=en

- S16 https://learn.chatgpt.com/docs/whats-new
- S17 https://learn.chatgpt.com/docs/models

## 수집과 제외 규칙

검색어는 정확한 모델명 + review/coding/writing/slow/feedback 및 Reddit/HN 조건이었습니다. 서로 다른 다섯 토론에서 직접 경험을 쓴 긍정·부정 사례를 골랐습니다. 전체 여론을 대표하는 표본이 아니므로 비율·만족률을 만들지 않았습니다. 상대 날짜가 수집 시점과 다르게 표시되는 페이지가 있어 개별 후기의 정확한 날짜는 본문에서 생략했습니다. 모델 하향 소문, 미공개 체크포인트, 내부 추론 구조, 댓글의 출력 한도 추측은 채택하지 않았습니다.

## 재현과 한계

python3 artifacts/compare_costs.py 로 산술 계산을 재현합니다. 입력 100K는 Astra 할증 임계값 미만이고 과금 출력 10K에는 사고 토큰을 포함합니다. 실제 API 실행·청구서가 아닙니다. 같은 토큰량 가정과 AA의 관측 과제비를 분리해 독자가 단가비를 실제 절감률로 오해하지 않도록 했습니다.
