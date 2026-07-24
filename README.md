# blog-workspace

티스토리 블로그 **[dev.log](https://dop3n.tistory.com)** 글 작성 작업 공간.
Claude Code로 리서치 → 초안 → 윤문 → 발행용 HTML 까지 처리한다.

## 빠른 시작

이 디렉토리에서 `claude`를 실행하면 아래 슬래시 명령을 쓸 수 있다.

```bash
cd ~/dev/blog-workspace
claude
```

| 명령 | 하는 일 | 결과물 |
|---|---|---|
| `/research <주제>` | 웹·네이버 검색으로 소재 조사, 출처 정리 | `research/*.md` |
| `/write-post <주제>` | 카테고리 판별 후 dop3n 문체로 초안 작성 | `drafts/*.md` |
| `/polish <파일>` | AI 티 제거, 문체 교정 (내용은 불변) | 같은 파일 갱신 |
| `/to-tistory <파일>` | 티스토리 붙여넣기용 HTML + 발행 체크리스트 | `dist/*.html` |

각 단계는 독립적이다. 이미 써둔 글을 변환만 해도 된다.

## 구조

```
blog-workspace/
├── CLAUDE.md              # 프로젝트 지침 (Claude가 매 세션 읽음)
├── references/            # 규칙의 단일 진실 원천
│   ├── voice.md           #   문체 가이드 — 글 쓰기 전 반드시 읽음
│   ├── categories.md      #   카테고리 체계, 태그 규칙, 면책 문구
│   └── seo.md             #   발행 전 체크리스트
├── .claude/skills/        # 워크플로우 스킬
│   ├── research/
│   ├── write-post/        #   references/ 아래 카테고리별 구조 템플릿
│   ├── polish/
│   └── to-tistory/
├── scripts/
│   └── md2tistory.py      # 마크다운 → 티스토리 HTML 변환기
├── research/              # 리서치 노트
├── drafts/                # 작성 중
├── published/             # 발행 완료
├── tests/sample.md        # 변환기 회귀 테스트용
└── dist/                  # 변환 결과 (git 미추적)
```

## 변환기 단독 사용

Claude 없이도 쓸 수 있다. 외부 의존성 없음(Python 3 표준 라이브러리만).

```bash
python3 scripts/md2tistory.py drafts/2026-07-25-my-post.md
```

지원: 제목, 문단, 굵게/기울임/취소선, 인라인 코드, 코드블록, 표(정렬 포함),
인용, 중첩 목록, 수평선, 링크, 이미지. HTML 주석은 제거된다.
티스토리 스킨 CSS에 영향받지 않도록 모든 스타일을 인라인으로 넣는다.

변환기를 수정했으면 회귀 테스트를 돌린다:

```bash
python3 scripts/md2tistory.py tests/sample.md --stdout
```

## 발행

**티스토리 Open API는 2024년 2월 완전 종료되어 자동 발행이 불가능하다.**
마지막 단계는 직접 한다.

1. 티스토리 글쓰기 → 우측 상단 **기본모드 → HTML**
2. `dist/*.html` 전체 복사 후 붙여넣기
3. 다시 **기본모드**로 전환
4. 이미지 업로드, 카테고리·태그 지정, 주소(slug)를 영문으로 변경
5. 발행 후 `drafts/`의 원본을 `published/`로 이동

## 규칙을 고칠 때

문체나 카테고리 규칙이 바뀌면 **`references/` 아래 파일만 고친다.**
스킬 파일에 규칙을 복사해 두지 않았으므로 한 곳만 바꾸면 전체에 반영된다.

새 문체 규칙을 추가할 때는 실제 발행글에서 관찰한 근거를 함께 적는다.
추측으로 규칙을 늘리면 글이 점점 이 블로그와 멀어진다.
