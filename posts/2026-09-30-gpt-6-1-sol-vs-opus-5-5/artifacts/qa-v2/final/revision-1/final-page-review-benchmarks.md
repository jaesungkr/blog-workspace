# 최종 페이지 독립 검토: 공식 벤치마크 추가 후보

검토자: independent benchmark_source_review

판정: **revision_required**. 390px light/dark에서 업무 자동화 figure 제목의 마지막 단어 `순위`가 `순`과 `위`로 나뉩니다. 나머지 검사에서는 추가 결함을 발견하지 않았습니다. 이 후보의 최종 페이지 승인은 기록하지 않았습니다.

## 검사한 후보와 범위

`final-page-qa-v2.md`를 읽고 현재 원격 미디어가 포함된 light/dark 후보를 검사했습니다. 소스 편집 심사를 반복하지 않았으며 article.md, brief.md, evidence.md 및 도구 코드를 수정하지 않았습니다.

| 후보 | SHA-256 |
| --- | --- |
| final-rendered/gpt-6-1-sol-vs-opus-5-5-rich-preview.html | 91232accdf02761aa1206606dc32db84dd28668e00625982de74253c6a6137b0 |
| final-dark-rendered/gpt-6-1-sol-vs-opus-5-5-rich-preview.html | 810ff1ea20067616a3ae2917877fa155ff08bf510a86603c32560ffeea06b715 |
| 두 테마의 Tistory fragment | 8506cd87d38effd31c8dfe64d901efc987c9f95716295c351d5ab60021841f33 |

저장소의 `capture_rich_qa_v2.py`를 `--mode final-light`와 `--mode final-dark`, `--by 'independent benchmark_source_review'`, `--include-390`으로 각각 새 브라우저 세션에서 실행했습니다. 두 자동 캡처 모두 성공했습니다. 영수증은 `final/light/browser-capture.json` 및 `final/dark/browser-capture.json`에 있습니다.

1280×900, 360×800, 390×844의 첫 화면과 전체 페이지를 두 테마에서 직접 시각 확인했습니다. 전체 페이지는 첫 화면부터 참고 자료까지 읽을 수 있는 크기의 분할 이미지로도 확인했습니다. 두 native HTML figure의 전체 컴포넌트 이미지를 여섯 환경 모두에서 확인했습니다. 모바일 표 다섯 개는 각 테마의 360px 및 390px에서 오른쪽 끝까지 실제로 스크롤한 뒤 확인했습니다.

## 발견한 결함

390px의 두 테마에서 `업무 자동화: 추론 설정에 따라 달라지는 순위`가 첫 줄의 `순`과 둘째 줄의 `위`로 갈라집니다. 그래프 제목에서 한 단어가 분리되어 읽기 어렵습니다. 제목 문구를 유지하면서 figure 제목에 `word-break: keep-all`을 적용한 새 후보를 다시 확인해야 합니다. 360px에서는 `순위`가 온전한 단어로 다음 줄에 표시되고, 1280px에서는 한 줄로 표시됩니다.

결함 증거를 후속 캡처와 분리하여 보존했습니다.

- `final/revision-1/light-automation-390.png`
- `final/revision-1/dark-automation-390.png`

## 그래프와 표의 검사 결과

PDF max figure의 모델별 점수와 과제당 비용은 Sol 31.0% / $0.42, Opus 26.2% / $1.55, Astra 31.0% / $2.08로 표시됩니다. 동일 점수인 Sol과 Astra의 막대 길이가 같고 Opus의 막대가 더 짧습니다.

자동화 medium figure는 Sol 31.7% / $0.19, Opus 29.5% / $0.65, Astra 34.1% / $1.27이며, max figure는 Sol 36.1% / $0.30, Opus 42.5% / $1.44, Astra 41.4% / $1.73입니다. medium에서는 Sol 막대가 Opus보다 길고 max에서는 Opus가 Sol보다 깁니다. 설정별 그룹 제목이 분명하게 분리되어 있습니다.

모든 figure에서 모델 이름, 점수, 막대, 과제당 비용의 대응이 정확합니다. 실측 막대 길이/트랙 길이를 백분율로 환산하여 54개 표시 행을 점검했고 표시 점수와의 최대 차이는 0.0052%p 미만으로 픽셀 반올림 범위입니다. 축 설명은 0–100%이며 높을수록 좋다는 방향을 명시합니다. 각 figure의 출처, 재구성 안내 및 Opus fallback 포함 캡션을 확인했습니다. 자동화 캡션은 medium과 max를 각각 비교한다는 점도 명시합니다.

위 제목 결함을 제외하면 모델 이름이나 숫자와 막대 사이에 겹침이 없고, 비용과 캡션이 잘리지 않습니다. 두 테마에서 색상 구분과 본문·캡션 대비를 읽을 수 있습니다. 그래프는 이미지로 축소되지 않아 모바일에서도 숫자와 비용을 읽을 수 있습니다.

공식 6항목 표, 자동화 전체 설정표, DeepSWE 전체 설정표, AA 표, API 비용표는 각 모바일 환경에서 마지막 열까지 보였습니다. 360px에서는 scrollLeft=300, 390px에서는 scrollLeft=270이며, 모두 scrollWidth−clientWidth와 일치합니다. 오른쪽 열의 Opus 결과와 미제공 표시, fallback 포함 안내, Astra 비용, max 과제당 비용 및 가정한 처리량의 비용이 잘리지 않습니다.

## 전체 페이지와 구조

여섯 환경 모두 페이지의 scrollWidth와 clientWidth가 같아 페이지 전체의 가로 넘침은 없습니다. 미디어는 모두 로드됐으며 원격 대표 이미지의 naturalWidth/naturalHeight는 1280×720입니다. 첫 화면 제목, 본문, 목차, 섹션, 표 주변 안내, figure와 캡션, 참고 자료의 배치를 실제 이미지로 확인했습니다. 다크 테마에서 링크, 표 테두리, 막대 및 이미지 주변 배경을 구분할 수 있습니다.

preview에는 H1이 하나이고 목차의 앵커 8개는 서로 다른 대상으로 연결됩니다. 두 테마가 공유하는 fragment에는 H1이 없고, 로컬 경로와 미해결 자리표시자가 없습니다. benchmark-chart JSON은 게시 페이지의 코드 블록으로 노출되지 않습니다.

추가 증거는 `final/{light,dark}/full-{1280,360,390}.png`, `full-*-reading-*.png`, `benchmark-{1,2}-{1280,360,390}.png`, `table-{1,2,3,4,5}-right-{360,390}.png` 및 `final/component-measurements.json`에 보존했습니다.

## 후속 조건

현재 후보의 `final-measurements.json` human fields는 pending 상태를 유지했습니다. `record_final_page_v2.py`를 실행하지 않았습니다. 제목 줄바꿈을 고친 새 light/dark 후보가 준비되면 그 후보를 새 브라우저 세션에서 다시 캡처하고 여섯 환경을 확인한 뒤, 통과한 후보에 대해서만 단일 최종 페이지 승인을 기록해야 합니다.
