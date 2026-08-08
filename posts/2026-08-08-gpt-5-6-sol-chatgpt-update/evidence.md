# 근거 지도: GPT-5.6 Sol 업데이트 및 Luna 무제한 무료

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 `공식`, `독립 검증`, `벤더 주장`, `사용자 제공`, `Codex 실행`,
`추정`, `구조 예시`처럼 실제 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | OpenAI는 2026-08-06 ChatGPT 일상 대화 개선과 무료 이용 확대를 발표했습니다. | 공식 | 확인 | OpenAI 발표 페이지의 날짜·제목·도입부, `artifacts/sources/openai-improving-gpt56-sol.html` | 벤더 발표이며 실제 계정별 배포 완료를 뜻하지 않습니다. |
| C02 | Plus·Pro에서는 GPT-5.6 Sol이 더 집중된 답변과 사실 신뢰성 향상을 목표로 업데이트됐습니다. | 벤더 주장 | 확인 | OpenAI 발표의 도입부와 `More focused answers`, `More reliable facts` | 실제 한국어 답변을 직접 비교하지 않았습니다. |
| C03 | OpenAI 내부 금융·의료·법률 평가에서 하나 이상의 사실 오류가 있는 답변 비율이 GPT-5.5 Instant 대비 Luna 62%, Sol 68% 적었다고 발표했습니다. | 벤더 내부 평가 | 확인 | OpenAI 발표 `More reliable facts` | 표본 수·프롬프트·판정자·신뢰구간이 발표문에 공개되지 않아 독립 재현으로 볼 수 없습니다. |
| C04 | Plus·Pro는 웹·모바일·데스크톱에서 응답 사고량을 조절하는 새 슬라이더를 사용할 수 있습니다. | 공식 | 확인 | OpenAI 발표 `More consistent...`·`Safety and availability` | 실제 Plus·Pro 계정의 UI는 직접 시험하지 않았습니다. |
| C05 | Free·Go의 기본 모델은 GPT-5.6 Luna로 바뀌고, Free·Go 사용자는 무제한 텍스트 채팅과 Think 버튼을 받습니다. | 공식 | 확인 | OpenAI 발표 `Expanding access for free users`·`Safety and availability` | 악용 방지 장치가 적용되며 파일·이미지·기타 도구에는 제한이 계속 적용됩니다. |
| C06 | 8월 6일 발표 기준 Sol·슬라이더는 Plus·Pro에 즉시, Luna 기본 전환은 그 주, 무제한 텍스트·Think는 다음 주로 예고됐습니다. | 공식 | 확인 | OpenAI 발표 `Safety and availability` | `이번 주`·`다음 주`는 발표 시점 기준 표현이며 정확한 계정별 날짜는 제공하지 않습니다. |
| C07 | 이번 ChatGPT 대화용 Sol 업데이트는 Work와 Codex에서 쓰는 Sol 버전을 변경하지 않습니다. | 공식 | 확인 | OpenAI 발표 `Safety and availability` | Work·Codex의 별도 향후 업데이트 가능성은 다루지 않습니다. |
| C08 | 청소년 보호를 위한 관계·연령 제한 콘텐츠·위험 행동 등에 대한 경계와 평가가 추가됐습니다. | 공식 | 확인 | OpenAI 발표 및 `https://deploymentsafety.openai.com/gpt-5-6-august-update` | 안전성 효과를 독립 시험하지 않았습니다. |
| C09 | 발표 제목·날짜와 무료 Luna·Think 안내 화면을 2026-08-08 실제 브라우저에서 캡처했습니다. | Codex 실행 | 확인 | `artifacts/captures/raw/openai-gpt56-sol-header.jpg`, `artifacts/captures/raw/openai-free-luna-think.jpg` | 제품 계정 화면이 아니라 공식 발표 페이지의 렌더링입니다. |
| C10 | OpenAI 발표 페이지의 Free 사용자 섹션에는 GPT-5.6 Luna 무제한 텍스트 채팅과 Think 버튼 설명·UI 예시가 함께 표시됩니다. | Codex 실행 + 공식 | 확인 | `artifacts/captures/raw/openai-free-luna-think.jpg` | 이 화면은 Go 대상이나 `이번 주/다음 주` 일정을 직접 보여 주지 않습니다. |
| C11 | OpenAI는 Luna를 GPT-5.6 제품군에서 가장 빠르고 비용 효율적인 모델로, API 문서에서는 비용에 민감한 대규모 작업용 모델로 설명합니다. | 공식·벤더 포지셔닝 | 확인 | `https://openai.com/index/gpt-5-6/`, `https://developers.openai.com/api/docs/models/gpt-5.6-luna` | API의 모델 위치를 무료 ChatGPT의 실제 속도 측정값으로 해석할 수 없습니다. |
| C12 | OpenAI 출시 평가에서 Luna/Sol/GPT-5.5는 Agents' Last Exam 50.3/52.7/46.9%, SWE-Bench Pro 62.7/64.6/59.4%, BrowseComp 83.3/90.4/84.4%를 기록했습니다. | 벤더 공개 평가 | 확인 | `https://openai.com/index/gpt-5-6/`의 Professional, Coding, Computer use 표 | 무료 ChatGPT와 추론·도구 조건이 같다는 근거가 없고 독립 한국어 평가가 아닙니다. 세 항목은 전체 모델 성능을 대표하는 종합 순위가 아닙니다. |
| C13 | 선택한 세 평가에서 Luna는 GPT-5.5보다 전문 업무·코딩 점수가 높고 웹 탐색은 1.1%포인트 낮으며, Sol보다는 세 항목 모두 낮습니다. | 계산·해석 | 확인 | C12의 공개 수치를 같은 항목끼리 비교 | 벤더 수치에서 계산한 제한된 비교이며 일반적인 우열로 확대하지 않습니다. |

## 직접 검증 설계

- 질문: 공식 발표가 요금제별 기능·시점·제한·비적용 범위를 명시하며, 출시 자료가 Luna의 상대적 성능을 확인할 수 있는 같은 조건의 수치를 제공하는가?
- 실행 주체: Codex
- 환경과 확인 시점: macOS, Codex in-app browser, 1280×720 CSS viewport, DPR 2, 2026-08-08 KST. 출력은 페이지 좌표 기준 1280×760·1280×980 clip입니다.
- 입력: OpenAI 8월 6일 공식 발표, 7월 GPT-5.6 출시 자료, Luna API 모델 문서, 8월 시스템 카드
- 전처리 또는 표현: 발표 DOM에서 제목·날짜·Sol·Luna·Think·availability 문장을 확인하고 두 근거 화면을 페이지 문맥이 남도록 캡처합니다. 출시 자료에서는 정의가 다른 평가를 세 항목으로 제한하고 Luna·Sol·GPT-5.5의 같은 행만 옮깁니다.
- 비교·판정 규칙: 본문 문장과 첫 표의 각 셀이 공식 문장의 주체·요금제·시점·제한을 빠뜨리지 않아야 합니다. 성능 표는 원문의 열·행 값을 그대로 유지하고, 높을수록 좋은 평가끼리 같은 열에서만 비교합니다.
- 성공 기준: C01-C13이 원문·캡처·계산에 일대일로 연결되고 벤더 공개 평가, 벤더 내부 평가, Codex 실행을 혼동하지 않음
- 반복 횟수와 표본 크기: 공식 제품 자료 2건, API 모델 문서 1건, 연결 시스템 카드 1건, 브라우저 캡처 2장, 선택 평가 3개
- 보존할 원자료: `artifacts/sources/*.html`, `artifacts/captures/raw/*.jpg`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | OpenAI 발표 상단 | 2026-08-06 날짜와 GPT-5.6 Sol·무료 Luna 확대 제목 확인 | `artifacts/captures/raw/openai-gpt56-sol-header.jpg` | 발표의 정체와 시점만 증명 |
| E02 | 무료 이용자 섹션 | Luna 무제한 텍스트 채팅과 Think 버튼 문장·예시 화면 확인 | `artifacts/captures/raw/openai-free-luna-think.jpg` | 제품 계정에서 실제 활성화됐다는 증거는 아님 |
| E03 | 발표 DOM | 요금제·시점·도구 제한·Codex 비적용 문장을 보존 | `artifacts/sources/openai-improving-gpt56-sol.html` | 브라우저가 받은 2026-08-08 페이지 스냅샷 |
| E04 | GPT-5.6 출시 평가표 | Luna·Sol·GPT-5.5의 전문 업무·코딩·웹 탐색 점수를 같은 평가 행에서 대조 | `https://openai.com/index/gpt-5-6/` | 벤더 공개 평가이며 무료 ChatGPT의 실사용 시험은 아님 |

## 실패와 반례

- 실패한 입력: `curl`로 OpenAI 발표 HTML을 직접 저장하려 했으나 서버가 HTTP 403을 반환했습니다.
- 예상과 달랐던 결과: 페이지의 무료 사용자 이미지는 초기 로드에서 지연 로딩 상태였습니다. 해당 섹션까지 실제 스크롤해 이미지의 `naturalWidth=640`, `naturalHeight=360` 로딩을 확인한 뒤 다시 캡처했습니다.
- 일반화하면 안 되는 범위: 두 캡처는 공식 발표 페이지이며 실제 한국 계정의 버튼 배치, 한국어 UI, 응답 품질, 배포 완료 여부를 증명하지 않습니다. 공개 성능표도 무료 ChatGPT의 속도나 한국어 품질을 직접 측정한 자료가 아닙니다.

## 미해결 항목

- 없음. 계정별 배포 완료 시점, 무료 한국 계정의 실사용 성능, 독립 성능 평가는 확인 범위 밖으로 명시합니다.

## 출처 메모

긴 원문을 복사하지 않습니다. 본문에 필요한 짧은 근거와 출처의 한계를 함께
기록합니다.

- 2026-08-06 OpenAI 제품 발표: Plus·Pro Sol 개선, 사고량 슬라이더, Free·Go Luna 기본 전환, 무제한 텍스트·Think, 도구 제한, Codex·Work 비적용.
- 2026-07-09 OpenAI GPT-5.6 출시 자료: Luna·Sol·GPT-5.5의 전문 업무·코딩·웹 탐색 평가와 Luna의 제품군 내 위치.
- OpenAI Luna API 모델 문서: 비용에 민감한 대규모 처리용이라는 모델 포지셔닝. API의 가격·성능 조건을 무료 ChatGPT 실사용으로 옮겨 말하지 않습니다.
- OpenAI 8월 시스템 카드: 청소년 대상 경계 강화와 추가 평가를 설명하는 연결 자료.
- 발표 페이지의 62%·68%는 오류율 자체가 62%·68%라는 뜻이 아니라, `하나 이상의 사실 오류가 포함된 답변 비율`이 GPT-5.5 Instant 대비 상대적으로 적었다는 의미입니다.
