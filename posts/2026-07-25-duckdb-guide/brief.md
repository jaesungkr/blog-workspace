# 기획: DuckDB 사용법 총정리 - 설치부터 CSV·Parquet·Pandas 분석까지

## 분류와 독자

- 상위 카테고리: `Log`
- 하위 카테고리: `개발 · 디지털`
- 한 명의 독자: Python·Pandas로 CSV를 분석하다 파일 크기와 메모리, 복잡한
  집계 때문에 DuckDB 도입을 검토하는 데이터 분석 입문자
- 검색 의도: DuckDB를 왜 쓰는지 이해하고, 설치부터 CSV·Parquet·Pandas
  조회와 파일 DB 저장까지 바로 재현하기
- 독자가 이미 아는 것: CSV, Python 패키지 설치, 표의 행과 열, 기초 SQL
  `SELECT`·`WHERE`·`GROUP BY`

## 글의 중심

- 독자가 기억할 한 문장: 서버를 운영하지 않고 로컬 파일과 DataFrame에
  분석용 SQL을 쓰고 싶다면 DuckDB부터 시작하되, 반복 조회 데이터는
  Parquet으로 바꾸고 CSV의 자동 타입 추론은 검증해야 합니다.
- 낯선 주제를 붙잡아 줄 익숙한 장면: Pandas로 큰 CSV 전체를 읽은 뒤
  필요한 열과 행만 거르느라 기다리는 노트북
- 이 글이 답하지 않는 범위: DuckDB의 모든 SQL 문법, 클라우드 데이터
  레이크 운영, 분산 처리 시스템의 벤치마크, 운영 DB 마이그레이션
- 가장 정직한 한계 또는 반론: DuckDB는 분석형 일괄 처리에 맞으며 여러
  프로세스가 같은 DB 파일에 자주 쓰는 서비스나 짧은 트랜잭션 중심
  애플리케이션의 기본 운영 DB는 아닙니다.

## dev.log만의 근거

- first-party contribution: DuckDB 1.4.5에서 500만 행 합성 데이터를 같은
  CSV와 Zstandard Parquet으로 내보내고, 날짜 필터·지역별 합계를 각각
  7회 교차 실행해 크기와 중앙값을 측정했습니다. 첫 비교에서 CSV
  `DOUBLE`과 Parquet `DECIMAL`의 결과 타입 차이로 검증이 실패한 기록도
  보존했습니다.
- 실제 실행 주체: `Codex`
- 보존할 원자료: `artifacts/benchmark_duckdb.py`,
  `artifacts/benchmark-results.json`, `artifacts/benchmark-failure.md`
- 기존 글 또는 시리즈 연결: 현재 저장소에 직접 연결할 데이터 도구 글이
  없어 `Log > 개발 · 디지털`의 재현 가능한 로컬 데이터 분석 클러스터를
  시작하는 글로 사용합니다.
- 다른 블로그 이름으로 바꿔도 성립하는 부분: 공식 문서 기반 설치와 API
  설명. dev.log의 직접 측정값, 실패 원인과 판정 기준이 대체 불가능한
  부분입니다.

## 설명 순서

| 순서 | 독자가 먼저 알아야 할 것 | 다음 내용과의 연결 |
|---|---|---|
| 1 | DuckDB는 서버가 아닌 프로세스 안의 분석용 SQL 엔진 | 설치와 첫 쿼리가 가벼운 이유 |
| 2 | CSV는 텍스트, Parquet은 타입·열 단위 구조를 가진 파일 | 직접 조회와 성능 차이의 원리 |
| 3 | 입력을 SQL로 필터·집계한 뒤 필요한 결과만 반환 | Python·Pandas·파일 DB 사용법 |
| 4 | 한 로컬 시나리오의 측정 조건과 타입 실패 | 실무 기본값과 한계를 구분 |

## 중앙 방법의 계산 또는 판단 사슬

`CSV·Parquet·Pandas 입력 -> DuckDB가 스키마 확인 및 필요한 열·행 스캔 -> SQL 필터·그룹·집계 -> 작은 결과표 또는 Parquet·DataFrame 출력`

## 독자가 이어서 물을 질문

- SQLite·Pandas·PostgreSQL과 어떤 상황에서 나눠 써야 하나요?
- CSV를 매번 읽는 것과 Parquet으로 변환하는 기준은 무엇인가요?
- 인메모리 연결과 `.duckdb` 파일 연결은 무엇이 다른가요?
- Pandas DataFrame을 복사하지 않고 바로 SQL로 조회할 수 있나요?
- 메모리보다 큰 데이터도 처리할 수 있나요?
- 여러 Python 프로세스가 같은 파일에 동시에 써도 되나요?

## 제목 후보

1. DuckDB 사용법 총정리 - 설치부터 CSV·Parquet·Pandas 분석까지
2. DuckDB 사용법 - 큰 CSV를 SQL로 바로 분석하는 가장 짧은 경로
3. DuckDB 사용법과 선택 기준 - Pandas·SQLite와 다른 분석용 DB
