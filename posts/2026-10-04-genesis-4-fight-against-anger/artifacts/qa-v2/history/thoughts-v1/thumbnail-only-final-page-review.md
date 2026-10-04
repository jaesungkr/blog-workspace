# 썸네일 전용 최종 페이지 독립 검수

- 판정: `pass`
- 검수자: `thumbnail_review`
- 범위: 사용자 명시 요청에 따른 본문 이미지 없는 Tistory 본문입니다. 썸네일은 별도 자산입니다.
- 상태 경계: 엄격한 v2 본문 media gate를 통과했다는 판정이 아닙니다. 본문 lead와 CDN 조건은 사용자 요청으로 해당하지 않습니다. ready 변경과 Git 작업은 수행하지 않았습니다.

## 실제 브라우저 증거

`final-page-qa-v2.md`를 읽고 stock `capture_rich_qa_v2.py`를 final-light와 final-dark 모드로 각각 실행했습니다. 두 명령 모두 `one or more remote images did not load; preview contains no images` 조건으로 실패했습니다. 본문 이미지가 없는 요청에서는 이 조건을 충족할 수 없습니다.

원본 스킬과 checker를 수정하지 않고, 기존 capture 모듈과 실제 Chrome을 사용하는 `thumbnail-only-capture-adapter.py`로 캡처했습니다. 이 어댑터는 본문 이미지 개수가 정확히 0인지 확인하고, 미디어 로딩 조건을 해당하지 않는 조건으로 처리합니다. document 준비 상태, 정확한 viewport, 가로 넘침, H1 개수, 목차 대상 중복은 그대로 확인합니다. 별도 세션에서 두 테마를 열어 기본 viewport와 전체 페이지 래스터를 저장했습니다. stock pass receipt는 생성하지 않았으며, 파일 이름에도 `thumbnail-only-browser-capture.json`을 사용했습니다.

| 테마 | viewport | 전체 래스터 | 가로 넘침 | H1 | 목차 대상 |
|---|---|---|---|---|---|
| light | 1280 × 900 | 1280 × 4606 | 없음 | 1개 | 3개, 모두 고유함 |
| light | 360 × 800 | 360 × 7467 | 없음 | 1개 | 3개, 모두 고유함 |
| dark | 1280 × 900 | 1280 × 4606 | 없음 | 1개 | 3개, 모두 고유함 |
| dark | 360 × 800 | 360 × 7467 | 없음 | 1개 | 3개, 모두 고유함 |

Chrome 버전은 `Chrome/154.0.8037.93`입니다. 두 테마의 세션 ID는 다릅니다. 원본 capture 모듈과 별도 어댑터의 해시를 receipt에 기록했습니다.

## 직접 열어 확인한 결과

네 전체 페이지 이미지를 모두 열고, 전체 이미지가 화면에 축소되어 보이는 점을 고려하여 원본 래스터를 연속 구간으로 잘라 추가로 확인했습니다. inspection 파생본은 확인 후 삭제했으며 실제 전체 캡처와 viewport 캡처는 보존했습니다.

- 첫 화면: 제목은 한 개이며 360px에서 두 줄로 정상 줄바꿈됩니다. 도입 문단과 세 항목의 목차가 읽히며, 제목이나 목차가 잘리지 않습니다.
- 성경 본문: 1절부터 14절까지 실제 화면에 모두 표시됩니다. 각 절의 번호와 절 사이 간격이 유지됩니다. 긴 7절과 14절도 화면 안에서 줄바꿈되며, 본문이 가로로 밀리거나 고정 높이에 잘리지 않습니다.
- 설교 요약: 회색 바탕의 구역 안에서 본문과 굵은 소제목을 구분할 수 있습니다. 세 인물과 세 권면의 번호가 표시되고, 모바일에서 긴 굵은 소제목이 두 줄로 넘어가도 글자가 겹치지 않습니다. 번호는 Markdown 강조 문단으로 표현됐으며 실제 순서 목록이라고 잘못 기록하지 않았습니다.
- Thoughts: 모든 문단과 마지막 적용 문장까지 표시됩니다. 문단 사이 간격이 유지되고, 요약 구역과 묵상 구역이 시각적으로 구별됩니다.
- dark: 기본 본문과 요약 구역에서 글자 대비가 충분히 보입니다. 파란 목차 링크가 구별되고 제목·강조 글자·문단 간격이 유지됩니다. 본문 이미지가 없으므로 image surround는 해당하지 않습니다.
- 그림·표·코드: 본문에는 존재하지 않으므로 캡션 연결과 가로 스크롤 검사도 해당하지 않습니다.

관찰된 페이지 결함이나 원문 단계로 돌려보낼 텍스트 결함은 없었습니다. source-review의 편집 심사를 반복하지 않았으며, 원본 텍스트와 CSS를 수정하지 않았습니다.

## 바이트와 승인 연결

light와 dark fragment는 바이트가 같습니다. fragment H1은 0개이고, 본문 이미지도 0개입니다. 미해결 media placeholder와 로컬 경로는 없습니다. `source-pass.json`은 pass이며, 현재 article의 `article_content_sha256`이 source pass의 값과 일치합니다.

`thumbnail-only-final-page.json`에 source pass, article content, 두 preview, fragment, measurements, 두 receipt와 여덟 실제 캡처의 SHA-256을 함께 기록했습니다. receipt에 기록된 preview와 screenshot 해시를 실제 파일에서 다시 계산해 일치 여부를 확인했습니다. 승인한 정확한 바이트가 바뀌면 이 승인을 그대로 사용할 수 없습니다.

## 전달

`final-measurements.json`에는 직접 확인한 human 판정과 검수자 이름을 기록했습니다. 본문 미디어와 image surround에는 `not_applicable`을 사용하여 엄격한 stock 미디어 gate를 통과한 것처럼 표시하지 않았습니다. 이번 결과는 사용자 요청에 따른 썸네일 전용 예외 페이지 승인입니다. 실제 Tistory에 붙여넣은 후 hELLO 테마와 공개 페이지의 상태는 사용자 preview 및 live URL 검수에서 별도로 확인해야 합니다.
