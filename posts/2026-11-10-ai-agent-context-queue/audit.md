# 작성·검토 기록

## 1차 구조·음성·밀도 점검
- reader-benefit contract: 여러 AI 작업을 혼자 확인하는 개발자에게 재개할 기록과 판단 대기 목록을 권한다. 일반 생산성·건강 조언으로 범위를 넓히지 않음.
- 첫 화면의 구체 상황: 코드 생성 대기 중 다른 작업 시작 -> 여러 질문 -> 중단 지점·다음 행동 기록 -> 원문의 개인 경험 범위.
- 원문 저자의 경험을 사용자의 경험으로 바꾸지 않았다. 가상 로그인 카드의 예시 성격을 표 앞에서 명시.
- 제목·headings는 모두 다로 끝나지 않고, 각 단계의 독자 질문을 맡는다.
- 제목 후보는 brief에 기록. 검색량 데이터는 사용하지 않았고 검색 유입을 보장하지 않음.
- 최근 같은 하위 카테고리 finished 표본: claude-duet-chatgpt-dots(published), ai-pdf-summary-verification(published), higgsfield-ai-video-guide(ready), openclaw-2(ready), xirp-ai-coding-workspace(ready). 대체 표본 필요 없음. 기존 설명형 나열을 복사하지 않고 대기 질문→카드→판단→재개→누적 처리로 구성.
- 소제목 초기 후보 '맥락 관리의 핵심'은 '다시 읽었을 때 이어갈 수 있는 작업 카드'로 구체화. 'AI보다 사람이 병목' 같은 역전·과장 제목은 제외.
- '결론부터 말하면', '이번 글에서는', 'A가 아니라 B', 방어적 보증 문구를 쓰지 않는다.

## 문단별 새 정보와 주장 소유
- 첫 절: AI가 요청하는 사람의 결정 / 원문 Git 기록 설계 / 판단 질문의 구체성.
- 카드 절: 자체 7항목 예시 / 근거 위치 / 갱신 시점 / commit-push 구별 및 보안.
- 판단 절: 대기 항목 선정 / 한 건 읽고 결정 / 반복 실행 중지 규칙.
- 재개 절: 연구의 시간압박 조건 / 재개 계획과 AI 미검증 범위 / 앞의 예시에 연결한 한 줄.
- 마지막 절: 검토량 누적 / WIP 정의 / 동시 작업 수 판단. 종료는 카드의 다음 행동으로 연결.
- 보존한 경계: 원문 주관적 효과, 논문 대상, 가상 예시, 테스트 미확인, 비밀 정보 제한.
- 기계적 균형을 위해 절별 요약·bold 결론을 반복하지 않음. 새 정보 없이 '핵심은 작업 관리입니다'를 덧붙이지 않음.

## 현재 검토 상태
- source independent cold read: pass. 상세는 artifacts/qa-v2/source-review.md 및 source-pass.json.
- generated hero/infographic independent review: 모두 pass. 각 매체의 exact hash에 유효.
- local light/dark preflight: 1280px·360px 실제 전체 화면 검토 완료. 아래 기록 참조.
- author publication approval: 요청되지 않았음. reviewing 유지. Tistory 편집기 접근·업로드·게시 없음.
- Git: 기존 dirty 파일 및 35 behind 상태 보존. 게시 후 커밋·push 지시를 적용해 이번 승인 전 초안은 커밋하지 않는다. 기존 게시물 복구는 별도 담당자가 수행한다.

## 폴리싱 1회
- before/after 분석기를 artifacts/prose-before.txt, prose-after.txt에 보존. 수치를 통과 근거로 쓰지 않음.
- 첫 문단 끝의 같은 독자를 반복한 한 문장을 삭제. 상황과 권고 두 문장만으로 이해 가능.
- 가상 예시 설명의 “실제 결과가 아니라”를 “로그인 오류 수정을 가정해 만든 예시”로 변경해 직접 서술.
- 연구 범위를 “측정한 연구는 아닙니다”에서 “효과는 측정하지 않았습니다”로 구체화.
- 연구의 긴 한 문장을 시간 압박 조건, 주의 잔여 현상, 용어 정의로 나눔. 날짜·링크·연구 범위를 보존.
- 독립 source reviewer가 첫 화면, 연구-실전 연결, 카드의 실용성, 마지막 한 건 제한의 제안 성격을 검토해야 함.

## 글별 표 레이아웃
- 기본 v2 표는 min-width 620px이므로 이 글의 2열 카드 예시에는 assets/post.css로 최소 너비를 해제하고 첫 열을 28%로 지정했다. 원문 변경은 없으며 360px 실제 화면에서 두 열과 줄바꿈을 확인했다. 공통 CSS는 수정하지 않았다.

## 독립 hero 검증: v1 pass
- 검토자: Codex independent reviewer independent source review.
- assets/ai-context-queue-hero-v1.png, 1672×941, SHA-256 d6f25c1ce3fbb47d38692afc1ae1467f895a530aed8ba60a8bbb6814f1d68dda.
- 원본과 독립 360×203 썸네일을 실제로 열어 검사했다. 세 코드 변경 흐름→대기 카드→사람이 선택한 한 장의 관계가 읽히며 +/−와 들여쓰기 단서가 일반 사무 그림과 구분한다. 손·종이·접촉 그림자·판의 물성이 일관적이고 불필요한 문구·가짜 UI·성과 상징이 없다.
- subject-swap pass. 사용자 제공 비교 reference 없음. problem→revision→re-verification: 수정이 필요한 결함 없음, 원본 및 썸네일 모두 pass.
- 배치: context-hero, 도입 뒤 첫 소제목 앞. alt 제안: 여러 코드 변경 흐름을 작업 카드로 모으고 손이 한 장을 파란 검토판으로 옮기는 모습.
- 상세 관찰: artifacts/qa-v2/hero/independent-review-v1.md. 이미지 hash에만 유효하며 infographic·최종 페이지·게시·Git을 승인하지 않는다.

## 독립 infographic 검증: v1 pass
- 검토자: Codex independent reviewer independent source review.
- assets/decision-flow-v1.jpg, 640×944, SHA-256 60a9a2cc25fd15aba1a4f08eb84b757ca631ed0a0e800de8ae3ae6a506538b56. C05 및 승인된 배치/라벨과 대조했다.
- 원본, 기존 creator 360px 페이지 캡처의 312px 표시, 독립 확대 영역 3개를 실제로 읽었다. 6개 라벨·가운데점·두 출력 경로가 정확하며 가림·충돌·잘림이 없다. 독립 픽셀 분석에서 글자 높이 28~33px, 완료 라벨의 최소 테두리 안쪽 여백 17px, record 라벨의 좌우 여백 85px 이상을 확인했다.
- 36px 주요 라벨과 32px record/return 라벨이 312px 폭에서 읽힌다. 제목 면적 0%, 외곽 장식 카드 없음. 흐름·반환·한 건 검토 강조가 먼저 읽혀 framed-poster 판정 통과.
- file:// 검사 페이지를 직접 여는 CUA 요청은 프로토콜 정책으로 실행 전 거절되었다. 재시도·다른 브라우저 우회·viewport 변경 없음. 기존 의도 크기 캡처를 독립 시각 검토했으며 직접 브라우저 캡처 재현으로 기록하지 않는다. 최종 페이지 QA는 별도다.
- problem→revision→re-verification: 최종 raster 수정이 필요한 결함 없음, 원본/의도 크기 캡처/확대 영역/픽셀 측정에서 일치.
- 상세: artifacts/qa-v2/infographic/independent-review-v1.md 및 .json. 이 판정은 exact infographic hash에만 유효하며 article ready/게시/Git 승인이 아니다.

## 로컬 페이지 preflight 및 전달 전 읽기
- light/dark 각각 1280×900, 360×800 CUA Chrome에서 전체 페이지를 실제로 읽었다. 로컬 preflight이며 독립 최종 원격 페이지 승인으로 기록하지 않는다.
- 1280px: 문서 scrollWidth 1280, 표 760px, hero 916px, 흐름도 480px. 360px: 문서 scrollWidth 360, 표와 두 이미지 모두 320px. 모든 이미지 로드 및 실제 캡처 페인트 확인.
- 목차 5개와 타깃, 표 두 열의 모든 내용, 캡션 위치, 제목 줄바꿈, 첫 행동이 대표 이미지 앞에 나오는 순서, light/dark 명암과 중립 그림 배경을 확인했다. 스크린샷은 artifacts/qa-v2/preflight-inspection/에 보존한다.
- 문단 사이 연결과 마지막 한 장의 중단 지점·다음 행동 권고를 렌더된 글에서 다시 읽었다. 새로운 문장 결함을 찾지 않아 source freeze 뒤 본문을 수정하지 않았다.
- 출판 승인·원격 매체·Tistory native attachment·최종 원격 페이지 검증은 아직 진행하지 않았다. reviewing 상태의 검토용 HTML은 이미지 2장을 내장해 별도 파일로 제공한다.
- repo unittest 75개 통과. 새 글 전용 CSS만 추가했고 기존 파일·공통 CSS·Git 브랜치에는 손대지 않았다.

## 구체 예시 개정: AI에게 코딩을 맡겼는데, 왜 더 피곤할까?
- 이전 source/media/preflight 기록은 이전 제목·본문의 이력이다. source 및 페이지 승인은 새 개정에 재사용하지 않는다. 원본과 이전 HTML은 history/before-example-revision에 보존했다.
- 사용자 지적: 제목이 관심을 끌지 못하고 추상적이며 직접적인 사례가 부족하다. 주제를 풀어 쓰는 대신 제목에서 AI에게 코딩을 맡긴 뒤 돌아오는 검토 부담을 묻는다.
- 도입: 로그인·검색 두 작업 -> 각각의 질문 -> 멈춘 지점/결정 기록 -> 재탐색 감소 -> 예시임을 명시. 용어 정의는 첫 절의 실제 파일 사용 설명 뒤에 둔다.
- 기존 카드의 ‘수정 화면, 변경 파일, 테스트 로그의 실제 위치’를 예시 경로와 미실행 상태로 바꾸었다. 막연한 ‘로그인 계속’과 작업 파일을 읽고 결정/검증을 이어가는 지시문을 직접 대비했다.
- 세 질문 -> 같은 로그인 카드 -> 결정 후 재실행 -> 다음 날 재개까지 같은 사례를 유지했다. 연구 요약은 재개 메모 바로 뒤로 압축했다.
- 제목/소제목 원본은 백업에 보존. 새 절 역할은 질문 증가의 원인, 파일 기반 지시 전후, 사람의 검토 순서, 다음 날 첫 행동, 대기 검토량 조절이다.
- 본문의 대화와 수치는 전체 가상 예시라고 명시하고 개인 경험/실측 향상률을 주장하지 않는다. 연구는 AI 도구 효과를 측정하지 않았다는 제한 유지. Git 커밋/push, 비밀 정보, 배포 제한 유지.
- 동일 하위 카테고리 표본을 재확인: claude-duet-chatgpt-dots(published), ai-pdf-summary-verification(published), higgsfield-ai-video-guide(ready), openclaw-2(ready), xirp-ai-coding-workspace(ready). 각 첫 화면의 직접적 사물/행동을 참고하되 같은 제목 틀을 복제하지 않는다.
- 원격 fetch만 수행했고 HEAD는 origin/master보다 37개 뒤다. 다른 담당자의 Git 복구와 충돌하지 않도록 이 작업은 커밋/통합/push하지 않는다.
- 기존 이미지 해시·픽셀 유지. 이번 개정은 글·배치 설명·전용 산출물만 변경한다. 독립 source 검토와 새 로컬 모바일 검토 예정.

## 독립 source 피드백 반영
- 검토자가 결정 후 AI로 돌려보낸 로그인 카드를 다시 답변 대기로 묘사한 시간순 혼동을 지적했다. 해당 문장을 ‘아직 답하지 않은 카드는 같은 수정을 반복하지 않도록 멈춰 둡니다.’로 바꾸어 미결 카드에만 정지 규칙이 적용되도록 했다. 재검토 요청.

## 개정본 로컬 렌더 검토 완료
- 새 source-pass와 blog.py(오류 0/경고 0), v2 번들 검사를 통과했다.
- 360/1280px 각각 light/dark 실제 전체 페이지를 읽고 표·예시 인용·목차·이미지·문단을 확인했다. 문서 가로 넘침 없음. 표 폭 320/760px. 지연 로딩한 흐름도는 해당 절로 이동 후 실제 픽셀을 확인했다.
- 예시 요청과 재개 메모가 일반 본문에 묻혀 글 전용 CSS에 인용 상자와 파란 왼쪽 선을 추가했다. 내용·공통 CSS·이미지 바이트는 변경하지 않았다.
- light360 실제 캡처를 파일에 보존. 나머지 실제 캡처는 도구 기록에 남았으며 저장 제한을 preflight-record.json에 명시했다. 게시용 원격 페이지 승인으로 기록하지 않는다.
- 최종 내장 이미지 HTML을 기존 Space 파일 버전 1로 교체했다. 이전 버전과 원본 글 백업은 보존했다.

## 최종 회귀 검사
- unittest 75개 통과. 전체 96개 글 check 오류 0개/경고 0개.
- 검토용 HTML 재생성 스크립트가 최신 revision-preflight를 읽도록 경로를 갱신했다. 예전 스크립트도 기존 이력 폴더에 보존했다. 생성 HTML 내용은 기존 Space 버전 1과 동일하다.
- 공식 파일 메타데이터 도우미는 시스템 Python 3.9와 호환되지 않아, 이미 설치되어 있는 Python 3.12로 성공 실행했다. 로컬 HTML의 Space ID와 버전 1 메타데이터 보존 완료.

## PDF 검토본
- 같은 HTML에서 읽기용 PDF 5페이지를 추가했다. 전 페이지를 시각 확인하고 58개 본문 블록, 표, 원본 이미지 두 장, 외부 링크 5개와 목차 링크 5개 보존을 확인했다.
- Space에 저장된 PDF를 다시 확인하여 검토본과 페이지 픽셀이 동일함을 검증했다. Mac delivery 폴더로 공식 전송 후 SHA-256과 3,817,499바이트 크기가 일치했다.

## 게시 전 마지막 수정
- 사용자 요청에 따라 결말만 자연스러운 행동 문장으로 바꾸고, 같은 로그인 사례의 전/후를 명시했다. 제목·외부 주장·기존 이미지 의미는 유지했다.
- diagram-design을 검토했으며 새 그림은 추가하지 않는다. 실제로 복사해 쓸 지시문과 파일의 차이를 명시하는 편이 직접적이고, 기존 판단 흐름도는 관계 설명을 담당한다.
- 최신 원격과 로컬 수정이 합쳐진 후보 checkout에서 작업한다. 원본/후보 전환 담당자가 쓰기를 중지했고, 다른 dirty 13개 파일은 보존한다.
- 새 source pass와 사전 light/dark 검토 뒤 사용자 승인으로 Tistory 게시를 진행한다.

## Final connected-Korean read: 게시 요청 반영본
- 새 본문 전체를 도입부터 결말까지 순서대로 다시 읽었다. 문장 내부의 의미와 각 문단 끝-다음 문단 시작을 연결해 확인했으며, 이번 읽기에서 추가 수정이 필요한 접속·지시 대상·문체 결함은 찾지 않았다. 분석기 결과로 이 읽기를 대체하지 않았다.
- 실제 인접 문장: “아까 하던 로그인 오류 계속 고쳐 주세요.” 다음에 “마지막 메시지가 ‘재발급 버튼을 넣을까요?’였다면, 이 요청만으로는 버튼을 넣을지 정해지지 않습니다.”가 온다. 전의 요청에서 빠진 결정 하나를 짚고 후의 카드로 넘어가므로 비교 이유가 바로 보인다. 문구 변경 없이 유지했다.
- 실제 문단 경계: “실제로 파일이 저장됐는지도 확인합니다.” → “다시 시작할 때는 카드를 읽어 보라고 지정하고, 내가 내린 결정을 함께 전달합니다.”는 최초 기록·저장 확인에서 재개로 넘어가는 시간 순서다. 다음 인용문이 파일 경로·결정·검증을 직접 적어 설명을 행동으로 잇는다. 자동 저장을 전제하지 않는 의미도 보존한다.
- 상태 연결: 결정한 로그인 카드를 AI에게 돌려보낸 뒤 “아직 답하지 않은 카드는 같은 수정을 반복하지 않도록 멈춰 둡니다.”라고 범위를 한정한다. 답한 카드와 미결 카드의 상태가 섞이지 않는다.
- 마지막 인접 문장: “지금 답할 질문과 나중에 이어갈 일을 구분해 두는 것.” → “작업을 멈추기 전에, 다음에 무엇부터 하면 되는지 짧게 적어 두세요.”는 원칙에서 당장 할 행동으로 이어진다. 이전의 ‘사람이 돌아올 위치도 함께 남겨 두어야 합니다’라는 비유를 구체적인 기록 행동으로 바꿨고, 새로운 효과나 실측 주장은 추가하지 않았다.
- 독립 검토자의 선행 cold read와 실제 연결 5곳은 artifacts/qa-v2/source-review-publication.md에 보존했다. 본문·근거 변경 없이 source pass 기록을 요청한다.

## 게시 요청 반영본 로컬 preflight
- 새 source pass를 기준으로 1280/360px light/dark 전체 렌더를 읽었다. 전/후 라벨, 요청 상자, 7행 카드와 결말이 자연스럽게 이어지고 문서 가로 넘침은 없다. 표 폭 760/320px. 지연 로드한 흐름도도 스크롤 후 실제 그림을 확인했다.
- 사용자 게시 지시·해당 source pass·매체 해시를 author-publication-approval.json에 기록했다. 승인 시점은 메시지 자체로 입증하고 현재 Asia/Seoul 기록 시각을 별도 명시했다.
- Mac과 클라우드의 공식 IAB 호출 모두 ‘Browser is not available: iab’로 실패했다. 가용성 오류이며 접근 거절이 아니다. Codex 패널 열기는 queued였지만 실제 브라우저 목록에 IAB가 나타나지 않았다. Tistory 연결 플러그인도 찾지 못했다.
- 기존 절차가 요구하는 내장 브라우저를 외부 Chrome으로 바꾸지 않았다. Tistory 편집·첨부·게시와 Git 커밋/push는 아직 실행하지 않았다. reviewing 상태에서 이어갈 수 있도록 publication-blocker.json을 남긴다.

## 최소 도입 절차 전면 개정
- 사용자 질문은 ‘이 글이 무엇을 어떻게 도입하라는지’였다. 이전 원고의 중심이 기록/재개로 치우친 문제를 인정하고 이번에는 판단 요청의 처리 순서를 직접 제안했다. 게시 중지 지시를 유지하고, 이전 승인과 source pass는 이력으로 옮겼다.
- 제목: ‘AI에게 코딩을 맡겼는데, 왜 더 피곤할까?’ → ‘AI 코딩 질문이 쌓일 때, ‘판단 대기함’부터 만드세요’. 질문 누적 상황과 첫 행동을 직접 이름 붙였다. 검색량/검색유입 결과는 측정하지 않았다.
- 기본 권고: 이미 쓰는 같은 로컬 프로젝트에서 AI가 규칙/카드/대기함을 만들게 하고, 사람이 한 건을 결정해 원래 대화로 반환한 뒤 목록을 갱신한다. 자동 감시/재개 기능이나 새 관리 서비스는 약속하지 않는다.
- 전후 축: ‘막연한 지시→상세 메모’에서 ‘도착한 질문마다 전환→한 건 판단·반환 후 다음 질문’으로 바꿨다. 첫 절이 전후와 원문 해석, 이후 절이 설정/작업 시작/취합/반환/성공·실패 확인을 소유한다.
- 기존 카드 표·재개 연구·Kanban 일반론을 걷어내고 네 개의 실제 복사 지시문, 초기 빈 상태, 판단 대기 두 건, 이미 허용된 조사 제외, 반환 뒤 갱신 결과를 넣었다. 원문 Git/script/artifact 구현과 dev.log 수동 제안을 명시적으로 구별했다.
- 1차 독립 구조 검토에서 동일 폴더, 해당 작업 정지, 결정 실제 전달, 갱신 후 제거, 짧은 대기 목록의 필요를 반영했다. 2차 독립 cold read에서 새 질문이 생긴 T01까지 반드시 사라진다고 단정하지 않도록 고쳤다. 같은 코드 파일 충돌은 두 작업의 예상 변경 파일을 먼저 받는 단계로 구체화했다.
- 보존한 범위: 가상 로그인/검색/테스트, 실제 자료 확인, 미실행 테스트, 원문 개인 보고, 권한/폴더 제한, 배포·삭제·권한 변경의 별도 허락, 비밀 정보 제외. Python fixture 검사는 실제 AI CLI/제품 동작 검증으로 쓰지 않았다.
- 동일 하위 카테고리 스타일 표본 재확인: claude-duet-chatgpt-dots(published), ai-pdf-summary-verification(published), higgsfield-ai-video-guide(ready), openclaw-2(ready), xirp-ai-coding-workspace(ready). 제목 틀을 복제하지 않고 이번 글의 도입 행동을 기준으로 선택했다.
- 기존 영문 인용 상자 CSS는 역사적 변경으로 보존한다. 현재 원고는 여러 문단 지시문이 생겼으므로 실제 렌더에서 문단 간격을 확인하며 공통 CSS는 수정하지 않는다.
- 첫 백업 명령이 인코딩 오류로 실행되지 않은 뒤 본문이 저장됐다. 직전 본문을 저장된 이전 원본과 실제 수정 내역에서 복구해 이전 source-pass 내용 SHA-256 65e7e78b…와 완전히 일치함을 확인했다. 마지막 brief 개정은 별도 백업 전에 덮어써졌으며 이전 brief/정확한 HTML/검토 기록은 남아 있다. preservation-note.txt에 한계를 명시했다.

## Final connected-Korean read: 최소 도입 개정본
- 새 본문 전체를 제목부터 결말까지 다시 읽었다. 첫 행동, 준비, 두 작업의 시작, 취합, 결정 반환, 실패 확인이 시간 순서로 연결된다. 매개체인 파일 설명에 결론을 맡기지 않고 한 건을 재개시키는 행동으로 닫았다.
- 실제 경계: “첫 준비가 끝났을 때는 빈 대기함이 정상입니다.” 뒤 “각 작업 대화에 목표를 설명한 뒤 ‘아직 수정하지 말고, 예상 변경 파일을 먼저 알려 주세요’라고 요청합니다.”가 이어진다. 준비 완료에서 실제 작업의 안전한 시작으로 넘어가는 순서다.
- 실제 연결: “질문과 자료를 저장하고 해당 작업을 멈춥니다.” 뒤 “이미 허용한 조사는 계속하고, 권한 부족이나 도구 오류는 ‘막힘’으로 적습니다.”는 판단 때문에 멈출 일과 이미 허용된 조사·도구 오류의 처리를 구별한다. 모든 일을 불필요하게 중단시키지 않는다.
- 수정 전 “T01은 목록에서 빠지고 T02 검색이 남아야 합니다”를 “T01이 ‘작업 중’이라면 방금 답한 버튼 위치 질문은 빠지고 T02 검색이 남습니다”로 바꿨다. 이어 “새 결과 검토를 요청했다면 이전 질문을 반복한 것인지, 새 결과를 확인해 달라는 것인지 구분합니다”를 붙여 재개 뒤 새로운 판단이 생길 수 있음을 보존했다.
- 검색 시작의 한 긴 문장을 ID·경로 지정과 목표 문장으로 나눴다. ‘T02’와 ‘T02-search.md’, 모바일 줄바꿈 조건과 선택 대기 의미는 그대로다.
- 도구 기능의 근거와 실행하지 않은 실서비스 검증을 구분했다. 가상 Python 검사 설명은 독자가 기대할 목록 변화를 확인하는 마지막 절에만 둔다.
- 기존 ‘완제품 설치법은 아닙니다’라는 대비 문장을 ‘아래 파일 구성과 지시문은 dev.log에서 제안하는 최소 도입안입니다’로 바꿔 제안의 주체를 직접 밝혔다.
- 결말은 오늘의 두 작업에 규칙을 붙이고 질문 한 건을 결정·반환하는 행동만 남겼다. 추가 생산성 약속이나 일반 자기계발 결론을 붙이지 않았다. 전체 연결 읽기에서 추가 문장 결함은 찾지 못했으며 독립 source 검토를 요청한다.


## Final authorized publication - 2026-11-10

- The author-approved restored title and final GeekNews opening were published as post 176. Earlier draft/publication-stop statements above describe earlier stages and are superseded by this entry.
- The submitted canonical fragment SHA-256 is fd40631b595a892df4ddbca9c46fbfee6bfcd53a2bd02b67af32860cc04645a8 (31,272 UTF-8 bytes; 22,315 characters). Exact private backup retained.
- Independent source review and the two real CDN GETs passed. The publishing operator checked the complete actual Chrome preview, two images, alt text, captions, and reported light/dark overflow measurements. Desktop preview was limited to 1060px rather than the requested 1280px.
- Automated final-page capture was not performed; final-page.json was not generated and the finalizer failed. No automatic or independent final-page pass is claimed. Publication proceeded with the author-authorized manual browser workflow.
- No post-publication visual inspection was performed. Publication confirmation, measurements, limitations, and original hashes are in artifacts/qa-v2/publication.json.
- Public archival HTML/media copies remove CDN signing parameters and private workspace references. These are historical publication records, not a fresh publication-ready bundle.
