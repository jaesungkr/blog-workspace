# dev.log workspace

개인 블로그 [dev.log](https://dop3n.tistory.com/)를 운영하면서 사용하는 AI-assisted publishing workflow의 작업 기록입니다.

글의 기획, 자료 조사, 원고, 이미지, 검수 결과와 게시 이력을 한곳에 보관합니다. 다른 사람에게 배포하기 위한 범용 도구나 완성된 제품보다는, 제가 실제로 사용하는 방식과 그 변화를 남기는 저장소에 가깝습니다. 스킬과 스크립트도 제 블로그의 문체와 티스토리 환경에 맞춰져 있습니다.

[작업 지침](AGENTS.md) · [기본 워크플로 v2](.agents/skills/dev-log-rich-post-workspace-v2/SKILL.md) · [글쓰기 기준](standards/editorial-standard.md)

## 보관하는 내용

| 위치 | 내용 |
| --- | --- |
| `posts/` | 글별 기획, 출처, 원고, 이미지, 검수 및 게시 기록 |
| `.agents/skills/dev-log-*/` | 작성·문장 다듬기·이미지·검증·발행을 위한 스킬 |
| `standards/` | 문체, 근거, 카테고리, 이미지 등 편집 기준 |
| `scripts/`, `tests/` | 작업 묶음 검사와 관련 회귀 테스트 |
| `archive/legacy-claude/` | 초기 워크플로의 기록. 현행 기준으로 검증된 자료는 아닙니다. |

## 현재 작업 흐름

새 글은 `dev-log-rich-post-workspace-v2`를 기본으로 사용합니다. 글의 성격에 따라 일반 글과 근거 중심 글의 경로를 나누고, 필요한 단계만 추가합니다.

1. **기획과 조사**: 독자가 궁금해할 질문을 정하고, 주장별 출처·확인 날짜·한계를 기록합니다.
2. **작성과 교정**: 원고를 작성한 뒤 존댓말, 문장 연결, 설명 순서를 다듬습니다.
3. **근거 검증**: 원고와 출처를 독립적으로 대조합니다. 이 검증을 통과한 원고를 기준으로 이미지 작업을 진행합니다.
4. **이미지와 미리보기**: 필요한 스크린샷·이미지를 준비하고, v2 렌더러로 HTML을 만듭니다. 밝은 테마와 어두운 테마, 모바일 가독성을 확인합니다.
5. **검토와 게시**: 작성자가 완성본을 검토하고 게시를 요청한 경우에만 티스토리에 발행합니다. 실제 이미지 첨부와 최종 미리보기도 이 단계에서 확인합니다.
6. **기록 보존**: 게시 결과와 공개 URL을 글 묶음에 남기고, 원고와 검수 자료를 Git 이력으로 보관합니다.

GitHub에 작업을 올리는 것과 티스토리에 글을 게시하는 것은 별도입니다. 게시에 성공했지만 Git 반영이 실패했다면, 글을 다시 게시하지 않고 아카이브 반영만 이어갑니다.

기존 `format: rich-post` 글은 v1 방식으로 유지합니다. 기존 글의 형식 변경이나 전체 재작성은 별도 요청이 있을 때 진행합니다.

## 글 한 편의 작업 묶음

```text
posts/YYYY-MM-DD-slug/
├── brief.md          # 독자, 주제, 핵심 질문과 구성
├── evidence.md       # 주장별 출처, 확인 결과와 한계
├── article.md        # 원고와 상태·게시 URL 등의 메타데이터
├── audit.md          # 검수 결과와 남은 문제
├── media.json        # v2 이미지·미디어 기록
├── workflow-v2.json  # v2 진행 단계와 검증 상태
├── assets/           # 대표·본문 이미지
└── artifacts/        # 스크린샷, 실험 출력, HTML 및 QA 기록
```

글의 상태는 같은 폴더 안에서 관리합니다.

```text
planning → researching → drafting → reviewing → ready → published
```

검증 뒤 원고나 이미지를 바꾸면 관련 검증도 다시 진행합니다. 이전에 통과한 결과를 변경된 글에 그대로 적용하지 않습니다.

## 작업 시작

저장소 루트에서 `AGENTS.md`와 필요한 스킬을 읽고 시작합니다. 예를 들면 다음처럼 요청합니다.

```text
dev-log-rich-post-workspace-v2를 사용해서 [주제] 글을 작성해줘.
근거와 이미지를 함께 준비하고, 게시 전 검토할 수 있는 완성본까지 만들어줘.
```

원고 교정이나 이미지 수정만 필요하면 해당 단계의 스킬만 사용합니다. 아래 명령은 저장소 루트에서 Python 3로 실행합니다.

```bash
# 새 v2 작업 묶음
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/init_bundle_v2.py my-post \
  --title "제목" --category Log --subcategory "개발 · 디지털" --profile standard-rich

# 생성된 실제 폴더 이름으로 바꿔서 실행
python3 scripts/blog.py check posts/YYYY-MM-DD-my-post

# 로컬 미리보기와 티스토리 HTML
python3 .agents/skills/dev-log-rich-post-workspace-v2/scripts/render_rich_post_v2.py \
  posts/YYYY-MM-DD-my-post --output-dir dist

# 전체 글 검사 / 스크립트 회귀 테스트
python3 scripts/blog.py check --all
python3 -m unittest discover -s tests -v
```

다른 작업 폴더에서 스킬을 사용할 때는 `sh scripts/link_codex_skill.sh`로 저장소의 스킬을 전역 Codex 스킬 경로에 연결할 수 있습니다. 복사본 대신 심볼릭 링크를 사용하므로 수정은 이 저장소에서 관리합니다.

AI 도구, 이미지 생성 기능, 로그인된 게시용 브라우저는 별도로 준비해야 합니다. 저장소를 복제하는 것만으로 이 환경이 자동 구성되지는 않습니다.

## 작성과 발행 기준

- 본문은 자연스러운 한국어 존댓말을 사용합니다. 제목과 구성은 글의 내용에 맞추고, 고정된 소제목이나 표를 억지로 채우지 않습니다.
- 제품 정보·가격·성능·규정은 가능한 한 공식 자료로 확인하고, 기준 시점과 적용 범위를 구분합니다.
- 직접 확인한 결과와 자료에서 인용한 내용을 구분합니다. 하지 않은 실험이나 개인 경험을 만들어 넣지 않습니다.
- 스크린샷과 이미지는 본문 설명을 돕는 용도로 사용하고, 실제 글 크기에서 가독성과 출처를 확인합니다.
- 게시에는 작성자가 지정한 Chrome 세션을 사용합니다. 계정 비밀번호·토큰 같은 인증 정보는 저장소에 남기지 않습니다.
- 직접 붙여넣을 때는 게시 HTML만 담은 `<slug>-tistory-fragment.txt`를 전달합니다. 게시 성공을 확인한 뒤에만 `published` 상태와 공개 URL을 기록합니다.

자동 검사는 형식과 일부 누락을 잡아내는 수단입니다. 출처가 문장을 실제로 뒷받침하는지, 설명이 자연스러운지, 공개해도 되는 내용인지는 별도로 검토합니다. 세부 절차는 [v2 워크플로](.agents/skills/dev-log-rich-post-workspace-v2/references/workflow-v2.md)와 [전달·기록 기준](.agents/skills/dev-log-rich-post-workspace-v2/references/delivery-v2.md)에 정리되어 있습니다.
