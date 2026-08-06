# 근거 지도: Qwen3.8-Max 성능 비교, 중국 AI의 추격은 어디까지 왔나

## 조사 기준

- 조사일: 2026-08-06
- 조사·재계산 주체: Codex
- 공식 자료: Qwen3.8-Max 출시 글과 API 사용 예시, Alibaba Cloud 가격 문서,
  QwenCloud 모델 문서, Moonshot AI Kimi K3 모델 카드
- 독립 자료: Arena 공개 리더보드의 동일 세션 관찰값
- 직접 실행하지 않은 범위: Qwen3.8-Max·Qwen3.7-Max·Kimi K3 추론,
  API 결제·지연 측정, 공개 전 Qwen3.8 가중치 다운로드

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C00 | Qwen3.8-Max는 Alibaba Qwen의 최상위 모델로 2026-08-03 공식 출시됨 | 공식 | 확인 | Qwen 공식 출시 글·공식 X 발표 | 벤더가 정한 제품 계층 |
| C01 | 전체 2.4조·활성 950억 파라미터이며 Qwen3.5 계열 구조를 바탕으로 함 | 공식 | 확인 | Qwen 공식 출시 글 | 상세 구조·활성화 방식은 독립 검사하지 않음 |
| C02 | 100만 토큰 문맥, 최대 64K 출력, 텍스트·이미지 입력, 도구 호출을 지원함 | 공식 | 확인 | Qwen 공식 출시 글의 Codex·OpenClaw 설정, QwenCloud 모델 표 | 100만 토큰 유효 성능 미측정 |
| C03 | 공식 API 가격은 입력 $2·출력 $6·암시적 캐시 $0.25/100만 토큰임 | 공식 | 확인 | Qwen 공식 X 발표와 출시 글 | 지역·프로모션·제공 방식에 따라 달라질 수 있음 |
| C04 | Qwen3.7-Max는 100만 문맥·64K 출력이며 싱가포르 공식 가격표는 입력 $2.5·출력 $7.5임 | 공식 | 확인 | Alibaba Cloud Model Studio 가격·모델 문서 | 기간 한정 할인과 캐시는 별도 |
| C05 | Kimi K3는 2.8조 전체·1,040억 활성·1,048,576 문맥의 오픈웨이트 모델임 | 공식 | 확인 | MoonshotAI/Kimi-K3 공식 README | 서로 다른 학습·하네스의 크기만으로 품질 비교 금지 |
| C06 | Qwen 벤치마크 표는 Opus4.8·Fable5·GPT5.6 Sol·Qwen3.7-Max·Qwen3.8-Max 5개를 비교함 | 공식 | 확인 | Qwen 공식 출시 HTML의 첫 성능표 | 일부 행은 모델 결과가 없어 비교 수가 3~5개 |
| C07 | 단일 점수 30행에서 Qwen3.8-Max는 1위 7·2위 11·3위 7·4위 5개임 | Codex 실행 | 확인 | `artifacts/run/qwen38-audit-summary.json` | Qwen 벤더 표 재계산, 독립 재실행 아님 |
| C08 | 같은 30행에서 Qwen3.8-Max 값이 Qwen3.7-Max보다 모두 높음 | Codex 실행 | 확인 | 재계산 CSV | 벤더가 고른 시험과 설정 범위에서만 성립 |
| C09 | Qwen3.8-Max의 1위 행은 PaperBench·WideSearch·IFBench·HealthBench·PLawBench·PRBench-Legal 공동·PRBench-Finance임 | Codex 실행 | 확인 | 재계산 CSV | 서로 단위가 달라 합산·평균 금지 |
| C10 | 이중 점수인 Agents' Last Exam 한 행은 사후 기준 선택을 피하려고 재계산에서 제외함 | Codex 실행 | 확인 | 재계산 스크립트와 보고서 | 공식 표 자체의 점수는 삭제하지 않음 |
| C11 | 2026-08-06 Arena 677개 모델 표에서 Qwen3.8-Max 종합 5위, Kimi K3 Max 13위, Qwen3.7-Max Preview 21위임 | 독립 관찰 | 확인 | `artifacts/run/arena-text-observation.json` | 공개 선호도 순위로 표·투표 누적에 따라 변함 |
| C12 | 같은 Arena 표에서 Qwen3.8-Max는 코딩 9위, 창작 3위, 긴 질문 5위이며 Qwen3.7-Max Preview는 16·33·11위임 | 독립 관찰 | 확인 | 같은 브라우저 세션의 열·행 값 | 고정 정답형 벤치마크와 성격이 다름 |
| C13 | Qwen은 8월 3일 `다음 주` 공개 가중치를 예고했지만 8월 6일 Qwen 공식 Hugging Face 조직 검색 결과는 0개임 | 공식 예고 + Codex 확인 | 확인 | 공식 출시 글, `huggingface-qwen38-search.json` | 이후 공개되면 즉시 낡는 시점 정보 |
| C14 | Qwen Studio 공식 링크는 비로그인 첫 화면에서 Qwen3.8-Max가 선택된 상태를 보여 줌 | Codex 브라우저 관찰 | 확인 | `https://chat.qwen.ai/?models=qwen3.8-max`의 모델 선택 표시 | 실제 프롬프트 전송·로그인 조건은 시험하지 않음 |
| C15 | API의 정확한 모델 ID는 `qwen3.8-max`이며 OpenAI·Anthropic 호환 경로를 제공함 | 공식 | 확인 | Qwen 공식 출시 글의 API·Claude Code·Codex 예시 | 계정·리전별 Base URL과 키가 필요함 |
| C16 | Qwen 공식 성능 이미지는 16개 선별 지표를 시각화하며 Gemini·Qwen3.7 Plus와 멀티모달 지표 등 30행 재계산표와 다른 비교 대상·지표를 포함함 | 공식 | 확인 | Qwen 공식 출시 글의 Performance 이미지 | 공식 발표의 고수준 개요이며, 뒤의 HTML은 별도 단일 점수 30행 재계산이므로 서로 합치지 않음 |

## 직접 검증 설계

- 질문:
  1. Qwen 공식 비교표의 단일 점수 행에서 Qwen3.8-Max는 몇 위인가요?
  2. 같은 행에서 Qwen3.7-Max를 실제로 몇 번 앞서나요?
  3. 독립 공개 선호도 표와 공개 가중치 현황은 공식 주장과 어떤 차이가 있나요?
- 실행 주체: Codex
- 환경과 확인 시점:
  - 2026-08-06, Asia/Seoul
  - macOS 26.5 계열, Python 3.9.6 표준 라이브러리
  - Codex 인앱 브라우저, Arena 표시 모델 677개
- 입력:
  - `artifacts/sources/qwen38-article.json`
  - Arena text leaderboard DOM과 동일 페이지 내장 현재 데이터
  - Hugging Face API `author=Qwen&search=Qwen3.8`
- 전처리 또는 표현:
  - 공식 HTML의 첫 성능표를 `html.parser`로 읽음
  - `/`가 들어간 이중 점수와 `--` 결측을 한 숫자로 임의 변환하지 않음
  - 각 행의 숫자만 높은 값 순으로 정렬하고 행별 비교 모델 수를 함께 보존
- 비교·판정 규칙:
  - 공식 표의 모든 단일 점수는 높을수록 좋다는 원문 기준 적용
  - 동점은 모두 같은 1위로 표시
  - 행마다 단위가 다르므로 점수를 합산·평균하지 않음
  - Arena는 별도 표로만 제시하고 공식 벤치마크와 합치지 않음
- 성공 기준:
  - 대상 표 모델 5개와 단일 점수 행 30개를 정확히 찾음
  - CSV·JSON·Markdown이 같은 7·11·7·5 순위 분포를 기록함
  - Qwen3.7-Max와 비교 가능한 30행을 모두 판정함
- 반복 횟수와 표본 크기:
  - 공식 출시 HTML 스냅샷 1개, 단일 점수 30행
  - Arena 공개 표 1회 관찰, Qwen Hugging Face 조직 검색 1회
- 보존한 원자료:
  - `artifacts/run/audit_qwen38.py`
  - `artifacts/run/qwen38-single-score-ranks.csv`
  - `artifacts/run/qwen38-audit-summary.json`
  - `artifacts/run/qwen38-audit-report.md`
  - `artifacts/run/arena-text-observation.json`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 공식 단일 점수 30행 | 1위 7·2위 11·3위 7·4위 5 | `artifacts/run/qwen38-audit-summary.json` | 벤더 표 내부 위치 |
| E02 | Qwen3.7-Max와 공통 30행 | Qwen3.8-Max가 30행 모두 높은 값 | `artifacts/run/qwen38-single-score-ranks.csv` | 선택된 공식 시험·설정 |
| E03 | Arena 677개 모델 표 | Qwen3.8 5위·Kimi K3 13위·Qwen3.7 Preview 21위 | `artifacts/run/arena-text-observation.json` | 2026-08-06 선호도 순위 |
| E04 | Qwen 공식 Hugging Face 조직 검색 | `Qwen3.8` 결과 0개 | `artifacts/sources/huggingface-qwen38-search.json` | 확인 시점 공개 상태 |

## 실패와 반례

- 실패한 예상: Qwen3.8-Max가 벤더 표 30개에서 대부분 1위일 것이라는 출시 문구 기반 예상
- 예상과 달랐던 결과: 1위는 7개였고 2위 11개·3위 7개·4위 5개였습니다.
- 반례의 의미: 이전 Qwen보다 전반적으로 개선됐다는 해석과, 비교한 최상위 모델을
  대부분 이겼다는 해석은 같은 말이 아닙니다.
- 제외한 입력: `Agents' Last Exam (Pass / Score)`는 한 셀에 지표 두 개가 있어
  어느 값을 대표로 고를지 원문 규칙을 추가하지 않고 제외했습니다.
- 일반화하면 안 되는 범위:
  - 벤더가 고른 30행을 모든 실제 업무의 종합 순위로 바꾸지 않음
  - 서로 다른 하네스·도구·추론 수준을 완전히 통제된 실험으로 보지 않음
  - Arena 선호도 순위를 사실 정확도나 API 안정성 순위로 바꾸지 않음
  - 공개 예고를 실제 가중치·라이선스·로컬 실행 지원으로 바꾸지 않음

## 미해결 항목

본문에 넣어야 할 미확인 주장은 없습니다. 아래 항목은 의도적으로 주장하지 않습니다.

- 한국어 답변 품질이 Fable5·GPT5.6 Sol·Kimi K3보다 높다는 주장
- Qwen3.8-Max의 실제 API 지연·처리량·토큰 소비량
- 공개 가중치의 정확한 파일 크기·라이선스·필요 GPU 수
- 100만 토큰 전체 구간에서의 안정적 회수·추론 품질

## 출처 메모

- 공식 출시 원문 JSON SHA-256:
  `e49ec2e824d0e2b447080e767f50e86735d59d0344bccf46e770fb2b5da7867a`
- Qwen 공식 대표 이미지와 성능 이미지 원본을
  `artifacts/captures/official/`에 보존했습니다.
- Qwen 성능표의 벤더 성격과 Arena의 독립·가변 성격을 본문에서 함께 밝힙니다.
