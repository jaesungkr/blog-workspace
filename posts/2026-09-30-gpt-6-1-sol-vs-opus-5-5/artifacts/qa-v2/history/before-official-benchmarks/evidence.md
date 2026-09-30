# GPT-6.1 Sol vs Claude Opus 5.5 - 새 GPT 모델의 성능과 가격

관찰일: 2026-09-30, Asia/Seoul입니다. 공개 웹 문서를 실제로 열어 확인했습니다. 검색 요약만으로 확정하지 않았습니다.

## 출처와 주장

| ID | 확인한 주장 | 근거 | 상태와 범위 |
| --- | --- | --- | --- |
| C01 | Sol 6.1은 GPT-6 Sol의 개선 모델이며 Work·Codex의 유료 플랜과 API에 제공됩니다. 일반 Chat에는 아직 제공되지 않습니다. | https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/ 및 https://openai.com/index/introducing-gpt-6-1-sol/ | 공식 출시 안내입니다. 계정·관리자 설정은 개인별로 다를 수 있습니다. |
| C02 | 출시일은 2026-09-29입니다. | https://openai.com/index/devday-2026-recap/ 및 https://deploymentsafety.openai.com/gpt-6-1-sol/respecting-auto-review | 실제 공개 시스템 카드의 Published September 29, 2026 및 DevDay 발표를 확인했습니다. |
| C03 | Opus 5.5는 2026-09-22 출시됐으며 대부분의 업무에서 Fable 5.1 수준이라고 Anthropic이 설명합니다. | https://www.anthropic.com/claude-opus-5-5 | 제조사 포지셔닝이며 동등성의 독립 입증이 아닙니다. |
| C04 | GDP.pdf에서 Sol은 Opus 5.5 with fallbacks보다 높은 점수, 과제 비용은 절반 미만입니다. | https://openai.com/index/introducing-gpt-6-1-sol/ | OpenAI 발표이며 tested reasoning settings 범위입니다. GDP.pdf는 PDF의 표·차트·각주를 포함한 전문 질문 평가입니다. 독립 재현을 주장하지 않습니다. |
| C05 | AutomationBench 1.0.6에서 Sol medium은 Opus보다 2.2%p 높고 과제 비용은 약 1/3입니다. Fable의 약 40% 과제 fallback 비용이 차트 비용에서 누락되었습니다. | 위 OpenAI 출시 페이지 | 47개 도구로 영업·운영·지원 등의 다단계 업무를 수행하는 벤치마크입니다. Fable 비용과 다른 모델을 단순하게 섞어 비용순위를 내지 않습니다. |
| C06 | DeepSWE v1.1에서 Sol은 Astra의 수준을 약 1/5 비용에 달성했다고 OpenAI가 보고합니다. | 위 OpenAI 출시 페이지 | 실제 저장소의 장기 개발 작업입니다. Opus와의 코딩 전체 우열을 선언하지 않습니다. |
| C07 | Opus 출시 표의 Sol은 GPT-5.6 Sol입니다. | https://www.anthropic.com/claude-opus-5-5 | Terminal-Bench 4.0, FrontierCode, CursorBench의 옛 Sol을 새 Sol 6.1로 바꾸어 인용하지 않습니다. |
| C08 | AA Intelligence Index v4.3.2는 10개 평가를 묶고 높은 점수가 좋은 종합 지수입니다. | https://artificialanalysis.ai/models/claude-opus-5-5 | 개별 모델 페이지의 명시 버전과 구성입니다. 정답률이 아닙니다. |
| C09 | AA의 medium/max 및 max 과제당 비용은 아래 관찰값과 같습니다. | https://artificialanalysis.ai/leaderboards/models | 독립 기관의 2026-09-30 정수 표시값입니다. Claude는 with fallback입니다. 각 회사의 effort 이름이 동일 계산량을 보장하지 않습니다. |
| C10 | Sol의 표준 입력/출력/캐시 입력 단가는 $2/$10/$0.10이며 입력 272K 초과 요청은 입력·캐시 2배 및 출력 1.5배입니다. | https://developers.openai.com/api/docs/models/gpt-6.1-sol | 100만 토큰당 USD입니다. Fast·Batch·Flex·지역 요금이 다르며 예시에서는 제외합니다. API ID와 Work 접근은 별개입니다. |
| C11 | Opus의 입력/출력/캐시 읽기 단가는 $4/$20/$0.20입니다. | https://www.anthropic.com/claude-opus-5-5 | 100만 토큰당 USD, 일반 API입니다. 캐시 쓰기 $5, Fast $8/$40은 본문 가격표에서 제외했습니다. |
| C12 | Astra와 Fable의 기본 입력/출력은 $10/$50입니다. | https://developers.openai.com/api/docs/models/gpt-6-astra 및 https://www.anthropic.com/claude-fable-and-mythos-5-1 | 100만 토큰당 USD입니다. 실제 작업 비용은 같다는 주장이 아닙니다. |
| C13 | 가장 어려운 과학 연구에는 OpenAI가 Astra를 권장합니다. | OpenAI 출시 페이지 | 제조사의 용도별 권고입니다. Anthropic의 과학 점수와 서로 다른 Astra 점수를 합쳐 새 순위를 만들지 않습니다. |
| C14 | 입력 100,000 및 출력 10,000 토큰의 요금은 Sol $0.30, Opus $0.60, Astra·Fable $1.50입니다. | artifacts/research/calculate_api_cost.py 및 api-cost-result.json | Codex가 Decimal로 실행한 가정 계산입니다. 성능시험이 아닙니다. 실제 토큰 소모·재시도·캐시·도구·모드·구독 요금은 제외했습니다. |
| C15 | 기존 결과와 같은 자료·완료 조건을 써서 재작업 시간과 총비용을 비교하라는 권고입니다. | C04-C14에 근거한 본 글의 판단 틀입니다. | 업무별 발표와 종합 지수의 차이를 선택 방법으로 연결합니다. 실제 전환 성공을 보장하지 않습니다. |

## AA 관찰값

| 모델 | medium | max | max 비용 USD/과제 |
| --- | ---: | ---: | ---: |
| GPT-6.1 Sol | 48 | 52 | 0.72 |
| Claude Opus 5.5 with fallback | 51 | 58 | 5.98 |
| GPT-6 Astra | 50 | 53 | 3.26 |
| Claude Fable 5.1 with fallback | 49 | 53 | 7.63 |

max의 Opus 비용은 개별 페이지 https://artificialanalysis.ai/models/claude-opus-5-5 에서도 $5.98로 확인했습니다. Sol 개별 페이지 https://artificialanalysis.ai/models/gpt-6-1-sol 을 열었으나 재조회 한 건에서 Internal Error가 발생했습니다. 표는 정상 열람한 리더보드 기준이며 오류 응답을 근거로 쓰지 않았습니다. 위 표는 HTML 원문 스냅샷이 아닌 열람값 전사 기록입니다.

## 연구에서 제외한 정보

- Reddit과 개인 블로그는 독자의 관심 질문을 찾는 데만 사용했고, 성능·사용한도·속도 사실의 근거로 사용하지 않았습니다.
- OpenRouter와 ModelCap의 종합 요약값은 독립 평가의 원출처를 찾는 데만 참고했습니다.
- 과거 AA 지수 버전의 점수와 이번 v4.3.2 점수를 섞지 않았습니다.
- Anthropic 발표의 Opus 58.7%, Astra 64.6%와 OpenAI의 Astra 68.1% 과학 점수를 합치지 않았습니다. 발표 주체·설정 차이가 있습니다.
- 실제 Sol/Opus 추론, 한국어 글쓰기 평가, GUI 실행, 구독 한도 비교를 수행하지 않았습니다.
- 공개 원고에는 수치가 영향을 주는 위치에서 조건과 발행 주체를 설명합니다. 포괄적인 미실행 면책 문구는 추가하지 않습니다.

## 재현

실행 주체는 Codex입니다. Python 3 표준 라이브러리 Decimal을 사용했습니다.

```bash
python3 posts/2026-09-30-gpt-6-1-sol-vs-opus-5-5/artifacts/research/calculate_api_cost.py
```

저장된 출력: `artifacts/research/api-cost-result.json`입니다. 입력단가 × 0.1 + 출력단가 × 0.01로 계산하며, 캐시·도구·모드 할증을 켜면 이 값으로 실제 청구액을 예측할 수 없다는 한계를 보존했습니다.
