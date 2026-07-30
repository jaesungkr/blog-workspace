# 근거 지도: Kimi K3란? 중국 AI 모델의 특징·성능과 현실적인 사용법

## 조사 기준

- 조사일: 2026-07-30
- 조사·재계산 주체: Codex
- 공식 자료: Moonshot AI 기술 블로그, GitHub README·라이선스, Hugging Face
  모델 메타데이터, Kimi API 문서
- 직접 실행하지 않은 범위: Kimi K3 웹·API 추론, Kimi Code 세션, 자체
  가중치 다운로드와 추론

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C00 | Kimi K3는 중국 베이징의 Moonshot AI가 만든 AI 모델임 | 공식 | 확인 | Moonshot AI About, Kimi K3 공식 발표 | 회사 소재지와 모델 개발 주체 확인 |
| C01 | Kimi K3는 2.8조 전체·1,040억 활성 파라미터의 MoE 모델임 | 공식 | 확인 | 공식 GitHub README Model Summary | 벤더 공개 사양 |
| C02 | 토큰마다 896개 전문가 중 16개와 공유 전문가 2개를 사용함 | 공식 | 확인 | 공식 GitHub README | 구현을 독립 검사하지 않음 |
| C03 | 문맥 길이는 1,048,576토큰이고 텍스트·이미지를 입력으로 받음 | 공식 | 확인 | 공식 GitHub README | 실제 유효 문맥 성능 미측정 |
| C04 | KDA·AttnRes·Stable LatentMoE를 사용함 | 공식 | 확인 | 공식 기술 블로그와 README | 효율 개선을 독립 재현하지 않음 |
| C05 | 공식 코딩표 9개에서 K3는 1위 2개·2위 6개·3위 1개임 | Codex 실행 | 확인 | `artifacts/run/audit-report.md` | 벤더 표 재계산, 하네스 차이 존재 |
| C06 | K3는 공식 표의 코딩 9개 항목에서 모두 3위 안에 있음 | Codex 실행 | 확인 | 같은 결과 파일 | 전체 코딩 능력으로 일반화 금지 |
| C07 | 공개 모델 샤드 96개의 합은 1,560,936,091,448바이트임 | Codex 실행 | 확인 | Hugging Face API 메타데이터 합산 | 저장 용량이며 추론 메모리가 아님 |
| C08 | 공식 발표는 64개 이상 가속기의 supernode 배포를 권장함 | 공식 | 확인 | Kimi K3 기술 블로그 Architecture and Infrastructure | 구체 하드웨어별 요구량 없음 |
| C09 | K3는 항상 추론하며 low·high·max effort를 지원함 | 공식 | 확인 | 공식 README Model Usage, API 문서 | API 동작을 직접 호출하지 않음 |
| C10 | 다중 턴·도구 호출에서 reasoning_content와 tool_calls를 포함한 assistant 메시지를 그대로 되돌려야 함 | 공식 | 확인 | 공식 README Model Usage | 비호환 하네스 실패를 직접 재현하지 않음 |
| C11 | 진행 중 세션 모델 전환과 누락된 추론 기록은 품질을 불안정하게 할 수 있음 | 공식 한계 | 확인 | 공식 기술 블로그 Limitations | 벤더 자가 보고 |
| C12 | 모호한 상황에서 예상 밖의 선제 결정을 할 수 있음 | 공식 한계 | 확인 | 공식 기술 블로그 Limitations | 빈도와 심각도 미측정 |
| C13 | 공식 보고서는 Claude Fable 5·GPT-5.6 Sol 대비 UX 격차를 인정함 | 공식 한계 | 확인 | 공식 기술 블로그 Limitations | 독립 사용자 연구 아님 |
| C14 | Kimi K3 License는 사용·복제·수정·배포를 허용하되 대형 MaaS·상용 서비스 조건을 둠 | 공식 | 확인 | 공식 GitHub LICENSE | 법률 자문이 아닌 문서 요약 |
| C15 | Kimi 웹은 입력창 위 모델 선택 버튼에서 K3를 고르며 Low·High·Max를 지원하고 크레딧을 사용함 | 공식 | 확인 | Kimi Help Center Getting started with Kimi | 계정·멤버십에 따라 이용 가능 범위가 달라질 수 있음 |
| C16 | Kimi Code CLI는 활성 멤버십 또는 호출 가능한 API Key가 필요하고, Kimi 계정의 `k3`는 Moderato 이상에서 `/model`로 선택하며 모델 전환 때 새 세션을 권장함 | 공식 | 확인 | Kimi Code CLI Getting started, Model Configuration | CLI를 직접 설치·실행하지 않음. 100만 토큰 문맥은 Allegretto 이상 |
| C17 | Kimi K3 API는 최소 1달러 충전 뒤 API Key를 만들고 모델 ID `kimi-k3`로 호출함 | 공식 | 확인 | Kimi K3 API Quickstart | API 호출·결제는 직접 수행하지 않음 |

## 직접 검증 설계

- 질문:
  1. 공식 코딩 벤치마크 9개에서 Kimi K3의 행별 위치는 어떻게 분포하나요?
  2. 공개 가중치 safetensors 샤드의 저장 용량 합계는 얼마인가요?
- 실행 주체: Codex
- 환경과 확인 시점:
  - 2026-07-30
  - macOS 26.5.2 arm64
  - Python 3 표준 라이브러리
  - Hugging Face 모델 revision `9f62e4e9fffbd0a83ddd60e1c209d828994b3569`
- 입력:
  - `artifacts/sources/kimi-k3-readme.md`
  - `artifacts/sources/huggingface-model-blobs.json`
- 전처리 또는 표현:
  - HTML table의 `Coding` 구간에서 7열 행을 추출
  - 각 행의 6개 모델 점수를 내림차순 정렬
  - `model-?????-of-??????.safetensors` 패턴의 파일 96개 크기 합산
- 비교·판정 규칙:
  - 벤치마크 순위는 같은 공식 표의 한 행 안에서 높은 점수 순
  - 동률은 원문 열 순서를 유지하며 이번 9개 코딩 행에는 K3 동률이 없음
  - 저장 용량은 Hugging Face API의 `size` 정수 합계
- 성공 기준:
  - 코딩 행이 정확히 9개이고 모델 샤드가 정확히 96개일 때만 통과
  - CSV·JSON·Markdown 결과가 같은 2·6·1 분포와 바이트 합계를 기록
- 반복 횟수와 표본 크기:
  - 공식 README 스냅샷 1개, 코딩 행 9개
  - Hugging Face revision 1개, 모델 샤드 96개
- 보존한 원자료:
  - `artifacts/run/audit_kimi_k3.py`
  - `artifacts/run/coding-benchmark-ranks.csv`
  - `artifacts/run/audit-summary.json`
  - `artifacts/run/audit-report.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 공식 코딩표 9행 | 1위 2개·2위 6개·3위 1개 | `artifacts/run/audit-report.md` | 벤더 표 내부의 위치 |
| E02 | K3의 모든 코딩 행 | 9개 모두 3위 안 | `artifacts/run/coding-benchmark-ranks.csv` | 독립 성능 검증 아님 |
| E03 | safetensors 96개 | 1,560,936,091,448바이트 | `artifacts/run/audit-summary.json` | 저장·전송 규모 |
| E04 | 단위 환산 | 1.561TB·1.420TiB | 같은 파일 | 추론 메모리 아님 |

## 실패와 반례

- 실패한 입력: 공식 코딩표에서 K3가 모든 항목 1위일 것이라는 단순 예상
- 예상과 달랐던 결과: 1위는 2개였고 나머지는 2위 6개·3위 1개였습니다.
- 반례의 의미: 출시 그래프의 강조색만으로 일관된 1위라고 읽으면 안 되며,
  여러 과제에서 상위권을 유지한다는 해석이 더 정확합니다.
- 일반화하면 안 되는 범위:
  - 벤더가 고른 벤치마크를 전체 코딩 품질 순위로 바꾸지 않음
  - 서로 다른 하네스·fallback·cyberguard 조건을 같은 통제 실험으로 보지 않음
  - 저장 파일 합계를 실제 GPU 메모리나 운영 비용으로 바꾸지 않음
  - API와 Kimi Code를 직접 실행한 사용 경험으로 서술하지 않음

## 미해결 항목

본문에 넣어야 할 미확인 주장은 없습니다. 다음 항목은 의도적으로 주장하지
않습니다.

- 한국어 응답 품질과 사실 정확도가 다른 최상위 모델보다 높다는 주장
- Kimi K3의 실제 API 지연·처리량·비용 우위
- 개인 GPU 구성에서의 실행 가능성과 성능
- 100만 토큰 전체 구간에서의 일관된 검색·추론 품질

## 출처 메모

- `artifacts/source-snapshot.md`에 URL, 확인일, 로컬 스냅샷과 SHA-256을
  기록합니다.
- 모델 카드의 벤치마크는 inline 출처와 `참고 자료` 양쪽에 연결합니다.
- 공식 발표의 성능 주장과 공식 한계를 같은 비중으로 다룹니다.
