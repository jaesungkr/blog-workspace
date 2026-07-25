# 근거 지도: Opus 5 vs Fable 5 - 클로드 모델 비교

## 조사 기준

- 조사일: 2026-07-25
- 공식 자료: Anthropic 출시 글, 모델 비교표, 시스템 카드, 프롬프팅 가이드,
  데이터 보존 및 거부 처리 문서
- 독립 평가: Artificial Analysis
- 공개 실사용 테스트: Nate Herk, Duncan Rogoff, Alex Finn의 출시 당일 영상
- 직접 계산 주체: Codex
- 핵심 구분: 벤더 자체 보고, 독립 평가, 제작자 주관 평가, Codex 재계산

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Opus 5는 2026-07-24 출시됐고 API 단가는 입력 $5, 출력 $25임 | 공식 | 확인 | Anthropic Opus 5 출시 글·모델 비교표 | 출시 시점의 표준 API 가격 |
| C02 | Fable 5의 API 단가는 $10/$50이며 두 모델 모두 1M 컨텍스트와 128K 최대 출력을 제공함 | 공식 | 확인 | Claude 모델 비교표 | 플랜별 사용량 제한은 별도 |
| C03 | Fable 5는 30일 데이터 보존 대상이며 Opus 5는 ZDR 적용이 가능함 | 공식 | 확인 | Claude API 데이터 보존 문서 | 고객 계약과 제공 경로별 확인 필요 |
| C04 | 공식 벤치마크에서 Opus는 Frontier-Bench·OSWorld·GDPval-AA·AutomationBench, Fable은 SWE-bench Pro·DeepSWE에서 앞섬 | 벤더 자체 보고 | 확인 | Claude Opus 5 시스템 카드의 대표 표 | 설정·하네스·샘플링에 종속 |
| C05 | Artificial Analysis 지수는 Opus max 61, Fable max 60이며 평균 작업비는 $2.03 대 $2.75임 | 독립 평가 | 확인 | Artificial Analysis Opus 5 평가 | Anthropic의 출시 전 평가 지원, 안전 거부에 Opus 4.8 폴백 |
| C06 | Nate 영상의 전체 출력 토큰은 Opus 약 200만/10회, Fable 약 83.2만/8회임 | 공개 실사용 테스트 | 확인 | 영상에 공개된 집계 수치 | 실행 수와 과제가 완전히 같지 않음 |
| C07 | C06을 실행당으로 정규화하면 약 20만 대 10.4만 토큰이며 출력 비용은 $5.00 대 $5.20임 | Codex 실행 | 확인 | 공식 출력 단가를 공개 토큰에 적용 | 입력·캐시·도구 비용 제외 |
| C08 | Duncan 테스트는 Opus $5.16·7분43초, Fable $5.93·6분20초였고 결과별 선호가 갈림 | 공개 실사용 테스트 | 확인 | Duncan Rogoff 영상 | 단 1회, 제작자의 주관 평가 |
| C09 | Alex의 5개 자체 과제에서는 대부분 Opus가 우세했지만 구조물 과제는 Fable이 앞섬 | 공개 실사용 테스트 | 확인 | Alex Finn 영상 | 반복·블라인드 채점 없음 |
| C10 | Opus 5는 스스로 검증하고 위임하는 경향이 강해 기존의 중복 검증 지시를 줄이는 편이 좋음 | 공식 | 확인 | Opus 5 프롬프팅 가이드 | 워크로드별 효과는 직접 측정 필요 |
| C11 | Anthropic은 Opus 5 안전 분류기의 개입 빈도가 Fable 5보다 약 85% 낮을 것으로 예상함 | 벤더 주장 | 확인 | Opus 5 출시 글 | 예상치이며 업무 영역별 비율은 다름 |
| C12 | Fable 출시 당시 안전 분류기는 전체 세션의 5% 미만에서 작동한다고 발표됨 | 벤더 주장 | 확인 | Fable 5 출시 글 | 평균값이며 특정 영역에서 더 높을 수 있음 |

## 직접 검증 설계

- 질문: Nate Herk 영상의 전체 집계에서 실행 수 차이를 보정하면 Opus 5의
  절반 단가가 실행당 출력 비용에 얼마나 남는가?
- 실행 주체: Codex
- 환경과 확인 시점: 공개 영상 전사와 화면 수치, Anthropic 표준 API 가격,
  2026-07-25
- 입력:
  - Opus 5 출력 토큰 약 2,000,000개, 실행 10회
  - Fable 5 출력 토큰 약 832,000개, 실행 8회
  - 출력 단가 Opus $25/M, Fable $50/M
  - 평균 실행 시간 Opus 약 63분, Fable 약 25분
- 전처리 또는 표현: 전체 출력 토큰을 모델별 실행 횟수로 나눠 실행당 토큰으로
  정규화
- 비교·판정 규칙:
  1. 실행당 출력 토큰 = 전체 출력 토큰 / 실행 횟수
  2. 실행당 출력 비용 = 실행당 출력 토큰 / 1,000,000 × 공식 출력 단가
  3. 비용 절감률 = 1 - Opus 실행당 비용 / Fable 실행당 비용
  4. 실행 시간 배수 = Opus 평균 시간 / Fable 평균 시간
- 성공 기준: 원시 합계의 실행 수 차이를 제거하고, 출력 비용에 한정된 비교라는
  범위를 본문에서 명확히 표시
- 반복 횟수와 표본 크기: 공개 집계 Opus 10회, Fable 8회
- 보존할 원자료:
  - `artifacts/nate-herk-normalized.csv`
  - `artifacts/recalculation-notes.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 실행당 출력 토큰 | Opus 200,000, Fable 104,000 | `artifacts/nate-herk-normalized.csv` | 공개 집계의 단순 평균 |
| E02 | 표준 출력 단가 적용 | Opus $5.00, Fable $5.20 | `artifacts/nate-herk-normalized.csv` | 입력·캐시·도구 비용 제외 |
| E03 | 실행당 출력 비용 차이 | Opus가 약 3.85% 낮음 | `artifacts/recalculation-notes.md` | 전체 청구액 절감률이 아님 |
| E04 | 평균 실행 시간 | Opus/Fable 약 2.52배 | `artifacts/recalculation-notes.md` | 과제 구성과 실행 수 불일치 |
| E05 | 단순 손익분기점 | Opus가 Fable의 2배 토큰을 쓰면 비용 동일 | `artifacts/recalculation-notes.md` | 입력·출력 비율과 부대비용 동일 가정 |

## 실패와 반례

- 실패한 비교 방식: Opus 10회와 Fable 8회의 전체 토큰 또는 전체 청구액을
  그대로 비교하면 실행 수 차이가 섞입니다.
- 예상과 달랐던 결과: Opus의 출력 단가는 절반이지만 실행당 출력 토큰이 약
  1.92배여서 출력 비용 절감 폭은 약 3.85%만 남았습니다.
- 반례: 공식 SWE-bench Pro와 DeepSWE에서는 Fable 5가 근소하게 앞섭니다.
- 일반화하면 안 되는 범위:
  - 공개 테스트 3건을 전체 워크로드의 보편 순위로 해석하지 않음
  - 제작자 선호를 객관적 품질 점수로 바꾸지 않음
  - 출력 토큰 비용을 전체 API 청구액으로 표현하지 않음
  - 출시 당일 관찰을 장기 운영 성능으로 확정하지 않음

## 미해결 항목

본문에 넣어야 할 미확인 사실은 없습니다. 다만 실제 조직별 비용과 성공률은 같은
과제를 반복해 별도로 측정해야 합니다.

## 출처 메모

- Anthropic Opus 5 출시:
  https://www.anthropic.com/news/claude-opus-5
- Claude 모델 비교표:
  https://platform.claude.com/docs/en/about-claude/models/overview
- Opus 5 시스템 카드:
  https://www.anthropic.com/claude-opus-5-system-card
- Opus 5 프롬프팅 가이드:
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Claude API 데이터 보존:
  https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
- 거부와 폴백:
  https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
- Anthropic Fable 5 출시:
  https://www.anthropic.com/news/claude-fable-5-mythos-5
- Artificial Analysis:
  https://artificialanalysis.ai/articles/opus-5
- Nate Herk:
  https://www.youtube.com/watch?v=2J3uX8iRNng
- Duncan Rogoff:
  https://www.youtube.com/watch?v=yKu03nBC9yY
- Alex Finn:
  https://www.youtube.com/watch?v=Vh1v2VSroes
