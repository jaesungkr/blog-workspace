# 감사 기록: GitHub 장애 대응, 코드 밖의 리뷰·빌드·배포까지 점검하는 법

## 경로와 수명주기

- 형식: `rich-post-v2`
- 경로: `standard-rich`
- 현재 상태: `ready`
- source freeze: `Codex /root/source_review` 재검토 PASS와 새 record 완료
- 최종 페이지 검토: 두 Tistory CDN URL을 결합한 canonical candidate를 `Codex /root/source_review`가 독립 검토해 PASS
- 라우팅 제외: direct capture, GIF, generated lead, infographic, complex layout, 390px, 768px, second remote fetch
- 제외 근거: 출처 기반 운영 설명이며 사용자 제공 GitHub 홈페이지 화면, 공식 Actions 다이어그램과 모바일 표로 충분합니다.

## 독자 계약과 설명 경계

- 독자가 겪는 상황: 로컬 코드는 남아 있지만 PR 검토, 자동 빌드와 배포가 함께 멈춥니다.
- 한 명의 독자: 장애 복구 범위를 아직 정리하지 않은 개발자 또는 작은 팀의 실무자
- 독자가 아는 것: 기본 Git 명령과 Pull Request
- 독자가 모르는 것: Git clone에 GitHub의 협업 메타데이터와 릴리스 자산이 포함되지 않는다는 점
- 독자가 기억할 판단: GitHub가 8시간 멈춰도 계속되어야 할 업무 하나를 고른 뒤, 코드·협업 기록·자동화·프로젝트 입구 중 해당 층부터 분리합니다.
- 제외한 내용: 대안 forge 전체 비교, 실제 이전 절차, 장애 장기 추세, AI 트래픽 원인론

## 근거와 구조 검토

- [x] 공식 GitHub Status에서 2026-08-17 장애 시간 7시간 47분과 영향 서비스, 오류율을 확인했습니다.
- [x] Git clone의 복구 범위는 Git 공식 문서로 확인했습니다.
- [x] Pull Request, Issues, Actions, Releases와 migration metadata는 GitHub 공식 문서로 확인했습니다.
- [x] 자체 호스팅 러너 문단을 공식 구조에서 도출한 운영상 판단으로 한정했습니다.
- [x] 단일 장애를 전체 가용성 평가나 대안 서비스 순위로 일반화하지 않았습니다.
- [x] 사용자가 요청한 대로 `해당 글에 따르면` 같은 2차 출처 소개 문장을 공개 원고에서 제외했습니다.
- first-party value: 기능을 `업무 산출물 -> 플랫폼 표면 -> 코드 미러 복구 여부 -> 최소 대체 경로`로 재구성한 네 층의 점검표와 세 질문

## v2 제목·소제목·밀도 게이트

### 제목과 소제목의 독자 작업

초안 strip:

1. `7시간 47분 장애가 드러낸 실제 의존성` - identify
2. `Git 저장소 사본으로 복구되는 범위` - verify
3. `GitHub 의존성을 네 층으로 나누기` - classify
4. `자체 호스팅 runner가 해결하지 못하는 부분` - bound
5. `GitHub 유지와 이전을 가르는 세 질문` - decide

선정 strip:

1. `7시간 47분 장애가 드러낸 실제 의존성` - 공식 사고의 범위를 식별합니다.
2. `Git 저장소 사본으로 복구되는 범위` - clone이 보존하는 자산을 확인합니다.
3. `GitHub 의존성을 네 층으로 나누기` - 자기 팀의 업무를 분류합니다.
4. `자체 호스팅 러너에 남는 GitHub 의존성` - 러너 소유와 제어면 독립을 구분합니다.
5. `GitHub 유지와 이전을 가르는 세 질문` - 유지·부분 분리·이전의 첫 판단을 내립니다.

변경 이유: 4번 초안은 부정형 문장처럼 들리고 독자가 확인할 대상을 숨겼습니다. `러너에 남는 GitHub 의존성`으로 바꿔 경계의 주어를 드러냈습니다. 다른 소제목은 서로 다른 독자 작업을 맡고 범용 `정체·구조·활용·정리` strip을 만들지 않아 유지했습니다.

### AI-template frame와 새 정보 검토

- `이때 필요한 것은 성급한 전면 이주가 아닙니다` -> `대응의 첫 단추는 ...입니다`: 방어형 대조를 직접 행동으로 바꿨습니다.
- `최신 파일만 받는 것이 아니라` -> `저장소 전체와 이력을 미러링`: 부정 프레임을 제거하고 사실만 남겼습니다.
- `전체 제품 비교가 아니라` -> 표의 실제 목적을 `코드 미러로 복구할 업무 가려내기`로 썼습니다.
- `runner가 해결하지 못하는 부분` -> `러너에 남는 GitHub 의존성`: 압축된 부정형 설명을 구체화했습니다.
- 초안 65문장, corrective-frame 밀도 6.0/1,000 Hangul에서 수정 후 63문장, 0.6/1,000 Hangul로 줄었습니다. 이 수치는 통과 점수가 아니라 재검토 위치를 찾는 목록으로만 사용했습니다.
- 삭제한 빈 문단: 없음. 첫 초안부터 각 문단이 사고 범위, 기능 경계, 행동, 비교 또는 한계를 하나씩 추가했습니다.
- 병합한 내용: GitHub 기능 소개와 포지 정의를 첫 소제목 한 문단에 묶었습니다.
- 반복 수치 처리: 20%와 50%는 첫 화면 한 곳에만 두고 표와 결론에서 반복하지 않았습니다.

### 중앙 주장·행동의 소유 문단

| 주장 또는 행동 | 소유 절 | 이후 사용 |
|---|---|---|
| 7시간 47분 장애와 오류율 | opening | 첫 소제목은 영향 범위만 해석 |
| Git clone의 복구 범위 | `Git 저장소 사본으로 복구되는 범위` | 표에서는 `대부분 가능`으로만 요약 |
| 네 층의 의존성 | `GitHub 의존성을 네 층으로 나누기` | 마지막은 세 질문으로 적용 |
| 자체 러너의 제어면 한계 | `자체 호스팅 러너에 남는 GitHub 의존성` | 다른 절에서 반복하지 않음 |
| 첫 분리 대상 | 같은 Actions 절의 긴급 릴리스 문단 | 결론은 팀별 답에 따라 층을 고르도록 마감 |

### 보호한 사실과 한계

- 장애 시간 `13:28~21:15 UTC`, 총 `7시간 47분`
- 웹·API 약 `20%`, 아카이브·Raw 콘텐츠 약 `50%` 오류율
- 영향 서비스와 서비스별 영향 시간이 달랐다는 경계
- GitHub Actions의 YAML 보존과 이벤트·작업 배정 의존성의 구분
- Git tag와 GitHub Release 객체의 구분
- 네 층은 벤치마크 순위가 아니라 운영 판단 프레임이라는 한계
- 모든 팀에 GitHub 이전을 권하지 않는 반론

## 일반 prose-polish 검토

- 비교 표본(슬러그·상태): `2026-08-10-vercel-deployment-guide` ready, `2026-08-10-bluetooth-headset-audio-quality` ready, `2026-08-07-koreaconnect-public-data-api` ready, `2026-08-02-github-stacked-pull-requests` ready, `2026-07-28-wsl-containers-without-docker-desktop` ready
- 같은 하위 카테고리 표본이 5개 있어 대체 표본은 쓰지 않았습니다.
- 최근 제목과 비교: `키워드, 기능 나열`에만 기대지 않도록 `GitHub 장애 대응` 뒤에 복구 범위를 명시했습니다. Vercel·Bluetooth 글의 절차형 heading을 복제하지 않고 이번 글의 사고 범위와 판단 순서를 따랐습니다.
- 문단 연결: `장애 범위 -> Git과 포지의 역할 -> clone의 범위 -> 협업 메타데이터 -> 네 층 -> Actions 제어면 -> 세 질문`으로 구체 명사를 이어 갔습니다.
- 잠근 내용: 날짜, 수치, URL, 표의 복구 판정, 실행 주체 Codex, 직접 장애 재현을 하지 않았다는 경계
- 새로 만들지 않은 내용: 사용자 경험, 팀 반응, 실패담, 실제 마이그레이션 결과, 장애 원인 추정
- 남은 문체·근거 위험: `forge`, `remote`, `runner`, `checksum` 같은 용어는 개발자 독자에게 필요한 범위에서 첫 설명 또는 문맥을 붙였습니다. 독립 source reviewer가 초면 독자의 이해를 다시 확인해야 합니다.

## 문단별 새 정보 reverse outline

1. opening scene - 로컬 코드와 협업 절차의 분리
2. official evidence - 사고 시간과 오류율
3. reader action - 약 8시간 동안 계속할 업무를 고르는 기준
4. identity - Git과 포지의 역할
5. observed consequence - PR·Issue·Actions가 막는 다음 단계
6. decision shift - 백업 대상을 코드 밖으로 확장
7. fact - 분산 clone의 보존 범위
8. comparison - commit과 PR metadata의 차이
9. boundary - migration metadata의 별도 범위
10. method - 업무 산출물 기준 점검표
11. comparison table - 네 층의 복구 판정과 대체 경로
12. exception - 공개 오픈소스의 입구 비용
13. action - 계속해야 할 업무 하나 선택
14. mechanism - Actions event·workflow·runner 순서
15. limitation - 자체 러너에 남는 GitHub 의존성
16. action - 최소 긴급 릴리스 경로
17. fact and boundary - Git tag와 Release asset의 차이
18. counterargument - GitHub 유지 비용 판단
19. decision questions - 중단 업무·재구성·복구 연습
20. closing action - 답하기 어려운 층부터 부분 분리

## 미디어와 최종 검토

- lead: `assets/github-homepage-user-v1.png` - 사용자가 캡처해 제공한 GitHub 홈페이지 화면을 opening 뒤에 배치합니다.
- concept: `assets/github-actions-workflow-official-v1.png` - GitHub Docs의 `overview-actions-simple.png`를 Actions 구조 설명 바로 뒤에 배치합니다.
- 역할 분리: lead는 GitHub가 계획·토론·코드 리뷰를 묶는 작업 공간임을 보여 주고, concept 이미지는 이벤트와 러너 사이의 workflow·job 배정을 설명합니다.
- infographic: `not_applicable` - 네 층의 관계는 본문 표가 같은 기능을 더 읽기 쉽게 수행합니다.
- source freeze 뒤 결과: 공식 PNG 원본(1536×538, SHA-256 `873d1510ee0c7b341246e6459a1612ab33b9cb4bdd90f75a164491519086ee2b`)을 자르거나 재인코딩하지 않고 등록했습니다.
- light/dark preflight: 1280px와 360px에서 문서 전체 가로 overflow 0, figure 2개, table 1개를 확인했습니다. 360px 표는 문서 폭을 늘리지 않고 320px 스크롤 컨테이너 안에 620px 표 전체를 보존합니다.
- 시각 확인: 홈페이지 lead는 opening과 의미가 맞고, Actions 다이어그램은 관련 구조 설명과 자체 러너 한계 사이에 붙습니다. 두 테마에서 이미지 비율·caption attachment·본문 대비가 유지됩니다.
- remote baseline: 두 CDN 응답이 HTTP 200 PNG로 관찰됐습니다. 홈페이지는 로컬과 같은 1280×693·동일 SHA-256이며, Actions는 Tistory R1280 변환 결과 1280×448로 확인됐습니다.

## 검사와 이력

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | v2 voice gate | 부정 대조 frame 6.0/1,000 Hangul, 부정형 runner heading | 직접 행동 문장과 구체 heading으로 수정 | corrective frame 0.6/1,000, generic heading 0개 |
| 2 | bundle check | 자동 검사 오류 없음 | 해당 없음 | `python3 scripts/blog.py check ...` 통과 |
| 3 | local light/dark preflight | 1280·360 문서 overflow 없음, 모바일 표는 내부 스크롤 필요 | 소스·CSS 수정 없음 | 두 테마에서 title, figure, TOC, heading, table과 list가 정상 렌더됨 |
| 4 | 사용자 미디어 추가 | 초반 이미지가 한 장뿐이라는 피드백 | 사용자 제공 GitHub 홈페이지 화면을 새 lead로 추가하고 Actions 구조도를 관련 절로 이동 | 독립 source re-review PASS와 새 source-pass record 완료 |
| 5 | 두 이미지 local preflight | stale 화면 증거 | light/dark 1280·360을 새로 렌더·검토 | 문서 overflow 0, figure 2개, table 내부 스크롤 유지 |
| 6 | final-page gate | 최종 결함 없음 | 소스·스타일 수정 없음 | light/dark 1280·360 독립 검토 PASS, `final-page.json` 기록 |

- 현재 검사: `python3 scripts/blog.py check posts/2026-08-21-github-beyond-git` - 오류 0, 경고 0
- 독립 source review: 변경 뒤 `Codex /root/source_review`가 다시 PASS하고 새 `source-pass.json`을 기록했습니다.
- 최종 종료 판단: source·local preflight·remote baseline·독립 final-page gate를 모두 통과했고 finalizer가 승인된 HTML과 붙여넣기 파일을 생성해 `ready`로 전환
