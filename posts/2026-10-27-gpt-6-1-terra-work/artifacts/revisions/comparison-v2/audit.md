# 감사: GPT-6.1 Terra vs Claude Opus 5.5, 성능과 가격으로 본 선택

- revision: comparison-v2. 사용자 피드백에 따라 단독 소개→모델 비교 구조 재작성. intro-v1 원문/게이트/전달본 보존.
- 실제 읽은 동일 카테고리 표본: 2026-10-25-kimi-k3-1-pro-strengths-vs-opus-5-5 (published), 2026-10-25-gemini-4-argon-vs-gpt-6-astra (published), 2026-09-02-fable-5-1-vs-fable-5 (published). 또한 ai-video-tools-guide 읽음.
- 공통 구성 추출: 독자 선택 질문→모델 장점→정의/조건 설명→비교표→비용예시→작업 선택/해석 결론→참고자료. 기사마다 있는 후기/독립 평가를 근거 없이 이식하지 않음.
- 최초 소개글의 티스토리 절차표 삭제. 대신 모델별 역할, 평가 관계, 단가, 작업별 선택 표로 개편.
- invariant: 공식 모델명, API 사양/단가, vendor 평가 귀속, OSWorld 버전 비동등, 직접 테스트 없음.
- closing의 ‘강점은 ~에 있지 않습니다’ 대비를 삭제해 직접 진술로 수정.
- heading strip: 대상→공식 평가→독립 평가→초기 후기→가격→선택. 모든 heading ~다 아님.
- 표는 각각 공식 평가/독립 종합 지수/가격/선택으로 기능 구분. 추론설정 비교와 같은 처리량 가정 보존.
- 현재 사용자 전환 의사/경험을 발명하지 않음. 기존 Gemini 글의 1인칭 결론을 복사하지 않음.
- infographic not_applicable: max-txt2img/diagram-design 검토 후 정확한 비교표와 중복해 제외.
- 독립 source/새 hero 검수 대기. 기존 source pass는 새 원고에 사용하지 않음.
- 전체 반응형 QA: 앞서 file:// 관리자 정책 거부로 미완료. 추가 브라우저 재시도/우회 없음.
- Library는 사용자용 원고/이미지/light/dark HTML만 같은 ID로 완성 후 교체. 내부 보고서/ZIP 전송 금지.

## 비교대상 재검토 완료

- 추가 부모 자료로 2026-09-30-gpt-6-1-sol-vs-opus-5-5 원문 및 공개 URL 열람. 같은회사3모델 제한을 풀고 경쟁 모델 검토.
- 공식 Terra 발표의 Opus 비교와 AA 직접측정, Reddit 원문2건 확보. 주 비교를 Terra vs Opus로 변경, Sol/Astra 보조.
- 원고 전체를 새 질문 ‘기존 모델을 바꿀 이유가 있는가’로 재작성. 공통 사양 장황한 절 삭제; 공식/독립/후기/단가 구분.
- 직접 경험 발명 없음. Reddit 정량 시간·quota를 순위표에 넣지 않음. AA fallback 및 effort조건 표 앞뒤 표기.
- 단가4배와 AA 과제비용 차이를 혼합하지 않음. fixed-token4회 손익 예시는 반복 비용 설명에만 사용.
- 제목/heading plain identity and comparison. 도입은 조건부 결론, 결론은 유지/분담과 concrete 누락·오입력 조건.

## 최종 폴리싱
- effort/fallback/가중평균 비용 용어를 결과표 앞에서 설명하도록 이동. 반복된 방어 평가 문장 삭제.
- 마지막 절은 선택표와 실제 판단 조건(누락·오입력·총비용)에 집중. 모든 날짜/수치/설정/초기후기 귀속 보존.

## 수정본 이미지·구조 검사

- 새 hero: assets/terra-opus-comparison-v2.png,1672×941,SHA256 47b71d0bf93f308a080251f021539f2feda0cb735e0449dc81844d7ac5f2c8bb.
- 독립 /root/hero_review: 원본 view_image 확인, 이름/동등비중/증거무결성 검토. 원본에서 즉시 수정할 결함 없음. 썸네일 실제 표시 미완료라 conditional/not fully validated, media captured 유지.
- 이번 수정에서 브라우저 접근 일절 재시도하지 않음. 이전 정책 제한 우회 없음.
- light/dark HTML 생성, 각각 H1 1개/표4개/이미지1개/alt확인/목차중복0/깨진anchor0. 실제 1280/360 시각 검수 아님.
- 단일파일 전달용 HTML에 새 PNG data URI 포함. 이는 전달용 파일 작성이며 브라우저 표시나 제한 우회 아님.
- 사용자용 파일만 /workspace/terra-user-review에 정리. 기존 파일 history는 /workspace/terra-user-review-intro-v1에 보존. Library 같은 ID 교체 예정, 내부자료 제외.

## 최종 수정본 전달

- /root/source_review 독립 source pass 기록 완료.
- 사용자용 원고·새PNG·light/dark HTML 4개를 기존 Library ID로 직접 replace 성공, 모두 current_version_number1. 파일 bytes 유지, metadata helper 성공.
- 원고 libfile_d11d2cfa778c81918cac992d181d085f; 이미지 libfile_8f50f36b79148191a18a9ee063dd83e0; light libfile_f451120d175881919dc06391a22db6c6; dark libfile_eadf0d40d9e48191839ec10a9483d37d.
- 이전 Library 버전0 보존. 내부 보고서·ZIP 미전송. 공개/푸시 없음.
