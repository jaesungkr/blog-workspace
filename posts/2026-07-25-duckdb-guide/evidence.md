# 근거 지도: DuckDB 사용법 총정리 - 설치부터 CSV·Parquet·Pandas 분석까지

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 `공식`, `독립 검증`, `벤더 주장`, `사용자 제공`, `Codex 실행`,
`추정`, `구조 예시`처럼 실제 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | DuckDB는 별도 서버 없이 호스트 프로세스 안에서 작동하는 분석용 관계형 DB입니다. | 공식 | 확인 | DuckDB `Why DuckDB` | 프로젝트 공식 설명이며 제품 간 독립 벤치마크는 아님 |
| C02 | 열 지향 벡터화 실행 엔진은 큰 범위를 집계하는 OLAP 작업을 목표로 합니다. | 공식 | 확인 | DuckDB `Why DuckDB` | 모든 쿼리에서 다른 DB보다 빠르다는 뜻은 아님 |
| C03 | Python에서 CSV·Parquet·JSON 파일과 Pandas·Polars·Arrow 객체를 직접 조회할 수 있습니다. | 공식 | 확인 | DuckDB Python API | 지원 세부 사항은 버전에 따라 바뀔 수 있음 |
| C04 | Parquet 조회는 필요한 열만 읽는 projection pushdown과 조건을 파일 스캔으로 내리는 filter pushdown을 지원합니다. | 공식 | 확인 | DuckDB Parquet overview | 효과는 정렬, row group, 통계, 쿼리 형태에 좌우됨 |
| C05 | CSV는 방언·헤더·타입을 표본으로 자동 감지하며 필요하면 옵션으로 고정해야 합니다. | 공식 | 확인 | DuckDB CSV auto detection | 기본 표본과 옵션은 버전별 확인 필요 |
| C06 | 메모리보다 큰 작업은 임시 디스크로 spill할 수 있습니다. | 공식 | 확인 | DuckDB tuning workloads | 모든 작업이 메모리 부족 없이 끝난다는 보장은 아님 |
| C07 | 여러 프로세스가 같은 DuckDB 파일에 자동으로 동시 쓰는 방식은 지원하지 않으며, 많은 작은 트랜잭션은 핵심 목표가 아닙니다. | 공식 | 확인 | DuckDB concurrency | 한 프로세스 안의 다중 스레드 규칙과 구분해야 함 |
| C08 | 500만 행 로컬 테스트에서 Parquet은 CSV보다 약 11.48배 작았고, 지정 쿼리 중앙값은 약 59.38배 빨랐습니다. | Codex 실행 | 확인 | `benchmark-results.json`, 포맷별 1회 워밍업 후 7회 교차 실행 | 날짜순 합성 데이터·웜 캐시·한 Mac·한 쿼리의 시나리오 결과 |
| C09 | CSV와 Parquet은 같은 원본이어도 자동 추론 타입이 달라질 수 있습니다. | Codex 실행 | 확인 | `benchmark-failure.md`: CSV `DOUBLE`, Parquet `DECIMAL(38,2)` | DuckDB 1.4.5와 해당 데이터에 한정 |
| C10 | Python 패키지는 `pip install duckdb`, CLI는 공식 설치 페이지에서 설치할 수 있습니다. | 공식 | 확인 | DuckDB installation, Python API | 최신 버전 번호를 본문에 고정하지 않음 |

## 직접 검증 설계

- 질문: 같은 500만 행 데이터를 DuckDB가 직접 내보낸 CSV와 Parquet으로
  읽을 때, 선택한 날짜 범위 집계의 결과 일치 여부·파일 크기·실행 시간은
  어떻게 다른가요?
- 실행 주체: Codex
- 환경과 확인 시점: 2026-07-25 19:05 KST, macOS 26.5.2 arm64,
  Apple Silicon 10 logical CPUs, Python 3.9.6, DuckDB 1.4.5, DuckDB threads 4
- 입력: `range(5_000_000)`으로 만든 6열 합성 이벤트 데이터. 날짜,
  지역 10개, 카테고리 100개, 수량, DECIMAL 금액을 포함하고 날짜·ID
  순서로 정렬했습니다.
- 전처리 또는 표현: 같은 DuckDB 테이블을 header 포함 CSV와
  `ZSTD`, `ROW_GROUP_SIZE 100000` Parquet으로 각각 출력했습니다.
- 비교·판정 규칙: 2025년 7월 범위를 거른 뒤 지역별 정확한 금액 합계와
  행 수를 구했습니다. 양쪽 결과가 완전히 같은지 먼저 확인하고, 포맷별
  1회 워밍업 뒤 실행 순서를 번갈아 7회 측정해 중앙값을 비교했습니다.
- 성공 기준: 결과 행이 일치하고, 각 포맷에서 7개 시간 표본과 파일
  크기를 기록합니다.
- 반복 횟수와 표본 크기: 500만 행, 포맷별 워밍업 1회, 측정 7회
- 보존할 원자료: 재현 스크립트, 전체 JSON 결과, 첫 실패 기록. 생성된
  253MB CSV와 22MB Parquet은 스크립트로 재생성 가능해 커밋하지 않았습니다.

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | CSV, 날짜 필터·지역 집계 | 241.61 MiB, 중앙값 0.1830초 | `artifacts/benchmark-results.json` | 로컬 웜 캐시 7회 |
| E02 | ZSTD Parquet, 같은 쿼리 | 21.05 MiB, 중앙값 0.003082초 | `artifacts/benchmark-results.json` | 날짜순·row group 10만의 이점 포함 |
| E03 | 첫 쿼리에서 `SUM(amount)` 직접 비교 | CSV는 `DOUBLE`, Parquet은 `DECIMAL(38,2)`여서 결과 일치 검사가 실패 | `artifacts/benchmark-failure.md` | CSV 자동 추론 실패 사례 |
| E04 | `amount`를 `DECIMAL(12,2)`로 고정해 재실행 | 10개 지역의 합계와 행 수가 모두 일치 | `artifacts/benchmark-results.json` | 타입 고정 뒤의 논리 결과 |

## 실패와 반례

- 실패한 입력: `SUM(amount)`에서 CSV 자동 감지 타입을 그대로 사용한 첫
  벤치마크
- 예상과 달랐던 결과: `region_00` 합계가 CSV에서는
  `20476966.870000023`(`DOUBLE`), Parquet에서는
  `20476966.87`(`DECIMAL`)로 반환되어 동등성 검사가 실패했습니다.
- 교정: 집계 전 `amount`를 `DECIMAL(12,2)`로 명시했습니다. 실무에서는
  `read_csv(..., types = {'amount': 'DECIMAL(12,2)'})`처럼 입력 단계에서
  고정하는 편이 더 명확합니다.
- 일반화하면 안 되는 범위: 59.38배라는 수치는 DuckDB 전체 성능 순위도,
  모든 CSV와 Parquet의 보편적 차이도 아닙니다. 날짜순 정렬, Parquet
  row group 통계, 높은 선택도의 날짜 조건, 웜 캐시가 반영된 한
  시나리오입니다.

## 미해결 항목

- 없음. 출시 버전처럼 바뀌는 값은 특정 최신 번호 대신 공식 설치 페이지
  확인 경로를 안내합니다.

## 출처 메모

- Why DuckDB: <https://duckdb.org/why_duckdb>
- Installation: <https://duckdb.org/install/>
- Python API: <https://duckdb.org/docs/stable/clients/python/overview>
- CSV overview: <https://duckdb.org/docs/stable/data/csv/overview>
- CSV auto detection: <https://duckdb.org/docs/stable/data/csv/auto_detection>
- Parquet overview: <https://duckdb.org/docs/stable/data/parquet/overview>
- Tuning workloads: <https://duckdb.org/docs/stable/guides/performance/how_to_tune_workloads>
- Concurrency: <https://duckdb.org/docs/stable/connect/concurrency>
- SQL on Pandas: <https://duckdb.org/docs/stable/guides/python/sql_on_pandas>

공식 문서는 기능과 설계 의도를 확인하는 1차 자료입니다. 성능 수치는 공식
홍보 문구가 아니라 위의 Codex 실행 결과만 사용하고 시나리오 한계를 함께
밝힙니다.
