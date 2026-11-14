# 승인 결말 렌더 영향 독립 검토

검토일2026-11-14 UTC / independent_article_review / **affected render pass (local preflight)**.

이번변경은승인된마지막문단뿐이다. 본문을수정하거나새조사·Git·Library·게시작업을하지않았다. source는같은디렉터리 source-review.md에서별도pass다.

## PDF 종료 쪽 — pass

현재 `approved-closing/pdf-final/page-07.png`를원본그대로view_image로열어실제PDF페이지를확인했다. 미국SAT/ETS소제목과두규정문단뒤에사용자승인결말두문장이같은쪽에있다. 결말이8쪽으로밀리거나마지막한줄만고립되지않는다. 한글깨짐·줄잘림·글자겹침·footer침범은없고,아래여백과`dev.log · 검토본 7/7`쪽번호가정상이다. 승인문구가페이지끝에서생략되지않는다.

1~6쪽은새PNG와직전독립검토본 `exam-context-revision/pdf-final/page-01.png`~`06.png`의바이트를각각대조해6개모두정확히같음을확인했다. 따라서이미직접열어검토한첫6쪽의사진3종·표2개·수능/TOEICSW조건결과를재사용한다. 이번에7쪽전부를새로시각판독했다고쓰지않는다. 텍스트추출순서나스크린리더접근성의새판정도아니다.

## HTML 종료 부분 — pass

`capture_closing_impact.py`를독립실행해최신embeddedHTML의 light/dark1280×900,360×800을각각열고마지막섹션의문서좌표영역을새로캡처했다. `independent-{light,dark}-{1280,360}-closing.png`4개모두원본그대로view_image로열었다. 한화면보다긴360종료영역은captureBeyondViewport문서clip이며전체글6프로필캡처의새재검증으로표현하지않는다.

- 마지막TOEFL문단과결말사이의문단간격이유지된다. 결말은기존과같은본문서체/색으로보이며추가소제목·별도상자·체크리스트가생기지않았다.
- desktop에서는2줄,360에서는자연스럽게여러줄로감기며두문장끝까지보인다. 글자가겹치거나화면옆으로나가지않는다.
- dark본문/링크/결말대비가읽을수있고,반전·투명글자·밝은배경잔여는없다.
- 독립계측4개모두문서가로넘침0이다. DOM기록의마지막두문장도source와같다.

증거는같은디렉터리의PNG4개, `independent-impact-receipt.json`과재현스크립트다. 나머지영역은직전 `exam-context-revision/render-review.md`의독립전체검토와현재Chrome실화면관찰기록을재사용한다. 대표사진은이번결말영향캡처에포함되지않으며이번에다시정상표시를확인했다고쓰지않는다. 과거headlessdark이미지의간헐paint제한과작성자Chrome정상관찰은그대로남아있다.

## 바인딩 해시

- article: `1c0841b7957ba8b2e319157261ec97a74419f130ea8c58d65189fcc4a3f5a906`
- brief: `a1701be45c03f033cff8b1e1acaeb7e3e5f383fba11232f574675f527db0d07a`
- evidence: `5837c6c8e506abc784f17b5bc70d138ea68fc365b1a64800d705c7030cef220b`
- embedded lightHTML: `16561a26a8fa1e137c8369a62f33de8d46c3d6b78eb28d453cece9d0195d0430`
- embedded darkHTML: `028ac1dfac5b2d91341467a6b1f152826926c2374a0ef9e15cee54986a5224ee`
- `exports/ai-glasses-products-exam-rules-mobile-review.pdf`: `7f134504aa681bad2ff683dd035b2791bd1515701e57f99ca96ef8005bfa18b3`

수정필요점은없다. 영향영역검토와미변경영역의이전검증을합쳐로컬preflight를유지할수있다. nativeTistory이미지첨부·CDN·최종플랫폼미리보기·실제게시성공까지통과한판정은아니다.
