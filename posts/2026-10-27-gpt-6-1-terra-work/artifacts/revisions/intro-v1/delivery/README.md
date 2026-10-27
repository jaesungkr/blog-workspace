# GPT-6.1 Terra 검토용 초안 인계

제목: GPT-6.1 Terra, 화면을 읽고 앱 작업을 돕는 AI
현재 상태: reviewing (검토용 초안, 게시 불가)

- article.md: 원고와 메타데이터 (상위 디렉터리)
- gpt-6-1-terra-work-preview-light.html / preview-dark.html: 이미지가 포함된 단일 파일 미리보기. 다운로드해 허용된 브라우저 환경에서 열 수 있음. 공개 배포 아님.
- gpt-6-1-terra-work-tistory-fragment-DRAFT.txt: 본문 HTML 초안. 이미지 위치에 __TISTORY_MEDIA_TERRA_LEAD__가 남아 있어 그대로 게시하면 안 됨.
- assets/terra-visual-action-v1.png: 이미지 원본 (상위 디렉터리)
- artifacts/qa-v2: 독립 원고·이미지 검수, 구조 검사, 차단 기록.

## 재개 순서

1. 지원되는 브라우저 환경에서 로컬 미리보기 전체를 1280px/360px, light/dark로 검사. 현재 환경은 file URL 접근이 ERR_BLOCKED_BY_ADMINISTRATOR로 거부됨. 우회/재시도하지 않았음.
2. 검토할 원고·이미지를 사용자에게 제시하고 해당 후보의 게시 승인을 받기.
3. 이미 로그인된 부모의 티스토리 브라우저에서 검증 이미지 첨부 후 편집기 생성 native attachment block을 확보. 이를 media.json에 bind하고 observed URL bytes 검증.
4. 저장소 v2 prepare_final_qa / independent final page / exact native Tistory preview를 완료. 현재는 이 게이트들이 미완료임.
5. 최종 fragment.txt를 생성하고 byte-identical HTML을 게시. 발행 성공/URL 확인 뒤 후속 화면 점검은 작성자가 수행.

현재 사용자 제한: 공개 발행 및 저장소 push 금지. 기존 글 변경 없음. 이번 작업에서 commit/push하지 않았음.

공식 근거 확인일: 2026-10-27 UTC. API release date 2026-10-26. Work/Codex 제공, 일반 Chat 미제공. 공식 발표와 문서에 귀속했으며 직접 모델 성능 테스트/한국어 비교는 수행하지 않음.
