# 근거 지도: 제브(Jev) AI, 고객 문의 예시로 이해하는 판단 전용 모델

확인 기준일: 2026-09-17 (Asia/Seoul)

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | TypeSafe AI는 2026년 9월 15일 첫 공개 System One 모델 제브를 초기 접근으로 공개함 | 공식 | 확인 | [TypeSafe 공식 발표](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 공개 후 기능·접근 범위가 바뀔 수 있음 |
| C02 | 제브는 상태와 정형 질문을 받아 자유 문장이 아닌 구조화된 판단과 확률을 반환함 | 공식 문서 | 확인 | [TypeSafe 문서 Introduction](https://docs.typesafe.ai/introduction) | 회사가 정의한 제품 범주이며 모델 내부 구조 전체는 공개되지 않음 |
| C03 | 공식 문서는 Choice·Score·Noul 세 질문 유형을 설명하며, 한 요청의 질문을 같은 상태에 대해 병렬·독립 평가한다고 밝힘 | 공식 문서 | 확인 | [TypeSafe 문서 Introduction](https://docs.typesafe.ai/introduction) | 실제 지연시간과 정확도는 질문 수·입력·지역·서비스 상태에 따라 달라질 수 있음 |
| C04 | TypeSafe는 입력 100만 토큰당 0.042달러, 출력 토큰 무료, 응답 70~500ms, 같은 System One 형태의 쿼리에서 40~200배 빠르다고 발표함 | 벤더 주장 | 확인 | [TypeSafe 공식 발표의 비교표](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 독립 재현이 아니며 회사는 가격 지속 가능성을 장기적으로 입증해야 한다고 밝힘 |
| C05 | 홈페이지의 193.6배 빠름·444.6배 저렴함은 System One 워크플로 평가에서 나온 수치임 | 벤더 주장 | 확인 | [TypeSafe 홈페이지](https://typesafe.ai/), [공식 평가 페이지](https://evals.typesafe.ai/) | 네 워크플로 평균과 회사가 만든 harness를 사용하며, 회사도 높은 쪽의 실제 개선치일 수 있다고 설명함 |
| C06 | 평가의 기준 확률은 GPT-6 Astra와 Claude Fable 5.1의 응답 평균이고, 공개 데이터셋의 독립 정답이 아님 | 공식 방법 설명 | 확인 | [Workflow evals](https://evals.typesafe.ai/), [TypeSafe 공식 발표](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 기준 모델의 편향과 harness 설계자의 편향이 결과에 남을 수 있음 |
| C07 | `환각 0%`는 미리 정의한 출력 형식 밖의 값을 만들지 않는다는 schema 보장을 가리키며, 판단이 언제나 옳다는 실증 수치가 아님 | 공식 설명+해석 | 확인 | [TypeSafe 공식 발표의 Hallucination and Type-safety](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 회사 스스로 0%가 경험적으로 측정한 수치가 아니라고 밝힘. 오답 확률은 별개임 |
| C08 | 디오고 알메이다는 2022년 InstructGPT 논문의 공동 저자이며 GPT-4 기술 보고서에도 이름을 올림 | 1차 연구 자료 | 확인 | [InstructGPT 논문](https://arxiv.org/abs/2203.02155), [GPT-4 기술 보고서](https://arxiv.org/abs/2303.08774) | `챗GPT 공동 개발자`는 대중적 요약 표현이며 공개 제품의 공식 기여자 목록과 동일한 표현은 아님 |
| C09 | TypeSafe는 알메이다가 RLHF와 InstructGPT를 공동 개발했고 이 방법이 ChatGPT와 GPT-4로 이어졌다고 소개함 | 당사자·회사 소개 | 확인 | [TypeSafe 팀 페이지](https://typesafe.ai/team), [TypeSafe 공식 발표](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 창업자 회사의 소개이므로 논문 저자 정보와 함께 제한적으로 사용함 |
| C10 | TypeSafe는 Jev라는 이름이 윌리엄 스탠리 제번스와 제번스의 역설에서 왔다고 설명함 | 공식 | 확인 | [TypeSafe 공식 발표 FAQ](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 이름의 배경이지 모델 효과를 입증하는 근거는 아님 |
| C11 | 제공받은 Instagram 게시물은 최대 200배 속도, 출력 토큰 무료, 분류·스팸 판별 용도를 요약함 | 사용자 제공 참고 자료 | 확인 | [AI Freaks Instagram 게시물](https://www.instagram.com/p/DdX5q1eGvUL/?img_index=1), 공개 캡션을 2026-09-17 브라우저에서 확인 | 2차 요약 자료이므로 수치와 기능의 본문 근거로 사용하지 않고 공식 자료와 대조함 |
| C12 | 제브는 2026년 9월 16일 Vercel AI Gateway에도 추가됨 | 공식 플랫폼 공지 | 확인 | [Vercel AI Gateway 변경 기록](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway), [모델 페이지](https://vercel.com/ai-gateway/models/jev) | TypeSafe의 초기 접근 정책과 Vercel 계정·요금 조건은 별개임 |

## 직접 검증 대신 수행한 주장 감사

### 예시 보강 시 추가 확인

- [공식 빠른 시작 문서](https://docs.typesafe.ai/introduction/quickstart): Playground에 텍스트를 상태로 넣고 질문을 추가하는 체험 경로와 API 연결 방식을 재확인함
- [Choice](https://docs.typesafe.ai/primitives/choice): 미리 정의한 선택지, 선택값, 선택지별 확률, confidence를 반환함
- [Score](https://docs.typesafe.ai/primitives/score): 단계 번호는 0부터 시작하며 점수는 각 단계 확률의 가중 평균임. 본문의 0~2 중 1.7점은 이를 설명하는 가상 값임
- [Noul](https://docs.typesafe.ai/primitives/noul): 주어진 진술이 참일 확률을 0~1로 반환함
- 예시 작성 주체: Codex. 고객 문의 문장, 배송 92%·결제 5%·계정 3%, 긴급도 1.7, Noul 0.85는 작동 방식 설명용으로 만든 가상 데이터임. 실행·정확도·한국어 성능을 입증하지 않으며 실제 API 출력 형식을 재현한 코드도 아님
- 본문에는 표 앞에서 가상 문의와 수치임을 밝히고, 모델이 부여한 확률이 실제 100건 중 정답 수를 뜻하지 않는다고 설명함

### 감사 설계

- 질문: 홈페이지의 속도·비용·환각 문구 중 무엇이 구조적으로 보장되고, 무엇이 회사 평가이며, 무엇이 아직 독립 검증되지 않았나요?
- 실행 주체: `Codex`
- 환경과 확인 시점: 공개 웹 자료, 2026-09-17, 한국 표준시 기준
- 입력: TypeSafe 홈페이지·발표문·문서·평가 페이지, InstructGPT·GPT-4 논문, Vercel 공지, 제공받은 Instagram 게시물
- 판정 규칙: `출력 형식으로 보장`, `회사 측정`, `독립 확인`, `미검증`을 구분하고 회사가 직접 적은 한계를 함께 기록함
- 성공 기준: 본문의 모든 수치와 강한 표현이 위 표의 주장 ID와 한계로 추적되고, 제브를 직접 썼다는 인상을 주지 않음
- 보존할 원자료: `evidence.md`, `assets/typesafe-jev-homepage-v1.png`, `media.json`

## 결과

| 감사 항목 | 관찰 결과 | 판정 | 본문에서의 처리 |
|---|---|---|---|
| 출력 형식 | Choice·Score·Noul처럼 가능한 값과 구조가 미리 정해짐 | 구조적 보장 | schema 밖의 값을 만들지 않는다는 뜻으로 한정 |
| 속도·비용 | 홈페이지와 발표문에 구체 수치가 있고 평가 페이지가 방법을 공개함 | 회사 측정 | 벤더 수치로 귀속하고 워크플로·지역·비교 조건을 함께 표기 |
| 지능·정확도 | 네 워크플로에서 기준 모델의 평균 확률과 비교함 | 제한적 회사 평가 | 범용 성능이나 독립 벤치마크로 일반화하지 않음 |
| 오답 가능성 | 확률과 confidence를 제공하고 낮은 확신을 사람 검토로 보낼 수 있음 | 오답 가능 | `환각 0%`를 `판단 오류 0%`로 번역하지 않음 |

## 실패와 반례

- 제브 계정과 초기 접근 권한이 없어 API 응답 시간·가격·정확도를 직접 재현하지 못함
- 공식 홈페이지의 `193.6x`, `444.6x`는 모든 업무에 적용되는 범용 배수가 아님
- 정해진 선택지 밖의 값을 내지 않는 모델도 선택지 안에서 틀린 답을 고를 수 있음
- 자유로운 글쓰기, 코드 생성, 긴 추론처럼 문자열 생성이 필요한 일은 제브의 공개 목적과 맞지 않음

## 미해결 항목

- 본문에 사용할 미해결 주장은 없음
- 모델 파라미터 수, 전체 학습 데이터, 공개 표준 벤치마크 성능은 확인 자료가 부족하므로 본문에서 다루지 않음

## 출처 사용 원칙

Instagram 게시물은 주제 발견과 독자 관심사를 파악하는 참고 자료로만 사용합니다. 제품 구조·수치·연구 이력은 TypeSafe 공식 자료와 원 논문으로 확인하며, 벤더 평가를 독립 검증처럼 서술하지 않습니다.
