# 야베스 HTML/CSS 독립 정적 검토

- 검토일: 2026-09-16입니다.
- 검토자: `/root/jabez_rewrite_review`입니다.
- 대상: `assets/post.css`, `artifacts/qa-v2/final-rendered/`와 `final-dark-rendered/`의 preview 및 fragment HTML 네 파일입니다.
- 최종 정적 판정: `pass`입니다. 최초 미리보기 제목 폭의 문제는 수정되었으며, 6절에 재검토 결과를 기록했습니다. 아래 1절부터 5절은 최초 후보의 검토 이력입니다.
- 범위: HTML 문자열과 CSS 규칙을 읽고 표준 라이브러리 `HTMLParser`로 태그 구조를 검사했습니다. 브라우저, raw CDP, 화면 렌더링, 캡처를 사용하지 않았습니다. 이 기록은 실제 시각 승인이나 최종 페이지 통과가 아닙니다.

## 1. 수정이 필요한 미리보기 제목 폭

두 preview HTML의 14행에는 `.rich-preview-header { width:min(calc(100% - 40px), 1040px); margin:0 auto; }`가 남아 있습니다. 본문은 `article.devlog-rich`에서 `width:100% !important; max-width:760px !important; margin:0 auto !important`로 바뀌었으므로 제목과 본문의 폭과 시작점이 달라집니다.

아래 계산은 preview의 body에 추가 padding이나 border가 없고, 부모 폭과 뷰포트 폭이 같은 경우입니다. 실제 화면 측정값이 아닙니다.

| 부모 폭 | 제목 폭 / 왼쪽 여백 | 본문 폭 / 왼쪽 여백 | 차이 |
|---|---|---|---|
| 360px | 320px / 20px | 360px / 0px | 제목이 본문보다 20px 안쪽에서 시작합니다. |
| 780px | 740px / 20px | 760px / 10px | 제목이 본문보다 10px 안쪽에서 시작합니다. |
| 1280px | 1040px / 120px | 760px / 260px | 제목이 본문보다 140px 바깥쪽에서 시작합니다. |

- 문제: 전체 미리보기의 제목과 본문이 동일한 읽기 열을 사용하지 않습니다. 두 테마에 같은 규칙이 있습니다.
- 최소 수정: 미리보기 제목 영역에도 본문과 같은 폭과 좌우 여백 정책을 적용합니다. 현재 본문 규칙을 유지한다면 header도 `width:100%; max-width:760px; margin:0 auto`로 맞출 수 있습니다. 모바일 바깥 여백을 따로 두려면 제목과 본문을 동일한 부모 안에서 함께 처리해야 합니다.
- 재검증: 후보를 다시 만든 뒤 두 preview의 header와 article 폭 규칙을 대조해야 합니다. fragment에는 preview header가 없으므로 이 문제는 붙여넣기용 본문 fragment에 직접 적용되지 않습니다.

## 2. 본문 폭과 CSS 우선순위

공통 CSS 뒤에 현재 `post.css`가 정확히 한 번 포함되어 있습니다. 공통 CSS의 980px canvas, 916px figure 폭, section의 데스크톱 좌우 32px·모바일 20px padding 규칙은 파일에 남아 있지만 현재 요소에서는 뒤의 글별 규칙이 이를 덮어씁니다.

- `article.devlog-rich`의 100% 폭과 760px 최대 폭이 공통 `.devlog-rich` 폭보다 우선합니다.
- 직계 section의 폭은 100%이고 padding은 0입니다. 이 선언은 `!important`이므로 공통 section 규칙과 735px 이하 미디어 규칙에서도 좌우 padding이 되살아나지 않습니다.
- 직계 p·h2·ol·blockquote와 figure·toc는 같은 100% 폭과 좌우 margin 0을 갖습니다. figure의 인라인 `--rich-media-width:916px`는 남아 있지만 최종 width 선언이 해당 변수를 사용하지 않으므로 이 후보의 figure 폭을 넓히지 않습니다.
- `.devlog-rich, .devlog-rich *`의 `box-sizing:border-box`가 인용과 목록의 padding을 요소 폭 안에 포함합니다. 현재 HTML에는 별도의 좁은 wrapper, 좌우 transform, position 이동 또는 float 규칙이 없습니다.
- 부모 콘텐츠 폭이 각각 360·780·1280px이면 article과 section의 폭은 360·760·760px입니다. p·h2·figure의 외곽 폭도 이 값과 같습니다. 이는 현재 규칙으로 계산한 값이며 실제 Tistory 스킨의 추가 규칙까지 관찰한 결과는 아닙니다.
- 735px 미디어 쿼리는 부모 폭이 아닌 뷰포트 폭을 기준으로 합니다. 글별 미디어 규칙은 h2 글자 크기만 28px에서 26px로 바꾸며 열 너비는 바꾸지 않습니다. 좁은 부모가 넓은 뷰포트 안에 있을 때에도 본문 폭은 부모를 따릅니다.
- 공통 CSS의 620px table 최소 폭, 모바일 720px 이미지 스크롤 규칙은 현재 HTML에 해당 요소나 class가 없어 이 후보의 열 폭에 영향을 주지 않습니다.

## 3. 세로 간격과 의도한 내부 여백

- 직계 section의 margin을 0으로 초기화한 다음 인접 section의 위 margin을 40px로 지정합니다. 목차 section은 같은 우선순위에서 뒤에 선언한 28px 위 margin을 사용합니다. 따라서 소개와 목차 사이는 28px, 목차 이후 본문 및 본문 절 사이는 40px라는 예외가 있습니다.
- 본문 p와 h2는 좌우 padding 0, 아래 margin 18px를 사용합니다. 마지막 p는 아래 margin 0입니다. 일반 본문 절 마지막 p와 다음 section의 시작을 합쳐 불필요한 별도 아래 여백이 추가되는 규칙은 없습니다.
- blockquote 외곽은 본문과 정렬되고, 내부는 좌우 20px padding과 왼쪽 3px border를 가집니다. 따라서 텍스트 시작점은 본문보다 23px 안쪽이며, 콘텐츠 폭은 열 폭에서 43px를 뺀 값입니다. 360px 열에서는 317px입니다. 인용을 구분하기 위한 내부 여백으로 판단했습니다.
- 본문 ol의 `padding-left:1.45em !important`는 유지됩니다. 본문 목록 글자 크기 17px에서는 왼쪽 내부 여백이 24.65px이며 decimal outside 번호가 이 공간에 배치되도록 선언되어 있습니다. 실제 글리프 위치를 측정한 것은 아닙니다.
- 목차 ol은 글자 크기 16px를 사용하므로 공통 `1.45em !important`가 23.2px로 적용됩니다. 뒤의 일반 `padding-left:22px`보다 `!important`가 우선합니다. 목차 항목 텍스트와 본문 목록 텍스트의 시작점은 각각의 번호 여백만큼 안쪽이며, 외곽 읽기 열의 불일치와 구분해야 합니다.
- 본문 목록 항목 사이의 `0.4em !important`는 6.8px이고 목록 위·아래 margin은 20px입니다. 목록 다음 p의 margin-top은 더 구체적인 글별 `0 !important`가 공통 `1.15em !important`보다 우선하므로 목록 아래 20px가 기준입니다.

## 4. HTML 구조와 내용 잔존 검사

네 HTML 파일에서 다음 결과를 확인했습니다.

- 시작·종료 태그 stack 불일치와 미종결 태그를 발견하지 못했습니다. p 안의 article·section·figure·blockquote·ol·h2 중첩 및 ol/ul 바깥의 li도 없습니다. 이는 사용한 정적 검사 범위이며 전체 HTML 명세 적합성 인증은 아닙니다.
- article은 1개, section은 6개, 본문 h2는 4개, figure와 img는 각각 1개입니다. 목차 4항목과 기도 4항목으로 ol은 2개, li는 8개입니다.
- 두 preview는 H1 1개, 두 fragment는 H1 0개입니다. 중복 ID와 존재하지 않는 목차 목적지가 없습니다.
- article 내부 p의 강제 br은 0개입니다. br 2개는 기도 인용의 장절·번역과 본문 사이에 있습니다.
- 이전에 삭제한 인물 평가 동어 반복과 이름 절의 재요약, `야베스라는 이름의 장소` 소제목이 남아 있지 않습니다. 현재의 네 소제목과 인물 소개, 기도 풀이, 응답·묵상 구성이 들어 있습니다.
- 두 테마의 fragment는 바이트가 같고, 네 파일의 article HTML도 같습니다. 각 파일에 현재 `post.css`가 한 번 들어 있습니다.
- article 내부에 로컬 파일 경로나 미해결 media 지시자가 없습니다. 이번 검토에서는 원격 이미지에 접속하지 않았습니다.

## 5. 스킨에 미치는 범위와 남은 한계

붙여넣기용 fragment의 CSS에는 일반 `body`, `html`, 독립적인 `p` 같은 전역 요소 선택자가 없습니다. `.devlog-rich`나 `.devlog-rich__*` 계열 class를 대상으로 하므로 통상적인 스킨 내 다른 본문·메뉴·버튼으로 직접 적용될 규칙은 발견하지 못했습니다. preview에만 들어 있는 html/body 규칙은 fragment에 포함되지 않습니다.

다만 `post.css`의 선택자는 야베스만의 고유 ID가 아니라 공유 class를 사용합니다. 같은 페이지에 다른 `article.devlog-rich`가 함께 존재하면 그 article에도 760px 제한과 section 여백 제거가 적용됩니다. 현재 후보는 article 하나이므로 이 현상이 발생하지 않습니다. 한 페이지에 여러 rich article을 삽입하는 구성이 필요하다면 고유 class나 ID로 범위를 좁혀야 합니다.

실제 hELLO 스킨의 추가 CSS가 가져올 우선순위, 부모의 실제 여백, 글꼴에 따른 줄바꿈, 번호의 시각적 위치와 어두운 테마의 대비는 이번 정적 검토에서 확인하지 않았습니다. 브라우저 보안 제한을 우회하지 않았으며 정적 결과로 시각 승인을 대신하지 않습니다.

최종적으로 현재 본문 fragment의 단일 읽기 폭 규칙은 일관되지만, 두 전체 preview의 제목 폭은 수정이 필요합니다.

## 6. 제목 폭 수정 후 정적 재검토

작성자가 다음 선택자에 `width:calc(100% - 40px) !important`, `max-width:760px !important`, 좌우 margin auto를 추가한 뒤 `post.css`와 새 HTML 네 파일을 확인했습니다.

```css
body > header.rich-preview-header,
body > header.rich-preview-header ~ article.devlog-rich
```

두 preview에는 body 직속 `header.rich-preview-header`가 하나씩 있으며, 해당 header 다음에 같은 body의 article이 있습니다. 둘 사이의 style 요소가 있어도 일반 형제 선택자 `~`는 article을 선택합니다. 새 article 선택자의 구체성 `(0,2,3)`은 뒤에 나오는 기본 `article.devlog-rich`의 `(0,1,1)`보다 높습니다. 두 width가 모두 `!important`여도 미리보기 전용 `calc` 규칙이 우선합니다. header 역시 기존 일반 width보다 새 `!important`가 우선합니다.

| preview body 폭 | 제목과 본문의 공통 폭 | 공통 왼쪽 여백 |
|---|---|---|
| 360px | 320px | 20px |
| 780px | 740px | 20px |
| 1280px | 760px | 260px |

이는 CSS의 정적 계산이며 실제 화면 측정값은 아닙니다. 제목과 본문이 같은 폭·여백을 사용하므로 1절에서 지적한 시작점 불일치가 해결됩니다. 본문 자식의 단일 열 규칙과 인용·목록의 내부 여백은 유지됩니다.

fragment에는 선택자의 기준인 `header.rich-preview-header`가 없으므로 미리보기 전용 폭 규칙이 적용되지 않습니다. Tistory 부모가 제공하는 콘텐츠 폭을 기준으로 기존 `width:100%; max-width:760px`를 사용합니다. 새 선택자에 body가 포함되어 있지만 body 자체를 스타일링하는 선언은 아니며, 지정한 class와 관계를 만족하는 header 또는 article만 대상으로 합니다. 동일한 class를 가진 body 직속 미리보기 header를 Tistory 페이지가 별도로 사용한다면 선택될 수 있으나 현재 fragment에는 그런 요소가 없습니다.

HTMLParser로 새 네 파일의 태그 stack도 다시 검사했으며 불일치와 미종결 태그가 없습니다. 현재 post.css는 각 파일에 정확히 한 번 포함되어 있고, 네 파일의 article HTML은 SHA-256 `2566265575e01533526c314c88c6c3e20c96024853eb319a7a7c7eb1c26ed9db`로 같습니다.

최종 정적 검토 판정은 `pass`이며 이 검토 범위에서 남은 수정 요구는 없습니다. 스킨과 글꼴을 포함한 실제 화면, 대비, 줄바꿈, 시각적 간격은 검증하지 않았습니다. 브라우저 또는 다른 화면 렌더링 수단을 사용하지 않았으며 최종 시각 승인과 구분합니다.
