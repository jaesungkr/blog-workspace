# 독립 최종 페이지 검토

판정: **pass**. 검토자는 `/root/source_cold_review`이며, 2026-10-25에 canonical remote-media 미리보기를 확인했다. 기존 소스·미디어 검토를 유지하고 출판 페이지의 표시와 동작만 검토했다.

밝은 테마와 어두운 테마를 각각 새 Chrome 세션에서 캡처했다. 두 테마 모두 1280×900, 360×800, 390×844에서 새로 로드했다. 공식 `capture_rich_qa_v2.py`가 두 canonical browser-capture.json을 생성했으며 모든 폭에서 자동 검사가 통과했다.

## 실제 관찰

| 항목 | 관찰 결과 |
|---|---|
| 전체 페이지 | 여섯 뷰를 제목부터 참고 자료까지 1,800px 단위의 변경하지 않은 브라우저 캡처로 전부 확인했다. 본문, 이미지, 캡션, 표, 참고 링크에 겹침이나 잘못된 줄바꿈으로 읽을 수 없는 부분이 없다. |
| 페이지 폭 | 양쪽 테마 모두 document scrollWidth가 1280/360/390으로 해당 clientWidth와 같다. 가로 이동은 이미지와 표 영역 내부에서만 일어난다. 본문 루트 overflowX는 visible이며 전체 페이지를 숨겨 측정값을 맞춘 상태가 아니다. |
| 이미지 | 다섯 이미지가 실제로 그려졌다. 대표 화면은 전체 구도를 보여 주고, 파일 메뉴와 3D Make·AA 비교·API 가격은 모바일에서 원본 폭을 유지한 채 좌우로 이동한다. 대표 화면의 세부 메뉴는 본문이 풀어 설명한다. 처음과 끝 스크롤 위치의 실제 픽셀을 추가로 확인했다. 빈 이미지 영역은 발견하지 못했다. |
| 이미지의 의미와 캡션 | 대표 화면, 파일 메뉴, 3D 제작 화면, AA 막대, 국제 API 가격표 순서가 유지된다. AA에서 58/55와 모델 이름·설정을 읽을 수 있다. 메뉴·가격 캡션이 해당 이미지 바로 아래에 있고 다른 문단과 섞이지 않는다. |
| 이미지 색상 | 어두운 테마에서도 UI 캡처의 흰 배경과 원래 막대 색상을 유지한다. 모든 이미지의 computed filter는 none, opacity는 1, mixBlendMode는 normal이다. 이미지 주변은 중성색이며 픽셀을 반전하거나 어둡게 덮지 않는다. |
| 표 | 데스크톱에서는 세 표가 모두 본문 폭 안에 들어온다. 모바일에서는 세 표 모두 내부 가로 스크롤이 끝까지 이동한다. 360px의 최대 이동량은 300px, 390px는 270px이다. 가격표의 오른쪽 출력·캐시 입력 열을 실제 화면으로 확인했다. |
| 목차와 제목 | 미리보기의 H1은 각각 1개다. 목차 링크 6개가 모두 고유한 실제 대상에 연결되며 마지막 참고 자료 링크의 이동도 확인했다. 모바일의 두 줄 제목과 소제목이 잘리지 않는다. |
| 목록 | 목차의 번호와 참고 자료의 글머리표가 보인다. 항목 사이 간격과 목록 주변 여백이 유지된다. 마지막 참고 자료 목록까지 확인했다. |
| 어두운 테마 | 본문·소제목·표·캡션·링크·인라인 코드의 대비가 충분하고, 배경 띠와 인라인 스타일이 유지된다. 밝은 이미지와 본문 사이의 경계도 인식할 수 있다. |
| 코드 | 긴 코드 블록은 없다. 인라인 코드와 중국어 메뉴는 정상적으로 줄바꿈한다. |
| 출판 fragment | H1 0개, 해결되지 않은 media placeholder 0개, local path 0개를 직접 확인했다. 실제 Tistory 이미지 문법 5개와 div 기반 native wrapper 5개가 있다. native attachment 문법은 정상적인 출판 블록이며 미해결 placeholder로 세지 않았다. |

## 증거와 범위

공식 캡처는 `artifacts/qa-v2/final/light/`와 `artifacts/qa-v2/final/dark/`에 있다. 전체 페이지와 처음·끝 스크롤 상태는 `artifacts/qa-v2/final/inspection/`에 보존했다. `observations.json`은 전체 페이지 폭, 이미지 스타일, 표·이미지 스크롤 이동, 목차 대상을 기록한다. `table-end-observations.json`과 price-table-end 캡처는 모바일 가격표 오른쪽 열을 확인한 증거다. 전 페이지 캡처에서 이미지가 실제로 표시되어 별도의 빈 영역 재검사는 필요하지 않았다.

`final-measurements.json`에서는 readable_media, status와 dark_theme의 인간 판단 필드만 채웠다. 자동 측정된 수치는 바꾸지 않았다. 원고·media.json·workflow·CSS·출판 편집기를 수정하지 않았다. 이 검토는 canonical local final-page gate이며, exact native fragment의 Tistory 미리보기와 게시 후 공개 페이지 검증은 다음 출판 단계에서 수행한다.

## 표지 전용 CSS 수정 후 기록 갱신

2026-10-25에 표지 오버레이를 66%로 높이는 `assets/post.css`가 추가된 후보를 확인했다. 규칙은 `#header[data-header-style="thumbnail"]`의 오버레이와 제목·메타데이터만 대상으로 하며, 본문 이미지나 문단 요소를 선택하지 않는다.

기존 승인본과 현재 후보의 정규화 article_content SHA-256은 모두 `4f8bf7328386904105ffcf0a2f1c1c0841f9d820f60ed56dd576110f7d6b238a`로 같았다. 다섯 이미지 파일도 manifest 해시와 일치한다. 따라서 원고와 본문 자산에 대한 실질 검토 결과를 재사용했다.

양 테마를 새 세션으로 다시 캡처했다. 1280·360·390px에서 이미지 5개가 모두 로드되고 H1 1개, 고유 목차 대상, 페이지 가로 넘침 없음이 유지된다. 새 여섯 첫 화면 캡처의 SHA-256은 이전 승인 캡처와 전부 동일하다. fragment에는 66% 표지 규칙이 포함됐고 H1 0개·native block 5개·미해결 placeholder 0개·local path 0개를 다시 확인했다. 인간 판단 필드는 기존 관찰 결과에 따라 유지했다.

canonical preview에는 hELLO의 `#header` 표지 요소가 없으므로 이 캡처만으로 실제 공개 표지의 대비를 승인하지 않는다. 실제 표지는 출판 담당자가 확인하는 별도 플랫폼 증거로 검증한다. 원고 심사와 전 페이지 수동 캡처는 반복하지 않았다.

## 실제 hELLO 표지 변경 부분의 독립 검토

변경 부분 판정: **pass**. 다음 실제 Tistory 수정 미리보기 네 화면을 직접 열어 표지만 확인했다.

- `artifacts/qa-v2/tistory-preview/cover-fixed-desktop-light.jpg`
- `artifacts/qa-v2/tistory-preview/cover-fixed-desktop-dark.jpg`
- `artifacts/qa-v2/tistory-preview/cover-fixed-mobile-light.jpg`
- `artifacts/qa-v2/tistory-preview/cover-fixed-mobile-dark.jpg`

1280px 데스크톱에서는 제목과 날짜·분류가 어두워진 UI 배경 위에 흰색으로 뚜렷하게 보인다. 360px 모바일에서도 세 줄 제목과 메타데이터가 표지 안에 온전히 들어오며, 글자가 잘리거나 배경에 묻히지 않는다. 밝은 테마와 어두운 테마의 표지 모두 같은 대비를 유지한다. 이번 수정 대상인 표지에서 추가 결함은 발견하지 못했다.

`cover-fixed-check.json`은 실제 fresh mobile iframe의 overlay가 `rgba(0, 0, 0, 0.66)`, 제목 색상이 `rgb(255, 255, 255)`, width와 scrollWidth가 모두 360임을 기록한다. `artifacts/qa-v2/cover-only-change.json`은 article body가 바이트 단위로 같고 native 첨부 참조·승인된 문구·캡션·URL·게시 날짜를 유지한 CSS 수정임을 기록한다. 이전 본문 검토 결과를 유지하며 원고 심사는 다시 수행하지 않았다.

**리사이즈 관찰은 별도로 남는다.** 데스크톱 미리보기 iframe을 360px로 줄였을 때 AdSense의 `aswift_1_host`가 800px 폭을 유지해 document scrollWidth가 816px가 된 관찰이 있다. 새로 로드한 360px iframe의 scrollWidth 360px 통과는 그 리사이즈 결함을 없애거나 모든 리사이즈 동작의 통과를 뜻하지 않는다. 이 문제는 표지 CSS의 대비 수정과 구분하며, 광고를 숨기거나 문서 전체의 가로 넘침을 감추는 변경은 요청하지 않는다.

독립 검토 범위에서 같은 공개 글에 표지 대비 수정을 저장하는 데 필요한 변경 부분 확인을 마쳤다. 이 기록은 저장 후 공개 페이지 검증을 대신하지 않는다.

## 로그인 표지 메타데이터 줄바꿈 CSS 후 기록 갱신

현재 `assets/post.css`의 표지 metadata 행에 추가된 flex-wrap·항목 nowrap 규칙이 밝은·어두운 canonical preview 양쪽에 포함된 것을 확인했다. 따라서 prepare_final_qa_v2.py가 현재 CSS로 실행된 후보임을 확인했다. 선택자는 thumbnail 표지의 `.info .desc`와 그 직계 date·category·admin 항목으로 한정되어 있다.

정규화 article_content 해시는 이전 gate와 같으며, 다섯 게시 이미지의 해시도 manifest와 모두 일치한다. 이미 관찰한 본문·이미지·표·목차·테마 검토 결과를 유지했다. 변경되지 않은 본문에 대한 전 페이지 수동 캡처나 원고 심사를 반복하지 않았다.

final-light와 final-dark를 각각 새 Chrome 세션에서 `--include-390`으로 다시 실행했다. 여섯 뷰 모두 페이지 폭과 scrollWidth가 일치하고 이미지 5개 로드·H1 1개·목차 대상 고유성이 유지된다. 현재 여섯 첫 화면 PNG 해시도 이전 승인 캡처와 모두 같다. 인간 판단 필드는 기존 관찰 결과대로 유지하며 현재 후보에 대한 final-page.json 기록을 갱신한다.

이번 metadata 규칙은 canonical preview의 본문에는 적용 대상이 없으므로, 실제 로그인 표지에서 날짜·분류·관리 버튼의 줄바꿈이 해결됐다는 판정은 이후 제공될 라이브 표지 캡처를 확인한 뒤 기록한다. 앞서 확인한 66% 오버레이의 대비 통과와 광고의 resize-only 넘침 관찰은 그대로 유지한다.

## 저장 후 실제 모바일 표지의 독립 확인

변경 부분 판정: **pass**. `artifacts/qa-v2/live/final-mobile-dark-top.jpg`와 `artifacts/qa-v2/live/final-mobile-light-top.jpg`를 직접 열어 저장 후 360px 표지를 확인했다.

두 테마 모두 `2026. 10. 25. 10:14`와 카테고리가 같은 행에서 각 항목의 형태를 유지하고, `수정 삭제 공개` 관리 버튼은 그 아래 한 행에 모여 있다. 날짜·카테고리·관리 버튼이 글자 단위로 세로 분리되던 문제는 보이지 않는다. 세 줄 제목과 흰색 메타데이터가 66% 오버레이 위에서 읽히며, 표지 안에서 잘리거나 겹치지 않는다. 캡처에 게시 시각 10:14가 유지된 것도 확인했다.

출판 담당자가 보고한 live fresh-load 측정은 document width=scrollWidth=360이며, date 120×20px·category 124.25×20px·admin 81.43×20px, 각 항목 nowrap이다. 이 수치는 담당자의 측정으로 구분하고, 독립 검토자는 위 두 실제 캡처에서 그 표시 결과를 확인했다. 본문과 canonical gate 캡처는 다시 생성하지 않았다. 앞서 기록한 광고의 resize-only 넘침과 fresh mobile 통과의 구분도 유지한다.
