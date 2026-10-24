# 도식 제작 기록

- 제작자: Codex. 실제 제작 방식은 HTML/SVG와 Chromium 렌더링입니다. ImageGen 또는 max-txt2img로 생성했다고 주장하지 않습니다.
- 사용자 지시: blog-diagram-design을 적절한 본문 위치에 활용. 이번 도식의 제작 방식만 적용하며 v2 스킬·스크립트를 수정하지 않았습니다.
- 원본 디자인 참고: https://github.com/cathrynlavery/diagram-design , Cathryn Lavery, MIT, commit 550fd66edff058bc73056c3416b76d69cfe865ba. 라이선스는 같은 폴더에 보존했습니다.
- 캔버스: 480×520 SVG, 960×1040 PNG, 불투명 배경 #f7f4ee.
- 한국어: Apple SD Gothic Neo 실제 사용을 CDP 플랫폼 폰트 조회로 확인했습니다. 제목 28px, 주 레이블 24px, 보조 문구 20px.
- 게시 예정 폭: 480 CSS px. 360px 뷰포트에서 본문 폭 320px로 표시하면 주 레이블은 16px, 보조 문구는 약 13.3px입니다.
- SHA-256: 92341368c49b67d10e12e36b6d384ad55c5763b988494af40145c13ca9fdca42
- 근거·문구·위치·대체 텍스트: copy-map.json, evidence.md와 media.json을 참조합니다.
- 자동 점검: self_check.py --offline 통과, export_svg.py --system-fonts 성공.
- PNG 도구: 기본 Python과 번들 Python에는 Playwright 모듈이 없어 원본 Python PNG 내보내기를 실행하지 않았습니다. 설치된 번들 Node Playwright와 로컬 Google Chrome으로 같은 SVG를 deviceScaleFactor=2로 캡처했습니다.
- 제작자 점검: 원본에서 한글 글리프, 연결선, 도형과 텍스트의 분리, 불투명 배경을 확인했습니다. 첫 연결선의 화살촉을 별도 path로 분리하고 주 레이블·보조 문구의 bbox 간격을 11px에서 15px로 늘린 뒤 출력했습니다.
- 독립 검수: 별도 검수자 review_sermon_diagram이 infographic-review.md에 pass를 기록했습니다. 원본, 480px 게시 폭, 360px 뷰포트의 320px 본문 폭과 확대 크롭을 직접 검사했습니다. 본 제작 기록과 독립 검토 기록은 구분합니다.
- 미디어 상태: 전체 source freeze 전 도식 후보이며, 대표 이미지와 CDN URL은 아직 없습니다.
