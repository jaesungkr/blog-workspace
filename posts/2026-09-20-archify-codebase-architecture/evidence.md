# 근거 지도: Archify란? AI가 읽은 코드 구조를 검증 가능한 다이어그램으로 만드는 방법

## 주장별 상태

상태는 `확인`, `부분 확인`, `미확인`, `원문 필요` 중 하나로 적습니다.
유형은 `공식`, `독립 검증`, `벤더 주장`, `사용자 제공`, `Codex 실행`,
`추정`, `구조 예시`처럼 실제 성격을 드러냅니다.

| ID | 본문에서 쓸 주장 | 유형 | 상태 | 출처·측정 기준 | 한계 |
|---|---|---|---|---|---|
| C01 | Archify는 Cursor, Claude Code, Codex CLI, OpenCode가 작성한 typed JSON IR을 HTML/SVG로 렌더링하고 검사하는 Node.js 기반 Agent Skill입니다. | 공식 | 확인 | [공식 README](https://github.com/tt-a1i/archify/blob/72c750bb070d95171dbb2244e5b62b1b7da69c12/README_EN.md) | 에이전트 자체나 독립형 SaaS가 아닙니다. |
| C03 | 공식 설치 명령은 `npx skills add tt-a1i/archify -g`이며 영구 설치 없이 `npx skills use tt-a1i/archify@archify --agent codex`로 시험할 수 있습니다. | 공식 | 확인 | 공식 README Quick start | `npx` 실행에는 네트워크와 Node.js가 필요합니다. |
| C04 | Architecture, Workflow, Sequence, Data Flow, Lifecycle 다섯 종류와 자체 포함 HTML, PNG·SVG·WebM·Share Card 내보내기를 지원합니다. | 공식 | 확인 | 공식 README의 기능·유형 표 | 이번 실험은 Architecture HTML만 확인했습니다. |
| C05 | 저장소 근거 검증은 Architecture에서 선택적으로 켜며, 공개 저장소 URL·40자 커밋·파일 경로와 줄 범위를 로컬 Git 객체로 검증합니다. | 공식 | 확인 | [Schema README](https://github.com/tt-a1i/archify/blob/72c750bb070d95171dbb2244e5b62b1b7da69c12/archify/schemas/README.md#runtime-validation), authoring contract | 코드 의미의 완전성이나 실제 운영 상태는 보증하지 않습니다. |
| C06 | 직접 만든 한국어 7노드 Architecture 입력은 showcase 품질에서 9개 검사, 오류 0개, 경고 0개로 통과했습니다. | Codex 실행 | 확인 | `artifacts/experiment-log.md`, `artifacts/archify-pipeline.architecture.json` | 한 개의 작은 수작업 명세 결과이며 에이전트의 자동 코드 해석 정확도를 측정한 시험이 아닙니다. |
| C07 | 전달된 HTML은 806,884바이트였고 입력 명세와 결과물 SHA-256이 영수증에 기록됐습니다. | Codex 실행 | 확인 | `artifacts/experiment-log.md`, `artifacts/archify-pipeline.html` | 단일 사례의 파일 크기입니다. |
| C08 | `visual-check`는 1440×900, 1600×1000, 1920×1080, 2048×1320에서 가로·세로 오버플로 없이 통과했지만 `visualReview`는 `pending`으로 남았습니다. | Codex 실행 | 확인 | `artifacts/archify-pipeline.visual-check.json` | 자동 브라우저 증거와 사람의 미적 판단을 분리하는 도구 설계입니다. |
| C09 | 존재하지 않는 `missing-node`를 연결 대상으로 둔 입력은 종료 코드 1과 `layout/constraint` 진단으로 거부됐습니다. | Codex 실행 | 확인 | `artifacts/archify-invalid.architecture.json`, `artifacts/experiment-log.md` | 구조적 연결 오류 한 종류만 확인했습니다. |
| C10 | 자동 Mermaid 파싱, 범용 자동 배치, 호스팅 공유, WYSIWYG 편집은 현재 공식 범위 밖입니다. | 공식 | 확인 | 공식 README Reference and scope | 에이전트가 Mermaid 내용을 읽어 새 IR을 작성하는 작업과 네이티브 파싱은 구분해야 합니다. |
| C11 | MIT 라이선스로 공개돼 있습니다. | 공식 | 확인 | 저장소 LICENSE | 포함된 제3자 아이콘에는 별도 권리 조건이 있을 수 있습니다. |
| C12 | PyTorchKR 소개 글도 지원 에이전트, 좁은 프롬프트, 로컬 CLI 필요성, Mermaid·WYSIWYG 한계를 정리합니다. | 독립 소개 | 확인 | [PyTorchKR 참고 글](https://discuss.pytorch.kr/t/archify/11536) | 공식 문서와 상당 부분 겹치므로 독립 성능 검증으로 취급하지 않습니다. |
| C13 | Mermaid는 Markdown과 비슷한 텍스트 정의로 다이어그램을 만들며, GitHub Markdown 안에서 렌더링할 수 있습니다. Flowchart는 보안 설정에 따라 노드 링크와 JavaScript 클릭 이벤트도 지원합니다. | 공식 | 확인 | [Mermaid Flowchart 문서](https://mermaid.js.org/syntax/flowchart.html#interaction), [GitHub Mermaid 설명](https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/) | Archify와의 표는 직접 성능 비교가 아니라 공식 기능을 바탕으로 한 사용 조건 비교입니다. |

## 직접 검증 설계

- 질문: Archify가 작은 한국어 Architecture 명세를 실제로 검증·전달하고, 잘못된 연결은 구조화된 오류로 거부하는가?
- 실행 주체: Codex
- 환경과 확인 시점: macOS, Node.js v26.0.0, Google Chrome, 2026-09-20 17:25 KST
- 입력: 한국어 7노드 파이프라인 JSON 1개, 존재하지 않는 연결 대상이 있는 실패 JSON 1개
- 전처리 또는 표현: Archify 저장소 main 커밋 `72c750b`를 얕게 복제하고 패키지 내부 CLI를 직접 호출했습니다.
- 비교·판정 규칙: 정상 입력은 `doctor`, showcase `validate`, `deliver`, `visual-check`가 성공해야 합니다. 실패 입력은 비정상 종료와 원인을 가리키는 JSON 진단을 반환해야 합니다.
- 성공 기준: 정상 입력의 오류·경고가 0이고 4개 뷰포트에서 오버플로와 가독성 검사가 통과하며, 실패 입력은 비정상 종료와 원인을 가리키는 JSON 진단을 반환해야 합니다.
- 반복 횟수와 표본 크기: 정상 입력 1회, 실패 입력 1회입니다.
- 보존할 원자료: `artifacts/archify-pipeline.architecture.json`, `artifacts/archify-invalid.architecture.json`, 전달 HTML, 자동 브라우저 검사 JSON·캡처, `artifacts/experiment-log.md`

## 결과

| 실험 ID | 조건 | 관찰 결과 | 원자료 경로 | 해석 범위 |
|---|---|---|---|---|
| E01 | `doctor` | Node.js와 다섯 렌더러를 포함한 검사 항목이 모두 `[ok]` | `artifacts/experiment-log.md` | 현재 복제본의 실행 준비 상태만 확인합니다. |
| E02 | 한국어 7노드 Architecture `validate` | 9/9 검사 통과, 오류 0, 경고 0 | `artifacts/archify-pipeline.architecture.json` | 코드 자동 분석이 아니라 작성한 IR의 형식·배치 검증입니다. |
| E03 | 같은 입력 `deliver` | 806,884바이트 HTML 생성, 명세·결과 SHA-256 기록 | `artifacts/archify-pipeline.html`, `artifacts/experiment-log.md` | 단일 파일의 휴대성과 파일 크기를 함께 보여 줍니다. |
| E04 | 결과 HTML `visual-check` | 네 뷰포트의 오버플로·가독성·Viewer 조작부 검사 통과, 시각 검토는 pending | `artifacts/archify-pipeline.visual-check.json` | 자동 검사가 미적 완성도를 승인하지는 않습니다. |
| E05 | 존재하지 않는 연결 대상 | 종료 코드 1, `layout/constraint`, 대상 `missing-node` 명시 | `artifacts/archify-invalid.architecture.json`, `artifacts/experiment-log.md` | 하나의 실패 유형만 확인했습니다. |

## 실패와 반례

- 실패한 입력: `source` 노드가 존재하지 않는 `missing-node`로 연결되도록 작성한 JSON입니다.
- 예상과 달랐던 결과: 정상 HTML은 7노드 수준에서도 약 807KB였습니다. 폰트와 Viewer 런타임을 한 파일에 넣는 휴대성의 비용이 확인됐습니다.
- 일반화하면 안 되는 범위: 이 시험으로 대규모 저장소 분석 정확도, 모델별 결과 차이, 코드 누락 탐지율, CI 성능을 판단할 수 없습니다.

## 미해결 항목

- 없음.

## 출처 메모

- 공식 저장소: https://github.com/tt-a1i/archify
- 공식 프로젝트 페이지: https://tt-a1i.github.io/archify/
- PyTorchKR 참고 글: https://discuss.pytorch.kr/t/archify/11536
- 독립 설명: https://betterstack.com/community/guides/ai/archify-architecture/
- Mermaid Flowchart 공식 문서: https://mermaid.js.org/syntax/flowchart.html
- GitHub의 Mermaid 지원 설명: https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/
