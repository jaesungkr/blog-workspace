# 근거 지도: Fable 5.1 vs Fable 5 - 클로드 모델 비교

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Claude Fable 5.1은 2026년 9월 1일 출시됐고 API ID는 `claude-fable-5-1`입니다. | 공식 | 확인 | [Fable 5.1 모델 문서](https://platform.claude.com/docs/en/models/fable-5-1/overview) | 플랫폼별 ID는 다를 수 있음 |
| C02 | Fable 5.1과 Fable 5는 100만 토큰 문맥, 최대 12만 8천 출력, 입력 $10·출력 $50/100만 토큰, 5분 캐시 쓰기 $12.50의 기본 사양을 공유합니다. | 공식 | 확인 | [Fable 5.1 문서](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1), [공식 가격표](https://platform.claude.com/docs/en/about-claude/pricing) | 실제 청구액은 출력량·캐시·도구 호출에 따라 달라짐 |
| C03 | 캐시 읽기는 Fable 5의 $1에서 Fable 5.1의 $0.25/100만 토큰으로 75% 인하됐습니다. | 공식 | 확인 | [공식 가격표](https://platform.claude.com/docs/en/about-claude/pricing) | 캐시가 적중한 입력에만 적용됨 |
| C04 | Fable 5.1의 신뢰도 높은 지식 기준일은 2026년 6월이고 Fable 5는 2026년 1월입니다. | 공식 | 확인 | [Fable 5.1 개요](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Fable 5 출시 문서](https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5) | 지식 기준일은 모든 사실의 정확성을 보장하지 않음 |
| C05 | Anthropic의 공개 비교표에서 Fable 5.1은 Fable 5보다 7개 평가군의 9개 결과 행에서 모두 높습니다. 비교군은 Terminal-Bench-Science, Terminal-Bench 4.0, GDPval-AA v2, OSWorld 2.0, HLE, AutomationBench, CursorBench 3.2.0입니다. | 벤더 평가 | 확인 | [Claude Fable 공식 페이지](https://www.anthropic.com/claude/fable), `artifacts/research/anthropic-fable-5-1-benchmarks.png` | 제조사 평가이며 설정·폴백·안전장치가 결과에 포함됨 |
| C06 | Terminal-Bench-Science는 52.6% 대 24.7%, Terminal-Bench 4.0은 55.8% 대 42.0%입니다. GDPval-AA v2는 실제 업무 결과물을 블라인드로 비교한 Elo 평점이며 1,853 대 1,723입니다. | 벤더 평가 | 확인 | 같은 공식 표 | Science 표준오차는 모델당 ±3.5~4.5점이며 다른 하네스와 직접 비교 불가 |
| C07 | OSWorld 2.0은 partial 77.9% 대 72.9%, strict 41.7% 대 36.1%, HLE는 도구 없음 60.9% 대 57.8%·도구 사용 65.0% 대 63.8%입니다. | 벤더 평가 | 확인 | 같은 공식 표 | OSWorld는 2026년 8월 작업 세트이며 이전 공개 수치와 직접 비교 불가 |
| C08 | AutomationBench는 31.4% 대 17.1%, CursorBench 3.2.0은 73.4% 대 70.5%입니다. | 벤더 평가 | 확인 | 같은 공식 표 | Fable 5의 AutomationBench 일부 안전장치 개입은 0점 처리됨 |
| C09 | Artificial Analysis에서 Fable 5.1 max는 지능 지수 66점, Fable 5 max는 62점입니다. | 외부 평가 | 확인 | [Artificial Analysis 출시 평가](https://artificialanalysis.ai/articles/claude-fable-5-1) | Anthropic 출시 전 평가를 지원했고 기본 폴백이 출력 토큰 약 4%를 처리함 |
| C10 | 같은 평가에서 Fable 5.1 max의 과제당 비용은 $3.76으로 Fable 5 max의 $3.14보다 20% 높고, 출력 토큰은 약 1.7배입니다. | 외부 평가 | 확인 | 같은 Artificial Analysis 글 | 해당 지수의 평균이며 실제 Claude Code 청구액이 아님 |
| C11 | Fable 5.1 xhigh는 65점·$2.72로 max보다 1점 낮고 $1.04 저렴합니다. | 외부 평가 | 확인 | 같은 Artificial Analysis 글 | 과제별 승패와 지연시간은 별도 확인 필요 |
| C12 | 캐시 읽기 4M인 구조 예시에서는 Fable 5 $12.50, 5.1 $9.50으로 24.0% 절감됩니다. 10M에서는 $18.50 대 $11.00으로 40.5% 절감됩니다. | Codex 실행 | 확인 | `artifacts/compare_fable_costs.py`, `artifacts/compare_fable_costs.txt` | 나머지 토큰 수를 동일하게 고정한 구조 예시이며 실측 청구서가 아님 |
| C13 | Fable 5.1은 forced tool use를 지원하지 않고, 이전 모델은 5.1의 thinking 블록을 읽지 못하며, 과거 대화를 수정하면 이후 thinking 블록이 무효가 될 수 있습니다. | 공식 | 확인 | [Fable 5.1 변경점](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1), [마이그레이션 가이드](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide) | API를 직접 구성하는 통합에서 특히 중요함 |
| C14 | Claude Code에서 Fable 5.1은 2.1.250 이상이 필요합니다. | 공식 | 확인 | [Anthropic 도움말](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan) | 앱 버전과 플랜 제공 범위는 바뀔 수 있음 |
| C15 | Anthropic은 대부분의 작업에 Opus 5부터 쓰고, 더 높은 effort에서도 부족한 장시간 난도 작업에 Fable 5.1을 권합니다. | 공식 권고 | 확인 | [Fable 5.1 모델 문서](https://platform.claude.com/docs/en/models/fable-5-1/overview) | 조직의 자체 평가가 공식 기본값보다 우선함 |
| C16 | Fable 계열은 기본적으로 30일 데이터 보존을 요구합니다. EFS 적용 대상 조직은 데이터를 자체 클라우드에 저장하며, 사람의 검토가 필요하면 기본적으로 Anthropic이 아니라 해당 조직이 담당합니다. EFS 제공 전에는 Fable 5.1을 zero data retention으로 사용할 수 있습니다. 대부분의 Claude 앱은 분류기 개입 시 자동 폴백하지만 API 고객은 Fallback API를 구성해야 합니다. | 공식 | 확인 | [Claude Fable 공식 페이지](https://www.anthropic.com/claude/fable), [Fable 5.1 변경점](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) | 조직별 자격·계약과 EFS 제공 상태를 별도로 확인해야 함 |
| C17 | Fable 5.1은 Fable 5가 여러 독립 도구를 묶어 호출하던 상황에서 한 턴에 하나씩 호출하는 경우가 있어 턴 수와 대기시간이 늘 수 있습니다. 여러 대상을 명시한 요청에서는 병렬 호출이 유지됩니다. | 공식 동작 차이 | 확인 | [Fable 5.1 변경점](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1) | 품질 저하나 병렬 호출 불가를 뜻하지 않으며 명시적 요청으로 완화 가능 |
| C18 | Fable 5.1은 작은 텍스트 파일 수정에서도 전체 파일을 다시 쓸 가능성이 높고, 일부 답변의 문장이 Fable 5보다 조밀할 수 있습니다. | 공식 동작 차이 | 확인 | 같은 변경점 문서 | 모든 작업에서 발생하는 것은 아니며 프롬프트로 완화 가능 |

## 비교 설계

- 질문: 기존 Fable 5 작업을 Fable 5.1로 옮기면 성능과 비용이 함께 좋아지나요?
- 실행 주체: 공개 평가는 Anthropic과 Artificial Analysis, 비용 구조 계산과 이전 판단은 Codex
- 환경과 확인 시점: 2026-09-02 Asia/Seoul, 공개 웹 문서와 저장소 계산 스크립트
- 입력: Anthropic 공식 사양·가격·벤치마크·마이그레이션 문서, Artificial Analysis 출시 평가, dev.log의 기존 Claude 비교 글
- 전처리 또는 표현: 제조사 표의 같은 행만 대조하고, 외부 평가는 같은 Intelligence Index 버전의 max·xhigh 수치만 사용
- 비교·판정 규칙: 벤치마크와 지능 지수는 높을수록, 과제당 비용은 낮을수록 유리합니다. 기본 단가·출력량·캐시 읽기를 분리해 어느 한 지표로 전체 우승을 정하지 않습니다.
- 성공 기준: 기존 Fable 작업의 기본 이전 후보는 주요 공식 지표가 악화되지 않고, 호환성 문제를 해결할 수 있으며, 자체 대표 과제의 성공률 또는 비용이 개선돼야 합니다.
- 반복 횟수와 표본 크기: 외부 평가 기관이 공개한 집계값을 사용했습니다. dev.log 비용 계산은 두 구조 예시를 각각 한 번 결정적으로 실행했습니다.
- 보존할 원자료: `artifacts/research/`, `artifacts/compare_fable_costs.py`, `artifacts/compare_fable_costs.txt`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 캐시 쓰기 0.2M, 캐시 읽기 4M, 비캐시 입력 0.1M, 출력 0.1M | Fable 5 $12.50, Fable 5.1 $9.50, 24.0% 절감 | `artifacts/compare_fable_costs.txt` | 캐시 읽기 단가 차이만 격리한 짧은 반복 세션 |
| E02 | 같은 고정 비용, 캐시 읽기만 10M | Fable 5 $18.50, Fable 5.1 $11.00, 40.5% 절감 | 같은 파일 | 같은 긴 문맥을 여러 번 읽는 에이전트 구조 |
| E03 | Anthropic 공개표의 Fable 5.1과 Fable 5 7개 평가군·9개 결과 행 비교 | Fable 5.1이 9개 결과 행 모두 높음 | `artifacts/research/anthropic-fable-5-1-benchmarks.png` | 제조사 표 안에서의 방향성만 확인 |

## 실패와 반례

- 예상과 달랐던 결과: 기본 입력·출력 단가와 캐시 쓰기 가격이 같아도 Artificial Analysis의 `max` 과제당 비용은 Fable 5.1이 20% 높았습니다.
- 원인 후보: 같은 평가에서 Fable 5.1이 약 1.7배의 출력 토큰을 사용했습니다.
- 반례: `xhigh`에서는 지능 지수가 max보다 1점만 낮으면서 과제당 비용이 $1.04 줄었습니다.
- 일반화하면 안 되는 범위: 이 외부 지수 한 묶음으로 Fable 5.1이 모든 실제 작업에서 더 비싸거나 `xhigh`가 항상 더 낫다고 결론 내리지 않습니다.

## 미해결 항목

- 없음. 직접 API 실행을 하지 않았으므로 한국어 품질, 실제 지연시간, 장시간 Claude Code 완주율은 본문 주장 범위에서 제외합니다.

## 출처 메모

- Anthropic 표는 생산 안전장치를 켠 실제 제품 구성을 평가했습니다. 일부 거부·폴백은 순수 모델 능력 비교에는 잡음이지만 실제 제품 완주율에는 포함되는 조건입니다.
- Artificial Analysis는 외부 평가 기관이지만 Anthropic의 출시 전 평가를 지원했습니다. `독립 블라인드 평가`라고 부르지 않고 `외부 평가`로 표시합니다.
- 공식 가격 인하는 캐시 읽기에만 적용됩니다. `Fable 5.1은 75% 저렴하다`처럼 전체 비용으로 넓혀 쓰지 않습니다.
