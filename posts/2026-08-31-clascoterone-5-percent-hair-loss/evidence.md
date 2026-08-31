# 근거 지도: 클라스코테론 5% 탈모약, 바르는 신약은 언제 쓸 수 있을까

확인 기준일은 2026년 8월 31일입니다. `회사 발표`는 개발사가 공개한 결과이며, 임상시험 등록부의 결과표나 동료평가 논문과 같은 독립 공개 단계와 구분합니다.

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | 클라스코테론 5% 용액은 성인 남성의 경증~중등도 안드로겐성 탈모를 대상으로 개발된 국소 안드로겐 수용체 억제 후보약임 | 공식 등록 | 확인 | [SCALP 1](https://clinicaltrials.gov/study/NCT05910450), [SCALP 2](https://clinicaltrials.gov/study/NCT05914805) | 여성, 중증 탈모, 미성년자에게 일반화할 수 없음 |
| C02 | SCALP 1과 2는 5% 용액 1.5mL를 하루 두 번 정수리와 관자 부위에 바르는 설계임 | 공식 등록 | 확인 | ClinicalTrials.gov API의 intervention description | 승인된 사용법이 아니라 시험 프로토콜임 |
| C03 | 두 3상은 각각 703명과 762명, 합계 1,465명을 등록했으며 완료 상태임 | 공식 등록·Codex 대조 | 확인 | `artifacts/source-snapshots/NCT05910450.json`, `NCT05914805.json` | 등록 인원이 모든 분석에 포함됐다는 뜻은 아님 |
| C04 | 6개월 주요 객관 지표는 비연모성 표적 부위 모발 수(TAHC)의 기저치 대비 변화임 | 공식 등록 | 확인 | 두 ClinicalTrials.gov primary outcome | 측정 면적과 절대 변화량은 공개 보도자료에 없음 |
| C05 | 개발사는 두 연구의 위약 대비 TAHC 상대 개선을 5.39배(회사 표기 539%)와 1.68배(168%)로 발표했고 p<0.05라고 밝힘 | 회사 발표 | 확인 | [2025-12-03 Cosmo topline PDF](https://files.schedulr.ch/news-files/7663/714d4f31-6df4-430a-824c-6eb0d6ca82f2.pdf) | `539% 높음`으로 번역하면 6.39배로 읽힐 수 있어 회사의 배수와 백분율을 병기함. 절대 모발 수 변화, 군별 평균, 신뢰구간은 공개되지 않음 |
| C06 | 5.39배(회사 표기 539%)는 개인의 전체 머리카락 수가 5.39배가 됐다는 뜻이 아니라 위약군과 비교한 상대 개선 표현임 | Codex 해석 | 확인 | C04·C05의 지표 정의와 보도자료 표현 대조 | 원자료가 없어 임상적으로 체감할 절대 차이를 계산할 수 없음 |
| C07 | 12개월 연장 단계는 첫 6개월에 환자 보고 결과로 반응한 참가자가 계속 5%를 쓰거나 vehicle로 전환하는 설계를 포함함 | 공식 등록·회사 발표 | 확인 | 2026-04 Cosmo PDF appendix, ClinicalTrials.gov arm descriptions | 전체 무작위 배정 집단의 12개월 결과로 읽으면 안 됨 |
| C08 | 개발사는 12개월 계속 사용군이 6개월 뒤 vehicle 전환군보다 TAHC가 2.39배 개선됐고 치료 만족도 상대 개선이 24.5%였다고 발표함 | 회사 발표 | 확인 | [2026-04-15 Cosmo 12-month PDF](https://files.schedulr.ch/news-files/8365/439087a1-8c04-4d60-ba05-aac2aa2158ae.pdf) | 절대 수치와 상세 통계표가 없고 연장 참가자 선택 조건이 있음 |
| C09 | 개발사는 12개월 안전성과 내약성이 vehicle과 비슷하고 유의한 전신 호르몬 부작용이 관찰되지 않았다고 발표함 | 회사 발표 | 확인 | 2026-04-15 Cosmo 12-month PDF | 상세 이상반응 표와 동료평가 논문이 아직 공개되지 않음 |
| C10 | 2026-08-31 현재 두 ClinicalTrials.gov 기록에는 resultsSection이 없음 | 공식 API·Codex 대조 | 확인 | 저장한 두 JSON의 `resultsSection: null`, version holder 2026-08-28 | 등록부 결과 게시가 논문 출판의 필수 전제는 아니지만 공개 데이터 수준을 보여 줌 |
| C11 | 같은 날짜 PubMed 검색에서 SCALP 1·2의 원저 3상 논문은 확인되지 않음 | 공식 API·Codex 검색 | 확인 | [PubMed 검색 결과](https://pubmed.ncbi.nlm.nih.gov/?term=%28clascoterone%5BTitle%2FAbstract%5D%29+AND+%28androgenetic+alopecia%5BTitle%2FAbstract%5D+OR+male+pattern+hair+loss%5BTitle%2FAbstract%5D%29), `pubmed-clascoterone-aga-search.json`, `pubmed-clascoterone-aga-summary.json` | 검색식 밖의 조기 공개나 비색인 자료가 있을 수 있음 |
| C12 | 미국 FDA의 클라스코테론 승인 제품 검색 결과는 1% 국소 크림 WINLEVI 한 건이며 탈모용 5% 용액은 없음 | 공식 API·Codex 대조 | 확인 | `openfda-clascoterone-drugsfda.json`, [WINLEVI DailyMed 라벨](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1673a84b-7f5c-47ab-a99c-1e3db21a6a09) | openFDA 갱신 지연 가능성을 회사의 2027 filing 계획과 함께 교차 확인함 |
| C13 | 개발사는 미국 NDA를 2027년 1분기, 유럽 신청을 2027년 2분기에 제출할 계획이라고 밝힘 | 회사 계획 | 확인 | [2026-07-23 Cosmo H1 발표](https://www.cosmohealthconfidence.com/news/64300770-h1-2026) | 신청 목표는 승인·출시일이 아니며 변경될 수 있음 |
| C14 | 1% 여드름 크림은 농도·제형·적응증이 달라 5% 탈모 용액의 대체제로 볼 수 없음 | 공식 라벨·판단 | 확인 | DailyMed 라벨의 1% cream, acne indication과 SCALP 5% solution protocol 대조 | 의사의 개별적인 비승인 사용 판단을 대신하지 않음 |
| C15 | 현재 치료를 중단·변경하거나 병용하면 더 낫다는 직접 근거는 공개된 SCALP 3상에서 확인되지 않음 | 증거 경계 | 확인 | 두 시험의 comparator는 vehicle이며 active comparator·combination arm이 없음 | 향후 별도 연구가 나올 수 있음 |
| C16 | 피나스테리드·두타스테리드는 5알파환원효소 억제제이고 클라스코테론은 안드로겐 수용체 길항제로 분류됨 | 동료평가 리뷰 | 확인 | [2024년 남성형 탈모 치료 리뷰](https://pubmed.ncbi.nlm.nih.gov/38666717/) | 약물 간 효능을 직접 비교한 근거로 쓰지 않음 |

## Codex 검증 설계

- 질문: `효과 539%`, `1년 안전성`, `출시 임박`을 각각 어느 증거 단계까지 말할 수 있는가?
- 실행 주체: Codex
- 환경과 확인 시점: macOS 로컬 셸, ClinicalTrials.gov API v2, openFDA Drugs@FDA API, NCBI PubMed E-utilities, 2026-08-31
- 입력: NCT05910450, NCT05914805, active ingredient `CLASCOTERONE`, PubMed 검색식 `clascoterone[Title/Abstract] AND (androgenetic alopecia[Title/Abstract] OR male pattern hair loss[Title/Abstract])`
- 비교·판정 규칙: 임상 설계와 등록 인원은 등록부, 승인 상태는 FDA 데이터베이스, 수치 결과는 개발사 원문, 논문 공개 여부는 PubMed 색인으로 역할을 분리함
- 성공 기준: 모든 강한 주장에 증거 유형과 한계가 붙고, 회사 발표를 독립 검증처럼 서술하지 않음
- 보존할 원자료: `artifacts/source-snapshots/`

## 결과

| 점검 항목 | 관찰 결과 | 원자료 경로 | 본문 판단 |
|---|---|---|---|
| 임상 완료·규모 | SCALP 1 703명, SCALP 2 762명, 모두 완료 | `artifacts/source-snapshots/NCT05910450.json`, `NCT05914805.json` | 3상 완료는 확인 |
| 등록부 결과표 | 두 기록 모두 `resultsSection: null` | 같은 JSON | 절대 효과 크기는 아직 평가 불가 |
| 미국 승인 제품 | 클라스코테론 1% 크림 한 건 | `artifacts/source-snapshots/openfda-clascoterone-drugsfda.json` | 5% 탈모 용액은 승인 제품 아님 |
| PubMed | 검색 결과 8건, SCALP 1·2 원저 3상 논문 없음 | `pubmed-clascoterone-aga-*.json` | 회사 보도자료를 동료평가 결과로 부르지 않음 |
| 허가 계획 | 미국 2027년 1분기, 유럽 2027년 2분기 신청 목표 | `cosmo-h1-2026.html` | 2027년 출시로 단정하지 않음 |

## 실패와 반례

- `539%`에서 절대 모발 증가량을 역산하려 했으나, vehicle과 5%군의 절대 평균 변화가 공개되지 않아 계산하지 않음
- 1년 결과를 전체 1,465명의 장기 결과로 요약하려 했으나, 연장 단계의 반응자 선별 조건 때문에 범위를 좁힘
- 한국 출시 연도와 가격을 추정할 수 있는 공식 5% 제품 계약·허가 자료를 확인하지 못해 본문에서 제외함
- 1% 여드름 크림의 안전성 라벨을 5% 두피 용액에 그대로 적용하지 않음. `국소 사용=전신 영향 0`이라는 단정만 경계하는 자료로 제한함

## 사용자 제공 참고 영상 처리

- 영상 URL: `https://www.youtube.com/watch?v=PuGWXVi7pK4`
- 사용 방식: 독자가 궁금해할 질문과 과장 가능성이 있는 표현을 찾는 배경 자료로만 사용함
- 본문에서 제외한 영상 기반 주장: 국내 2028~2029년 출시 예상, 월 20만 원 가격 예상, 기존 약과의 시너지 보장, 전신 부작용이 전혀 없다는 단정
- 본문에서는 영상을 언급하거나 영상에 권위를 부여하지 않고, 채택한 사실을 공식 자료로 다시 확인함

## 미해결 항목

- 없음. 공개되지 않은 절대 3상 결과는 `공개 전`이라는 한계로 처리하며 수치를 추정하지 않음

## 원자료 해시

| 파일 | SHA-256 |
|---|---|
| `NCT05910450.json` | `7fa6f54c942f1058e395fbb986bc62b0106313cb62e1d1c0d0cdc5fba4e43144` |
| `NCT05914805.json` | `f73bdf790b4355aa4806845a62df8351515f2b2a498f36ca30423dfab725fbe9` |
| `cosmo-2025-12-phase3-topline.pdf` | `52983c9fd38bd5f6f27acedc4a6b0ecfa36706a7ead3554ccb81c5edbae15fb2` |
| `cosmo-2026-04-12month.pdf` | `3b2c9483ba74d6e8d449e59599aec31fc5342290e2286def08d4287055b1cd17` |
| `openfda-clascoterone-drugsfda.json` | `ef7d36059d6990fefd54f987d0a769a543641317ce5c3459b4c71370f7b63d6f` |
| `pubmed-clascoterone-aga-search.json` | `d8ec771686d7ef35ad9d5e5c13b75f5f1e0a8d5ac1d0d57e3917ceef2c81d55d` |
| `pubmed-clascoterone-aga-summary.json` | `25110cdaabf1c231e3a6df35f13534c18707bbdbd94399f313083d1bedf0a886` |
| `cosmo-h1-2026.html` | `991d211e42aebcf1bbd17b783efb2ab8839c26490ff1b853089c5c83faab13e8` |
| `dailymed-winlevi.html` | `6653807f620324371d8ccb4e4f3561cdd96083dea18d4caf7b259ef734021831` |
