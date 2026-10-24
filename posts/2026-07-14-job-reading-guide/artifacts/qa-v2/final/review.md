# 욥기 글 독립 최종 페이지 검토

- 날짜: 2026-10-24
- 검토자: `Codex independent job_reviewer`
- 최종 판정: `pass`
- 범위: 원격 CDN 이미지를 참조하는 canonical 로컬 미리보기와 제출용 fragment입니다. 인증된 티스토리와 Search Console에는 접근하지 않았습니다. 실제 티스토리 변환 화면·공개 페이지 검증은 오케스트레이터가 별도로 담당합니다.

## 실제 캡처와 독립성

지정된 `capture_rich_qa_v2.py`를 `final-light`, `final-dark` 모드에서 실제 실행했습니다. 두 모드는 서로 다른 임시 프로필의 fresh headless Chrome 세션을 사용했습니다. 검토자는 제작자의 화면 캡처나 기존 통과 표시로 판정을 대신하지 않았습니다.

- 브라우저: Chrome/155.0.8059.85
- 밝은 테마 session: `4fbf230a-b9a9-4697-8ca0-d4a6fd1ca90f`
- 어두운 테마 session: `6bf33ba7-7c5f-4c34-9a79-ce128e10cd02`
- 밝은 canonical SHA-256: `df310b379ed40f4468b1ecc05783c3e435bfbfcd3c97490496030379d0a1746e`
- 어두운 canonical SHA-256: `17b82a6d162dc416c083bafe1e6b119b4511365c555b5c2b2bc8436b2dcef8d8`

기본 증거는 `final/light/browser-capture.json`, `final/dark/browser-capture.json`과 각 폴더의 1280×900 및 360×800 PNG입니다. 두 영수증은 스크립트가 실제 브라우저 세션에서 작성한 것입니다. 캡처나 세션 번호를 임의로 만들지 않았습니다.

첫 화면 아래도 검토하기 위해 같은 캡처 모듈의 실제 Chrome/CDP 구현으로 별도 임시 프로필을 열고 네 가지 full-page PNG를 생성했습니다. 이미지 뷰어가 긴 PNG를 축소하므로, 최종 검토에서는 동일한 실제 페이지를 1280×1800 이하 및 360×1500 이하 구간으로 직접 캡처하여 인사부터 마지막 문단까지 원래 표시 폭으로 읽었습니다. 이 구간은 원본을 편집한 이미지가 아니라 실제 CDP clip 캡처입니다. `supplemental/view-crops/`라는 경로 이름을 사용하지만, 현재 파일은 브라우저에서 캡처한 구간 PNG입니다.

보조 관찰값과 각 실제 캡처의 해시는 `supplemental/actual-supplemental-observations.json`에 기록돼 있습니다. 보조 캡처의 preview hash와 첫 화면 screenshot hash가 canonical 영수증의 해당 값과 일치함도 확인했습니다. 보조 기록을 canonical 영수증으로 바꾸거나 그 일부로 가장하지 않았습니다.

## 네 화면에서 확인한 결과

| 확인 항목 | 1280×900 밝음·어두움 | 360×800 밝음·어두움 |
|---|---|---|
| 페이지 가로 범위 | clientWidth=scrollWidth=1280 | clientWidth=scrollWidth=360 |
| 본문 전체 높이 | 5082px | 7052px |
| H1·목차 | H1 1개, 목차 6개, 각 target이 한 번씩 존재 | 같은 결과 |
| 원격 이미지 | 1개 정상 로드, naturalWidth=1672/naturalHeight=941 | 같은 결과 |
| 이미지 표시 | 폭 916px, 비율 유지 | 폭 320px, 비율 유지 |
| 표 | wrapper 760/760px, 3열이 함께 보임 | wrapper clientWidth=320/scrollWidth=620, overflowX=auto |

페이지 자체에 가로 넘침이 없고 모바일 표만 지정한 영역에서 가로로 움직입니다. 실제 보조 세션에서 표의 `scrollLeft`를 300px까지 옮긴 뒤, 양 테마의 마지막 열을 캡처해 읽었습니다. `final-light-360-table-right.png`와 `final-dark-360-table-right.png`에서 ‘눈여겨볼 점’의 일곱 행 전체가 읽히며 마지막 열의 오른쪽도 잘리지 않습니다. 표 앞의 가로 스크롤 안내가 이 동작과 일치합니다.

제목은 모바일에서 두 줄로 표시되고 글자가 잘리거나 다음 문단과 겹치지 않습니다. 본문의 긴 소제목도 자연스럽게 줄바꿈되며 상하 간격과 글자 높이가 유지됩니다. 대표 이미지 전의 ‘누가 말하는지’라는 읽기 행동이 먼저 보이고, 대표 이미지 아래에 삽화임을 밝힌 캡션이 붙습니다. 네 사람의 구분과 재·기와 조각의 의미가 모바일 표시에서도 남습니다.

목차는 실제 여섯 절의 순서를 그대로 보여 줍니다. 번호가 표시되고, 항목 간 간격과 목차 다음 절의 간격이 구분됩니다. 이 글에는 본문용 별도 목록이나 코드 블록이 없으므로 해당 마커·코드 스크롤의 추가 검토 대상은 없습니다. 일반 문단과 링크·강조의 줄 높이, 절 사이의 배경 전환, 마지막 문단까지의 표시가 정상입니다.

어두운 테마에서는 본문·소제목·링크·표·캡션이 각 배경에서 읽힙니다. 본문 색은 rgb(209,209,214), 페이지 배경은 rgb(30,31,33)로 관찰됐습니다. 교차 절 배경과 표의 경계가 본문과 충돌하지 않습니다. 이미지는 `filter: none`이며 아이보리 색과 인물의 원래 색이 유지됩니다. 이미지 밖의 주변은 어두운 중성색으로 연결되고, 이미지를 반전하거나 덧칠하지 않습니다. inline media width 스타일과 원격 이미지 크기·배치도 보존됩니다.

## Fragment와 수정된 native alt

실제 canonical fragment를 읽어 H1이 0개이며 media directive나 로컬 파일 URI가 없음을 확인했습니다. native Tistory attachment block의 metadata에는 다음 alt가 들어 있습니다.

“재 위에서 기와 조각을 든 욥과 말없이 곁에 앉은 세 친구를 표현한 종이 부조 삽화”

캡션은 native block 다음의 별도 caption 문단으로 붙으며 삽화와 본문 범위를 밝힙니다. `post.css`의 목차 링크 `display: inline !important` 보정이 포함된 canonical 후보를 검토했습니다. 플랫폼 변환 뒤의 번호 위치는 제작자가 실제 티스토리 미리보기에서 확인할 사항이며, 로컬 통과로 실제 서비스 확인까지 했다고 주장하지 않습니다.

## 기록과 검증

직접 화면을 읽은 뒤 `final-measurements.json`의 사람 평가만 통과로 채웠습니다. 이후 실제 `record_final_page_v2.py`를 canonical preview, dark-preview, fragment 및 measurements 경로로 실행해 `artifacts/qa-v2/final-page.json`을 생성했습니다. 스크립트는 오류 없이 통과했습니다.

`check_rich_post_v2.py --require-publish-urls --require-final-pass`도 `pass`입니다. 원고, media manifest, source pass, remote-media record는 이 검토에서 수정하지 않았으며 검토 시작과 종료의 SHA-256이 모두 일치합니다. 기사 lifecycle도 검토자가 변경하지 않았습니다.

이전 후보는 제작자가 native alt 및 플랫폼 목차 CSS를 보완하는 동안 판정을 보류했습니다. 현재 영수증과 구간 캡처는 마지막 canonical 재생성 뒤 실제로 다시 생성한 후보입니다. 남은 로컬 최종 페이지 결함은 발견하지 못했습니다.
