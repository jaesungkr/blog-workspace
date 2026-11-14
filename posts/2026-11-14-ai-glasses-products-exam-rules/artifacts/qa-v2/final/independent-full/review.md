# 최종 native 첨부 연결 페이지 독립 검토

2026-11-14 UTC / Codex independent_article_review final native-bound page / **final local page pass**.

## 실행과 범위

적용 final-page-qa-v2.md를 다시 읽고 canonical `capture_rich_qa_v2.py --mode final-light`와 `--mode final-dark`를각각별도freshChrome세션에서실행했다. workflow-v2.json의include_390=true를확인하고두명령에--include-390을적용했다. canonical browserreceipt/첫viewportPNG6개는 bundle `artifacts/qa-v2/final/{light,dark}/`에있다. 자동receipt의이미지loaded만으로시각판정하지않았다.

기본PNG는첫viewport만담으므로원격CDN이연결된동일canonical light/darkHTML을별도스크립트로1280/360/390fullraster6개추가캡처했다. full6개를모두view_image로실제열어처음부터끝까지읽었다. 마지막승인결말까지누락·겹침·잘림없음. 그림3종의순서/캡션/연출범위,한국/해외가격조건,국내제재와미국·국제시험절,목차5개와번호마커를확인했다. 새source결함은발견하지못했고원고를재편집하지않았다.

6profile모두document scrollWidth=clientWidth이며previewH1하나·고유TOCtarget5개·remote이미지3개다. 양theme본문/링크/강조/캡션/표색대비가읽히고이미지주변은중립색이다. inline figure폭style와native wrapper표현이유지된다. 코드블록·본문인용/요청상자는이글에없으므로그검사범위를허위로추가하지않는다. 절차형문서가아니며사용자가명시삭제한개인준비체크를다시요구하지않았다.

## 표의 숨은 열

desktop표2개는폭760/760,360은320/620,390은350/620이며내부가로스크롤이다. full에서보이지않는360마지막열을양theme각표오른쪽끝으로이동해focused4개로확인했다. 유형표답변방식과가격표판매상태의마지막행끝까지읽을수있다. 페이지전체overflow를숨기는새CSS는추가하지않았다.

## 대표사진 paint 관찰 — full blank와 정상 focused 모두 보존

전체full6개중light3개는대표안경/Even/삼성사진실제픽셀이정상이다. darkfull3개는대표사진의밝은상자만남는paint누락을보였다. 기존문제라고자동승인하지않았다.

동일최종CDN미리보기의canonical첫viewport dark1280/360/390에서는안경픽셀이실제로보였다. fullblank를본뒤지침에따라dark360의대표사진을viewport중앙으로가져와**focused딱1회**촬영했고 `dark-lead-focus-once.png`에서검은안경전체와정중체캡션을직접확인했다. natural874×492/bounds320×181과decode성공은보조기록일뿐통과근거를대신하지않는다. fullblank·정상canonical첫viewport·정상focused를함께보존하고capture paint omission으로구분한다. 정상결과를얻기위해반복찍거나CSS/원본사진을바꾸지않았다. dark의Even/삼성사진은full에서도정상이다.

## canonical fragment와 기록

HTMLParser/텍스트검사로native발행fragment H1=0,devlog-rich wrapper1,section7,tablewrapper2,native mediawrapper3,local경로0,미해결media/TODOplaceholder0을확인했다. Tistorynative imageblock문자열이포함되어있으며이를미해결자리표시자로오인하지않았다. preview이미지URL은관측된CDN이며finalrecord가렌더러/CSS/source/media/remote-fetch/receipt해시와canonicalfragment재현을검증한다.

final-measurements.json에서human필드만수정했다:6viewport의readable_media/status,fragmentstatus,dark contrast/inline_styles/image_surrounds/status. width와자동fragment수치는보존했다. `record_final_page_v2.py`실행은exit0으로성공해canonical`artifacts/qa-v2/final-page.json`을생성했다.

- final-page.json SHA256: `39dbe70c7408fea7c0046de9855007f9966840f930cd2f96a58c15c8a0fd796a`
- article 파일: `1c0841b7957ba8b2e319157261ec97a74419f130ea8c58d65189fcc4a3f5a906`
- article lifecycle-normalized content: `8313eeb146cba4415b2bd269922ca2b9a3484c6e4b893c45e4deca53b13df863`
- lightpreview: `66ad9e5b898d849a0c83d0b65c88599de0ead8c38bee37eadfc0d4dfe3588c51`
- darkpreview: `7256577a501cf30101e6064c9984a0ba04878140e5aaeb0c5444374e58d63b11`
- nativefragment: `de9bc6b1e78c6b3786b301c857ce2c667d0b7bcc393fa0143dd2726723ffb628`
- media: `7431dbe63530a9cc9510a35aceeeb58222b376c96488c11629106fa094a5366f`
- renderer: `ff20392d99ceafa4615fc7a5f1cf4828ed0e8f12eb738c0288b111f5c16a4a51`
- CSS: `dd5bcf036ad48a3bef81bfcf19ff388db79c68f3b49ee5b7a082ec2185b61c47`

## 플랫폼 확인과 구분

이것은독립canonicalremote final-page검토다. 내가실제Tistoryeditor native미리보기를직접조작·판독했다는뜻은아니다. 작성자는별도actualChrome nativepreview1280/360에서alt3개·사진3개·목차5개·articleoverflow0,입력HTMLexactparity를확인했다고전달했다. nativepreview테마버튼이html.dark로전환되지않은한계도전달받았으며이를정상native dark검사로기록하지않는다. canonical dark최종검사와그플랫폼관찰은별개다. 실제발행/성공URL확인및finalizer는작성자가이어간다. 나는게시·Git·Library작업을수행하지않았다.
