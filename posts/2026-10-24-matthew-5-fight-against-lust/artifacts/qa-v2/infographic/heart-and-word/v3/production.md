# diagram-design 적용 기록

- 적용 요청: 사용자가 현재 글에 diagram-design을 직접 지정했습니다. 첫 스타일 선택에서 “diagram-design 기본 회색·주황색 사용”이라고 답했습니다.
- 실제 제작: Codex의 HTML/SVG와 host-provisioned Node Playwright/Google Chrome 렌더링. 의존성은 설치하지 않았습니다. 기존 글 제작 요청에서 정한 HTML·SVG·본문용 PNG 산출 범위를 이어 갑니다.
- 스킬: /Users/ja2sng/.codex/skills/diagram-design/SKILL.md . 기본 스타일 확인 후 type-state.md, semantic-patterns.md, output-spec.md, layout-budget.md, export.md 및 템플릿을 읽었습니다.
- 유형: 상태 변화형의 개념도, 3개 상태와 2개 전환. 불필요한 종료 상태나 실패를 되풀이하는 경로는 만들지 않았습니다.
- 기본 팔레트: paper #f5f5f5, ink #2d3142, muted #4f5d75, accent #bf4520. 강조한 상태는 마지막 하나입니다.
- 캔버스: fit 320×512, PNG 640×1024. 게시 폭 320 CSS px. 좁은 화면에서도 원본 HTML은 320px 최소 폭과 요소 내부 스크롤을 유지합니다.
- 글꼴: 제목 Instrument Serif/Noto Serif KR, 본문 Geist/Noto Sans KR. 실제 로드 결과는 render-metrics.json에 기록했습니다. 글꼴 요청 실패가 없습니다.
- 폰트 크기: 제목 28px, 상태 이름 16px, 한국어 전환·보조 문구 12px. 블로그 본문 폭과 동일한 320px 캔버스로 라벨의 실제 크기를 유지합니다.
- PNG SHA-256: 39a0263af95f017d79d50a29f6dfa1f070a898289946b4b8ea7127fd82e00eb9
- 검사: packaged self_check.py 통과. packaged export_svg.py로 접근성 ID·CSS를 유지하는 SVG를 추출했습니다. PNG는 기존에 사용하던 호스트 제공 Node Playwright와 Google Chrome을 재사용했습니다. Python 모듈이 없는 환경에 패키지를 자동 설치하지 않았습니다.
- 콘텐츠: 본문의 C6·C8 및 녹취에 대응합니다. 새 설교 주장과 저자의 Thoughts는 추가하지 않았습니다.
- 수명주기: reviewing 초안. 독립 도식 검수 전에는 captured이며, 승인 후 해당 미디어만 validated로 바꿉니다. 전체 source freeze나 final-page 승인을 의미하지 않습니다.
- 전역 설정: 설치된 스타일 가이드와 프로젝트 .diagram-design 표시는 쓰지 않았습니다. 사용자의 선택을 이 작업의 기록에만 보존합니다.
- v1 이미지와 원본 및 승인 이력은 그대로 보존합니다. 이번 v3 그림이 새 게시 후보입니다.

- 독립 검토에서 지적한 하단의 역할 없는 여백 60px를 삭제했습니다. 마지막 상태 아래에는 40px만 남습니다. 문구와 모든 요소의 위치는 바꾸지 않았습니다.

- 독립 최종 검수: review_sermon_diagram의 pass. exact SHA-256을 대조했으며 원본, 게시 폭 320px, 360px 화면과 확대 영역을 확인했습니다. 이 PNG만 validated로 확정했습니다.
