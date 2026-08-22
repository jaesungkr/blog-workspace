# 최종 감사: 세계 로봇 기업 지도: 누가 무엇을 잘하고 어디까지 왔나

## 소스 단계 요약

- lifecycle: `reviewing`
- 경로: `standard-rich`
- 확인 기준일: 2026-08-22 KST
- 직접 사용·성능시험 주장: 없음
- first-party contribution: 22개 기업·그룹의 공개 근거를 `환경 구조화 정도`, `사람 개입`, `고객 배치`, `작업 확장성`으로 다시 분류한 `artifacts/robot-company-readiness-map.csv`
- 보류 중인 게이트: 독립 source review, source freeze, hero·infographic 생성과 독립 검수, 로컬 preflight, 사용자 CDN 매핑, final-page QA, ready·Git delivery

## 독자와 약속

- 한 명의 독자: 휴머노이드 뉴스는 보지만 산업용·물류·수술·서비스·현장 로봇을 포함한 시장 전체의 위치를 알고 싶은 비전문 독자
- 지식 기준선: Tesla Optimus나 Boston Dynamics 이름은 들었지만 출하, 배치, 자율성, 생산계획을 같은 수준으로 읽기 쉬움
- 첫 화면 답: 로봇 시장의 선두는 작업마다 다르며, 전문 로봇은 이미 대규모 운영 중이고 범용 휴머노이드는 초기 상용·고객 검증에 가까움
- 실용 결과: 다음 로봇 뉴스를 볼 때 회사 이름과 시연보다 작업, 고객, 반복 시간, 사람 개입, 총소유비용을 먼저 확인함
- 제외 범위: 모든 스타트업 명단, 비공개 계약·개입률, 군사용 무기 체계, 완전자율주행 승용차, 투자 추천, 근거 없는 세계 1위

## 제목과 소제목 strip

초안:

1. 휴머노이드 밖에 더 큰 시장이 있습니다
2. 기술 수준은 네 가지 질문으로 읽었습니다
3. 공장에서는 오래된 강자가 가장 앞섭니다
4. 창고와 수술실은 상용화의 깊이를 보여 줍니다
5. 식당과 위험 시설에서는 전용 로봇이 이깁니다
6. 휴머노이드는 고객 현장에 막 들어섰습니다
7. 지역마다 강점이 다른 이유
8. 앞으로 볼 숫자는 출하량보다 까다롭습니다

선정본과 독자 job:

| 소제목 | job | 선정 이유 |
|---|---|---|
| 휴머노이드 밖의 더 큰 로봇 시장 | identify | 시장을 여섯 분야로 나누고 전문 로봇의 현재 규모를 먼저 보여 줌 |
| 로봇의 현재를 가르는 네 가지 질문 | compare | 서로 다른 기업 발표를 출하·자율성·배치·확장으로 구분함 |
| 산업용 로봇이 쌓은 운영 경험 | identify | FANUC·ABB·Yaskawa·KUKA·UR의 특화와 기반을 설명함 |
| 반복 운영 수치로 본 창고·수술 로봇 | verify | 설치·픽·시술 수가 뜻하는 반복 운영을 확인함 |
| 식당·농지·위험 시설을 맡은 전용 로봇 | compare | 몸 모양보다 작업 환경이 전문 로봇을 결정한다는 사례를 묶음 |
| 고객 현장에 들어선 휴머노이드의 현재 | compare | 유료 배치, 고객 검증, 파일럿, 생산 준비, 사전 주문을 구분함 |
| 로봇 강국을 가른 공급망과 첫 고객 | identify | 일본·유럽, 미국, 중국, 한국의 산업 기반 차이를 설명함 |
| 출하량 다음에 확인할 다섯 숫자 | act | 독자가 이후 발표에서 확인할 운영 지표를 제시함 |

초안의 모든 소제목이 `~습니다`로 끝나 저장소 규칙과 scan strip에 맞지 않았습니다. 선정본은 문장형 설명을 줄이고 각 절의 대상과 독자 job을 남겼습니다. `지역마다 강점이 다른 이유`는 다른 산업에도 붙일 수 있어 공급망과 첫 고객을 명시했습니다.

## 문체·밀도 통과 기록

### analyzer 전·후

- 8 headings, generic-heading signal 1, prose 110문장, 평균 35.9자
- stock phrase 0
- corrective frame 3.1/1,000 Hangul
- 50자 초과 19문장, 70자 초과 4문장
- 이 수치는 편집 지시가 아니라 긴 문장과 대조 프레임을 찾아 읽는 inventory로만 사용함
- 수정 후: 8 headings, generic-heading signal 0, prose 111문장, 평균 35.5자
- 수정 후 stock phrase 0, corrective frame 2.8/1,000 Hangul, 50자 초과 18문장, 70자 초과 3문장
- 남은 긴 문장은 출처·수치·한계를 한 호흡에 묶어야 의미가 보존되는지 문맥으로 다시 읽었으며, 길이만을 이유로 쪼개지 않음

### AI-template frame 수정

- `KUKA는 ... Automation 1.0, ... Automation 2.0으로 설명합니다` 한 문장에 두 정의를 압축한 부분을 두 문장으로 나눠 plain identity를 먼저 둠
- `산업용 팔이 사라지는 것이 아니라` 대조 프레임을 `잘 검증된 산업용 팔의 작업 반경이 ... 넓어지고 있습니다`라는 직접 관찰로 교체함
- Yaskawa의 `i3-Mechatronics`, 물류의 `피킹`, KUKA의 `Physical AI`, Agility의 `fleet`처럼 비전문 독자가 번역해야 하는 표현을 쉬운 한국어로 풀거나 제거함
- `이번 글에서는`, `차근차근`, `알아보겠습니다` 같은 presenter roadmap은 사용하지 않음

### 새 정보 reverse outline

| 문단 묶음 | primary job | 새 정보 | 중앙 주장 owner |
|---|---|---|---|
| 인사 뒤 두 문단 | diagnose | 휴머노이드 뉴스와 실제 상용 중심의 간극 | `전문 로봇은 깊고 범용 휴머노이드는 초기` 결론의 첫 화면 owner |
| IFR 기준선과 여섯 시장 표 | fact | 산업용 54.2만 신규·466.4만 가동, 서비스 약 20만, 분야 구분 | 시장 크기와 분야 구분 owner |
| 네 질문과 단계 정의 | decision rule | 환경·개입·배치·확장의 비교 규칙 | 상용화 깊이 판정 owner |
| 산업용 기업 표와 해설 | compare | 기존 5개사의 특화·설치 기반·AI 확장 목표 | 산업용 강자 owner |
| 물류·수술 | evidence | Amazon 100만, Locus 70억 픽, da Vinci 310만 시술, Hugo 허가 | 구조화·규제 환경의 반복 운영 owner |
| 서비스·점검·농업 | example | Pudu 13만 출하, ANYmal 3.3만 점검, 자율 경운 | 전용 로봇 효용 owner |
| 휴머노이드 표와 네 해설 | compare | 유료 반복·고객 검증·출하·공장 건설·하드웨어 판매·사전 주문 구분 | 휴머노이드 현재 단계 owner |
| 지역별 기반 | explanation | 첫 고객·공급망이 국가별 강점을 만든다는 연결 | 지역 차이 owner |
| 다섯 운영 지표와 결론 | action | 개입 없는 시간·처리량·학습 시간·안전·총비용 | 향후 판정 행동 owner |

- 삭제·병합 판단: 시장 여섯 층을 설명한 뒤 `상용화 깊이`의 뜻을 따로 남겼습니다. 시장 규모 순위와 로봇 자율성을 혼동하지 않게 하는 새 경계이므로 유지했습니다.
- 반복 ownership: 첫 화면은 결론을 짧게 제시하고, 근거는 네 질문·분야별 절이 소유합니다. 결론은 근거를 다시 요약하지 않고 다음 뉴스에서 볼 다섯 지표로 독자의 행동을 바꿉니다.
- 수치 이동: 회사별 세부 사양과 투자금·기업가치·특허 수는 본문에서 제외하고 `evidence.md`에도 핵심 판단에서 뺀 이유를 적었습니다.

## 비교 표본과 prose polish

- 같은 하위 카테고리: `china-ai-rewrites-the-race` (`ready`), `gpt-5-6-sol-chatgpt-update` (`ready`)
- 대체 표본: `living-cost-144-items` (`ready`, 데이터 기반 시장 해설형), `github-beyond-git` (`ready`, 복수 계층을 판단 기준으로 나누는 분석형)
- 대체 이유: 같은 하위 카테고리의 finished post가 2개뿐이어서 기사 형태와 독자 의도가 가까운 최근 ready 글 2개를 보충함
- 반복 회피: 최근 글의 `세 가지 신호`, `몇 개 중 몇 개`형 제목을 답습하지 않고 `기업 지도`라는 검색어와 `누가 무엇을 잘하고 어디까지 왔나`라는 실제 독자 질문을 결합함
- private spine: `휴머노이드 영상이 로봇 시장 전체처럼 보이는 상황에서 공개 배치 근거의 단위가 달랐으므로, Codex가 네 축으로 다시 분류했고 전문 로봇과 범용 휴머노이드의 상용화 시계가 다르다는 판단에 도달했습니다.`

## 보호한 사실과 경계

- IFR의 산업용·서비스 로봇 숫자는 서로 다른 분류이므로 합계 시장규모로 만들지 않음
- 회사 발표 수치는 `회사 발표 기준`, `밝힙니다`, `예상`을 가까이 붙임
- Intuitive는 자율 수술이 아니라 의사 조작 보조라는 정의를 유지함
- Locus 70억 픽은 사람과 협업한 작업을 포함한다는 제한을 유지함
- Figure·Agility의 반복 작업을 범용 능력으로 확대하지 않음
- UBTECH 출하량을 자율 가동률로 해석하지 않음
- Tesla 생산설비 계획을 실제 생산·외부 고객 배치와 분리함
- Unitree의 가격·운동 성능을 고용 가능한 자율 작업자로 표현하지 않음
- 1X 원격 전문가 모드를 자율 기능과 분리해 사생활·개입 경계를 숨기지 않음
- Codex가 만든 분류를 사용자의 개인 조사나 경험으로 쓰지 않음

## 독립 source review 1차 수정

| 문제 | 수정 | 재검증 상태 |
|---|---|---|
| Pudu 청소 매출 70% 링크가 실제 주장을 재현하지 못함 | 해당 수치와 링크를 본문·frontmatter에서 삭제하고, 공식 회사 소개가 확인하는 출하량과 제품군만 남김 | 원고·evidence 대조 완료 |
| IFR 서비스 로봇 URL이 다른 페이지로 연결됨 | 공식 `service-robots-see-global-growth-boom` URL로 article·frontmatter·evidence를 모두 교체하고 통계 바로 옆에 링크 배치 | 공식 IFR 페이지 대조 완료 |
| 네 축을 적용했다는 약속과 CSV 열이 불일치 | CSV에 `environment`, `intervention_evidence`, `deployment_evidence`, `expansion_evidence`, `stage_4` 열을 추가하고 22개 기업·그룹을 모두 재코딩함 | CSV 헤더·모든 행 대조 완료 |
| 본문 휴머노이드 단계 표현이 4단계와 불일치 | 모든 단계를 `대규모 운영`, `반복 상용`, `초기 상용·고객 검증`, `개발·사전 주문`으로 통일함 | article 표·evidence 분류 규칙·CSV stage 매핑 완료 |
| 중국 54%·57%, 한국 밀도, Spot·Stretch 용도에 가까운 근거가 없음 | 중국 수치에 IFR 링크, 한국에 1만 명당 1,220대 IFR 근거와 한계, Spot·Stretch에 공식 제품 페이지를 각각 추가함 | article·evidence R28·R29 대조 완료 |
| `공장을 지배한`, `숫자가 증명하는`, `여섯 층`이 근거보다 강함 | `산업용 로봇이 쌓은 운영 경험`, `반복 운영 수치로 본 창고·수술 로봇`, `이 글에서 비교할 여섯 영역`으로 낮춤 | heading-only와 본문 범위 재독 완료 |
| Atlas·Apptronik·Unitree가 자체 단계 규칙보다 높게 분류됨 | 발표된 배치·파일럿 계획과 하드웨어 판매를 실제 고객 반복 운영과 분리하고 세 회사를 `개발·사전 주문`으로 재분류 | article·evidence·CSV의 단계와 근거 문구 동기화 완료 |

## 소스 단계 체크

- [x] 제목 앞부분이 `세계 로봇 기업 지도`라는 검색 의도에서 시작함
- [x] 제목과 모든 소제목이 `~다`로 끝나지 않음
- [x] 인사 뒤 2-4문장 안에 익숙한 휴머노이드 뉴스 장면과 실제 시장의 간극이 나옴
- [x] 첫 5-6문장 안에 `작업마다 선두가 다르다`는 기억할 결론이 나옴
- [x] 독자가 의존하는 표보다 먼저 비교 단위 또는 바로 뒤의 정확한 경계를 설명함
- [x] 네 축의 판단 사슬과 단계 정의가 보임
- [x] 벤더 주장, 고객 현장 근거, 규제 허가, 생산계획을 구분함
- [x] 존대어, 직접 동사, 제한된 굵은 강조, Trends 마무리를 유지함
- [x] em dash, 참고문헌 부록, 일반 면책문구, 미확인 TODO가 없음
- [x] 데이터셋과 evidence claim map이 first-party contribution을 재현함

## 미디어 결정

- generated hero: 필요. `로봇 시장은 휴머노이드 한 종목이 아니다`라는 첫 화면 인식을 16:9 장면으로 보여 줌
- infographic: 1장 필요. 구조화된 환경에서 개방된 환경으로 갈수록 상용화 깊이가 달라지는 관계와 대표 기업을 한 화면에서 비교함
- direct capture/GIF: 불필요. 직접 제품 사용이나 화면 절차를 주장하지 않음
- complex layout: 표 3개와 단계 지도가 있어 768px 전환 QA를 추가함

| 후보 파일 | 유형 | 해결하는 질문 | 위치 | 상태 |
|---|---|---|---|---|
| `assets/robot-market-hero-v2.png` | generated lead | 로봇 시장이 왜 휴머노이드만이 아닌가 | opening 결론 뒤 | 독립 검수 통과 |
| `assets/robot-commercialization-map-v4.png` | 비교 인포그래픽 | 어느 분야와 기업이 실제 반복 운영에 가까운가 | 네 가지 질문 뒤 | 구분선·장면 여백 재설계, 독립 검수 통과 |

### 대표 이미지 후보 v1

- 후보: `assets/robot-market-hero-v1.png` (1672×941, SHA-256 `296bdac273f7e5f1452e9acd2e5a8a18dadd24a0f3afe81a259f134b36a89f46`)
- 원본 보존: `artifacts/captures/generated/robot-market-hero-source.png`
- 생성 방법: OpenAI built-in image generation, 2026-08-22
- 권장 위치: 대표 이미지 - 첫 결론 뒤 `{{media:robot-market-hero}}`
- 대체 텍스트: 전용 작업 레인을 따라 산업용 팔·물류·의료 로봇이 일하고, 갈라지는 길 끝에 휴머노이드가 서 있는 밝은 작업 공간
- 인식 단서: 실제 그리퍼와 가공 부품, 바닥에 접촉한 창고 운반 로봇, 청정 유리 안의 정밀 팔, 정해진 레인이 여러 갈래의 열린 길로 바뀌는 경계
- subject-swap 사전 점검: 전경의 전용 작업 도구와 후경의 개방 경로 대비가 사라지면 글의 `전문 로봇은 깊고 범용 휴머노이드는 초기`라는 결론도 약해짐
- 제작자 확인: 전체 크기에서 관절·그리퍼·접촉 그림자·투시가 일관되고 로고·문자·가짜 UI가 없음. 360px 썸네일에서도 산업용 팔, 물류 로봇, 후경 휴머노이드의 위계가 한 번에 읽힘
- 알려진 위험: 중앙 청정 부스의 팔이 실제 수술 로봇으로 단정되기보다 정밀 작업 로봇으로 읽힐 수 있어, alt와 캡션은 `의료 수술 실적의 증거`가 아니라 `전문화된 작업 환경의 대비`로 제한함
- 최종 프롬프트: `밝은 건축형 작업 공간의 하나의 연속 트랙에서 산업용 팔·창고 운반 로봇·청정 유리 안의 정밀 조작기가 각자 전용 레인을 따라 실제 작업을 수행하고, 멀리 작은 미완성 휴머노이드가 여러 갈래의 열린 경로 입구에 서 있는 16:9 캠페인 사진. 확산 주광, 따뜻한 가장자리 빛, 오프화이트 콘크리트·브러시드 알루미늄·차콜 고무와 절제된 안전 주황, 현실적 마모와 접촉 그림자. 로고·문자·워터마크·UI·네온·홀로그램·영웅적 휴머노이드·플라스틱 장난감 질감 없음.`

#### 대표 이미지 독립 검수 수정 이력

- v1 판정: `targeted_edit` by `/root/hero_validator`
- 문제: 전경 엔드 이펙터가 여러 조각으로 갈라져 힘 전달 면이 불명확했고, AMR·팔 베이스 주변에 라벨처럼 보이는 미세 표시가 남음
- 수정: 정렬된 2지 평행 그리퍼가 단일 가공물의 양쪽 평면을 잡는 구조로 단순화하고, 작은 문자성 표시를 무문자 재질과 단색 안전 표식으로 정리함
- 수정본: `assets/robot-market-hero-v2.png` (1672×941, SHA-256 `6b39d26f2ae6b37fd4356536f7e7f2d9234443a395809fe6b38053b7b19c6638`)
- 제작자 재확인: 전체 크기에서 그리퍼 접촉 구조와 가공물 중심이 명확하고, 360×202 썸네일에서 기존의 전용 로봇→후경 휴머노이드 위계가 유지됨
- v2 독립 재검수: `pass` by `/root/hero_validator`. 하나의 2지 그리퍼가 단일 가공물 양쪽 평면을 잡는 힘 전달, 무문자 상태등·안전 표식, 관절·바퀴 접지·유리 반사·광원 일관성을 전체 크기와 360×202에서 확인함

### 상용화 지도 후보 v1

- 후보: `assets/robot-commercialization-map-v1.png` (1080×1350, SHA-256 `63652f39058cfed882cdf215f87e248475a6ea7c99167a8b88d0b7d8aa01e158`)
- 편집 원본·렌더 코드: `artifacts/robot-commercialization-map-copy.md`, `artifacts/render_robot_commercialization_map.py`
- 제작 방법: Python Pillow와 Apple SD Gothic Neo로 한글·회사명·연결선을 결정적으로 렌더링
- 유형과 질문: 비교형 단계 지도. `어느 분야와 기업이 실제 반복 운영에 가까운가?`
- 권장 위치: `로봇의 현재를 가르는 네 가지 질문` 절의 단계 정의 바로 뒤 `{{media:robot-commercialization-map}}`
- 대체 텍스트: 정돈된 환경의 대규모 운영에서 열린 환경의 개발·사전 주문까지 로봇 분야와 대표 기업을 네 단계로 나눈 지도
- 캡션: 같은 휴머노이드라도 고객 반복 작업, 배치 발표, 파일럿 계획, 하드웨어 판매는 서로 다른 근거입니다.
- copy source: article의 4단계 정의와 분야별 표, evidence R01·R05·R06·R10·R13·R16·R17·R18~R25·R27
- type scale: headline 62px→20.7 CSS px, primary 48px→16.0px, support 38/36px→12.7/12.0px, caveat 34px→11.3px. 모두 기본 band 통과
- headline zone: 205/1350 = 15.2%, 22% 상한 통과
- 전체 크기 제작자 확인: 네 구간의 문구·회사명·한글 자소가 정확하고, 경계선·궤도·분기선이 글자 영역을 침범하지 않음. `대규모 운영`에서 정렬된 레일, `개발·사전 주문`에서 열린 분기로 시각 관계가 남음
- 360 CSS px 브라우저 확인: 원본 1080×1350 래스터를 `width:360px`로 표시해 읽음. 제목보다 단계 변화가 함께 먼저 보이고, 네 단계·회사명·기준일 문구가 확대 없이 읽힘. 큰 외곽 카드나 작은 삽입 도표처럼 보이지 않음
- 한계: 이 지도는 시장 규모나 기업 종합 순위가 아니며, 같은 단계 안의 작업 범위와 사람 개입률도 서로 다름

#### 상용화 지도 독립 검수 수정 이력

- v1 내용 검수: `revision_required` by `/root/infographic_validator`
- 문제: Intuitive를 `반복 상용`, Agility를 `초기 상용·고객 검증`에 둬 article·evidence의 단계와 불일치
- 수정: 1만 1,100대 이상 설치·연 310만 건 이상 시술 근거가 있는 Intuitive를 `대규모 운영`으로, GXO 유료 배치에서 좁은 토트 작업을 10만 회 이상 반복한 Agility를 `반복 상용`으로 이동. copy map의 claim ID도 실제 evidence R05·R06·R10·R13 / R15·R16·R17·R19 / R20·R23 / R18·R21·R22·R24·R25에 맞춤
- 수정본: `assets/robot-commercialization-map-v2.png` (1080×1350, SHA-256 `1cc2f2540cc3ad032b6a753dba8aeb2f6636b5454c9ea89415ba24465397a9a4`)
- 제작자 재확인: type-scale 전 항목 PASS, 원본 전체와 브라우저 width:360px에서 단계·회사명·한글 자소·줄바꿈·경계선·분기선이 충돌 없이 읽힘
- v2 데이터 대조에서 Pudu의 CSV 단계만 `scaled_operation`으로 남은 불일치를 발견해 article·evidence·지도와 같은 `repeat_commercial`로 수정함. 13만 대는 회사 발표 출하량이며 표준화된 개입률·가동률이 공개되지 않았다는 한계를 유지함
- v2 독립 재검수: `pass` by `/root/infographic_validator`. 원본 1080×1350, Chrome 360×450 표시, 전체 확대 crop, type-scale, one-second relationship, framed-poster rejection, article·evidence·CSV·copy map 일치를 모두 확인함

#### 상용화 지도 사용자 피드백과 v3 재설계

- 사용자 피드백: 문구의 양보다 각 글자 묶음의 위아래 간격이 지나치게 조밀하고, 글자 크기를 조금만 줄이면 해결될 문제를 모바일 규격이 오히려 키운다고 지적함
- 원인: v2 제작·검수 규칙이 360 CSS px에서의 최소 글자 크기를 원본 1080px 캔버스에 역산해 강제했습니다. 그 결과 제목 62px, 단계 48px, 회사명 38/36px로 글자 위계 전체가 커졌고, 기준선 간격만 확인해 실제 글자 윤곽 사이의 숨 쉴 공간을 측정하지 못했습니다. 자동 검사 통과와 자연스러운 조판이 어긋난 이유입니다.
- 규칙 수정: `dev-log-infographic`과 `dev-log-infographic-validation`, `supporting-infographic-guide.md`, `image-art-direction.md`에서 모바일 최소 글자 크기와 360px 필수 판정을 제거했습니다. 글자 크기는 원본 캔버스와 의도된 게시 폭에서 정하고, 서로 다른 글자 묶음의 간격은 실제 painted glyph bounds로 측정하도록 바꿨습니다. 두 skill은 `quick_validate.py`를 통과했습니다.
- 새 후보: `assets/robot-commercialization-map-v3.png` (1080×1250, SHA-256 `ff805e9965537a117769f706cfc130413018491dc85b131386890453f5eb52ad`)
- 편집 원본·copy map: `artifacts/render_robot_commercialization_map_v3.py`, `artifacts/robot-commercialization-map-v3-copy.md`
- 조판: 제목 56px, 단계명 40px, 회사명 30px, 보조 문구 28px. 부제 블록을 없애고 제목 영역을 126/1250 = 10.1%로 줄였습니다.
- 실제 글자 윤곽 간격: 단계명→회사명 46.0px, 44.5px, 46.0px, 45.0px. 두 줄 회사명 사이 26.5px. 렌더 스크립트가 이 값을 직접 계산하고 최소 간격 미달 시 실패합니다.
- 구성: 큰 외곽 카드와 작은 텍스트 패널의 반복을 없애고, 공장 팔·운반 경로·점검 로봇·휴머노이드 분기 장면이 캔버스 면적을 더 많이 차지하도록 교차 배치했습니다.
- 제작자 확인: 원본 1080×1250과 의도된 게시 폭 760px에서 제목·단계명·회사명이 서로 붙지 않고, 텍스트보다 단계 변화와 작업 장면이 먼저 읽힙니다. 이번 수정에는 모바일 최소 크기나 360px 통과 여부를 설계 기준으로 사용하지 않았습니다.
- 독립 v3 검수: `pass` by `/root/infographic_validator`. 원본 전체, Chrome 실제 게시 폭 760px, 제목·축·4개 단계·회사명·연결선·각주의 확대 crop 11개를 확인했습니다. 한국어·회사명·근거 단계가 article·brief·evidence·copy map과 일치하고, 1초 안에 `정돈된 환경의 대규모 운영 → 열린 환경의 개발·사전 주문` 관계가 읽혔습니다. 큰 프레임 안에 작은 도식을 넣은 framed-poster 구성도 아니며, 모바일 최소 글자 크기나 360px 기준은 적용하지 않았습니다.

#### 상용화 지도 v3 구분선 결함과 v4 재설계

- 사용자 피드백: 글자 크기는 개선됐지만 긴 가로 구분선이 장면에 붙고, 단계마다 선과 이미지 사이 간격이 달라 저품질 표처럼 보인다고 지적함
- v3 재판정: `revision_required`. 첫 구분선 `y=414`은 다음 장면의 22px 경로 외곽과 실제로 맞닿았습니다. 두 번째 구분선 `y=628`은 위쪽 로봇 다리와 16px, 아래쪽 휴머노이드 머리와 15px만 떨어졌지만 세 번째 구분선은 인접 장면과 30~40px 이상 떨어져 광학 리듬이 불규칙했습니다.
- 누락된 검수 기준: v3 렌더 assertion은 단계명과 회사명 사이의 painted glyph 간격만 확인했고, 도형·연결선 전체 외곽과 구분선 사이의 여백은 측정하지 않았습니다. 충돌이 없는 것과 전문적인 여백 리듬을 같은 의미로 본 것이 원인이었습니다.
- 규칙 수정: 제작·검수 skill과 supporting infographic·art direction 표준에 `complete painted scene envelope`, `object-to-rule clearance`, `repeated boundary optical rhythm`을 추가했습니다. 의미 없는 구분선은 제거하고 정렬점과 음영 없는 여백으로 구조를 표현하도록 했습니다. 두 skill은 `quick_validate.py`, 저장소 unit test 57개를 통과했습니다.
- 새 후보: `assets/robot-commercialization-map-v4.png` (1080×1320, SHA-256 `63fb81fda3d458db75ecd97ef8d7804daaa5cd488bd369f75d5c730c0005d880`)
- 편집 원본·copy map: `artifacts/render_robot_commercialization_map_v4.py`, `artifacts/robot-commercialization-map-v4-copy.md`
- 수정: 단계 사이의 가로선을 모두 제거했습니다. 왼쪽 환경 축의 네 색점과 충분한 음영 없는 공간으로 네 단계를 구분하고, 제목·본문·각주 정렬 기준을 `x=72/122` 체계로 통일했습니다.
- 장면 외곽 간격: 공장→반복 상용 58px, 반복 상용→고객 검증 71px, 고객 검증→개발 단계 65px, 마지막 장면→각주 102px. 앞의 세 단계 간 차이는 13px 이내이며 렌더 assertion이 각각 최소 48px을 강제합니다.
- 글자 조판: v3의 제목 56px, 단계명 40px, 회사명 30px, 보조 문구 28px과 painted glyph 간격 44.5~46px·26.5px를 그대로 보존했습니다.
- 제작자 확인: 원본 1080×1320과 Chrome 실제 게시 폭 760px(760×929)에서 가로 구분선의 압박이 사라졌고, 네 단계는 환경 축의 점과 장면 사이 여백으로 먼저 읽힙니다. 텍스트·도형·축이 충돌하지 않고 표 또는 카드 묶음처럼 보이지 않습니다.
- 독립 v4 검수: `pass` by `/root/infographic_v4_validator`. 원본 1080×1320, 정확한 게시 폭 760×929 표시, 제목·네 단계·축·연결선·각주 확대 crop을 확인했습니다. 글자·도형 침범이나 잘림이 없고, 단계별 기업 배치는 article·evidence·CSV·copy map과 일치합니다. 장면 간 58/71/65/102px 여백과 1초 관계 인식이 통과했으며, 가로선과 외곽 카드가 없어 표·framed-poster 위험도 없습니다.

## 로컬 rich-post v2 preflight

- checker: media 2개·directive 2개, 오류 0·경고 0
- 렌더: 밝은 테마와 어두운 테마의 로컬 HTML·Tistory fragment 생성
- 실제 Chrome viewport: 1280px, 768px, 360px를 밝은·어두운 테마에서 확인
- 본문 가로 overflow: 모든 폭에서 없음. 360px의 표 3개는 320px viewport 안에서 620px 가로 스크롤 영역으로 동작
- 이미지 로드: 대표 이미지 1672px 원본이 916/704/320px, 인포그래픽 1080px 원본이 760/704/320px로 정상 표시
- 시각 확인: 두 이미지와 캡션이 해당 설명 바로 뒤에 배치되고, 밝은·어두운 테마 모두 대비·모서리·여백이 안정적임. 모바일에서 소제목·목차·목록·표 뒤 본문이 겹치거나 잘리지 않음
- QA 증거: `artifacts/qa-v2/preflight/`, `artifacts/qa-v2/preflight-dark/`의 HTML·fragment·1280/768/360 screenshot

## 남은 위험과 독립 reviewer 도전 항목

- 22개 기업을 다루면서도 독자가 회사 목록보다 상용화 단계의 차이를 기억하는지
- 회사별 공개 단위가 다른 표가 은연중에 종합 순위로 읽히지 않는지
- Figure·Agility·UBTECH의 회사 발표 수치와 독립 검증의 차이가 충분히 가까이 표시됐는지
- 한국의 기회 문단이 근거를 넘어선 국가 전략 처방으로 커지지 않았는지

## 검사와 최종 게이트

- baseline analyzer: 실행 완료, 결과 위 기록
- post-polish analyzer: generic-heading signal 0, stock phrase 0, 보호한 사실·한계 변화 없음
- `python3 scripts/blog.py check posts/2026-08-22-global-robotics-company-map`: 소제목 수정 전 오류 7개 -> 수정 후 오류 0개, 경고 0개
- 독립 source review: `pass` by `Codex (/root/source_review)`
- source freeze: `artifacts/qa-v2/source-pass.json` 기록 완료
- hero validator: v1 targeted edit -> v2 `pass` by `/root/hero_validator`
- infographic validator: v1 내용 수정 -> v2 CSV 동기화 -> v3 글자 조판 개선 뒤 구분선 결함으로 재판정 -> 가로선 제거와 장면-envelope 검사를 반영한 v4 `pass` by `/root/infographic_v4_validator`
- infographic rule regression: 수정된 제작·검수 skill 모두 `quick_validate.py` 통과, 저장소 unit test 57개 통과
- local light/dark preflight: 1280/768/360 완료, checker 오류 0·경고 0
- 사용자 CDN URL: `robot-market-hero`, `robot-commercialization-map` 모두 매핑 완료. 대표 이미지는 CDN 1280×720 축소본이 로컬 원본과 재표본화 오차만 보였고, 인포그래픽 CDN 1080×1320은 로컬 v4와 픽셀 단위로 일치함. `remote_media_v2.py record` 통과
- final light/dark page QA: `pass` by `Codex (/root/robot_final_page_qa)`. 라이트·다크 1280/768/360에서 clientWidth=scrollWidth, H1·TOC·원격 이미지 로드·캡션·목록·표 스크롤·다크 대비를 확인함. fragment H1 0, placeholder 0, local path 0
- ready: `finalize_rich_post_v2.py` 통과, `article.md` lifecycle을 `ready`로 전환하고 byte-identical Tistory paste TXT 생성 완료
- Git delivery: 진행 중
