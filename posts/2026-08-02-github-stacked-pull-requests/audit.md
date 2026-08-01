# 최종 감사: GitHub Stacked Pull Request 사용법, 큰 변경을 작은 PR로 쌓는 순서

## 현재 단계

- 수명 주기: `ready`
- 원고·근거·로컬 렌더: 검사 완료
- 독립 원고 검토: `source-level pass`
- Tistory CDN URL·원격 미디어 2회 확인·creator/independent 브라우저 QA: `pass`
- 준비 상태 판단: `ready`

## 구조와 독자

- [x] 제목 앞부분에 검색어 `GitHub Stacked Pull Request`가 있습니다.
- [x] 제목과 소제목이 `~다`로 끝나지 않습니다.
- [x] 표준 인사 뒤에 큰 PR과 수동 종속 브랜치 관리라는 익숙한 문제를 제시합니다.
- [x] 첫 5-6문장 안에 큰 변경을 작은 종속 PR로 나누고 GitHub가 순서와 병합을 관리한다는 결론이 나옵니다.
- [x] stack·top·bottom·base를 결과와 명령보다 먼저 설명합니다.
- [x] `큰 변경 -> 브랜치 분리 -> base 연결 -> 레이어별 리뷰 -> bottom-up 병합` 사슬이 보입니다.
- [x] 하나의 큰 PR, 수동 종속 PR, GitHub Stacked PR을 정성 비교하며 벤치마크 순위로 오해할 표현이 없습니다.
- [x] 웹과 CLI 시작 경로, 버전·인증·push 권한, 정확한 명령이 있습니다.
- [x] cross-fork, GitHub Desktop, signed commit, merge queue rollout 한계를 함께 설명합니다.

## 근거와 저자성

- [x] 2026-07-30 출시일, CLI·Git 버전, 명령, 지원 범위는 GitHub 공식 출처에 연결됩니다.
- [x] 공식 주장과 Codex 브라우저 관찰을 `evidence.md`에서 분리했습니다.
- [x] Codex가 2026-08-02 공개 페이지를 캡처한 사실을 사용자의 경험으로 바꾸지 않았습니다.
- [x] 검은 lazy-load 영상 프레임을 폐기하고 읽히는 프레임을 다시 캡처한 실패·복구 기록이 있습니다.
- [x] 실제 사용자 저장소에서 stack 생성·CI·병합을 수행하지 않았다는 범위를 도입부와 근거 문서에 남겼습니다.
- [x] 미확인 강한 주장과 본문 TODO는 없습니다.
- [x] 공식 화면 4개, 원본 캡처, crop, SHA-256, alt, caption, placement가 `media.json`에 연결됩니다.

## 제목·문체 폴리싱

- 비교 표본: `2026-07-28-ccshare-manycode-guide`(ready), `2026-07-25-duckdb-guide`(ready), `2026-07-28-wsl-containers-without-docker-desktop`(ready)
- 대체 기준: 같은 `Log > 개발 · 디지털`의 최근 ready 글이 3개 있어 대체 표본이 필요하지 않았습니다.
- 대표 제목 변경: `GitHub Stacked Pull Request - 큰 변경을 작은 PR로 나누는 방법` -> `GitHub Stacked Pull Request 사용법, 큰 변경을 작은 PR로 쌓는 순서`
- 대표 소제목 변경: `리뷰가 작아지는 이유` -> `레이어별 diff와 stack map`, `첫 스택을 만들 때의 순서` -> `테스트 저장소에서 시작할 순서`
- 대표 문단 연결 수정: 큰 PR 문제에서 Stacked PR 정의로 바로 이어지도록 `이 둘 사이를 노린 기능`을 `두 가지 수고를 줄이는 기능`으로 고쳤습니다.
- 삭제한 빈 문구 또는 반복: `이번 글에서는`, `핵심은`, 연속된 `아닙니다/그렇다고` 방어 문장을 줄였습니다.
- 보존 확인한 핵심 사실: 날짜, GitHub CLI 2.90.0+, Git 2.20+, 명령, cross-fork/Desktop 제한, bottom-up 병합, signed commit 주의, merge queue rollout
- 분석기 재검증: 평균 문장 37.8자 -> 35.0자, 70자 초과 3개 -> 0개, 추상명사 밀도 9.9 -> 4.0/1,000 Hangul, 반복 문단 시작 2개 -> 0개
- 남은 문체·근거 위험: public preview라 향후 명령과 UI가 바뀔 수 있습니다. 본문은 2026-08-02 확인 시점을 명시합니다.

## 미디어 검토

- lead: `assets/screenshots/github-changelog-hero.jpg`
- infographic: `not_applicable` - 공식 stack map과 CLI·병합 캡처가 필요한 관계를 이미 보여 줍니다.
- creator 원본 확인: 1280×720 원본 4개를 열어 공개 GitHub 페이지, 민감정보 없음, 잘못된 계정·저장소 정보 없음 확인
- creator crop 확인: 1080×560 1개, 520×340 1개, 440×260 1개, 520×240 1개
- creator 360px 표시 확인: 제목, CLI 핵심 명령, auth/api/frontend 레이어, `Merge stack 3` 상태가 각각 식별됩니다.
- independent media judgment: `pass` - 1차 `revision_required` 뒤 claim-specific crop을 다시 만들었습니다. 독립 검토자는 360px viewport의 실제 콘텐츠 폭을 보수적으로 320px로 잡아도 lead 제목, CLI init/add/submit, auth/api/frontend stack map, 세 레이어와 Merge stack 3 버튼을 확대 없이 식별했습니다.
- Tistory remote-media verification: creator baseline과 `Codex independent validator`의 두 번째 실제 fetch 모두 `pass`

## 렌더와 반응형 상태

- 로컬 light preview: `dist/github-stacked-pull-requests-rich-preview.html`
- 로컬 dark preview: `artifacts/qa/dark-preview/github-stacked-pull-requests-rich-preview.html`
- 구조 확인: light preview H1 1개, Tistory fragment H1 0개
- unresolved media: 0개. Tistory fragment의 H1·local path도 0개입니다.
- creator 브라우저 QA: remote-media preview를 Chrome 150의 1280·390·360에서 확인했고 hash-bound `rich-post.json`이 `pass`입니다. light/dark full-page와 모바일 표 양끝은 `component-details/`와 `dark-component-details/`에 보존했습니다.
- independent 브라우저 QA: `Codex independent validator`가 별도 Chrome 세션에서 같은 remote-media 후보를 1280·390·360으로 다시 캡처했습니다. 문서 overflow 없음, H1 1개, 고유 TOC, 이미지 4개 로드, figure 4개·pre 3개·table 2개, 390/360 표 양끝과 360 코드 양끝을 직접 확인했습니다.
- creator/independent hash-bound QA: 두 세션과 reviewer가 다르며 `artifacts/qa/independent-final-page.json`이 `pass`입니다.

## 수정과 재검증 이력

| 회차 | 검토 대상 | 발견한 문제 | 반영한 수정 | 재검증 결과 |
|---|---|---|---|---|
| 1 | 공식 페이지 캡처 | CLI 데모가 lazy-load 직후 검은 프레임으로 잡힘 | 명령이 표시된 프레임까지 기다린 뒤 다시 캡처 | `gh stack init`·`add`·`submit` 안내가 보이는 자산 선택 |
| 2 | 본문용 미디어 | 1280px 전체 화면은 모바일에서 UI가 작음 | 원본을 보존하고 중심 UI만 1080px 또는 640px로 crop | 360px 임시 표시에서 핵심 상태 식별 |
| 3 | 코드 블록 검사 | `#` 셸 주석을 Markdown 소제목으로 오인 | 코드 블록의 설명 주석을 제거하고 주변 본문이 순서를 설명 | `scripts/blog.py check` 오류 6개 -> 0개 |
| 4 | 제목·소제목·문장 | 최근 글의 `키워드 - 설명` 형식과 범용 소제목 반복 | 제목 문법을 바꾸고 diff·stack map·테스트 저장소를 소제목에 명시 | analyzer의 generic-heading signal 2개 -> 1개, source check 통과 |
| 5 | 로컬 브라우저 QA | 인앱 브라우저가 `file:` preview URL 차단 | 정책 우회 없이 구조 검사와 360px 미디어 검토만 수행 | final page pass 보류, status `reviewing` 유지 |
| 6 | 독립 source/media 검토 | 도입부의 첫 행동과 인라인 출처가 부족하고, 기술 용어가 늦게 풀리며, 캡션 역따옴표·credit 중복·360px 글자 크기 문제가 있음 | 테스트 저장소 두 레이어 시작점을 도입부에 추가, Creating·Quickstart·About·Managing·Merging 링크를 주장 곁에 배치, 연쇄 rebase·retarget을 한국어로 설명, actor·caption 정리, 세 UI를 더 좁게 crop | 독립 재검토에서 source-level·local media semantic/360px pass |
| 7 | 독립 최종 페이지 검토 | 알려진 결함 없음 | creator와 다른 reviewer·Chrome 세션으로 CDN 재검증, 독립 렌더·canonical 캡처·full-page·figure·pre·모바일 표 양끝을 재현 | remote verification, independent final-page, strict rich-post gate 모두 pass |

## 검사와 남은 위험

- `python3 scripts/blog.py check posts/2026-08-02-github-stacked-pull-requests`: 오류 0, 경고 0
- `python3 scripts/blog.py check posts/2026-08-02-github-stacked-pull-requests --strict`: 오류 0, 경고 0
- `python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py posts/2026-08-02-github-stacked-pull-requests --require-publish-urls --require-independent-pass`: pass
- `render_rich_post.py --require-publish-urls --preview-media-source remote`: 최종 `dist/` preview와 fragment 생성
- 아직 남은 위험: public preview의 UI·명령 변경 가능성과 사용자의 실제 저장소 정책·CI·충돌·merge queue 동작은 이 글에서 재현하지 않았습니다.
- 사람이 티스토리에서 확인할 항목: 최종 CDN 이미지, HTML 모드 paste, hELLO light/dark, 모바일 표·코드 스크롤, 공개 직전 preview
- 최종 종료 판단: `ready` - 독립 final-page와 strict render가 모두 `pass`이며 Git 전달 대상입니다. 실제 Tistory HTML 붙여넣기·preview·발행은 사용자 단계입니다.
