# 최종 페이지 독립 검토: 공식 벤치마크 추가 후보

검토자: independent benchmark_source_review

판정: **pass**. 수정한 현재 후보를 새 브라우저 세션으로 캡처하고 1280·360·390px light/dark 전체 페이지를 확인했습니다. 390px 두 테마에서 업무 자동화 figure 제목의 `순위`가 온전한 단어로 다음 줄에 표시됩니다. 추가 결함은 없으며 현재 후보의 단일 최종 페이지 승인을 기록했습니다.

## 검사한 후보와 범위

`final-page-qa-v2.md`를 읽고 현재 원격 미디어가 포함된 light/dark 후보를 검사했습니다. 소스 편집 심사를 반복하지 않았으며 article.md, brief.md, evidence.md 및 도구 코드를 수정하지 않았습니다.

| 후보 | SHA-256 |
| --- | --- |
| final-rendered/gpt-6-1-sol-vs-opus-5-5-rich-preview.html | 326e0286b8d5369686e0bd8b325c5916c8220557976cef3592238957505c726e |
| final-dark-rendered/gpt-6-1-sol-vs-opus-5-5-rich-preview.html | d4c6527faf8e4d70e4091667951d8f55ababcde7b4909c9ac600a9981490a334 |
| 두 테마의 Tistory fragment | 8a20b00d66d36aea3980d5eed0727546e5ba94a40941b7df7808413899741a1f |

저장소의 `capture_rich_qa_v2.py`를 `--mode final-light`와 `--mode final-dark`, `--by 'independent benchmark_source_review'`, `--include-390`으로 각각 새 브라우저 세션에서 실행했습니다. 두 자동 캡처 모두 성공했습니다. 영수증은 `final/light/browser-capture.json` 및 `final/dark/browser-capture.json`에 있습니다.

1280×900, 360×800, 390×844의 첫 화면과 전체 페이지를 두 테마에서 직접 시각 확인했습니다. 전체 페이지는 첫 화면부터 참고 자료까지 읽을 수 있는 크기의 분할 이미지로도 확인했습니다. 두 native HTML figure의 전체 컴포넌트 이미지를 여섯 환경 모두에서 확인했습니다. 모바일 표 다섯 개는 각 테마의 360px 및 390px에서 오른쪽 끝까지 실제로 스크롤한 뒤 확인했습니다.

## 이전 결함의 수정 확인

이전 후보의 390px 두 테마에서 자동화 figure 제목 `순위`가 `순/위`로 갈라졌습니다. 현재 후보에서는 제목에 `word-break: keep-all`과 `overflow-wrap: anywhere`가 적용됐고, 두 테마에서 `순위`가 통째로 둘째 줄에 배치됩니다. 360px에서도 단어가 온전하게 다음 줄에 표시되고, 1280px에서는 한 줄로 표시됩니다. 제목 줄바꿈 수정 이후 새로 발생한 겹침이나 잘림은 없습니다.

이전 실패 보고서, 결함 이미지, 캡처 영수증 및 컴포넌트 실측은 `final/revision-1/`에 보존했습니다. 이전 후보에 대해서는 승인 기록을 만들지 않았습니다.

- `final/revision-1/final-page-review-benchmarks.md`
- `final/revision-1/light-automation-390.png`
- `final/revision-1/dark-automation-390.png`

## 그래프와 표의 검사 결과

PDF max figure의 모델별 점수와 과제당 비용은 Sol 31.0% / $0.42, Opus 26.2% / $1.55, Astra 31.0% / $2.08로 표시됩니다. 동일 점수인 Sol과 Astra의 막대 길이가 같고 Opus의 막대가 더 짧습니다.

자동화 medium figure는 Sol 31.7% / $0.19, Opus 29.5% / $0.65, Astra 34.1% / $1.27이며, max figure는 Sol 36.1% / $0.30, Opus 42.5% / $1.44, Astra 41.4% / $1.73입니다. medium에서는 Sol 막대가 Opus보다 길고 max에서는 Opus가 Sol보다 깁니다. 설정별 그룹 제목이 분명하게 분리되어 있습니다.

모든 figure에서 모델 이름, 점수, 막대, 과제당 비용의 대응이 정확합니다. 실측 막대 길이/트랙 길이를 백분율로 환산하여 54개 표시 행을 점검했고 표시 점수와의 최대 차이는 0.0052%p 미만으로 픽셀 반올림 범위입니다. 축 설명은 0–100%이며 높을수록 좋다는 방향을 명시합니다. 각 figure의 출처, 재구성 안내 및 Opus fallback 포함 캡션을 확인했습니다. 자동화 캡션은 medium과 max를 각각 비교한다는 점도 명시합니다.

모델 이름이나 숫자와 막대 사이에 겹침이 없고, 비용과 캡션이 잘리지 않습니다. 두 테마에서 색상 구분과 본문·캡션 대비를 읽을 수 있습니다. 그래프는 이미지로 축소되지 않아 모바일에서도 숫자와 비용을 읽을 수 있습니다.

공식 6항목 표, 자동화 전체 설정표, DeepSWE 전체 설정표, AA 표, API 비용표는 각 모바일 환경에서 마지막 열까지 보였습니다. 360px에서는 scrollLeft=300, 390px에서는 scrollLeft=270이며, 모두 scrollWidth−clientWidth와 일치합니다. 오른쪽 열의 Opus 결과와 미제공 표시, fallback 포함 안내, Astra 비용, max 과제당 비용 및 가정한 처리량의 비용이 잘리지 않습니다.

## 전체 페이지와 구조

여섯 환경 모두 페이지의 scrollWidth와 clientWidth가 같아 페이지 전체의 가로 넘침은 없습니다. 미디어는 모두 로드됐으며 원격 대표 이미지의 naturalWidth/naturalHeight는 1280×720입니다. 첫 화면 제목, 본문, 목차, 섹션, 표 주변 안내, figure와 캡션, 참고 자료의 배치를 실제 이미지로 확인했습니다. 다크 테마에서 링크, 표 테두리, 막대 및 이미지 주변 배경을 구분할 수 있습니다.

preview에는 H1이 하나이고 목차의 앵커 8개는 서로 다른 대상으로 연결됩니다. 두 테마가 공유하는 fragment에는 H1이 없고, 로컬 경로와 미해결 자리표시자가 없습니다. benchmark-chart JSON은 게시 페이지의 코드 블록으로 노출되지 않습니다.

추가 증거는 `final/{light,dark}/full-{1280,360,390}.png`, `full-*-reading-*.png`, `benchmark-{1,2}-{1280,360,390}.png`, `table-{1,2,3,4,5}-right-{360,390}.png` 및 `final/component-measurements.json`에 보존했습니다.

## 승인 기록

직접 확인한 `final-measurements.json`의 human fields만 pass로 채웠습니다. 수치, 경로 및 자동 계측값은 변경하지 않았습니다. `record_final_page_v2.py`가 성공하여 현재 후보에 묶인 `final-page.json`을 생성했습니다. 이 기록의 fragment SHA-256은 위 표와 일치하며, 새 light/dark 영수증 및 같은 독립 검토자의 여섯 환경 검사가 연결되어 있습니다. 소스 파일과 도구 코드는 이 검토에서 수정하지 않았습니다.
