# 최종 감사: GLM-5.3-Flash 비교 - Ox Alpha 정체 공개 뒤 다시 본 성능과 가격

## v2 독자 효용 계약

- 독자가 알아보는 상황: 무료 익명 모델 Ox Alpha가 정식 공개된 뒤 계속 사용할 가치가 있는지 판단하는 순간
- 지식 기준선: Ox Alpha가 무료 추론 모델이었다는 사실은 알지만 Z.AI의 확인, 공개 가중치, 벤더·독립 평가의 차이는 모릅니다.
- 한 명의 독자: 코딩 에이전트에 넣을 가성비 모델을 고르는 비전문 개발자입니다.
- 기본 추천: 비용이 중요한 코딩·도구 사용에는 GLM-5.3-Flash를 첫 후보로 두고, 중요한 정답은 검산합니다. 속도가 병목이면 다른 Flash 모델과 완료 시간을 직접 비교합니다.
- 유용한 결과: `Flash`라는 이름이나 단일 벤치마크를 따라가지 않고 지능·비용·출력 속도·답변량 가운데 실제 병목으로 선택합니다.
- 의도적으로 제외한 세부 사항: 전체 16개 제조사 벤치마크, 로컬 GPU 구성, 100만 토큰 전체 재현, 멀티모달 품질, Coding Plan 구독 세부 조건입니다.
- 첫 화면 점검: Z.AI가 OpenCode·OpenRouter에서 제공한 Ox Alpha와 GLM-5.3-Flash의 관계, 비용 대비 강점, 속도와 정확도의 별도 검증 필요성이 대표 이미지보다 먼저 나옵니다.

## 제목과 소제목만 읽은 결과

### 초기 소제목

1. `Ox Alpha 이름 뒤에서 확인된 모델`
2. `제조사 표에서는 GLM-5.2를 앞선 코딩·도구 사용`
3. `독립 측정은 싸지만 느리고 긴 답변`
4. `10M 입력과 2M 출력이면 정상가 $2.50`
5. `처음 고를 모델과 바꿔야 할 조건`
6. `지난 네 문항 결과가 남긴 경고`

### 선택한 소제목과 독자 역할

| 소제목 | 역할 | 바꾼 이유 |
|---|---|---|
| Ox Alpha 정체 공개로 확인된 GLM-5.3-Flash | 식별 | 확인된 서비스 경로의 공개 사건과 모델명을 명시했습니다. |
| GLM-5.2보다 높아진 Z.AI 코딩·도구 점수 | 비교 | 제조사 평가임을 제목에서 드러내고 비교 대상을 남겼습니다. |
| GLM-5.3-Flash 지능 지수 57, 출력 50.2토큰/초 | 측정 | `싸지만 느리다`는 대비 문장 대신 독립 측정의 대표 결과를 적었습니다. |
| 입력 1,000만·출력 200만 토큰의 정상가 $2.50 | 계산 | 한국어 수량과 토큰 단위를 제목만으로 확인할 수 있습니다. |
| GLM-5.3-Flash를 먼저 써 볼 조건 | 선택 | 기본 추천을 뒤늦게 추론하지 않도록 모델과 행동을 함께 적었습니다. |
| oxalpha.com 테스트의 상위 제공자는 미확인 | 검증 | 독립 사이트의 테스트를 공식 모델에 귀속하지 않는 경계를 제목에 적었습니다. |
| 참고 자료 | 확인 | 카테고리 필수 탐색 제목이라 유지했습니다. |

소제목만 읽으면 `정체 확인 -> 제조사 비교 -> 독립 측정 -> 비용 계산 -> 선택 -> 기존 실패`가 이어집니다. 두 선택을 억지로 묶은 대칭형 소제목이나 `A가 아니라 B` 형태는 없습니다.

## v2 문체·밀도 점검

### 분석기 전후 기록

| 항목 | 첫 초안 | v2 수정 뒤 | 최종 문장 다듬기 뒤 |
|---|---:|---:|---:|
| 소제목 수 | 7 | 7 | 7 |
| 범용 소제목 신호 | 0 | 0 | 0 |
| 대비·교정 표현 밀도 | 3.8/1,000자 | 1.2/1,000자 | 1.2/1,000자 |
| 50자 초과 문장 | 20 | 17 | 16 |
| 70자 초과 문장 | 2 | 2 | 1 |
| 반복 문단 시작 | `정식 공개로` 2회 | 없음 | 없음 |

독립 검토 1회차 수정 뒤에는 63문장, 범용 소제목 신호 0개, 대비·교정 표현 1.1/1,000자, 50자 초과 17문장, 70자 초과 3문장으로 확인했습니다. `2026년 8월`로 시작하는 두 문단은 독립 평가 확인일과 별도 Codex 테스트 실행일을 각각 고정하므로 유지했습니다.

분석 결과는 통과 점수로 쓰지 않았습니다. `그러나`와 `반면`은 제조사 표의 항목별 선두와 독립 측정의 비용·속도 교환을 정확히 나타내므로 각각 한 번 유지했습니다.

### 없애거나 합친 대표 문구

- `가격 대비 성능은 강하지만, 빠른 응답과 첫 답의 정확도까지 한 번에 보장하는 모델은 아닙니다.`를 지우고, 가격 대비 지능 점수·출력 속도·검산 오류를 각각 한 문장으로 분리했습니다.
- `정식 공개로 확인된 사양은 다음과 같습니다.`는 다음 문장을 예고할 뿐 새 정보가 없어 삭제했습니다.
- `따라서 Flash를 가장 빨리 답하는 모델이라는 뜻으로...`는 직접 관찰인 `Flash는 가장 빨리 답하는 모델이라는 뜻이 아니었습니다.`로 줄였습니다.
- `다만 다음 조건에서는 비교 모델을...`이라는 목록 예고 문단을 삭제하고 조건 목록을 바로 시작했습니다.
- 마지막 문단의 긴 권고를 `낮은 단가를 검증 횟수로 돌려주는 선택`으로 정리해 글의 선택을 새로 확정했습니다.

## 문단별 새 정보와 주장 소유권

| 구간 | 문단의 새 정보 | 소유하는 주장·행동 |
|---|---|---|
| 첫 화면 | 공식 OpenCode·OpenRouter 경로의 모델 정체와 기본 추천·예외 | 기본 선택과 두 가지 병목 |
| Ox Alpha 공개 | 공식 확인, 구조·입력·라이선스·추론 설정 | C01-C03, C13 |
| Z.AI 점수 | 벤더 평가의 세 항목과 항목별 선두 변화 | C05-C06 |
| 독립 측정 | 지표 정의와 네 모델의 지능·속도·비용·출력량 | C07-C09 |
| 비용 계산 | 정상가와 한시 할인, 입력 1,000만·출력 200만 토큰 시나리오 | C10-C11 |
| 선택 조건 | 기본 후보와 속도·장문·난도·정답형 예외 | 독자의 실제 선택 |
| 서비스 경로 | oxalpha.com 네 문항의 통과·실패와 공식 경로에 귀속할 수 없는 한계 | C12 |
| 마무리 | 싼 단가를 재실행과 교차 검토에 배분 | 최종 행동 |

- 반복 주장 소유권: `가격 대비 강점`은 독립 측정 절이 근거를 소유하고, 비용 절은 실제 사용량으로만 확장합니다.
- `첫 답 검산`은 oxalpha.com 관찰 절이 근거를 소유하며, GLM-5.3-Flash 성능 근거로 사용하지 않습니다.
- `공식 ox-alpha와 같은 모델`은 첫 절이 근거를 소유하고, 마지막 절에서는 기존 oxalpha.com 응답의 귀속을 바꿀 수 없다는 한계만 다룹니다.
- 각 문단을 지웠을 때 잃는 사실·비교·행동·한계 가운데 하나를 확인했습니다. 표를 예고하거나 직전 결론만 되풀이한 문장은 남기지 않았습니다.

## 보존한 사실과 한계

- 날짜 `2026-08-26`, 매개변수 `320B/18B`, 문맥 `100만 토큰`, MIT 라이선스를 유지했습니다.
- Z.AI 표의 DeepSWE·Toolathlon·AutomationBench 수치와 실행 주체를 바꾸지 않았습니다.
- Artificial Analysis의 지능 지수·출력 속도·과제당 비용·출력량을 각 모델 페이지와 대조했습니다.
- 정상가와 `2026-09-09 24:00 UTC+8`까지의 50% 할인을 분리했습니다.
- 입력 1,000만·출력 200만 토큰 계산에서 캐시·도구 호출·공급자 가격을 제외했다는 한계를 비용 표 바로 뒤에 뒀습니다.
- 2026-08-24 테스트의 실행 주체를 Codex로 유지하고 문항당 1회, 전체 성능으로 일반화 불가라는 한계를 실패 해석과 함께 뒀습니다.
- oxalpha.com의 모든 요청 경로가 공식 익명 테스트와 같았다고 주장하지 않았습니다.
- 100만 토큰 전체 문맥, 멀티모달, 로컬 배포, 추론 노력별 성능을 직접 확인했다고 쓰지 않았습니다.

## 정상 문장 다듬기 기록

- 개인 문체를 모방하지 않고 사건·측정·판단이 이어지는 기술 비교 글의 흐름을 유지했습니다.
- 비교 표본: `2026-08-06-qwen-3-8-max-comparison`(ready), `2026-07-30-kimi-k3-guide`(ready), `2026-07-25-opus-5-vs-fable-5`(ready)
- 대체 기준: 동일 하위 카테고리의 ready 글이 세 편이라 다른 카테고리로 확장하지 않았습니다.
- 최근 반복 위험: `검색어 - 설명형 훅` 제목이 이미 있어 현재 제목을 재검토했습니다. 사용자의 `비교글` 요청과 `GLM-5.3-Flash 비교` 검색 의도를 직접 갚고, 본문이 Ox Alpha 공개 전후라는 고유 사건을 다루므로 유지했습니다.
- 대표 문장 수정: 한 문장에 있던 공식 익명 테스트의 이름·경로·해석을 두 문장으로 나눴습니다.
- 대표 연결 수정: 제조사 표 뒤에는 항목별 선두 변화가, 독립 표 뒤에는 비용과 속도의 교환이 바로 이어지도록 했습니다.
- 보존한 내용 불변식: 모든 날짜·수치·표·URL·테스트 주체·실패·표본 한계·가격 계산식을 유지했습니다.
- 남은 문체 우려: 영문 모델명과 벤치마크 이름이 많지만 비교 정확성을 위해 원어를 유지했습니다. 첫 등장에서는 각 지표의 독자 의미를 설명했습니다.

## 이미지와 화면 구성 결정

- 대표 이미지: 생성형 비교 이미지 1장, `assets/glm-5-3-flash-comparison-hero.png`
- 대표 이미지 역할: 익명 상태의 Ox Alpha가 공개 가중치 GLM-5.3-Flash로 드러난 사건과 빠른 모델 비교의 분위기를 전달합니다.
- 화면 스크린샷: 0장입니다. 사용 절차가 없고 공개 화면이 표의 정보를 반복하며 빠르게 낡을 수 있습니다.
- 보조 인포그래픽: 만들지 않습니다. 네 모델의 네 지표와 비용 계산은 반응형 HTML 표가 더 정확합니다.
- 조건부 QA: 정적 PNG 1장과 일반 표만 사용하므로 GIF·390px·768px·두 번째 원격 fetch를 요구하지 않습니다.

### 대표 이미지 생성 기록

- 후보: `assets/glm-5-3-flash-comparison-hero.png`
- 1차 후보 보존: `assets/glm-5-3-flash-comparison-hero-v1.png`, `artifacts/captures/generated/glm-5-3-flash-comparison-hero-source.png`
- 수정 원본 보존: `artifacts/captures/generated/glm-5-3-flash-comparison-hero-v2-source.png`
- 최종 후보 크기와 해시: `1672×941`, `1df533ba91dfaa3fab34f9f413ebecc39828f6280779c29703cc27e86cf6543e`
- 생성 방법: OpenAI built-in image generation, Codex art direction
- 권장 위치: 첫 화면의 추천과 경계 문단 다음
- 한국어 alt: `OX ALPHA 외피에서 같은 내부 구조가 GLM-5.3-FLASH 금속 모듈로 이어지는 대표 이미지`
- 인식 단서: 정확한 두 모델명과 하나로 이어진 내부 금속 격자가 익명 이름에서 정식 모델명으로의 공개를 나타냅니다.
- subject-swap 사전 점검: 다른 모델명으로 바꾸면 이 글의 공개 사건과 연결이 사라지므로 범용 AI 이미지로 대체되지 않습니다.
- 생성자 전체 크기 점검: 두 이름의 철자, 한 개의 연속 구조물, 종이·아크릴·금속의 접촉과 그림자, 대각선 경계가 모두 자연스럽습니다. 우승·속도·벤치마크를 암시하는 표식은 없습니다.
- 생성자 320px 썸네일 점검: `OX ALPHA`와 `GLM-5.3-FLASH`가 읽히며, 밝은 왼쪽 외피와 어두운 오른쪽 모듈의 공개 전환이 유지됩니다.

### 대표 이미지 독립 검수와 수정

| 단계 | 문제 | 수정 | 재검증 |
|---|---|---|---|
| 1차 독립 검수 | 오른쪽 모듈의 규칙적인 3×3 통풍구가 원본에서는 엠블럼, 320px에서는 `III/III/III` 형태의 가짜 로고처럼 보임 | 통풍구만 제거하고 두 이름, 연속 구조, 구도, 재질, 조명을 유지한 수정본을 생성 | 최종 후보와 320×180 썸네일에서 통풍구 제거, 텍스트 정확성, 새 결함 여부를 다시 확인 |

- 1차 독립 판정: `targeted_edit`
- 수정 뒤 생성자 점검: 규칙적인 통풍구와 유사 문자가 사라졌습니다. 두 모델명의 철자와 하이픈, 같은 물체로 이어지는 내부 격자, 재질과 접촉 그림자는 원본 크기와 320px에서 유지됩니다.
- 최종 독립 재검수: `pass`입니다. 원본 1672×941과 320×180 썸네일에서 통풍구가 완전히 제거됐고, 주변 금속판의 결·명암·원근에 패치 경계가 남지 않았습니다. 두 모델명의 철자와 하나로 이어지는 내부 격자도 유지됐습니다.
- 320px QA 파일 해시: `57909fdc25c4fa17454a87737b0619ab1b152eb86ad7bf1f2c18296d6afe442a`

최종 생성 프롬프트:

```text
Use case: stylized-concept
Asset type: wide 16:9 Korean Tistory technology comparison hero image
Primary request: create an iconic editorial campaign image about the anonymous coding model OX ALPHA being revealed as GLM-5.3-FLASH, while communicating that the underlying model is the same and the public identity has changed.
Creative intent: a precise reveal, not a battle and not a winner announcement.
Visual idea: a single continuous engineered object crosses a narrow diagonal reveal seam. On the left it is enclosed in a softly frosted ivory archival sleeve stamped with the exact text “OX ALPHA”; on the right the same object emerges as a refined exposed module in brushed charcoal titanium with the exact text “GLM-5.3-FLASH”. The uninterrupted internal lattice and matching alignment make it obvious that both names refer to one underlying object. No VS symbol.
Subject-recognition cue: the two exact model names, the single uninterrupted object, and a small restrained stack of code-like punched slots with no pseudo-code.
Art direction: crafted editorial still life and architectural material study, major enterprise technology campaign quality, commissioned and contemporary, not generic AI art.
Scene/backdrop: luminous warm-neutral studio surface with generous quiet negative space, no computer, no UI.
Composition/framing: 16:9 landscape, controlled asymmetry, object runs from lower-left toward upper-right through one diagonal seam, large confident scale, crop-safe margins, immediate one-second hierarchy, balanced visual weight without mirror symmetry.
Lighting/mood: large diffused daylight from upper left, soft neutral fill, restrained violet edge light only on the revealed right side, believable contact shadows, calm investigative mood.
Color palette: luminous ivory and muted champagne on the left; deep charcoal and restrained violet on the right; no saturated neon.
Materials/textures: uncoated paper fibers, softly frosted acrylic, brushed titanium, sandblasted glass, subtle microtexture, realistic thickness and contact.
Text (verbatim): “OX ALPHA” and “GLM-5.3-FLASH” only. Render both exactly, large, clean, and legible; no other letters, numbers, symbols, or pseudo-writing.
Constraints: factually neutral, publication-ready, same underlying object, no logos, no watermark, no headline, no benchmark numbers, no winner marks, no arrows, no fake proof.
Avoid: robots, brains, circuit-board wallpaper, dark neon cyberpunk, floating dashboards, holograms, glassmorphism panels, generic laptop scenes, symmetric pods, plastic icons, excessive bloom, malformed typography, unsupported speed symbolism.
```

## 현재 판단

- 원고 상태: `reviewing`
- 제목·소제목 어미: 모두 `~다`로 끝나지 않습니다.
- 인사와 본문: 존대어가 일관됩니다.
- 엠대시, 일반 참고문헌 부록, 공개 경로 TODO: 없습니다. `AI 모델 · 비교` 필수 `참고 자료` 절만 유지했습니다.
- 미해결 publishable claim: 없습니다.
- 독립 검토자가 다시 확인할 지점: OpenCode·OpenRouter의 공식 익명 테스트와 oxalpha.com 관찰이 분리됐는지, Artificial Analysis의 전체 출력량을 화면에 보이는 답변 길이로 오독할 문장이 없는지 확인해야 합니다.

## 독립 원고 검토 1회차와 수정

| 문제 | 수정 | 재검증 대상 |
|---|---|---|
| 공식 `ox-alpha`와 oxalpha.com 테스트를 동일 경로로 단정 | 첫 화면과 마지막 절에서 Z.AI가 확인한 OpenCode·OpenRouter만 GLM-5.3-Flash로 귀속하고, oxalpha.com은 상위 제공자 미확인 관찰로 분리 | 제목, 첫 화면, C01·C12, 마지막 절 |
| 직접 테스트 주체가 `dev.log`로 보임 | `2026년 8월 24일 Codex`, `oxalpha.com`, 문항별 1회를 명시 | 본문과 원자료의 actor·URL·반복 횟수 |
| 제조사 표를 Z.AI의 단일 실행처럼 표현 | 표 머리를 `Z.AI가 공개한 비교표`로 바꾸고 항목별 하네스·설정·반복 횟수가 다르다고 명시 | 공식 발표의 각 벤치마크 각주 |
| Artificial Analysis 전체 출력량을 답변 길이로 해석 | 답변·추론 토큰의 합이며 비슷한 지능 점수의 생성량·비용 참고 자료로 한정 | 지표 정의와 선택 조건 |
| 근거 없이 GLM-5.3을 어려운 저장소 작업의 대안으로 권함 | Z.AI DeepSWE 표에서 실제로 더 높았던 GPT-5.6 Terra·Gemini 3.7 Flash로 비교 대상을 제한 | 제조사 표와 선택 목록 |
| `M` 단위와 `Ox Alpha 공개 뒤`가 모호함 | 한국어 수량·토큰 단위와 `정체 공개`를 제목·소제목에 명시 | 제목과 소제목만 읽기 |
