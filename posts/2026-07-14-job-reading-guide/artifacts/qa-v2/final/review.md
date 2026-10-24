# 욥기 글 독립 최종 페이지 검토: 본문 복원 후보

- 날짜: 2026-10-24
- 검토자: `Codex independent job_reviewer`
- 최종 판정: `pass`
- 대상: 쉬운성경 42장·1,070절을 하단에 복원한 현재 canonical 로컬 미리보기와 제출용 fragment
- 범위: 인증된 티스토리와 Search Console에는 접근하지 않았습니다. 실제 티스토리 변환 및 공개 페이지 확인은 제작자가 별도로 담당합니다.

## 실제 독립 캡처

지정된 `capture_rich_qa_v2.py`를 변경하지 않고 `final-light`, `final-dark` 모드로 실제 실행했습니다. 각 모드에서 fresh headless Chrome 임시 프로필을 사용했습니다. 제작자의 캡처나 기존 통과 표시로 판정을 대신하지 않았습니다.

- 브라우저: Chrome/155.0.8059.85
- 밝은 session: `25a3edd2-e722-4563-a1a0-0141b621e858`
- 어두운 session: `cde0871c-02f0-47eb-88b8-0c674a6deb41`
- 밝은 canonical SHA-256: `aadeb58f381d52b59cc14c26379f445b5a93dba7870581028f308426fc82fa2a`
- 어두운 canonical SHA-256: `851fa904e2fb7ce9e79f5b5aa5afb078be24b747ded0276c815bd1711ffd1aca`

기본 영수증은 `final/light/browser-capture.json`, `final/dark/browser-capture.json`입니다. 각 폴더의 1280×900 및 360×800 PNG를 실제로 열어 확인했습니다. 영수증과 캡처는 실행된 브라우저에서 생성된 결과입니다.

복원 부록은 긴 full-page 이미지로 만들지 않았습니다. 변경하지 않은 캡처 모듈의 실제 Chrome/CDP 구현을 별도 fresh 세션에서 사용해 부록 시작·21장·42장의 뷰포트와 대표 이미지·목차, 모바일 표의 마지막 열을 확인했습니다. 마지막 42:17이 정상 표시되는 화면도 확인했습니다. 현재 후보의 보조 증거는 `final/restore-scripture-check/`에 있습니다. 이 폴더의 첫 화면 해시와 canonical 기본 영수증의 첫 화면 해시가 네 프로필 모두 일치합니다.

이전 해설 단독 후보의 `final/supplemental/` 이미지는 현재 복원 후보의 근거로 사용하지 않았습니다.

## 전체 본문 보존 대조

`final/rendered-scripture-preservation.json`은 두 테마의 canonical HTML과 제출용 fragment에서 부록 H2 아래의 `<p>` 텍스트를 독립 추출한 결과입니다. 세 파일 모두 원본의 1,112개 문자열 배열과 문자·순서가 정확히 일치합니다. 42개 장 표제와 1,070개 절 문단이 유지됩니다. preview의 H1은 1개이고 fragment의 H1은 0개입니다.

별도로 네 가지 실제 브라우저 DOM에서도 부록 문단 전체의 `textContent`를 읽어 `original-paragraphs.json`과 정확히 비교했습니다. 네 프로필 모두 1,112개 배열이 일치했습니다. 전체 부록 문단 중 가로로 넘치는 문단은 0개, 숨겨졌거나 높이가 0인 문단도 0개였습니다. 이 검토는 보존된 인용의 표시와 동일성을 확인하며 인용문을 재번역하거나 다듬지 않습니다.

## 화면과 동작

| 항목 | 1280×900 밝음·어두움 | 360×800 밝음·어두움 |
|---|---|---|
| 페이지 가로 범위 | clientWidth=scrollWidth=1280 | clientWidth=scrollWidth=360 |
| 전체 높이 | 61,693px | 97,846px |
| H1·목차 | H1 1개, 목차 7개, target 고유 | 같은 결과 |
| 부록 문단 | 1,112개, 숨김·가로 넘침 없음 | 같은 결과 |
| 원격 이미지 | 1개 정상 로드, 1672×941 | 같은 결과 |
| 이미지 표시 폭 | 916px, 비율 유지 | 320px, 비율 유지 |
| 표 wrapper | 760/760px | 320/620px, overflowX=auto |

부록 표제는 ‘욥기 본문 (쉬운성경)’으로 해설과 구분되고, 장 표제는 굵게 표시됩니다. 절 번호는 문단 앞에 그대로 남습니다. 1장·21장·42장의 실제 화면에서 긴 구절의 줄바꿈과 문단 간격이 유지되며 글자가 잘리거나 겹치지 않습니다. 어두운 테마에서도 장 표제와 번호가 본문 배경과 구별됩니다. 42:17의 마지막 문장도 네 화면에서 실제로 보입니다.

목차는 기존 해설 6항목과 본문 1항목입니다. 네 프로필에서 일곱 번째 링크를 실제 클릭해 `#욥기-본문-쉬운성경`으로 이동하고 해당 부록 제목을 대상으로 삼는지 확인했습니다. 모바일의 목차 번호, 링크 줄바꿈과 항목 간격이 정상입니다. 관련 실제 결과는 `restore-scripture-check/actual-end-and-toc-observations.json`에 있습니다.

대표 이미지는 재생성하지 않았습니다. 네 프로필에서 원격 로드, alt, 캡션과 비율을 확인했습니다. 어두운 테마에서도 이미지 필터는 `none`이고 원래 색과 중성 주변 배경이 유지됩니다. 두 모바일 화면에서 표의 `scrollLeft`를 300px까지 실제로 옮긴 뒤 마지막 열을 읽었습니다. 마지막 열의 7개 행을 볼 수 있고 페이지 전체는 가로로 넘치지 않습니다.

복원 본문에 코드 블록이나 추가 목록은 없습니다. 절 번호를 목록 마커로 다시 만든 것도 아닙니다. 기존 inline media 폭과 목차 링크 스타일이 유지됩니다. source 해설·표·이미지와 연결된 기존 동작에 새 결함을 발견하지 못했습니다.

## 실제 최종 기록

실제 캡처와 화면 확인 뒤 `final-measurements.json`의 사람 평가를 현재 후보에 대해 갱신했습니다. 이어서 `record_final_page_v2.py`를 실제 실행해 `artifacts/qa-v2/final-page.json`을 생성했습니다. `check_rich_post_v2.py --require-publish-urls --require-final-pass`도 `pass`입니다.

검토자는 원고, 미디어, post.css, source-pass, remote-media record와 공용 스크립트를 수정하지 않았습니다. 원고·미디어·post.css·source-pass·remote-media record의 시작·종료 해시가 일치함을 확인했습니다. 추가로 생성한 것은 실제 검토 결과와 캡처뿐입니다.

현재 복원 후보에서 남은 로컬 최종 페이지 결함은 발견하지 못했습니다. 이 기록은 실제 티스토리 공개 저장이나 라이브 검증을 대신하지 않습니다.
