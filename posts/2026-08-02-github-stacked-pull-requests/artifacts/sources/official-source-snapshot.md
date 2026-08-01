# GitHub Stacked pull requests 공식 출처 스냅샷

- 확인일: 2026-08-02 (Asia/Seoul)
- 확인 주체: Codex
- 범위: GitHub 공식 Changelog, GitHub Docs, `github/gh-stack` 공개 저장소

## 1. 출시 공지

- URL: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
- 게시일: 2026-07-30
- 확인한 내용: public preview 발표, 작은 종속 PR로 분할, 레이어별 리뷰, 일부 또는 전체 병합, 기존 보호 규칙·체크 유지, 전체 저장소 대상 순차 배포, merge queue 지원의 점진 배포
- 캡처: `artifacts/captures/raw/github-changelog-hero.jpg`, `github-stack-workflow.jpg`, `github-review-map.jpg`, `github-merge-stack.jpg`

## 2. 개념과 지원 범위

- URL: https://docs.github.com/en/pull-requests/get-started/about-stacked-prs
- 확인한 내용: 같은 저장소의 PR 두 개 이상, bottom PR은 trunk 대상, 위 PR은 아래 PR의 브랜치를 base로 설정, 각 레이어 diff 분리, website·CLI·Mobile·API 지원, cross-fork와 GitHub Desktop 미지원, bottom-up 병합

## 3. 빠른 시작

- URL: https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart
- 확인한 내용: GitHub CLI 2.90.0+, Git 2.20+, `gh auth login`, push 권한, `gh extension install github/gh-stack`, `init`·`add`·`push`·`submit`·`view`

## 4. 생성과 관리

- URL: https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests
- URL: https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests
- 확인한 내용: 웹에서 아래 PR 브랜치를 base로 선택하고 Create stack 사용, 기존 종속 PR 연결, cascading rebase, signed commit 저장소에서 CLI rebase 권장, `gh stack sync --prune`

## 5. 공개 CLI 확장

- URL: https://github.com/github/gh-stack
- 확인한 내용: `gh extension install github/gh-stack`, stack 메타데이터와 branch 순서 관리, `submit`이 branch push와 PR 생성·연결을 수행, 명령별 역할

## 해석 경계

이 스냅샷은 공식 출처를 확인하고 화면을 직접 캡처한 기록입니다. 사용자의 실제 저장소에서 stack 생성, CI, rebase, merge queue, 병합을 실행한 결과가 아닙니다. public preview 중이므로 이후 UI와 명령이 바뀔 수 있습니다.
