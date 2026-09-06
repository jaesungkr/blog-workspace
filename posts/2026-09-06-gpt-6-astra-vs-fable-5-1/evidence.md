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

## 2026-09-06 전면 개정 근거

| ID | 추가 주장 | 근거와 관찰 | 범위 |
| --- | --- | --- | --- |
| C16 | Fable 5.1은 9월 1일, Astra는 9월 3일에 공개되어 이틀 간격입니다. | Anthropic Fable 페이지 Announcements 날짜, AA 9월 3일 Astra 출시 평가입니다. | 웹을 다시 열었고 공식 화면과 DOM을 보존했습니다. |
| C17 | Fable와 Mythos 5.1은 기반 모델이 같으며 안전장치와 접근 대상이 다릅니다. | https://www.anthropic.com/claude-fable-and-mythos-5-1 Introduction | 비교는 Fable 5.1입니다. |
| C18 | 공식 9종: Terminal4 57.9/55.8, DeepSWE74.1/67.4, FrontierCodeExtended64.5/63.6, Automation41.4/31.4, Science64.6/52.6, FrontierMath97.6/87.8, GPQA96.0/93.7, HLE57.2/65.0, ARC2 95.0/90.0입니다. | https://openai.com/index/gpt-6-astra/ 하단 표, artifacts/captures/revision/openai-astra-dom.txt | OpenAI 발표값, 최고 effort, 연구/API 환경입니다. FrontierCode 개발자 지시 주석을 유지합니다. |
| C19 | 과학 평가 그래프는 해결률과 API 비용을 여러 effort 점으로 표시합니다. | C18 공식 그래프 캡처, Anthropic 발표 표준오차 ±3.5~4.5 | 브라우저 그래프를 캡처했으며 결과를 편집하지 않았습니다. |
| C20 | GDP.pdf는 Astra33.2/Fable26.2, 모든 조건을 충족해야 성공입니다. | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2 | 해당 문서 추론 평가이며 모든 장문 작업으로 일반화하지 않습니다. |
| C21 | OSWorld·BenchCAD·ARC3는 동일 비교표에서 제외합니다. | OpenAI 각주3/5와 Fable 공란, Anthropic OSWorld 과제 변경 설명입니다. | 임의로 다른 버전 수치를 채우지 않습니다. |
| C22 | Astra를 코딩·분석 첫 시험 후보로 제안하되 Fable의 종합·긴 작업·캐시 강점을 비교합니다. | C04~C14, C18~C21에 근거한 편집 제안입니다. | 기존의 광범위한 완성도=Fable 주장은 폐기했습니다. PDF 수치와 한국어 품질 한계를 별도로 다룹니다. |

현재 AA 두 모델 페이지와 개편 발표를 다시 열어 55/57, 2.57/6.12, 33.2/26.2를 확인했습니다. 원문 검색 반환은 revision_*.txt에 보존했습니다. 기존 C14 추천 규칙은 C22로 대체됩니다. 이전 섹션의 원문 설명은 초기 리서치 이력입니다.

스크린샷 3장은 공식 웹페이지의 일부를 해설에 필요한 범위로 캡처했습니다. 원본과 출판본 경로·해시·권리는 media.json에 기록합니다. OpenAI 별도 Chrome 캡처가 로딩 대기 화면에 머물러 해당 이미지는 사용하지 않았습니다. Codex in-app browser에서 정상 렌더링한 실제 화면으로 다시 캡처했습니다.
