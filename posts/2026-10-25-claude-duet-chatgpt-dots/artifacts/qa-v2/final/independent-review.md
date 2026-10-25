# 단일 독립 최종 페이지 검증

- 검토자: /root/source_review
- 확인일: 2026-10-25 Asia/Seoul
- 최종 판정: **final-page pass**
- 정식 승인 기록: artifacts/qa-v2/final-page.json
- 범위: canonical 원격 이미지 라이트·다크 후보의 독립 페이지 검증입니다. 본문·미디어·CSS·첨부코드를 변경하거나 편집 검증을 다시 시작하지 않았습니다. 실제 Tistory 편집기 변환과 게시 후 공개 페이지 확인은 별도로 수행해야 합니다.

## 실제 실행

1. final-page-qa-v2.md와 media-release-v2.md, workflow-v2.json과 저자의 구체적인 게시 승인 기록을 읽었습니다.
2. capture_rich_qa_v2.py를 --mode final-light와 --mode final-dark, --by /root/source_review로 각각 실행했습니다. Chrome/155.0.8059.85의 서로 다른 새 세션에서 1280×900·360×800 실제 캡처와 hash-bound browser-capture.json 두 개를 만들었습니다. 조건부 390·768은 라우팅되지 않아 추가하지 않았습니다.
3. 네 canonical 뷰포트 캡처를 직접 열었습니다. 이미지가 첫 화면 아래에 있어 동일한 원격 후보를 새 독립 보조 세션에서 다시 열고 전체 페이지·Duet·Dots·표와 모바일 스크롤 양끝을 캡처했습니다. supplemental/observations.json에 후보 해시·이미지 로딩·표시 크기·스크롤 폭을 기록했습니다.
4. 네 전체 캡처, 두 테마의 모바일 Duet, 데스크톱 Dots, 모바일 Dots의 좌우 끝, 모바일 표의 좌우 끝과 데스크톱 표를 직접 열었습니다. 긴 모바일 전체 캡처는 원래 픽셀 크기의 읽기 구간으로 나눈 검사 이미지에서도 모든 본문 구간을 확인했습니다. 원본 캡처와 후보 파일은 변경하지 않았습니다.
5. final-measurements.json에서는 readable_media·status와 다크 테마의 contrast·inline_styles·image_surrounds 등 사람 판단 필드만 채웠습니다. 자동 측정값을 덮어쓰지 않았습니다.
6. record_final_page_v2.py를 canonical 라이트·다크·fragment와 측정 파일로 실행했고, 현재 렌더러 출력과 후보 해시의 일치를 검증한 final-page.json이 생성됐습니다.

## 직접 확인한 사항

- 네 뷰포트에서 제목과 본문이 화면 안에 들어오며 페이지 전체의 가로 넘침이 없습니다. 미리보기 H1은 하나이며 목차 7개 대상은 각각 유일합니다. 실제 목차의 숫자·링크와 줄바꿈, 목록 뒤 여백이 보입니다.
- 두 원격 이미지가 실제 픽셀로 그려져 있습니다. 전체 캡처와 근접 캡처에 빈 이미지 영역이 없고, Duet의 Ready for review·Needs input·Working과 Tasks 탭을 모바일에서 확인할 수 있습니다. 캡션이 이미지에 붙어 있고 홀로 남은 음절이나 인접 문단 겹침이 없습니다.
- Dots는 모바일에서 원래 600px 폭을 유지하고 320px 영역 안에서 가로로 스크롤됩니다. 왼쪽의 대화 시작과 오른쪽의 사용자 질문·답변 끝을 실제로 노출했습니다. 좌우로 움직이는 것은 이미지 영역뿐이며 캡션과 본문은 고정돼 있습니다.
- 표는 데스크톱에서 세 열이 모두 보이고, 모바일에서는 620px 표를 320px 영역 안에서 좌우로 읽습니다. 양끝 캡처에서 항목·Duet·Dots 헤더와 모든 행을 확인했습니다. 표 스크롤 안내도 보입니다.
- 전체 페이지의 절 배경과 문단·제목·링크 간격을 확인했습니다. 다크 테마의 본문과 출처 링크·캡션은 읽을 수 있고, 공식 이미지의 흰 배경과 UI 픽셀은 바뀌지 않았습니다. 주변은 중립적인 어두운 바탕이며 이미지 위에 반전 필터를 적용한 모습이 없습니다.
- fragment는 H1 0개, native 이미지 블록 2개이며, 두 블록의 alt가 media.json과 일치합니다. 캡처한 원래 첨부코드가 fragment에 그대로 포함됩니다. 미해결 미디어 토큰·file URI·사용자 절대 경로·상대 asset src가 없습니다.
- 코드 블록은 이 원고에 없어 코드 가로 스크롤은 해당하지 않습니다. 이 글은 제품 소개·비교이므로 절차 가이드의 ‘첫 안전 조치’ 게이트는 해당하지 않습니다.

실제 페이지 결함이나 미해결 시각 문제는 발견하지 못했습니다. 이 단일 승인은 정확한 원격 이미지 후보에만 적용되며, 이후 본문·미디어·CSS·첨부코드가 바뀌면 스킬에 따른 재검증이 필요합니다.

## 최초 승인한 후보 해시(이력)

- preview_sha256: fa3d2db7300bd9d116180b5b41b516f52442664e515cd5a1c6ca4c71ba4ed402
- dark_preview_sha256: 641ee4400dbc088faa8bb41cdd1f02c47e90879fcfefa747e056515947c999fb
- fragment_sha256: da651d59f716470e7ef8636910c06f35057a3a8863e1aa77b23e1952fa044f5f
- article_content_sha256: 720b8d470c911097299b0b201ea20f609ad533396b1136dd1c94679fee6692b5
- media_sha256: 26d2fd5185d0fcf02f97818e95a657bbd16114c38a794fcdc54e36f9df83bc96

## 자동 커버 CSS 수정 후 최종 증거 갱신

- 변경 범위: assets/post.css의 게시물 media-id에 한정한 hELLO 자동 커버 숨김과 제목 영역의 라이트·다크 배경/글자 색입니다.
- 본문 정규화 해시와 media.json 해시가 최초 최종 승인 기록과 같은지 확인했습니다. 원고 편집 검증을 다시 열거나 본문·미디어·CSS·첨부코드를 수정하지 않았습니다.
- 변경된 post.css가 들어 있는 두 canonical 후보에 지정된 capture_rich_qa_v2.py를 각각 실행했습니다. 라이트·다크는 다시 서로 다른 새 세션이며 1280×900·360×800 네 캡처와 receipt를 갱신했습니다. 최신 네 실제 캡처를 직접 열어 제목·본문 대비·줄바꿈·페이지 폭과 상단 배치를 확인했습니다. 자동 관찰에서도 페이지 폭, H1 1개, 목차 대상 유일성, 두 원격 이미지 로딩이 통과했습니다.
- 변경되지 않은 본문·미디어와 표·Dots 스크롤의 기존 실질 검토를 재사용했습니다. 현재 수정은 해당 본문 구성요소에 적용되지 않는 게시물 헤더 selector이며, 사용하지 않은 이전 후보 해시를 새 최종 승인으로 복사하지 않았습니다.
- fragment에 H1·로컬 경로·미해결 토큰이 없고 native 이미지 블록 두 개가 남아 있는지도 확인했습니다. record_final_page_v2.py를 다시 실행해 현재 후보 해시와 새 receipt를 묶은 final-page.json을 생성했습니다.
- 현재 독립 후보 gate 판정: **final-page pass**.
- 경계: standalone canonical 미리보기에는 실제 hELLO의 자동 커버 DOM이 없습니다. 따라서 실제 공개 페이지에서 커버가 숨겨지고 제목 대비가 고쳐졌다는 판정은 이 기록에 포함하지 않습니다. 그 변경부는 루트가 같은 공개 URL의 실제 스킨에서 확인해야 합니다. 별도 중복 게시·편집기 조작·Git 작업은 수행하지 않았습니다.

### 현재 승인한 후보 해시

- preview_sha256: 5d612add4f07f6555da52c39156161dca7d78380935016a5ff06fb4c743d9349
- dark_preview_sha256: a82df64222040fc2b2e7def1c22b9e1fc70dab838a7569bee6beba0ea0c75f48
- fragment_sha256: 1c97a2b7a4f8c64e4d228485e91d7aee7c4c45be3dff352784647f37537d907b
- article_content_sha256: 720b8d470c911097299b0b201ea20f609ad533396b1136dd1c94679fee6692b5
- media_sha256: 26d2fd5185d0fcf02f97818e95a657bbd16114c38a794fcdc54e36f9df83bc96
- post.css SHA-256: 2b1f8058f011984f602bbaaee47cec6c57b9bf778e27c123ff8833b6ccfd214f

## 모바일 게시물 메타데이터 줄바꿈 CSS 수정 후 갱신

- 변경 범위: 글의 media-id에 한정한 hELLO 헤더 .desc의 flex-wrap·중앙 정렬, .date·.category·#admin의 nowrap과 flex-shrink:0입니다. 본문과 미디어 해시는 직전 승인과 동일합니다.
- 이전 final-page 기록, 두 receipt와 네 실제 캡처는 final/metadata-wrap-revision/before/에 보관했습니다.
- 최신 canonical 후보에 지정 캡처 도구를 두 테마별 새 세션으로 다시 실행했습니다. 1280×900과 360×800 네 캡처를 직접 열어 제목과 본문 색·폭·줄바꿈이 유지되는지 확인했습니다. 페이지 가로 넘침 없음, H1 1개, 목차 대상 유일, 원격 이미지 두 개 로드가 자동 측정과 일치합니다.
- 변경되지 않은 본문과 이미지·표·스크롤의 기존 실질 검토는 유지했습니다. source review를 다시 시작하거나 원고·CSS·첨부코드를 수정하지 않았습니다. fragment의 native 블록 2개와 H1·로컬 경로·미해결 토큰 부재도 재확인했습니다.
- record_final_page_v2.py를 현재 후보와 새 receipt로 실행해 단일 final-page gate를 다시 생성했습니다. 판정은 **final-page pass**입니다.
- standalone 후보에는 hELLO의 작성자 관리 버튼·날짜·카테고리 헤더 DOM이 없으므로, 실제 작성자 화면에서 이 요소들의 줄바꿈이 고쳐진 결과는 루트의 같은 공개 URL 라이브 검증으로 확인해야 합니다.

### 현재 최종 후보 해시

- preview_sha256: 3523f606efe3a43ff7dbfe03092489d1b69b8c049b80c183d66daf7f948ac850
- dark_preview_sha256: 077b6872ff56e0ad09f544fed1a34f5fe49bd01f31eaf7b661037d749eeff158
- fragment_sha256: 2dee9bba91f05de6bf9b3884c9a01b101d1638bdc63b028c65394c809837f2ff
- article_content_sha256: 720b8d470c911097299b0b201ea20f609ad533396b1136dd1c94679fee6692b5
- media_sha256: 26d2fd5185d0fcf02f97818e95a657bbd16114c38a794fcdc54e36f9df83bc96
- post.css SHA-256: 24c5ddf0b58ecf4845e606da21be37aa930eacc1e9c3b4d88008fbbecf20a4b4
