# 근거 지도: GitHub 장애 대응, 코드 밖의 리뷰·빌드·배포까지 점검하는 법

## 주장별 상태

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | 2026-08-17 GitHub.com 장애는 13:28~21:15 UTC, 7시간 47분 이어졌고 Issues·PR·API·Actions·Copilot 등에 오류와 지연이 발생함 | 공식 장애 보고 | 확인 | https://www.githubstatus.com/incidents/zkxwbgr0cnmx | 서비스별 영향 시간은 달랐으며 모든 사용자 요청이 실패한 것은 아님 |
| C02 | 장애 정점의 웹/API 오류율은 약 20%, 아카이브·Raw 콘텐츠 다운로드 오류율은 약 50%였음 | 공식 장애 보고 | 확인 | https://www.githubstatus.com/incidents/zkxwbgr0cnmx | GitHub가 보고한 근삿값이며 지역·기능별 체감과 다를 수 있음 |
| C03 | Git 같은 분산 버전 관리 시스템의 clone은 저장소 전체와 이력을 미러링하며 여러 remote를 둘 수 있음 | 공식 기술 문서 | 확인 | https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control.html | LFS 객체, GitHub Issue·PR 같은 플랫폼 메타데이터는 Git 이력에 자동 포함되지 않음 |
| C04 | Pull Request는 변경 diff뿐 아니라 설명·댓글·review·checks·activity timeline과 병합 조건을 묶음 | 공식 제품 문서 | 확인 | https://docs.github.com/en/pull-requests/get-started/about-pull-requests | GitHub의 현재 데이터 모델 설명이며 다른 forge의 보존 범위는 별도 확인 필요 |
| C05 | Issues와 Projects는 아이디어·버그·업무·책임·상태·의존 관계를 추적함 | 공식 제품 문서 | 확인 | https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues | 조직별 사용 방식과 필드 구성은 다름 |
| C06 | GitHub Actions workflow는 저장소 이벤트가 workflow를 시작하고 job을 runner에 배정하는 구조이며 YAML은 저장소의 `.github/workflows`에 있음 | 공식 제품 문서 | 확인 | https://docs.github.com/en/actions/get-started/understand-github-actions | 자체 runner가 GitHub 전체 장애에서 반드시 멈춘다는 직접 보장은 아님. 이벤트·workflow orchestration이 GitHub에 남는다는 구조적 추론만 사용 |
| C07 | GitHub Release는 Git tag를 기반으로 하지만 release notes와 binary assets를 별도로 묶어 배포함 | 공식 제품 문서 | 확인 | https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases | tag 자체와 GitHub Release 객체의 복구 범위를 구분해야 함 |
| C08 | GitHub 마이그레이션 문서는 `source`, `source+history`, `source+history+metadata`를 구분하며 metadata에는 Issues·PR·settings가 포함됨 | 공식 제품 문서 | 확인 | https://docs.github.com/en/migrations/overview/planning-your-migration-to-github | GitHub로 들어오는 마이그레이션 문서이므로 GitHub 밖으로 나가는 모든 경로의 충실도를 보장하지 않음 |
| C09 | 네 층의 의존성 점검표와 긴급 릴리스 우선순위는 공식 기능을 운영 산출물 기준으로 재구성한 dev.log의 판단 프레임임 | Codex 분석 | 확인 | C03~C08의 기능 경계와 복구 가능성을 비교 | 실제 조직의 RTO·규제·비용을 측정한 벤치마크나 보편적 순위가 아님 |
| C10 | GitHub를 유지하면서 mirror, 저장소 안의 ADR/runbook, 재현 가능한 release command를 두는 부분 분리가 가능함 | 공식 문서+운영 판단 | 확인 | https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository, C03~C09 | mirror가 있다는 사실만으로 복구 성공을 보장하지 않으며 실제 restore drill이 필요함 |

## 분석 설계

- 질문: GitHub가 약 8시간 멈췄을 때 코드 미러만으로 어떤 업무가 복구되고, 무엇은 별도 대체 경로가 필요한가?
- 실행 주체: Codex
- 확인 시점: 2026-08-21 KST
- 입력: 공식 GitHub Status 장애 보고서, Git·GitHub 공식 문서, 사용자 제공 GeekNews 글
- 표현: 업무 산출물을 `코드와 Git 이력`, `협업 기록`, `자동화와 릴리스`, `입구와 정체성` 네 층으로 분류
- 비교·판정 규칙: Git 저장소 clone/mirror만으로 원상 복구 가능한지, 장애 중 계속되어야 하는지, 대체 경로를 저장소 안에서 재현할 수 있는지
- 성공 기준: 독자가 자기 팀의 한 업무를 네 층에 배치하고 첫 분리 대상을 고를 수 있음
- 표본 크기: 공식 장애 1건과 기능·마이그레이션 문서 7종. 빈도나 전체 가용성을 평가하지 않음
- 보존할 원자료: 이 파일의 URL·확인 시점·한계

## 분석 결과

| 분석 ID | 조건 | 판단 | 근거 | 해석 범위 |
|---|---|---|---|---|
| A01 | Git 저장소 clone/mirror 존재 | 코드와 일반 Git 이력은 다른 remote로 복원 가능 | C03, C10 | LFS와 플랫폼 메타데이터는 별도 확인 |
| A02 | 결정 근거가 PR·Issue 댓글에만 존재 | 코드 사본만으로 논의·승인·상호 링크가 복원되지 않음 | C04, C05, C08 | export/import 도구의 충실도에 따라 일부 이동 가능 |
| A03 | 빌드·배포가 GitHub Actions에만 존재 | workflow YAML은 남지만 trigger·job orchestration의 가용성은 GitHub에 의존 | C01, C06 | 조직별 외부 CI·수동 경로 유무에 따라 영향이 달라짐 |
| A04 | release note·binary asset가 GitHub Release에만 존재 | tag는 Git에 남아도 배포 자산과 설명은 별도 보존 대상 | C07 | 패키지 저장소나 외부 artifact registry를 쓰면 위험이 낮아짐 |

## 실패와 반례

- 모든 GitHub 기능을 외부로 복제하면 운영 복잡도와 보안 책임이 커져 장애 비용보다 비쌀 수 있음.
- 자체 호스팅 runner는 실행 자원 통제에는 도움이 되지만 GitHub 이벤트·workflow orchestration까지 독립시킨다는 근거는 없음.
- 공개 오픈소스는 GitHub 계정, URL, Star와 익숙한 기여 절차의 네트워크 효과를 잃을 수 있어 단순 기능표만으로 전면 이전을 결정하면 안 됨.
- 한 번의 7시간 47분 장애만으로 GitHub 전체 가용성이나 대안 서비스의 우위를 일반화하지 않음.

## 미해결 항목

- 없음. GitHub Actions 실행량 증가나 장애의 장기 추세처럼 본문 결론에 필요하지 않은 불안정한 주장은 제외함.

## 출처 메모

- 사용자 제공 GeekNews 글은 문제 범위와 질문을 찾는 출발점으로 사용함: https://news.hada.io/article/github-is-not-just-git
- 공개 본문에서는 `해당 글에 따르면` 같은 2차 출처 의존 문장을 쓰지 않고, 수치와 기능 경계는 공식 원문에 직접 연결함.
- 공식 장애 보고서의 원인 세부사항은 이 글의 운영 결론에 필요하지 않아 본문에서 확장하지 않음.
