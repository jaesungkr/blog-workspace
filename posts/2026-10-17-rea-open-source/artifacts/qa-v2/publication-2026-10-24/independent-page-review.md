# REA 원격 이미지 후보 페이지 독립 판독

- 검토자: /root/rea_source_review
- 검토일: 2026-10-24
- 범위: 부모 에이전트가 CUA로 촬영한 canonical remote light/dark 후보의 독립 시각 판독과 HTML 대조
- 시각 판정: 관찰한 네 페이지는 pass
- strict v2 final-page record/finalizer: 미실행, 통과로 기록하지 않음
- 코드 가로 조작: 추가 CUA 화면과 DOM에서 성공 확인
- native preview 추가 판정: light/dark 1280/360 관찰 pass, dark PC 초기 흰 화면은 정상 캡처로 재확인

## 직접 읽은 자료와 수행 구별

remote-light-1280.jpg·remote-light-360.jpg·remote-dark-1280.jpg·remote-dark-360.jpg를 실제로 열어 전체 페이지를 읽었습니다. 각 360px 원본 전체 캡처는 길이가 길어 도구가 한 번에 표시할 때 축소하므로, 원본 픽셀을 유지한 3개 세로 구간으로 나누어 두 테마의 여섯 구간을 다시 열었습니다. independent-inspection-bands/에 해당 PNG를 보존했습니다. 원본 screenshot을 축소하거나 보정하지 않았습니다.

remote-cua-measurements.json을 읽고 canonical final-rendered/final-dark-rendered HTML과 final fragment를 직접 파싱했습니다. 부모의 통과 설명만으로 승인하지 않았습니다. 실제 CUA 캡처와 DOM 관찰은 부모가 수행했고, 그 자료를 제가 독립적으로 판독했습니다. 제 에이전트 환경에는 CUA 브라우저가 없어 직접 캡처를 수행하지 않았습니다. 외부 Chrome·CDP·Playwright를 사용하지 않았습니다.

검토한 HTML 해시:
- final-rendered/rea-open-source-rich-preview.html: `670a06c1766d1c29d893a5fc9d17faf41abbb236b355cff7bf97eb8e7ad44e66`
- final-dark-rendered/rea-open-source-rich-preview.html: `44e768a629e7aa0241ca6a8a75ab4d7cd52ee32680bdb845ebb31583715dfec4`
- final-rendered/rea-open-source-tistory-fragment.html: `fb2aacd2b88eceb01c9c7c49c222f4a08cb41a853b6e937f6ea55adde4b7ba37`

## 네 페이지 시각 관찰

1280px 두 테마에서 제목·도입·대표 이미지·목차·네 소제목·표·두 설명 그림·재현 명령·결말과 MIT 출처 토글까지 읽었습니다. 360px 두 테마에서도 같은 순서가 유지되며 제목과 긴 소제목의 줄바꿈이 잘리거나 서로 겹치지 않습니다. 처음 권하는 공식 작은 메모 예제는 lead와 목차보다 앞에 있습니다. 목차는 네 단계 설명과 재현으로 간결하게 구성돼 있습니다.

공식 카드와 두 설명 그림이 모두 보이고 캡션이 바로 아래에 붙습니다. 새 그림은 PC 약538px, 모바일318px에 표시되며 단계·라벨·CSV 따옴표 변환을 읽을 수 있습니다. 다크모드에서도 원본의 흰 배경과 파랑을 보존하고 픽셀 색을 반전하거나 재색칠하지 않았습니다. 주변은 중립적인 배경이며 흰 그림 테두리가 본문이나 caption을 가리지 않습니다.

저장 동작 표는 모바일320px 컨테이너에 두 열이 모두 들어갑니다. 왼쪽 질문과 오른쪽 답이 자연스럽게 줄바꿈되며 테두리 밖으로 나가지 않습니다. Node 지원 버전 목록의 bullet이 실제로 보이고 줄간격과 다음 문단 사이 여백이 있습니다. 본문·링크·인라인 코드·굵은 문장의 대비는 두 테마에서 읽을 수 있습니다. caption의 대비도 유지됩니다.

CSV 대표 출력은 모바일에서 전체가 보입니다. 긴 Bash와 node -e 코드는 페이지 밖으로 레이아웃을 밀지 않고 코드 영역 안에서 오른쪽이 이어지는 모습입니다. CSS에 overflow-x:auto가 실제 들어 있습니다. 다만 전체 캡처와 현재 DOM에는 코드의 scrollLeft·clientWidth·scrollWidth 및 조작 후 오른쪽 끝이 보인 기록이 없으므로, 제가 실제 가로 스크롤 성공을 확인했다고 쓰지 않습니다. 부모에게 CUA 조작 증거를 요청했습니다.

MIT 고지는 하단의 ‘대표 이미지 출처 · REA MIT License’ 토글로 묶여 페이지를 불필요하게 늘리지 않습니다. 캡처에서는 접힌 상태이며 HTML에 전체 license가 들어 있음을 확인했습니다. 토글을 실제 클릭해 펼친 결과까지 확인한 것은 아닙니다.

## DOM과 canonical HTML 대조

네 DOM 관찰에서 document scrollWidth=clientWidth=1280 또는360, preview H1=1/H2=4입니다. 세 CDN 이미지 모두 natural dimensions가 유효합니다. 1280에서 lead914/그림538, 360에서 모두318px로 기록됐고 이미지 비율이 원본과 맞습니다. 모바일 표는 parent/scroll/width 모두320px입니다.

canonical HTML 파싱 결과 두 preview는 H1 1개/H2 4개, fragment는 H1 0개/H2 4개입니다. 모든 ID가 고유하며 목차의 네 hash는 실제 ID를 가리킵니다. 두 preview의 img 3개는 모두 HTTPS CDN 주소와 승인한 alt를 갖고 로컬 파일경로나 media placeholder가 없습니다. fragment는 관찰한 native attachment를 사용하는 구조여서 일반 img가 없으며 중복 H1이나 로컬 경로를 포함하지 않습니다. native block의 실제 티스토리 확장과 alt는 이 standalone HTML의 판독만으로 검증할 수 없습니다.

## 판정과 남은 단계

관찰한 canonical 원격 이미지 페이지 네 화면에 시각 결함을 발견하지 못해 **remote page visual pass**를 기록합니다. 현재 확인되지 않은 코드 조작 증거는 별도로 보완해야 합니다. 이는 strict v2의 record_final_page_v2.py나 finalize_rich_post_v2.py가 통과했다는 뜻이 아닙니다.

상위 도구 지침은 브라우저를 CUA로 조작하도록 제한하지만 현재 capture helper는 외부 headless Chrome CDP만 지원합니다. 그 helper를 실행하지 않았으며 실행한 것처럼 session receipt·strict approval JSON을 만들지 않았습니다. 이 기록은 실제 CUA 산출물의 독립 판독이라는 대체 관찰을 정직하게 남깁니다. 정해진 helper receipt를 요구하는 자동 게이트의 미충족을 이 문서가 대신 통과시키지 않습니다.

실제 Tistory editor native preview의 PC/모바일 및 hELLO 테마 변환, exact submitted bytes, 게시 동작, 공개 live URL의 최종 이미지·레이아웃·목차·코드 조작은 별도 검증 대상입니다. 아직 live 성공을 승인하지 않습니다. 이 단계에서는 원고·이미지·ready/published 상태를 바꾸지 않았습니다.


## 코드 가로 조작 증거 보완

mobile-code-scroll.json과 mobile-code-scroll.jpg를 직접 읽었습니다. 긴 node -e 코드의 clientWidth318, scrollWidth942, scrollLeft624.5가 기록되었고 실제 화면에서 오른쪽 끝의 `Hello, \"REA\""}]))'`를 확인했습니다. 따라서 canonical 모바일 코드의 자체 가로 스크롤은 관찰로 확인됐으며 이전 pending 항목은 해소됐습니다. 페이지 전체 가로 넘침을 코드가 유발하지 않습니다.

## 실제 Tistory native 미리보기 추가 관찰

tistory-native-measurements.json과 light/dark 각1280/360의 실제 미리보기 캡처 네 장을 열었습니다. DOM에는 native figure3개, 이미지 모두 naturalWidth 유효, 승인 alt 보존, document scrollWidth=clientWidth가 기록되어 있습니다. PC 본문과 표는736px, 두 그림540px이며 모바일 본문·표·세 이미지288px입니다.

모바일 light/dark의 CSV 그림은 실제288px에서 세 노드·라벨·입력/출력·파란 CSV 따옴표를 구별할 수 있습니다. 보조 문구도 읽히며 캡션과 다음 문단을 가리지 않습니다. native 정렬이 왼쪽으로 밀리는 현상은 없었습니다. PC light의540px CSV 그림도 정상입니다.

**관찰한 결함: tistory-native-dark-1280.jpg의 CSV 그림 영역이 흰 빈 사각형으로 보입니다.** 이미지 외곽과 caption은 있으나 제목·세 노드·문자·화살표가 하나도 표시되지 않았습니다. DOM의 naturalWidth가 양수라는 사실만으로 이 시각 관찰을 무시하지 않았습니다. 부모에게 다크 PC 상태를 다시 실제 관찰해 그림이 정상 페인트된 화면을 확보하도록 요청했습니다. 일시적 페인트/캡처 상태인지는 현 증거로 확정하지 않습니다. 이 화면은 해결 전까지 native preview pass로 기록하지 않습니다.

canonical remote page visual pass는 위에서 관찰한 네 standalone 후보에 한정하여 유지합니다. strict helper/receipt/finalizer 미실행이라는 한계도 그대로입니다.


## native dark PC 재관찰 완료

부모가 정상 표시를 다시 관찰해 저장한 tistory-native-dark-1280.jpg의 현재 SHA-256은 `b1643ecf8696294a3c92f98c5ea5afcec2cd54732f598e331b2d8f18d6fd946d`입니다. 초기 실패 화면은 tistory-native-dark-1280-initial-paint.jpg(SHA `3b61020a6814cef09477be861003ef7ad82e603413dc67e15e82e16e4cd7a6c0`)로 보존됐습니다.

같은 원본 경로를 view_image로 다시 열었을 때 이전 빈 화면과 같은 응답이 보여 처음에는 현재 파일도 실패라고 판단했습니다. 현재 파일의 CSV 영역을 원본 픽셀로 추출해 새 경로 independent-inspection-bands/native-dark-1280-csv-final.png에서 열자 제목·입력 노드·중앙 CSV 문자열·설명·출력 노드·두 화살표가 모두 보였고 정확하게 읽혔습니다. 파일을 직접 읽은 픽셀 측정도 현재 파일에 도식이 존재함을 뒷받침합니다. 따라서 현재 파일이 빈 화면이라는 중간 판단을 정정합니다. view_image가 이전 같은 경로 응답을 재사용했을 가능성은 추론이며 확정 원인으로 쓰지 않습니다.

현재 도식은 dark PC540px 표시에서 정상이며 주변 caption·본문과 겹치지 않습니다. 앞서 확인한 native mobile288px 두 테마 및 native light PC와 합쳐 **관찰한 Tistory native preview 네 경우의 시각 판정은 pass**입니다. 초기 흰 화면처럼 보인 관찰은 새 경로 원본 픽셀 판독으로 해소됐고 본문·첨부·CSS를 바꾼 수정은 없습니다.

canonical remote 페이지와 native preview의 현재 관찰 범위에서 남은 시각 결함은 발견하지 못했습니다. strict v2 helper/record/finalizer를 실행하거나 통과시켰다는 의미는 여전히 아닙니다. 모든 CUA 촬영·조작은 부모가 했고 저는 실제 화면과 DOM을 독립 판독했습니다. 공개 live URL 검증은 게시 뒤 별도로 필요합니다.


### 원인 범위 정정

추가로 역사본 initial-paint.jpg와 현재 파일을 같은 좌표에서 직접 읽었더니 두 파일 모두 CSV 내부에 도식 픽셀이 존재했습니다(관심 영역450,235~950,935에서 채널값230 미만인 픽셀23,216개). 그러므로 역사본의 실제 저장 바이트까지 빈 이미지였다고 확정할 수 없습니다. 최초 view_image 전체 표시가 흰색으로 보였다는 관찰과 실제 파일의 정상 내용은 구별해야 합니다. 도구 표시·미리보기·뷰어 캐시의 어느 단계 문제인지는 확정하지 않았으며, 자산 자체의 실패나 실제 Tistory의 지속적인 페인트 결함으로 기록하지 않습니다.

부모는 동일한 CUA 캡처 바이트를 writeFile과 emitImage에 전달한 exact 파일도 보존했다고 알려 왔습니다. 최종 판단의 근거는 그 설명만이 아니라 제가 직접 열어 읽은 최종 파일의 새 경로 픽셀 crop입니다. **최종 native preview 시각 pass를 유지하며, 지속적인 asset 문제는 발견하지 못했습니다.** strict helper 실행·가짜 receipt·finalizer 통과를 주장하지 않는 한계도 유지합니다.
