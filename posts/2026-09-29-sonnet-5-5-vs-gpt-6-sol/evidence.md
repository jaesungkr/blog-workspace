# 근거 지도: Sonnet 5.5 vs GPT-6 Sol - AI 모델 비교

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Sonnet 5.5는 범위가 분명한 일상 작업, 버그 수정, 문서·슬라이드·스프레드시트 제작에 초점을 둔 Sonnet 등급 모델입니다. | 공식 | 확인 | [Anthropic 발표](https://www.anthropic.com/claude-sonnet-5-5), 2026-09-28 | 제조사 설명이며 실제 조직별 품질을 보장하지 않습니다. |
| C02 | Sonnet 5.5의 API 단가는 입력 $2, 출력 $10, 캐시 읽기 $0.20/MTok입니다. 캐시 쓰기는 5분 기준 $2.50, 1시간 기준 $4입니다. | 공식 | 확인 | [Claude Platform 모델 문서](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) | Batch, 클라우드 공급자, 데이터 지역 조건은 별도입니다. |
| C03 | Sonnet 5.5는 1M 문맥과 128K 최대 출력을 지원합니다. | 공식 | 확인 | [Claude Platform 모델 문서](https://platform.claude.com/docs/en/models/sonnet-5-5/overview) | 실제 사용 가능량은 도구 결과와 thinking 토큰을 포함합니다. |
| C04 | GPT-6 Sol은 복잡한 코딩과 에이전트 작업을 겨냥하며, 1.05M 문맥과 128K 최대 출력을 지원합니다. | 공식 | 확인 | [OpenAI 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-sol) | 계정별 사용 한도와 가용성은 다를 수 있습니다. |
| C05 | GPT-6 Sol의 표준 API 단가는 입력 $2, 출력 $10, 캐시 읽기 $0.20, 캐시 쓰기 $2.50/MTok입니다. | 공식 | 확인 | [OpenAI 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-sol) | 272K 초과 입력에는 장문 할증이 적용됩니다. Batch, Flex, Fast, 지역 처리는 별도입니다. |
| C06 | GPT-6 Sol은 272K를 넘는 입력에서 전체 요청의 입력·캐시 요금이 2배, 출력 요금이 1.5배가 됩니다. | 공식 | 확인 | [OpenAI 모델 문서](https://developers.openai.com/api/docs/models/gpt-6-sol) | 토큰 수는 모델별 토크나이저로 다시 계산해야 합니다. |
| C07 | Opus 5.5는 입력 $4, 출력 $20/MTok이며 1M 문맥과 128K 최대 출력을 지원합니다. | 공식 | 확인 | [Anthropic 발표](https://www.anthropic.com/claude-opus-5-5), [Claude 문맥 문서](https://platform.claude.com/docs/en/build-with-claude/context-windows) | Fast mode와 클라우드 공급자 비용은 제외합니다. |
| C08 | FrontierCode 1.1 Main에서 Sonnet 5.5의 최고 공개 점수는 52.1%, GPT-6 Sol은 49.3%, Opus 5.5는 54.4%입니다. | 벤더 정리·독립 평가 | 확인 | [Anthropic Sonnet 5.5 발표](https://www.anthropic.com/claude-sonnet-5-5), [Cognition 리더보드](https://cognition.com/frontiercode) | 노력 수준이 다르고 Sonnet 5.5는 Max에서 46.2%로 내려갔습니다. 한 벤치마크의 순위입니다. |
| C09 | GDPval-AA v2.1에서 Sonnet 5.5는 1844, GPT-6 Sol은 1487, Opus 5.5는 1846 Elo로 보고됐습니다. | 벤더 정리·외부 실행 | 확인 | [Anthropic Sonnet 5.5 발표](https://www.anthropic.com/claude-sonnet-5-5), Artificial Analysis 실행 | Sonnet 사전 배포본의 structured output 버그와 GPT-6 Sol 이미지 이해 버그 수정이 점수에 완전히 반영되지 않았을 수 있습니다. |
| C10 | Terminal-Bench 4.0에서 Sonnet 5.5는 70.6%, Opus 5.5는 66.4%지만 GPT-6 Sol 점수는 공개되지 않았습니다. | 벤더 정리·공개 평가 | 확인 | [Anthropic Sonnet 5.5 발표](https://www.anthropic.com/claude-sonnet-5-5) | 이 평가로 Sonnet과 GPT-6 Sol의 우열을 말할 수 없습니다. |
| C11 | Anthropic은 Opus 5.5가 복잡하고 개방적이며 지속적인 판단이 필요한 작업에서 Sonnet 5.5보다 분명히 강하다고 설명합니다. | 벤더 주장 | 확인 | [Anthropic Sonnet 5.5 발표](https://www.anthropic.com/claude-sonnet-5-5) | 정량적 보편 우위가 아니라 제조사의 제품 포지셔닝과 테스트 판단입니다. |
| C12 | 같은 청구 토큰 기준으로 100K 입력·20K 출력은 Sonnet과 Sol이 $0.40, Opus가 $0.80입니다. 500K 입력·50K 출력은 Sonnet $1.50, Sol $2.75, Opus $3.00입니다. | Codex 실행 | 확인 | `artifacts/cost-comparison.py`, `artifacts/cost-comparison.json` | 도구 호출, 캐시, 할인, 지역 할증, 실제 모델별 토큰화 차이는 제외합니다. |

## 직접 검증 설계

- 질문: 공식 가격표가 같은 Sonnet 5.5와 GPT-6 Sol은 짧은 요청과 장문 요청에서도 같은 비용이 드나요?
- 실행 주체: Codex
- 환경과 확인 시점: Python 3 표준 라이브러리, 2026-09-29
- 입력: 짧은 시나리오 100,000 입력·20,000 출력 토큰, 장문 시나리오 500,000 입력·50,000 출력 토큰
- 전처리 또는 표현: 각 모델에서 청구된 토큰 수가 같다고 가정합니다.
- 비교·판정 규칙: `입력 토큰/1M × 입력 단가 + 출력 토큰/1M × 출력 단가`; GPT-6 Sol은 입력 272K 초과 시 입력 $4·출력 $15를 적용합니다.
- 성공 기준: 공식 단가를 그대로 대입한 결과를 재현할 수 있고, 반올림 전 값과 가정을 JSON에 보존합니다.
- 반복 횟수와 표본 크기: 고정 시나리오 2개를 각 모델에 1회 계산합니다.
- 보존할 원자료: `artifacts/cost-comparison.py`, `artifacts/cost-comparison.json`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 100K 입력·20K 출력 | Sonnet $0.40, Sol $0.40, Opus $0.80 | `artifacts/cost-comparison.json` | 캐시와 도구를 제외한 짧은 표준 API 요청 |
| E02 | 500K 입력·50K 출력 | Sonnet $1.50, Sol $2.75, Opus $3.00 | `artifacts/cost-comparison.json` | GPT-6 Sol 장문 할증을 적용한 동일 청구 토큰 가정 |

## 실패와 반례

- 실패한 입력: 해당 없음. 고정 공식 계산이라 실행 실패가 없었습니다.
- 예상과 달랐던 결과: 기본 단가만 보면 Sonnet과 Sol이 같지만, 272K 초과 입력에서는 Sol의 장문 할증 때문에 차이가 생겼습니다.
- 일반화하면 안 되는 범위: 동일한 원문도 모델별 토크나이저와 reasoning 사용량 때문에 같은 토큰 수가 되지 않을 수 있습니다. 소비자 구독료와 실제 작업 성공률도 이 계산에 포함되지 않습니다.

## 미해결 항목

- 없음. 직접 품질 테스트를 수행하지 않았다는 범위는 본문의 추천 문장에 반영합니다.

## 출처 메모

- Anthropic 발표의 벤치마크 표는 여러 외부 평가를 모았지만 발표 주체는 Anthropic입니다. 본문에서 `공개 점수` 또는 `Anthropic이 정리한 표`로 표현합니다.
- Terminal-Bench 4.0에는 GPT-6 Sol 공개 점수가 없으므로 Sonnet의 점수만으로 Sol보다 낫다고 쓰지 않습니다.
- GDPval-AA 점수는 양쪽 모델의 알려진 버그 영향을 완전히 제거한 확정 비교가 아닐 수 있습니다.
- API 요금은 소비자용 Claude·ChatGPT 구독료와 구분합니다.
