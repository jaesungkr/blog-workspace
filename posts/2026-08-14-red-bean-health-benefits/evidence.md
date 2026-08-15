# 근거 지도: 짜게 먹고 잘 붓고 화장실이 답답하다면, 팥을 추천하는 이유

## 주장별 상태

| ID | 본문 주장 | 유형 | 상태 | 출처·실행 | 경계 |
|---|---|---|---|---|---|
| C01 | 소금 없이 삶은 팥 100g은 칼륨 532mg, 식이섬유 7.3g이다. | 공식 식품성분 | 확인 | USDA FDC 173728, API 원자료 보존 | 미국 `adzuki bean` 자료이며 국내 모든 품종·조리를 대표하지 않음 |
| C02 | 소금 없이 지은 흰쌀밥 100g은 칼륨 35mg, 식이섬유 0.4g이다. | 공식 식품성분 | 확인 | USDA FDC 169757, API 원자료 보존 | 장립종·비강화 쌀 자료이며 모든 쌀밥을 대표하지 않음 |
| C03 | 같은 100g에서 팥은 흰쌀밥보다 칼륨 15.2배, 식이섬유 18.3배다. | Codex 계산 | 확인 | C01 ÷ C02, `artifacts/red-bean-vs-white-rice-100g.csv` | 영양성분 비교이며 붓기·변비 치료 효과의 크기가 아님 |
| C04 | 칼륨은 나트륨과 체액 균형에 관여하며, 칼륨을 늘리고 나트륨을 줄이는 식사는 혈압 관리에 도움이 될 수 있다. | 공식 영양 안내 | 확인 | NIH ODS Potassium Consumer·Health Professional | 팥이나 칼륨이 부종을 치료한다는 근거로 확대하지 않음 |
| C05 | 과도한 소금 섭취는 부종의 여러 원인 중 하나다. | 공식 의학 안내 | 확인 | MedlinePlus Edema | 지속되거나 원인이 불분명한 붓기는 음식 문제로 단정하지 않음 |
| C06 | 식이섬유와 충분한 물은 변을 부드럽게 하고 변비 예방·완화에 도움이 될 수 있다. | 공식 보건 안내 | 확인 | NIDDK constipation diet page | 식이섬유를 갑자기 늘리지 않음 |
| C07 | 팥물만 마실 때 삶은 팥 알맹이 100g과 같은 7.3g의 식이섬유를 먹는다고 볼 수 없다. | 범위 해석 | 확인 | USDA 수치는 알맹이를 포함한 `Beans, adzuki, mature seeds, cooked, boiled, without salt`의 가식부 100g | 팥물의 실제 식이섬유 함량을 측정하지 않았으므로 0이라고 쓰지 않음 |
| C08 | 신장 기능 저하 및 ACE 억제제·ARB·칼륨 보존 이뇨제 사용 시 혈중 칼륨이 너무 높아질 수 있다. | 공식 의학 안내 | 확인 | NIH ODS Potassium Consumer | 개인별 제한량은 의료진 판단 영역 |
| C09 | 한쪽 다리의 갑작스러운 붓기, 가슴 통증, 숨참은 음식으로 버티지 말고 의료진의 평가가 필요하다. | 공식 의학 안내 | 확인 | MedlinePlus foot, leg and ankle swelling | 응급 신호를 팥 섭취 안내 뒤로 숨기지 않음 |
| C10 | 사용자는 팥빙수의 팥을 좋아하지만 붓기·배변 효과를 체험했다고 말하지 않았다. | 사용자 제공 | 확인 | 2026-08-14~15 사용자 메시지 | 개인 경험을 만들지 않음 |

## 직접 검증 설계

- 질문: 삶은 팥 알맹이를 먹으면 흰쌀밥과 비교해 칼륨과 식이섬유를 얼마나 더 섭취하는가?
- 실행 주체: Codex
- 데이터 확인일: 2026-08-14
- 입력: USDA FoodData Central FDC 173728, FDC 169757 API 응답
- 본문 표시 영양소: 칼륨, 식이섬유
- 계산: `삶은 팥 값 / 흰쌀밥 값`
- 반올림: 두 비율 모두 소수 첫째 자리
- 판단 규칙: 영양성분 차이로만 해석하고 부종이나 변비 치료 효과량으로 바꾸지 않음

## 본문 표시 계산

| 영양소 | 삶은 팥 | 흰쌀밥 | 계산값 | 본문 표시 |
|---|---:|---:|---:|---:|
| 칼륨 | 532mg | 35mg | 15.2 | 15.2배 |
| 식이섬유 | 7.3g | 0.4g | 18.25 | 18.3배 |

원자료 CSV의 칼로리·단백질·철·엽산 계산은 보존하지만, 붓기와 배변 독자에게 바로 필요한 칼륨과 식이섬유만 본문에 표시합니다.

## 표현 경계

- 제목은 팥 효능을 모르는 독자가 자신의 식습관과 불편을 발견하도록 대상을 직접 부릅니다. 원인이 밝혀지지 않은 부종이나 변비를 팥으로 치료한다는 뜻은 아닙니다.
- 팥을 즉효성 이뇨제, 해독제, 부종 치료제로 부르지 않습니다. 붓기가 신경 쓰이는 독자가 짠 음식을 줄이고 칼륨이 든 식품을 고르는 식사 방향으로 한정합니다.
- 팥물의 식이섬유 함량은 직접 측정하지 않았습니다. 알맹이 100g의 수치를 팥물에 옮기지 않고, 같은 양을 보장할 수 없다고만 씁니다.
- 가당 앙금·빙수팥과 간을 세게 한 팥죽은 무가당·무염 삶은 팥과 구분합니다.
- 지속되는 붓기와 응급 신호, 신장·약물 안전선은 짧지만 눈에 띄게 남깁니다.

## 출처 메모

- USDA FoodData Central: https://fdc.nal.usda.gov/ (cooked adzuki beans FDC 173728, cooked white rice FDC 169757)
- NIH ODS Potassium Consumer: https://ods.od.nih.gov/factsheets/Potassium-Consumer/
- NIH ODS Potassium Health Professional: https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/
- NIDDK constipation diet guidance: https://www.niddk.nih.gov/health-information/digestive-diseases/constipation/eating-diet-nutrition
- MedlinePlus Edema: https://medlineplus.gov/edema.html
- MedlinePlus foot, leg and ankle swelling: https://medlineplus.gov/ency/article/003104.htm

본문은 붓기와 배변이라는 독자의 불편을 먼저 말하고, 칼륨·식이섬유라는 용어는 그다음에 설명합니다.
