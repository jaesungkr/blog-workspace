---
title: "DuckDB 사용법 총정리 - 설치부터 CSV·Parquet·Pandas 분석까지"
slug: duckdb-guide
date: 2026-07-25
category: "Log"
subcategory: "개발 · 디지털"
status: ready
tags: [DuckDB, DuckDB 사용법, 데이터 분석, SQL, CSV, Parquet, Pandas, Python]
summary: "DuckDB를 사람들이 쓰는 이유부터 설치, CSV·Parquet 직접 조회, Pandas 연동, 파일 DB 저장, 성능 팁과 한계까지 500만 행 실험과 함께 정리합니다."
hero_image: assets/duckdb-local-analytics-hero-v2.png
published_url: ""
sources:
    - https://duckdb.org/why_duckdb
    - https://duckdb.org/install/
    - https://duckdb.org/docs/stable/clients/cli/overview
    - https://duckdb.org/docs/stable/clients/python/overview
    - https://duckdb.org/docs/stable/data/csv/overview
    - https://duckdb.org/docs/stable/data/csv/auto_detection
    - https://duckdb.org/docs/stable/data/parquet/overview
    - https://duckdb.org/docs/stable/guides/python/sql_on_pandas
    - https://duckdb.org/docs/stable/guides/performance/how_to_tune_workloads
    - https://duckdb.org/docs/stable/connect/concurrency
---

안녕하세요. dev.log입니다.

대규모 데이터를 자주 분석하는 개발자라면 DuckDB라는 이름이 이미 익숙하실 수 있습니다. 저도 주변에서 별도 서버 없이 파일을 바로 분석할 수 있어 편리하다는 이야기를 자주 들었고, 이번 기회에 그 장점과 한계를 함께 확인해 봤습니다.

Pandas로 큰 CSV를 열었는데 필요한 것은 지난달 매출 합계 몇 줄뿐인 경우가 있습니다. 파일 전체를 DataFrame에 올린 뒤 필터와 그룹 연산을 이어 붙이면 코드도 메모리도 금세 무거워집니다. **이럴 때 DuckDB는 별도 서버 없이 파일에 바로 SQL을 실행하고, 필요한 결과만 Python으로 가져오는 가장 간단한 출발점입니다.** 다만 여러 사용자가 동시에 주문을 쓰는 운영 DB를 대신하는 도구는 아닙니다.

이번 글에서는 DuckDB를 왜 쓰는지부터 설치, CSV·Parquet 조회, Pandas 연동, 파일 DB 저장과 성능 팁까지 한 흐름으로 정리합니다. 공식 문서만 옮기지 않고 500만 행 데이터를 직접 만들어 CSV와 Parquet의 크기·조회 시간을 비교했으며, 자동 타입 추론 때문에 첫 검증이 실패한 과정도 함께 남겼습니다.

### 1. DuckDB의 정체

DuckDB는 SQL로 표 형태 데이터를 다루는 관계형 데이터베이스입니다. PostgreSQL처럼 별도의 DB 서버를 먼저 띄우는 방식이 아니라 Python, R, Java 같은 프로그램의 **프로세스 안에 분석 엔진이 들어가는 내장형 데이터베이스**입니다. `pip install duckdb`만으로 노트북 안에서 바로 시작할 수 있는 이유입니다.

[DuckDB의 공식 설계 설명](https://duckdb.org/why_duckdb)에 따르면 목표 작업은 OLAP(Online Analytical Processing), 즉 많은 행을 읽어 집계·정렬·조인하는 분석입니다. 한 행씩 자주 추가하고 수정하는 주문 처리보다 “1년치 로그를 지역별로 묶어 합계를 구한다” 같은 질문에 맞습니다.

데이터가 엔진을 통과하는 경로는 다음과 같습니다.

> CSV·Parquet·DataFrame 입력 → 스키마와 필요한 열·행 확인 → SQL 필터·조인·집계 → 작은 결과표 또는 새 파일 출력

DuckDB는 열 단위 저장과 벡터화 실행을 사용합니다. 쉽게 말하면 한 행씩 같은 계산을 반복하기보다 필요한 열의 값 묶음을 한 번에 처리합니다. 그래서 전체 행의 일부 열을 훑는 합계와 그룹 집계에 잘 맞지만, 단일 행을 초당 수천 번 수정하는 서비스까지 자동으로 잘하는 것은 아닙니다.

### 2. 사람들이 쓰는 네 가지 이유

첫째, 서버 설치와 계정·포트 운영이 없습니다. 분석 스크립트와 같은 프로세스에서 실행되며, 메모리에서만 쓰거나 하나의 `.duckdb` 파일에 테이블을 저장할 수 있습니다. SQLite가 애플리케이션 안의 소형 저장소를 간단하게 만든 것처럼, DuckDB는 로컬 분석을 간단하게 만드는 쪽에 가깝습니다.

둘째, 파일을 적재하기 전에 바로 물어볼 수 있습니다. [Python API](https://duckdb.org/docs/stable/clients/python/overview)는 CSV·Parquet·JSON 경로를 테이블처럼 조회하고, Pandas·Polars·Arrow 객체도 직접 읽는 방식을 제공합니다. “DB에 넣고 나서 SQL”이 아니라 **파일 경로 자체에 SQL**을 쓸 수 있습니다.

셋째, Parquet과의 궁합이 좋습니다. Parquet은 열별 타입과 통계를 가진 압축 열 지향 파일입니다. [공식 Parquet 문서](https://duckdb.org/docs/stable/data/parquet/overview)에 따르면 DuckDB는 쿼리에 필요한 열만 읽는 projection pushdown과 조건에 맞지 않는 영역을 건너뛰는 filter pushdown을 지원합니다. `SELECT region, SUM(amount)`에 필요 없는 긴 설명 열을 읽지 않을 수 있다는 뜻입니다.

넷째, 분석 결과가 메모리보다 클 때 디스크를 임시 작업 공간으로 쓸 수 있습니다. [공식 성능 가이드](https://duckdb.org/docs/stable/guides/performance/how_to_tune_workloads)는 그룹화·조인·정렬 같은 작업이 메모리를 넘으면 임시 디렉터리에 spill하는 방식을 설명합니다. 메모리 제한이 사라지는 것은 아니지만, “파일보다 RAM이 작으니 시작도 못 한다”는 제약을 줄여 줍니다.

### 3. Pandas·SQLite·PostgreSQL과의 선택

도구를 기능 목록보다 작업 모양으로 고르면 판단이 쉬워집니다.

| 상황 | 먼저 고를 도구 | 이유 |
|---|---|---|
| 작은 표를 Python 문법으로 정리·시각화 | Pandas | 생태계와 행·열 변환 API가 편리함 |
| 로컬 CSV·Parquet의 큰 집계·조인 | DuckDB | 파일 직접 조회와 분석 SQL에 최적화 |
| 앱 내부의 잦은 단건 저장·조회 | SQLite | 단순한 내장형 트랜잭션 저장소에 적합 |
| 여러 서버·사용자가 동시에 읽고 쓰는 운영 DB | PostgreSQL·MySQL | 서버형 동시성·권한·운영 기능이 중심 |
| 단일 머신을 넘어선 분산 데이터 처리 | Spark 등 | 여러 노드에 작업을 분산 |

Pandas와 DuckDB는 경쟁 관계로만 볼 필요가 없습니다. DuckDB에서 큰 원본을 필터·집계한 뒤 작은 결과만 `.df()`로 넘겨 시각화하면 두 도구의 장점을 함께 쓸 수 있습니다. 반대로 수천 행짜리 표에서 단순 열 하나를 바꾸는 작업이라면 DuckDB를 추가해도 이점이 작습니다.

**기본 선택은 “로컬 파일에 복잡한 SQL 분석이 필요하면 DuckDB, 다중 사용자 운영 데이터는 서버형 DB”입니다.** 속도만 보고 기존 서비스 DB를 DuckDB 파일 하나로 바꾸면 동시 쓰기와 운영 요구에서 막힐 수 있습니다.

### 4. 설치와 첫 쿼리

Python에서 시작하는 방법이 가장 짧습니다. 새 가상환경을 만들고 패키지를 설치합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install duckdb
```

Windows PowerShell에서는 활성화 명령만 `.venv\Scripts\Activate.ps1`로 바꿉니다. 최신 버전과 운영체제별 CLI 설치 방법은 [공식 설치 페이지](https://duckdb.org/install/)에서 확인할 수 있습니다. 글의 실험은 재현성을 위해 DuckDB 1.4.5 LTS와 Python 3.9.6을 사용했습니다.

설치와 실제 버전을 바로 확인합니다.

```python
import duckdb

print(duckdb.__version__)
duckdb.sql("SELECT 42 AS answer").show()
```

`duckdb.sql()`은 기본 인메모리 연결을 사용합니다. 프로그램이 끝나면 만든 테이블도 사라지므로 탐색용 쿼리에 알맞습니다. 라이브러리나 장기 실행 프로그램에서는 공유되는 기본 연결보다 `duckdb.connect()`로 연결 객체를 명시하는 편이 안전합니다.

터미널에서 SQL만 빠르게 실행하려면 [DuckDB CLI](https://duckdb.org/docs/stable/clients/cli/overview)를 설치한 뒤 `-c` 옵션을 사용합니다. 첫 명령은 메모리에서 CSV를 조회하고, 두 번째 명령은 `analytics.duckdb` 파일을 열어 테이블 목록을 보여 줍니다.

```bash
duckdb -c "SELECT * FROM 'sales.csv' LIMIT 5;"
duckdb analytics.duckdb -c "SHOW TABLES;"
```

### 5. CSV를 테이블처럼 조회하는 방법

`sales.csv`에 `sold_at`, `region`, `amount` 열이 있다고 가정하겠습니다. 테이블을 만들지 않아도 경로를 `FROM`에 바로 넣을 수 있습니다.

```python
import duckdb

con = duckdb.connect()
result = con.sql("""
    SELECT
        region,
        SUM(amount) AS revenue
    FROM 'sales.csv'
    WHERE sold_at >= DATE '2026-07-01'
    GROUP BY region
    ORDER BY revenue DESC
""")

result.show()
```

CSV는 구분자와 헤더, 열 타입을 파일 안에 표준 스키마로 저장하지 않습니다. DuckDB는 [CSV sniffer](https://duckdb.org/docs/stable/data/csv/auto_detection)로 표본을 읽어 이를 추론하지만, 코드처럼 생긴 `00123`을 숫자로 판단하거나 날짜 형식이 모호할 수 있습니다. 중요한 열은 처음부터 타입을 지정합니다.

```sql
SELECT *
FROM read_csv(
    'sales.csv',
    header = true,
    types = {
        'sold_at': 'DATE',
        'region': 'VARCHAR',
        'amount': 'DECIMAL(12,2)'
    }
);
```

먼저 추론 결과를 보고 싶다면 `FROM sniff_csv('sales.csv');`를 실행합니다. 여러 CSV의 열 구성이 조금씩 다르다면 `union_by_name = true`도 쓸 수 있지만, 공식 문서가 안내하듯 추가 메모리가 필요합니다.

### 6. Parquet 조회와 변환

확정된 CSV를 반복해서 분석한다면 Parquet 변환을 고려할 만합니다. 아래 SQL은 CSV를 읽고 타입을 고정한 뒤 Zstandard 압축 Parquet으로 저장합니다.

```sql
COPY (
    SELECT *
    FROM read_csv(
        'sales.csv',
        header = true,
        types = {
            'sold_at': 'DATE',
            'region': 'VARCHAR',
            'amount': 'DECIMAL(12,2)'
        }
    )
)
TO 'sales.parquet'
(FORMAT PARQUET, COMPRESSION ZSTD);
```

조회 문법은 CSV와 같습니다.

```sql
SELECT region, SUM(amount) AS revenue
FROM 'sales.parquet'
WHERE sold_at >= DATE '2026-07-01'
GROUP BY region
ORDER BY revenue DESC;
```

폴더 안의 여러 파일도 하나의 표처럼 읽습니다.

```sql
SELECT
    filename,
    COUNT(*) AS rows
FROM read_parquet('data/2026-*/sales-*.parquet')
GROUP BY filename
ORDER BY filename;
```

원본 파일을 복사해 내부 테이블로 넣을 필요가 없다면 view를 만들 수 있습니다.

```sql
CREATE VIEW sales AS
SELECT * FROM read_parquet('data/2026-*/sales-*.parquet');
```

이 view는 데이터 자체가 아니라 조회 정의를 저장합니다. 원본 파일의 경로나 스키마가 바뀌면 view도 영향을 받으므로, 파일 배치 규칙을 함께 관리해야 합니다.

### 7. 500만 행 직접 비교

Parquet이 언제 유리한지 확인하려고 Codex가 2026년 7월 25일 로컬 Apple Silicon Mac에서 실험했습니다. DuckDB 1.4.5로 날짜·지역·카테고리·수량·금액을 가진 500만 행을 만들고 날짜와 ID 순으로 정렬했습니다. 같은 테이블을 header 포함 CSV와 `ZSTD`, row group 10만 행의 Parquet으로 내보냈습니다.

쿼리는 2025년 7월 데이터만 골라 10개 지역의 정확한 금액 합계와 행 수를 구했습니다. 포맷별로 한 번 워밍업한 뒤 실행 순서를 번갈아 7회 측정했고, 두 결과표가 같은지도 매번 검사했습니다.

| 이 로컬 시나리오 | CSV | Parquet |
|---|---:|---:|
| 파일 크기 | 241.61 MiB | 21.05 MiB |
| 측정 7회 중앙값 | 0.1830초 | 0.003082초 |
| CSV 대비 | 기준 | 크기 11.48분의 1, 조회 59.38배 빠름 |

**이 결과는 Parquet의 보편적 속도 배수가 아니라, 날짜순 데이터에서 한 달만 거르는 조건이 row group 건너뛰기에 잘 맞은 사례입니다.** 데이터 정렬, 열의 종류, 압축, 저장 장치, 캐시, 선택하는 행의 비율이 바뀌면 차이도 달라집니다. 전체 재현 스크립트와 14개 시간 표본은 글 번들의 `artifacts/benchmark_duckdb.py`와 `benchmark-results.json`에 보존했습니다.

그래도 실무 판단은 분명합니다. 한 번 받고 버릴 작은 CSV라면 그대로 조회해도 됩니다. 같은 파일을 반복 집계하거나 필요한 열이 일부뿐이고 데이터가 계속 쌓인다면, 타입을 확정한 Parquet으로 변환한 뒤 분석하는 편이 저장 공간과 조회 양쪽에서 유리할 가능성이 큽니다.

### 8. 첫 검증이 실패한 이유

첫 실행은 속도를 재기도 전에 결과 일치 검사에서 실패했습니다. DuckDB가 원본 `DECIMAL(12,2)` 금액을 Parquet에는 그대로 보존했지만, 스키마가 없는 CSV에서는 `DOUBLE`로 추론했기 때문입니다.

```text
CSV     20476966.870000023  -> DOUBLE
Parquet 20476966.87         -> DECIMAL(38,2)
```

두 값은 화면에서 비슷해 보여도 정확히 같은 타입과 값은 아닙니다. 벤치마크에서는 집계 전에 `amount`를 `DECIMAL(12,2)`로 고정해 다시 실행했고, 10개 지역 결과가 모두 일치한 뒤 시간을 비교했습니다.

이 실패는 CSV 자동 감지를 믿지 말아야 한다는 과장된 결론보다 구체적인 기준을 줍니다. **식별자, 날짜, 통화처럼 의미가 타입에 의존하는 열은 `read_csv`의 `types`로 고정하고, `DESCRIBE SELECT * FROM '파일경로'`로 실제 스키마를 확인해야 합니다.** 빠른 탐색에서는 자동 감지를 쓰되, 재사용할 분석에서는 감지 결과를 코드로 확정하는 순서가 안전합니다.

### 9. Pandas와 함께 쓰는 방법

Pandas DataFrame이 이미 메모리에 있다면 변수 이름을 SQL의 테이블처럼 조회할 수 있습니다. [공식 SQL on Pandas 가이드](https://duckdb.org/docs/stable/guides/python/sql_on_pandas)는 이 연결을 replacement scan이라고 설명합니다.

```python
import duckdb
import pandas as pd

orders_df = pd.DataFrame({
    "region": ["Seoul", "Busan", "Seoul"],
    "amount": [12000, 8000, 15000],
})

summary_df = duckdb.sql("""
    SELECT region, SUM(amount) AS revenue
    FROM orders_df
    GROUP BY region
    ORDER BY revenue DESC
""").df()

print(summary_df)
```

`orders_df`는 읽기 전용 입력처럼 사용되고 결과만 새 DataFrame으로 받습니다. 긴 전처리 전체를 SQL로 바꿀 필요는 없습니다. 큰 조인과 집계는 DuckDB에서 줄이고, 최종 표 정리와 그래프는 Pandas로 넘기는 경계를 잡으면 됩니다.

모든 결과를 `.df()`로 가져오면 최종 결과 크기만큼 Python 메모리가 필요합니다. 결과가 여전히 크다면 SQL에서 더 집계하거나 Parquet으로 바로 씁니다.

```python
con = duckdb.connect()
con.sql("""
    SELECT region, DATE_TRUNC('month', sold_at) AS month, SUM(amount) AS revenue
    FROM 'sales.parquet'
    GROUP BY region, month
""").write_parquet("monthly_revenue.parquet")
```

### 10. 결과를 파일 DB에 저장하는 방법

분석 중 만든 테이블을 다음 실행에서도 쓰려면 파일 경로로 연결합니다.

```python
import duckdb

with duckdb.connect("analytics.duckdb") as con:
    con.sql("""
        CREATE OR REPLACE TABLE monthly_revenue AS
        SELECT
            region,
            DATE_TRUNC('month', sold_at) AS month,
            SUM(amount) AS revenue
        FROM 'sales.parquet'
        GROUP BY region, month
    """)
```

`duckdb.connect()`처럼 인자를 생략하면 인메모리 DB이고, `duckdb.connect("analytics.duckdb")`처럼 경로를 주면 파일 DB입니다. 원본 Parquet을 계속 직접 조회할지, 자주 쓰는 정제 결과를 내부 테이블로 저장할지는 갱신 주기와 재사용 빈도로 결정합니다.

| 방식 | 잘 맞는 경우 | 주의점 |
|---|---|---|
| 파일 직접 조회 | 원본이 Parquet으로 잘 관리됨 | 경로·스키마 변경에 영향 |
| view 저장 | 같은 파일 패턴을 반복 조회 | 데이터가 복사되지는 않음 |
| 내부 table 저장 | 정제 결과를 자주 재사용 | 중복 저장과 갱신 책임 |
| 인메모리 연결 | 일회성 탐색·테스트 | 종료하면 상태가 사라짐 |

### 11. 느릴 때 확인할 순서

속도가 기대보다 느리다고 바로 `threads`를 크게 올리면 오히려 경쟁이 늘 수 있습니다. 다음 순서로 병목을 좁히는 편이 낫습니다.

1. `EXPLAIN`으로 파일 스캔과 필터 위치를 확인합니다.
2. `SELECT *` 대신 필요한 열만 선택합니다.
3. 반복 분석 CSV는 타입을 확정해 Parquet으로 변환합니다.
4. Parquet 파일이 지나치게 작게 쪼개졌거나 row group이 쿼리와 맞지 않는지 봅니다.
5. `ORDER BY`가 없는 결과의 입력 순서 보존이 필요하지 않다면 대용량 import·export에서 `SET preserve_insertion_order = false;`를 검토합니다.
6. 다른 프로그램과 메모리를 경쟁한다면 `SET memory_limit = '4GB';`처럼 한도를 명시하고 임시 디렉터리의 여유 공간을 확인합니다.

`GROUP BY`, `JOIN`, `ORDER BY`, window 함수는 중간 상태가 커질 수 있습니다. 메모리보다 큰 작업을 처리할 수 있다는 말은 디스크 공간과 I/O 비용이 사라진다는 뜻이 아닙니다. 느린 네트워크 드라이브보다 로컬 SSD에서 임시 작업을 수행하고, 큰 결과를 Python 객체로 한꺼번에 가져오지 않는 것이 중요합니다.

### 12. 도입 전에 알아둘 한계

가장 중요한 한계는 동시 쓰기 모델입니다. [공식 concurrency 문서](https://duckdb.org/docs/stable/connect/concurrency)에 따르면 한 프로세스 안에서는 충돌하지 않는 여러 쓰기를 처리할 수 있지만, 여러 프로세스가 같은 파일에 자동으로 동시에 쓰는 방식은 지원하지 않습니다. 여러 프로세스가 읽기 전용으로 여는 것과 여러 프로세스가 쓰는 것은 다른 문제입니다.

또한 많은 작은 트랜잭션은 DuckDB의 핵심 설계 목표가 아닙니다. 웹 요청마다 한 행을 쓰고 여러 서버 인스턴스가 같은 DB를 갱신해야 한다면 PostgreSQL·MySQL 같은 서버형 DB를 먼저 검토해야 합니다. 운영 DB의 데이터를 주기적으로 Parquet으로 내보내 DuckDB로 분석하는 조합은 가능하지만, 저장과 분석의 책임을 분리해야 합니다.

Python 병렬 처리에서도 연결을 무심코 공유하면 안 됩니다. 공식 Python API는 `duckdb.sql()`이 사용하는 전역 연결을 여러 스레드에서 함께 쓰지 말고, 각 스레드에 별도 연결을 만들도록 안내합니다.

마지막으로 외부 URL과 확장 기능은 편리한 만큼 접근 범위가 넓어집니다. 신뢰할 수 없는 unsigned extension을 불러오지 말고, 자동 다운로드나 외부 파일 접근이 허용되는 실행 환경인지 확인해야 합니다.

### 13. 가장 실용적인 시작 순서

DuckDB를 처음 도입한다면 거대한 데이터 플랫폼부터 설계할 필요가 없습니다.

1. `pip install duckdb`로 현재 분석 환경에만 설치합니다.
2. 기존 CSV 하나에 `DESCRIBE SELECT *`를 실행해 추론 타입을 확인합니다.
3. 실제로 자주 쓰는 필터·집계 SQL 하나를 파일에 직접 실행합니다.
4. 날짜·통화·식별자 타입을 명시하고 결과를 기존 집계와 대조합니다.
5. 반복 조회가 많다면 Parquet으로 변환해 파일 크기와 같은 쿼리 시간을 측정합니다.
6. 필요한 경우에만 view나 `.duckdb` 파일로 재사용 범위를 넓힙니다.

**DuckDB의 장점은 새로운 서버를 하나 더 운영하는 데 있지 않고, 이미 가진 파일에 분석용 SQL을 가장 짧게 가져오는 데 있습니다.** 먼저 실제 CSV 한 개와 자주 묻는 질문 하나로 결과를 검증해 보세요. 타입이 맞고 반복 분석이 단순해졌다면 그때 Parquet 변환과 파일 DB 저장을 다음 단계로 넓히는 것이 가장 안전한 사용법입니다.
