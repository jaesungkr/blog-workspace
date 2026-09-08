# 근거 지도: Github vs. Cursor Origin, 코드 저장소 비교

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Origin은 Cursor가 코드를 저장·공유하기 위해 만든 git forge이며 표준 Git clone·push·pull, 코드 탐색·검색, PR 열기·검토·병합을 지원함 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin | 2026-09-08 early beta 범위이며 기능이 바뀔 수 있음 |
| C02 | Origin 코드 저장소는 Pro, Teams, Enterprise에서 제공되고 Free에는 없으며 접근은 순차적으로 열림 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin | 유료 플랜 사용자도 즉시 보이지 않을 수 있으며 가격 총액은 비교하지 않음 |
| C03 | Origin 저장소는 Internal 또는 Private로 만들 수 있고 팀의 codebase 권한을 따름 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/create-repository | 현재 문서에 명시된 공개 범위이며 Public 저장소 지원 여부를 추정하지 않음 |
| C04 | GitHub 미러에는 Git 이력·브랜치·태그·코드 탐색·검색·양방향 PR·지속 업데이트가 포함됨 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/mirror-github | 동기화 지연과 GitHub App 접근 권한의 영향을 받을 수 있음 |
| C05 | GitHub 미러에는 GitHub Issues, Actions 워크플로와 비밀값이 포함되지 않으며 GitHub가 원본으로 남음 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/mirror-github | Origin 밖의 다른 이전 도구나 향후 기능까지 부정하는 주장이 아님 |
| C06 | 미러 저장소에 Origin remote로 push하면 GitHub로 전달되며 Origin에서 다룬 PR도 GitHub와 동기화됨 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/mirror-github | GitHub가 원본인 미러에 한함. Detach 뒤에는 Origin이 원본이 됨 |
| C07 | Origin은 Cursor Automations와 cloud agents를 저장소의 push·PR 이벤트에 연결할 수 있음 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/integrations | 자동화 성능·품질·비용을 직접 시험하지 않음 |
| C08 | Origin의 현재 문서화된 외부 앱은 Vercel, Depot, Buildkite이며 미러 저장소의 CI는 GitHub에 남음 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/settings | early beta의 현재 목록이며 이후 확대될 수 있음 |
| C09 | GitHub 저장소는 PR 외에 Issues, Discussions, Projects로 업무와 커뮤니티를 관리함 | 공식 제품 문서 | 확인 | https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories, https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects | 조직별 실제 사용 범위는 다름 |
| C10 | GitHub는 Actions, Packages, Pages와 코드·비밀값·의존성 보안 기능을 별도 제품 영역으로 제공함 | 공식 제품 문서 | 확인 | https://docs.github.com/en/actions/reference, https://docs.github.com/en/packages, https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages, https://docs.github.com/en/code-security/getting-started/quickstart-for-securing-your-repository | 일부 기능은 요금제와 저장소 공개 범위에 따라 이용 조건이 다름 |
| C11 | GitHub에도 Copilot cloud agent와 Claude·Codex 같은 타사 coding agent를 Issue·PR 흐름에 연결하는 기능이 있음 | 공식 제품 문서 | 확인 | https://github.com/features/copilot/agents, https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents | GitHub의 agent 기능도 플랜·미리보기 상태·AI Credits 등의 조건이 있음 |
| C12 | GitHub Free는 공개 저장소와 비공개 저장소를 제공하고, 공개 저장소와 조직 협업의 진입점으로 쓸 수 있음 | 공식 제품 문서 | 확인 | https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories | 비공개 저장소의 고급 기능과 엔터프라이즈 기능은 별도 플랜이 필요할 수 있음 |
| C13 | 기존 프로젝트는 GitHub 미러로 시험하고, 새 비공개 프로젝트에서 Cursor agent 중심 흐름이 필요할 때 Origin 단독 호스팅을 검토한다는 선택표 | Codex 분석 | 확인 | C01~C12를 `원본 위치`, `옮겨지는 데이터`, `필요한 플랫폼 기능`, `에이전트 작업 중심성`으로 재분류 | 성능 벤치마크나 보편적 우위가 아니라 2026-09-08 공개 기능 기준의 도입 순서임 |
| C14 | 사용자 제공 Instagram 게시물은 Origin을 `Cursor가 만든 자체 코드 호스팅`으로 소개하고 GitHub 미러·순차 공개를 강조함 | 사용자 제공 보조 자료 | 확인 | https://www.instagram.com/p/DdAinVJk37q/ | 2차 해설이며 `협업은 GitHub, 에이전트는 Origin` 같은 권고는 공식 기능의 범위와 정확히 일치하지 않아 본문 근거로 사용하지 않음 |
| C15 | Origin API는 초기 베타이며 변경될 수 있음 | 공식 제품 문서 | 확인 | https://cursor.com/docs/api/origin | API의 향후 호환성이나 변경 주기를 예측하지 않음 |
| C16 | Cursor Automations는 일정과 소스 제어 이벤트로 실행되며 연결된 GitHub·GitLab 저장소도 대상으로 삼을 수 있음 | 공식 제품 문서 | 확인 | https://cursor.com/docs/origin/integrations | 2026-09-09 재확인. Origin 도입이 Cursor 자동화의 필수 조건이라는 오해를 막기 위해 본문에 명시함 |

## 2026-09-09 개정 재확인

Codex가 Origin 개요·미러·통합 문서와 GitHub 타사 에이전트 문서를 다시 열어 기존 핵심 주장과 이용 조건을 확인했습니다. 비교 기준일은 기존의 2026-09-08을 유지하고, 새로 명시한 C16은 2026-09-09 재확인한 동일 공식 통합 문서에 연결했습니다. Detach 뒤 기존 GitHub 저장소가 영향을 받지 않는다는 내용과 `Settings → General`의 동기화 상태 확인 위치도 미러 문서에서 대조했습니다. 새 성능·가격·실사용 주장은 추가하지 않았습니다.

## 분석 설계

- 질문: Cursor Origin은 GitHub를 대체하는가, 아니면 GitHub 저장소 위에 Cursor 에이전트 작업면을 더하는가?
- 실행 주체: Codex
- 확인 시점: 2026-09-08 KST
- 입력: Cursor 공식 랜딩·문서 7종, GitHub 공식 제품 페이지·문서 8종, 사용자 제공 Instagram 게시물 1종
- 표현: 기능을 `Git 저장소`, `PR`, `계획·커뮤니티`, `CI·배포`, `보안·배포 자산`, `AI 에이전트`, `공개 범위`, `접근 조건`으로 분류
- 비교·판정 규칙: 공식 문서에 현재 명시된 기능만 `지원`으로 표시하고, Origin 문서에 없는 GitHub 영역은 `현재 문서에 확인되지 않음`으로 구분함. `없음`으로 단정하지 않음
- 성공 기준: 독자가 자신의 프로젝트를 `GitHub 유지`, `GitHub 원본+Origin 미러`, `Origin 단독 호스팅` 가운데 하나에 배치할 수 있음
- 보존할 원자료: `artifacts/origin-github-feature-matrix.csv`, 이 파일의 URL·확인일·한계

## 분석 결과

| 분석 ID | 조건 | 권장 시작 | 근거 | 해석 범위 |
|---|---|---|---|---|
| A01 | 이미 GitHub에서 Issue·Actions·보안·공개 기여 흐름을 사용함 | GitHub 유지 또는 Origin 미러 | C04~C06, C09~C12 | Origin 미러가 GitHub 플랫폼 메타데이터 전체를 옮기지 않음 |
| A02 | 기존 GitHub 저장소에 Cursor cloud agent와 Origin 코드 탐색만 먼저 붙이고 싶음 | GitHub 원본+Origin 미러 | C04~C08 | GitHub admin 권한과 Cursor GitHub App 연결 필요 |
| A03 | 새 비공개 프로젝트이며 Cursor agent가 저장소 생성부터 PR까지 맡는 흐름이 중심임 | Origin 단독 호스팅 시험 | C01, C03, C07 | early beta와 제한된 외부 앱 범위를 감수해야 함 |
| A04 | 공개 오픈소스, 채용 포트폴리오, 외부 기여자가 중요함 | GitHub 유지 | C09, C12 | 발견 가능성을 정량 측정한 결과가 아니라 공개 저장소·커뮤니티 기능의 문서화 범위에 따른 판단 |
| A05 | AI 에이전트가 필요하다는 이유 하나만 있음 | 두 플랫폼의 agent 기능을 따로 비교 | C07, C11 | Origin만 agent를 지원한다는 이분법을 피함 |

## 실패와 반례

- Origin은 `GitHub 대체품`이라는 한 문장으로 설명하기에는 GitHub 미러 경로를 공식 지원합니다. 기존 저장소에서는 두 서비스를 함께 쓰는 구성이 제품 설계에 포함됩니다.
- GitHub도 coding agent와 타사 agent를 지원하므로 `GitHub는 사람용, Origin은 agent용`이라는 구분은 정확하지 않습니다. 차이는 agent의 존재보다 어느 플랫폼이 원본 저장소와 제어면을 맡느냐에 있습니다.
- Origin 문서에 Issues·Packages·Pages가 보이지 않는다고 해서 앞으로도 없다고 단정할 수 없습니다. 글은 early beta의 현재 공개 문서 범위만 비교합니다.
- 공개 기능표로 성능, 장애 내성, 보안 인증, 데이터 이전 비용을 판단할 수 없습니다. 해당 항목은 본문 추천 범위에서 제외합니다.

## 미해결 항목

- 계정별 Origin 접근 시점과 실제 화면 배치는 순차 공개라 확인하지 않음.
- Origin의 대규모 monorepo 검색 속도, PR 동기화 지연, agent 성공률은 직접 시험하지 않음.
- Cursor 및 GitHub의 플랜별 총비용은 사용량과 조직 계약에 따라 달라 본문에서 비교하지 않음.
