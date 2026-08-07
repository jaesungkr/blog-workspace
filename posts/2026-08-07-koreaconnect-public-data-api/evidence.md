# 근거 지도: 공공데이터 API 활용기, 전국 화재 현황 29만 건을 받아보니

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | 디지털융합플랫폼 데이터·API 마켓은 2026-08-07 화면에서 전체 113,389건, 데이터파일 100,416건, 오픈API 12,973건, MCP 52건을 표시함 | 공식 화면 직접 관찰 | 확인 | `https://portal.koreaconnect.kr/market/mk/getMkDigitStore`, `artifacts/source-snapshot.md` | 수시로 바뀌는 시점값 |
| C02 | 목록에는 화재·구급·119 신고·구조, 주유소 가격, 주차장, 날씨, 의약품, 상권지수 등이 보임 | 공식 화면 직접 관찰 | 확인 | API 마켓 첫 페이지와 재난안전 필터 | 모든 항목을 호출한 것은 아님 |
| C03 | 전국 화재 현황 API는 POST이며 인증 헤더 이름은 `api_user_key_id`임 | 공식 | 확인 | API 상세 명세 | 키 발급과 승인 필요 |
| C04 | 요청 변수는 `page`, `size`, 선택 `q`, `sort`이며 size 최대값은 100임 | 공식 | 확인 | API 상세 명세 | 서버 정책이 바뀔 수 있음 |
| C05 | 2026-08-07 인증 호출은 HTTP 200, JSON, 전체 295,105건을 반환함 | Codex 실행 | 확인 | `artifacts/run/api-response-headers.txt`, 세 정렬 응답 JSON | 한 시점의 전체 건수 |
| C06 | 응답 명세는 페이지 정보 7개와 화재 항목 상세 62개를 제공함 | 공식 명세 대조 | 확인 | API 상세 페이지의 Response Element 69행 | 선택 필드는 빈 문자열이나 null일 수 있음 |
| C07 | 접수일 내림차순 최신 행은 2026-08-02 20:38 경기도 용인시 기흥구 건축·구조물 화재임 | Codex 실행 | 확인 | `artifacts/run/latest-by-received-at.json` | 공개 API가 반환한 최신 행이며 실시간 사건 전체를 뜻하지 않음 |
| C08 | 상위 최신 행의 `gtrRegDt`는 모두 1785792679730이며 KST로 2026-08-04 06:31:19임 | Codex 실행 | 확인 | 세 정렬 응답 JSON | 등록 시각 의미는 명세상 Unix timestamp, 묶음 처리 사유는 미확인 |
| C09 | 8월 7일 확인 시 최신 접수와 약 5일, 등록 시각과 약 3일 차이가 관찰돼 실시간 스트림보다 배치형 제공 정황이 강함 | 관찰 기반 해석 | 확인 | C07·C08 | 고정 갱신 주기나 SLA를 확정하지 않음 |
| C10 | 등록일 내림차순 첫 행은 같은 등록 시각을 공유하는 묶음 안에서 실제 최신 접수 행이 아니었음 | Codex 실행 | 확인 | `latest-by-ingested-at.json`과 `latest-by-received-at.json` 비교 | 동률 정렬의 내부 순서는 문서화되지 않음 |
| C11 | 인증 헤더가 없으면 401 `AGW-E40102`가 반환됨 | Codex 실행 | 확인 | 2026-08-07 무인증 요청 관찰 | 인증 실패 한 사례 |
| C12 | 차량 화재 행에서는 건물 관련 필드가 null·빈 문자열이었음 | Codex 실행 | 확인 | 최초 `gtrRegDt,desc` 1건 응답 | 결측 패턴의 전체 비율은 측정하지 않음 |

## 직접 검증 설계

- 질문: 승인받은 전국 화재 현황 API가 실제로 응답하며, 현재 제공 범위와 최신성은
  어느 정도인가?
- 실행 주체: 사용자가 인증키를 제공하고 Codex가 호출·정렬·검산
- 환경과 확인 시점: macOS, curl, 2026-08-07 23:03 KST
- 호출 URL: `https://api.koreaconnect.kr/01/1/2605060927592107314KFSBDP/SAFETY/fsdpApi/rest/v1/fire-incidents`
- 입력: `page=1`, `size=5`, `sort=rcptDt,desc`·`dsptDt,desc`·`gtrRegDt,desc`
- 인증: `api_user_key_id` 헤더. 실제 키는 파일에 저장하지 않음
- 비교·판정 규칙: HTTP 200과 JSON을 성공으로 보고, 최신성은 접수일과 등록일을
  각각 내림차순으로 정렬해 비교
- 반복 횟수와 표본 크기: 세 정렬 조건에서 상위 5행
- 보존할 원자료: `artifacts/run/`의 응답 JSON 3개와 응답 헤더

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | 인증 없음, page 1, size 1 | HTTP 401, `AGW-E40102` | 감사 기록 | URL과 게이트웨이 도달, 정상 인증 여부는 미확인 |
| E02 | 인증 있음, `gtrRegDt,desc`, size 1 | HTTP 200, total 295,105 | `artifacts/run/api-response-headers.txt`, `latest-by-ingested-at.json` | 전체 건수와 등록일 정렬 첫 행 |
| E03 | 인증 있음, `rcptDt,desc`, size 5 | 최신 접수 2026-08-02 20:38 | `artifacts/run/latest-by-received-at.json` | API가 현재 제공한 행 중 최신 접수 |
| E04 | 인증 있음, `dsptDt,desc`, size 5 | 최신 출동 2026-08-02 20:38:55 | `artifacts/run/latest-by-dispatched-at.json` | 접수 최신 행과 출동 최신 행은 다를 수 있음 |
| E05 | 세 정렬 응답의 `gtrRegDt` 비교 | 상위 행들이 동일한 2026-08-04 06:31:19 KST 등록 시각 공유 | 응답 JSON 3개 | 묶음 등록 정황, 처리 방식 자체는 미확인 |

## 실패와 반례

- 첫 설명에서는 `gtrRegDt,desc`의 첫 행인 파주시 차량 화재를 최신 화재라고
  보았습니다. 여러 행이 같은 등록 시각을 공유해 접수일 최신과 일치하지 않았습니다.
- `rcptDt,desc`로 다시 정렬한 결과 실제 최신 접수는 용인시 기흥구의
  2026-08-02 20:38 건이었습니다.
- 이 실패는 수집 등록일과 사건 발생일을 구분해야 한다는 본문의 핵심 사례로
  반영합니다.

## 해석하지 않는 범위

- `배치형`은 관찰된 시차와 동일 등록 타임스탬프에 대한 표현이며, 공식 SLA나
  고정 주기를 뜻하지 않습니다.
- 전국 화재 사건의 완전성·정확성·누락률을 검증하지 않았습니다.
- `재산피해금액`의 단위는 상세 명세에서 찾지 못해 본문 수치 해석에서 제외합니다.
- API 마켓의 다른 항목은 목록과 설명만 확인했으며 인증 호출은 하지 않았습니다.

## 공식 출처

- 데이터·API 마켓: https://portal.koreaconnect.kr/market/mk/getMkDigitStore
- 전국 화재 현황 상세: https://portal.koreaconnect.kr/market/mk/getMkApiDetail?drsTcd=02&drsno=77a018d8298c4921932ea8b51f3c1598
