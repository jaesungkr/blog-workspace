# GPT-6 Astra vs. Fable 5.1 - AI 모델 비교

Codex가 2026-09-06 공개 원문을 검색한 뒤 실제 페이지를 열어 확인했습니다. 공식 사실, 평가 기관의 측정, 로컬 계산, 편집 판단을 구분합니다.

| ID | 주장 | 근거 | 상태와 한계 |
| --- | --- | --- | --- |
| C01 | Astra는 OpenAI, Fable은 Anthropic의 복잡한 작업용 모델입니다. | https://developers.openai.com/api/docs/models/gpt-6-astra ; https://platform.claude.com/docs/en/models/fable-5-1/overview | 공식 사실이며 생성 이미지는 이를 시각화할 뿐 성능 증거가 아닙니다. |
| C02 | Astra 105만/12만8천, Fable 100만/12만8천 컨텍스트/최대 출력이며 글·이미지 입력과 글 출력을 지원합니다. | C01 양 문서 | 앱 업로드 한도나 동일 문서량으로 바꾸지 않습니다. |
| C03 | AA v4.2는 9월 4일 개편되었습니다. | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2 | 개편 전후 수치를 혼합하지 않습니다. |
| C04 | Astra max: 55점, 과제당 $2.57입니다. | https://artificialanalysis.ai/models/gpt-6-astra | 모델 요약과 v4.2 표제를 함께 확인했습니다. 동적 페이지입니다. |
| C05 | Fable max default fallback: 57점, 과제당 $6.12입니다. | https://artificialanalysis.ai/models/claude-fable-5-1 | 동등 연산량이 아니며 fallback 조건을 포함합니다. |
| C06 | 9월 3일 Coding Agent Index 발표: Astra/Codex 67, Fable 5.1/Claude Code 70입니다. | https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra | 도구 환경이 포함된 별도 척도이며 날짜가 고정된 발표입니다. |
| C07 | 과제당 비용은 입력·캐시·추론·답변 비용을 평가별로 가중평균합니다. | C04/C05 Cost per Intelligence Index Task 설명 | 구독료나 내 작업 견적이 아닙니다. |
| C08 | Astra 비동기 도구 호출, 작업 도중 지시 변경입니다. | https://developers.openai.com/api/docs/guides/latest-model | API 통합 기능이며 모든 앱에 일반화하지 않습니다. |
| C09 | Fable 대화 중 effort 변경 및 진행 텍스트 수신 베타입니다. | https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1 | 기본 display omitted에서는 진행 블록이 비어 있을 수 있습니다. |
| C10 | MTok당 입력 $10/출력 $50은 같고 캐시 읽기는 $1/$0.25입니다. 쓰기는 Astra $12.50/Fable 5분 $12.50입니다. | https://developers.openai.com/api/docs/models/gpt-6-astra ; https://platform.claude.com/docs/en/about-claude/pricing | 표준 요금이며 Fable 1시간 쓰기는 $20입니다. 캐시 보존 옵션 동등성을 주장하지 않습니다. |
| C11 | Astra 입력 >272K이면 요청 전체 입력·캐시 2배, 출력 1.5배입니다. Fable 1M은 표준 요금입니다. | C10 Astra 문서 ; https://platform.claude.com/docs/en/build-with-claude/context-windows | 초과분만 할증하는 구조가 아닙니다. |
| C12 | 계산 예시: 1.50/1.50, 0.70/0.625, 6.75/3.50입니다. | artifacts/cost_scenarios.py ; artifacts/cost-results.json | Codex 로컬 Decimal 계산이며 실제 API 측정이 아닙니다. |
| C13 | Fable 메뉴, Code >=2.1.255, Pro 별도 크레딧, Max 주간 제한입니다. | https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan | 유료 플랜이면 무제한 포함된다고 쓰지 않습니다. |
| C14 | 먼저 기존 환경에서 대표 작업을 시험하고 목적별 후보를 고릅니다. | C04~C13에 근거한 dev.log 선택 규칙입니다. | 순위나 결과 보장이 아닙니다. |
| C15 | 대표 이미지는 동등 비중의 모델 비교입니다. | C01, C14 및 기존 비교 시리즈 방향입니다. | 생성 이미지가 성능 증거로 쓰이지 않습니다. |

## 평가 버전과 제외한 수치

9월 3일 출시 글에는 v4.1.1의 61/66이 있고 현재 페이지는 v4.2의 55/57입니다. 9월 4일 개편 원문에서 항목 추가와 재가중을 확인했습니다. 최신 비교에는 v4.2를 사용하고 코딩 에이전트 점수는 날짜를 붙입니다. 제3자 블로그의 67.0/67.2와 $1.67/~$3.70은 섞지 않았습니다. Astra 출력 속도도 요약과 FAQ에 다른 값이 있어 제외했습니다. 미확인 앱 플랜 한도와 한국어 품질 우열은 넣지 않았습니다.

## 원래 기여와 재현

`python3 posts/2026-09-06-gpt-6-astra-vs-fable-5-1/artifacts/cost_scenarios.py`로 계산합니다. 입력은 스크립트에, 결과와 가정은 JSON에 있습니다. 고정 토큰 수의 가상 요청 3개이며 모델 호출, 한국어 토큰화, 품질, 지연시간 실험은 수행하지 않았습니다. 출력에는 추론 비용을 포함하고 캐시 적중 행은 최초 쓰기를 제외합니다. 도구 비용, 세금, 할인도 제외합니다. 원문 반환은 artifacts/sources에 보존합니다.
