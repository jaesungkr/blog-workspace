# 근거 지도: Opus 5.5 vs GPT-6 Astra - AI 모델 비교

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Anthropic은 2026-09-22 Opus 5.5를 공개했고, Fable 5.1 수준의 성능을 대부분의 작업에서 더 낮은 비용으로 제공한다고 설명합니다. | 벤더 주장 | 확인 | https://www.anthropic.com/claude-opus-5-5 | 제공사의 종합 설명이며 모든 작업의 동등성을 뜻하지 않습니다. |
| C02 | Opus 5.5는 1M 문맥, 128K 최대 출력, 기본 `medium` effort, 입력 $4·출력 $20·캐시 읽기 $0.20/MTok입니다. | 공식 | 확인 | https://platform.claude.com/docs/en/models/opus-5-5/overview | Claude API 표준 요금이며 Fast mode와 중개 서비스는 다릅니다. |
| C03 | GPT-6 Astra는 1.05M 문맥, 128K 최대 출력, `low`부터 `max` effort, 입력 $10·출력 $50·캐시 읽기 $1/MTok입니다. | 공식 | 확인 | https://developers.openai.com/api/docs/models/gpt-6-astra | OpenAI API 표준 요금입니다. 272K 입력 초과 요청은 전체 요청에 장문 요금이 적용됩니다. |
| C04 | Fable 5.1은 1M 문맥, 128K 최대 출력, 기본 `high` effort, 입력 $10·출력 $50·캐시 읽기 $0.25/MTok입니다. | 공식 | 확인 | https://platform.claude.com/docs/en/models/fable-5-1/overview | Claude API 표준 요금입니다. |
| C05 | Astra는 Responses API에서 비동기 도구 호출, 작업 중 지시 변경, 대화 중 reasoning effort 변경을 지원합니다. | 공식 | 확인 | https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra | API 기능이며 ChatGPT의 화면 기능과 동일하다고 볼 수 없습니다. |
| C06 | Anthropic 표에서 Opus 5.5는 Terminal-Bench 4.0, FrontierCode, GDPval-AA, HLE에서 Astra보다 높고, Astra는 AutomationBench와 Terminal-Bench-Science에서 높습니다. | 벤더 비교 | 확인 | https://www.anthropic.com/claude-opus-5-5 | 평가별 effort, 도구, 실행 주체가 다르고 일부 Astra 수치는 OpenAI·공개 리더보드에서 가져왔습니다. |
| C07 | 같은 Anthropic 표에서 Opus 5.5는 본문에 제시한 여섯 항목 모두 Fable 5.1보다 높지만, Anthropic은 실제 체감 격차가 표보다 작다고 설명합니다. | 벤더 비교 | 확인 | 동일 발표 페이지 | 제공사가 자사 모델끼리 비교한 결과이며 제품별 fallback 영향이 있습니다. |
| C08 | Artificial Analysis v4.3.2의 최대 추론 구성에서 Intelligence Index는 Opus 58, Astra 53, Fable 53입니다. | 독립 평가 | 확인 | https://artificialanalysis.ai/models/claude-opus-5-5, https://artificialanalysis.ai/models/gpt-6-astra, https://artificialanalysis.ai/models/claude-fable-5-1 | Claude 두 모델은 Default Fallback 구성입니다. 종합 지수는 10개 평가의 가중 결과입니다. |
| C09 | 같은 평가에서 출력 속도는 Opus 92.5, Fable 67.9, Astra 59.1 tok/s입니다. | 독립 평가 | 확인 | 동일 Artificial Analysis 모델 페이지 | 출력 시작 전 대기와 도구 실행을 포함한 종단 간 완료 시간이 아닙니다. |
| C10 | 같은 평가의 과제당 비용은 Astra $3.26, Opus $5.98, Fable $7.63입니다. | 독립 평가 | 확인 | 동일 Artificial Analysis 모델 페이지 | 모델마다 생성한 토큰 수가 달라 단가표와 순서가 다릅니다. 최대 추론 구성에 한정합니다. |
| C11 | Artificial Analysis 전체 지수 실행의 출력 토큰은 Opus 260M, Fable 190M, Astra 60M으로 표시됩니다. | 독립 평가 | 확인 | 동일 Artificial Analysis 모델 페이지 | 평가 전체 합계이며 한 과제의 출력 길이가 아닙니다. |
| C12 | 동일한 입력·출력 토큰 수를 가정하면 Opus의 일반 입출력 비용은 Astra·Fable보다 60% 낮습니다. | Codex 계산 | 확인 | `artifacts/compare_costs.py`, `artifacts/compare_costs.json` | 품질, 재시도, 모델별 토큰 사용량이 같다는 구조 예시입니다. |
| C13 | 입력 2M·캐시 읽기 20M·출력 1M의 반복 작업 예시에서는 Opus $32, Astra $90, Fable $75입니다. | Codex 계산 | 확인 | 동일 계산 산출물 | 캐시 쓰기, 도구 호출료, 세금과 중개 수수료를 제외합니다. |
| C14 | 입력 300K·출력 50K의 단일 요청 예시에서는 Opus $2.20, Astra $9.75, Fable $5.50입니다. | Codex 계산 | 확인 | 동일 계산 산출물 | Astra의 272K 초과 장문 요금을 전체 요청에 적용한 구조 예시입니다. |
| C15 | Anthropic은 Fable 5.1을 까다로운 추론과 장시간 에이전트 작업, 또는 Opus의 높은 effort에서도 부족한 작업에 권합니다. | 공식 | 확인 | https://platform.claude.com/docs/en/models/fable-5-1/overview | 문서의 Opus 비교 문구는 Opus 5를 가리키지만, 후속 Opus 5.5 발표는 대부분의 작업에서 Fable 5.1 수준이라고 설명합니다. |
| C16 | Opus·Fable은 1M, Astra는 1.05M 문맥이며 세 모델 모두 128K 최대 출력을 제공합니다. | 공식 | 확인 | 세 모델 공식 사양 페이지 | 실제 입력 가능량은 시스템·도구·출력 예약 토큰에 따라 줄 수 있습니다. |
| C17 | 새 API의 기본 시험 모델은 Opus 5.5, OpenAI 도구 기능이 중요한 경우 Astra, Opus로 목표 품질을 못 맞춘 장기 과제는 Fable 5.1이라는 선택 순서가 합리적입니다. | 근거 기반 판단 | 확인 | C01~C16 | 직접 동일 프롬프트 실험의 결론이 아니라 공개 근거에서 만든 시작점입니다. |

## Arena 추가 근거: 2026-09-29 확인

| ID | 주장 | 출처와 조건 | 해석 범위 |
|---|---|---|---|
| C18 | Arena는 이름을 가린 두 모델의 응답 중 사용자가 선호하는 결과에 투표하는 비교 방식을 제공합니다. | https://arena.ai/how-it-works | 사용자 선호도이며 정답률과 같지 않습니다. Agent의 별도 지표까지 같은 방식이라고 설명하지 않습니다. |
| C19 | Text Overall에서 Opus 5.5 high는 1위 1509±12, Astra max는 26위 1478±8, Fable 5.1 max는 5위 1501±7입니다. | https://arena.ai/leaderboard/text, 표시 갱신일 2026-09-25 | Opus 투표 2,307건, Rank Spread 1~10. Fable의 점수 구간과 겹칩니다. 모델별 effort가 다릅니다. |
| C20 | WebDev에서 Opus 5.5 max는 1위 1827±18, Astra max는 2위 1792±11, Fable 5.1 max는 3위 1751±10입니다. | https://arena.ai/leaderboard/code/webdev, 표시 갱신일 2026-09-25 | 프런트엔드 웹 개발 결과물 비교이며 모든 코딩 업무의 우위를 뜻하지 않습니다. |
| C21 | Agent에서는 Fable 5.1 max 1위, Opus 5.5 high 2위, Astra max 3위입니다. | https://arena.ai/leaderboard/agent, 표시 갱신일 2026-09-28 | 도구 신뢰성·작업 완료·지시 변경 등의 신호를 사용하는 별도 동적 순위입니다. Net Improvement를 정답률이나 성공률로 바꾸지 않습니다. |
| C22 | Opus 5에서 Opus 5.5로 엠대시는 15.2→0.8회, 세미콜론은 6.10→1.64회로 감소했습니다. | 사용자가 제공한 Arena Language Markers 차트, Text Arena 2026년 8~9월, reasoning high, 1,000단어당 빈도 | 문체 특징만 보여 줍니다. 한국어 자연스러움·정확성·아첨 감소 또는 순위 상승의 원인으로 단정하지 않습니다. |

- C19~C21의 숫자와 날짜는 각 공식 리더보드를 직접 열어 확인했습니다. Text의 화면 제목은 Overall이며, 추출 결과로는 Style Control 조정 선택 여부를 판별할 수 없어 이에 관한 주장은 하지 않습니다.
- C22 원자료는 `artifacts/sources/arena-language-markers-user.png`에 보존했습니다. 사용자가 제공한 차트의 숫자·단위·기간·추론 조건을 직접 읽었습니다.
- 차트의 Arena 게시물 링크는 `https://x.com/arena/status/2103532528946839901/photo/2`입니다. 공개 보도에 연결된 원문 링크로 위치를 확인했으나 X 직접 요청은 HTTP 403으로 차단됐습니다. 따라서 수치 확인은 첨부된 차트에 근거하며, X 본문 전체를 읽었다고 주장하지 않습니다.
- 첨부 차트는 검증용 근거로만 보존하며 게시용 이미지로 재배포하지 않습니다. 기존 대표 이미지와 CDN 연결은 변경하지 않습니다.

## 직접 검증 설계

- 질문: 공식 단가와 공개 평가를 분리하면 세 모델의 합리적인 시험 순서를 만들 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: 공개 웹 문서, Python 3 결정적 계산, 2026-09-29
- 입력: 세 모델 공식 사양·가격, Anthropic Opus 5.5 비교표, Artificial Analysis v4.3.2 모델 페이지
- 전처리 또는 표현: 가격은 100만 토큰당 미국 달러로 통일하고, 성능 점수는 서로 다른 평가끼리 합산하지 않습니다.
- 비교·판정 규칙: 벤더 결과와 독립 결과를 분리하고, 높은 점수·속도는 높을수록 좋으며 비용은 낮을수록 좋다고 읽습니다. 토큰 단가 예시는 동일한 사용량만 대입합니다.
- 성공 기준: 계산 스크립트를 다시 실행하면 같은 금액과 절감률이 나오며, 모든 수치가 2026-09-29에 확인한 원문과 일치합니다.
- 반복 횟수와 표본 크기: 결정적 비용 계산 1회, 공개 모델 페이지 6개 대조
- 보존할 원자료: `artifacts/compare_costs.py`, `artifacts/compare_costs.json`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 일반 요청 묶음: 입력 1M·출력 0.2M | Opus $8.00, Astra $20.00, Fable $20.00 | `artifacts/compare_costs.json` | 같은 토큰 수일 때 Opus가 60% 저렴합니다. |
| E02 | 반복 에이전트: 입력 2M·캐시 읽기 20M·출력 1M | Opus $32.00, Astra $90.00, Fable $75.00 | `artifacts/compare_costs.json` | 캐시 쓰기와 도구비는 제외합니다. |
| E03 | 단일 장문 요청: 입력 0.3M·출력 0.05M | Opus $2.20, Astra $9.75, Fable $5.50 | `artifacts/compare_costs.json` | Astra의 272K 초과 장문 요금을 적용했습니다. |
| E04 | Artificial Analysis v4.3.2 최대 추론 구성 | 지수 Opus 58, Astra 53, Fable 53. 과제당 비용은 Astra $3.26, Opus $5.98, Fable $7.63 | 외부 모델 페이지 | 단가와 과제당 비용의 순서가 다름을 보여 줍니다. |

## 실패와 반례

- `Opus는 단가가 낮으므로 모든 실제 과제에서 가장 저렴하다`는 주장은 Artificial Analysis의 최대 추론 구성과 충돌합니다. Astra가 적은 출력 토큰을 사용해 과제당 비용이 더 낮았습니다.
- Anthropic 표에서도 Astra는 AutomationBench와 Terminal-Bench-Science에서 Opus 5.5보다 높았습니다. Opus가 모든 업무에서 우세하다고 일반화할 수 없습니다.
- Artificial Analysis의 Opus·Fable 결과는 fallback이 허용된 구성입니다. 모델 가중치 하나만의 결과라고 부르지 않습니다.
- 출력 토큰/초는 첫 토큰 대기와 도구 실행 시간을 포함한 전체 완료 속도가 아닙니다.

## 미해결 항목

- 없음. 소비자 구독 한도와 직접 API 품질 실험은 본문 주장 범위에서 제외합니다.

## 출처 메모

- 사용자가 제공한 Anthropic 발표문을 중심 출처로 사용하고, 모델 사양은 각 공식 문서에서 다시 확인했습니다.
- OpenAI 정보는 official OpenAI documentation의 GPT-6 Astra 모델 페이지와 최신 모델 가이드에서 확인했습니다.
- 2026-09-29의 공개 자료 스냅샷에 근거합니다. 가격과 평가값은 이후 바뀔 수 있습니다.
