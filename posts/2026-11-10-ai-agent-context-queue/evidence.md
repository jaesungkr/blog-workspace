# 근거 지도: AI 코딩 질문이 쌓일 때, ‘판단 대기함’부터 만드세요

확인일: 2026-11-10. 이번 개정은 기록 권장에서 판단 요청의 제출·취합·결정·반환 절차로 중심을 바꾼다.

| ID | 주장과 성격 | 근거 | 한계 |
|---|---|---|---|
| C01 | 원문은 sequencing/context 문제, owner inbox, 한 건의 맥락 읽기·결정·큐 반환을 설명한다. | https://sergeykuhne.com/blog/fighting-ai-brain-fry , 2026-11-08 원문을 공개 HTTP GET으로 직접 읽음. ‘Then comes the part that matters most’ 이후 단락 | 저자 개인 실험이며 공개 제품의 설치 문서가 아님 |
| C02 | 원문 저자는 여전히 피곤하나 산만함/길을 잃는 느낌이 줄었다고 보고한다. | 같은 원문 ‘It is still exhausting’ 단락 | 정량 생산성·의학적 피로 감소를 측정하지 않음 |
| C03 | Codex CLI는 로컬 프로젝트 파일을 읽고 편집하며 명령을 실행한다. | https://learn.chatgpt.com/docs/codex/cli , https://learn.chatgpt.com/docs/sandboxing , https://learn.chatgpt.com/docs/permissions | 현재 작업 폴더·파일 권한에 의존. 읽기 권한과 쓰기 권한 구별 |
| C04 | Claude Code는 파일 읽기·생성·편집 도구와 작업 디렉터리/권한 모드를 사용한다. | https://code.claude.com/docs/en/how-claude-code-works , https://code.claude.com/docs/en/permissions , https://code.claude.com/docs/en/memory | 일반 README의 자동 로딩이나 세션 간 자동 공유를 가정하지 않음 |
| C05 | 같은 프로젝트에서 작업 카드별 질문 등록과 대기, 요청 시 판단 대기함 갱신, 한 건 결정 후 원래 작업 대화 반환·목록 재갱신 | article.md의 초기 설정/작업 시작/목록 갱신/결정 반환 지시문. 가상 로그인·검색·테스트 사례. artifacts/adoption-demo의 fixture·snapshot·검증 | dev.log 최소 도입 제안. 자동화된 원문 도구를 복제하거나 실제 AI CLI 실행을 검증한 것이 아님 |
| C06 | 가상 카드의 판단 대기 필터와 결정 반환 후 목록 변화 | artifacts/adoption-demo/results.json, verification.log, test_queue_demo.py, queue_demo.py | Python 규칙의 일관성만 검사. 실제 대화 전달·동시 파일 접근·제품 코드 테스트·인지 효과 미검증 |

## 실제 확인과 재현
- 검증 담당 Codex가 공식 문서를 웹 도구로 열어 기능·작업 폴더·권한 범위를 확인했다. 상세 source-check.md에 진입 URL 및 현재 문서 URL 보존.
- 원문은 웹 도구 오류 후 일반 공개 HTTP 읽기로 200 응답을 얻어 본문 전체를 확인했다. 인증이나 계정 조작을 하지 않았다.
- fixture: T01 로그인 버튼 위치 판단, T02 검색 배치 판단, T03 이미 허용된 테스트 원인 조사. 모두 가상 사례이며 실제 화면/테스트 성공으로 쓰지 않는다.
- 기대 결과: T01/T02만 대기함에 포함. T01 결정이 정확한 원래 대화에 전달돼 카드가 작업 중이 되고 새 질문이 없다는 가정 뒤에는 T02만 남는다. 새 결과 검토가 생기면 T01도 다시 판단 대기가 될 수 있다.
- 미전달 결정, 잘못된 반환 대상, 바뀐 질문, 오래된 결정은 검증용 코드에서 거절한다. 실제 대화 도구가 이 검증 코드를 실행하는 것은 아니다.
- 원문 카드/보드의 Git 기록은 사실로 설명하되, 제안한 수동 시작안에 Git 자동 커밋이나 push를 포함하지 않는다.

## 보존한 운영 경계
- 같은 실제 로컬 폴더를 읽고 쓰는 세션만 대상이다. 별도 worktree/클라우드 파일이 자동 공유되지 않는다.
- 예상 변경 파일을 먼저 확인하고 공통 파일이 겹치는 작업은 순서대로 진행한다. 카드별 단일 작성자, inbox는 검토 대화 하나만 작성한다.
- 판단 대기와 권한·도구 문제의 막힘을 분리한다. 긴급 운영 문제는 묶음 검토까지 미루지 않는다.
- 사람의 답을 카드에 적는 것만으로 다른 세션이 자동 재개하지 않는다. 원래 대화로 실제 전달하고 상태를 확인한 후 목록을 다시 갱신한다.
- 기존 재개 연구/Kanban 설명은 이번 중심 질문을 직접 해결하지 않아 본문에서 제외했다. 이전 근거와 source 기록은 history/before-adoption-rewrite 및 before-publication-revision에 보존했다.
