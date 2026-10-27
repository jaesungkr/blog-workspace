# 감사: GPT-6.1 Terra, 화면을 읽고 앱 작업을 돕는 AI

상태: reviewing. 새 로컬 초안만 작성. 기존 글 변경·push·발행 없음.

## 문체 및 근거 점검

- 읽는 순서: 일반 Chat에서 찾을 혼동 → Work 제공 → 화면 정보와 앱 작업 → 비용 단위 → 지원 범위.
- 첫 화면에서 정체/용도/제공 위치를 설명. 내부 검수 과정은 본문에 넣지 않음.
- 모든 제목은 명사/구 형태. 본문은 존대어이며 실사용·작가 경험을 만들어 넣지 않음.
- 원래 요청의 'ChatGPT Terra 6.1'을 공식 'GPT-6.1 Terra'로 수정.
- ‘핵심 메시지’ 템플릿 heading을 실제 제공 위치·이미지 작업·비용·성능 질문으로 교체.
- 첫-party contribution: 작업별 준비조건/완료 확인대상 판단표. 비용 예시는 코드 산술 결과 보존. 모델 성능 테스트 아님.
- 제목 질문 소유권 및 제외: brief.md 참조. 범용 프롬프트 팁과 구독 추천은 삭제 대상에서 제외한 주제임.
- 보존 사실: 2026-10-26 출시, Work/Codex/Chat 제외, API ID, $1/$5 요금, 네이티브 audio/video 미지원.
- 주제 연결 검사: 티스토리 로그인은 computer use 실행 조건을 설명하므로 유지. API 계산은 비용 단위의 의미를 보여 주므로 유지. 전체 benchmark 점수표 제외.
- 폴리싱 표본: 2026-10-26-ai-video-tools-guide (published), 2026-10-25-kimi-k3-1-pro-strengths-vs-opus-5-5 (published), 2026-10-25-gemini-4-argon-vs-gpt-6-astra (published). 같은 하위 카테고리 3개; 대체 없음.
- 문단 연결: 명칭→제공 화면, 사진 대조→실행 조건, API 비용→구독 한도, 벤치마크 범위→입출력 한계로 이어짐.
- 폴리싱 전후 analyzer 기록은 artifacts/prose-before.txt 및 prose-after.txt. 신호 수를 품질 점수로 삼지 않음.
- 보조 infographic: not_applicable. max-txt2img와 diagram-design을 검토했으나 3행 판단표 이상의 새 정보를 주지 않음.

## 아직 남은 게이트

독립 source pass, 생성 hero/독립 이미지 검수, 로컬 light/dark 1280/360 inspection, 사용자 승인, 네이티브 Tistory 이미지와 remote QA 순서. 후반 게시 게이트는 이번 로컬 초안 범위 밖이며 완료로 기록하지 않음.

## 독립 검수 반영 2차

- 성능 순위/실측 결과와의 수사적 대비를 조건 판단표/계산 예시의 직접 설명으로 수정. 실제 청구 미측정 경계는 보존.
- 비용 heading에 API와 ChatGPT 명시, 마지막 heading에 미지원 입출력 포함.
- 마지막 문단이 조건표의 내용을 재진술해 삭제. 공식 입출력 제한으로 본문 종료.
- 불명확한 통칭의 일반 사용을 입증할 수 없어 삭제하고 공식 명칭부터 설명.

## 로컬 QA 결과

- 독립 source review 2차 pass 및 source-pass.json 기록 완료.
- 기본 blog 검사 오류 0/경고 0. v2 checker는 미검증 이미지 상태 경고만 있었으며 이후 독립 이미지 게이트 결과로 갱신 예정.
- light/dark canonical preflight HTML 생성 완료. 구조 검사: 각각 H1 1개, 중복 ID 0, 깨진 목차 anchor 0, 이미지 alt 있음. fragment H1 0개.
- Playwright Chromium file:// 접근은 ERR_BLOCKED_BY_ADMINISTRATOR로 거부됨. 1280/360 화면 캡처와 실제 시각 QA는 수행되지 않았음. 우회하지 않음.
- preview 파일은 전달용으로 이미지 data URI를 포함한 portable 사본도 생성. 이는 게시용 HTML이 아님.
- 원본 fragment에는 아직 native image placeholder가 있음. DRAFT 명칭으로 전달하며 exact publish-ready TXT/finalizer는 실행하지 않음.
- 부모 보고: Tistory 로그인 완료. 이 실행 환경에서 로그인 검사한 것으로 기록하지 않음.
- 사용자 승인, native 첨부, remote byte 검증, final page QA, 실제 Tistory preview, 게시 및 URL 확인은 미실행.

## 독립 이미지 검수 완료

- /root/hero_review가 원본 전체와 360px 썸네일을 열람, pass. assets/terra-visual-action-v1.png, 1672×941, SHA-256 5f333fe06baae60341e52b280111cdd822a6f09248dd876173a49509be65c048.
- 도면과 입체 모형 경계의 녹색 커서가 시각 정보→동작이라는 주제 단서를 제공. 특정 UI/실행 성공 증거로 사용하지 않음.
- 상세 경과: artifacts/qa-v2/hero-review.md. 검수 agent는 중단 알림을 받기 전 file URL 거부 후 data URL로 썸네일을 표시했음을 보고함. 이후 브라우저 작업 중단. 전체 페이지 검수는 여전히 미완료.
- 최종 v2 checker pass, blog check 오류 0/경고 0. check-result.txt 보존.
