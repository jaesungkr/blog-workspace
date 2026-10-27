# 근거: GPT-6.1 Terra vs Claude Opus 5.5, 성능과 가격으로 본 선택

확인: 2026-10-27 UTC. 주체 Codex. 원문 web open/find로 확인.

| ID | 주장 | 근거 | 조건/한계 |
|---|---|---|---|
| C1 | Terra 용도/요금, >272k 할증 | https://developers.openai.com/api/docs/models/gpt-6.1-terra | API standard, 실제 청구 아님 |
| C2 | Work/Codex 제공, Chat 제외 | https://learn.chatgpt.com/docs/whats-new/october-26-30-2026 | 계정 실측 없음 |
| C3 | MMMU근접/ALE medium Astra대등/max Opus비용~1/9/TBScience Sol앞섬 Opus5점이내 비용<1/5 | https://openai.com/index/introducing-gpt-6-1-terra/ lines31-40 | OpenAI 발표관계, 모든 조건/absolute점수 직접 추정 금지. 일부 comparator effort 미명시 |
| C4 | Opus장시간코딩/지식업무 | https://platform.claude.com/docs/en/models/opus-5-5/overview | vendor 설명 |
| C5 | Opus input4/output20/cache.20 | https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5 | standard USD/1M |
| C6 | AA v4.3.2 max Terra48/.40 | https://artificialanalysis.ai/models/gpt-6-1-terra | integer display; cost weighted avg |
| C7 | AA Opus58/5.98 max default fallback | https://artificialanalysis.ai/models/claude-opus-5-5 | 실제 Opus 단독과 차이; % 아님 |
| C8 | AA Sol52/.72, Astra53/3.26 max | https://artificialanalysis.ai/models/gpt-6-1-sol 및 /models/gpt-6-astra | same index version summaries directly read |
| C9 | Coding index2.0 Terra48 Sol54, TB4.0 경쟁수준, low/medium cost frontier | https://artificialanalysis.ai/articles/gpt-6-1-terra-pushes-the-cost-efficiency-frontier | 2026-10-26 평가 원저자, 종합 지수와 coding index 숫자 구분 |
| C10 | 빠름 후기 | https://www.reddit.com/r/ChatGPT/comments/1xg7rfk/its_my_impression_or_terra_61_is_fing_fast/ | 개인 경험, 같은 prompt/effort 미통제, 정량 배수 본문 미전재 |
| C11 | 제작/사용량 부정 후기 | https://www.reddit.com/r/codex/comments/1xgcjjb/gpt_61_terra_on_gpt_plus/ | Terrahigh→max,Sol/Opusmedium,시각선호와 각 서비스 quota, 일반화 금지 |
| C12 | Sol2/10/.10 Astra10/50/1 | https://developers.openai.com/api/docs/models/gpt-6.1-sol 및 /models/gpt-6-astra | standard USD/1M |
| C13 | 모델/effort 용도 | https://learn.chatgpt.com/docs/models | vendor recommendation |
| D1 | 100k+10k 비용 .15/.60/.30/1.50 및 Terra4회=Opus1회 | artifacts/comparison-cost-check.json | Codex 산술; fixed billable tokens; 실제 retry token 증가 제외 |

공통조건 absolute vendor score 미확보→정성관계 표로만 구성. OSWorld 비교 제외. 독립 평가/후기 추가 확보에 따라 이전 미확보 기록은 intro-v1 역사로 보존하며 현재 결론 아님. 인용은 요약, 웹 원문 25단어 이상 연속 인용 없음. 각 출처 파생 본문은 필요한 소수 주장에 한정.

## 명료한 비교 원고 수정

새 수치: 부모의 독립 검증자가 공식 Vega-Lite 데이터에서 ALEv1 60.0/63.2/58.6/59.3, MMMUPro85.5/미표시/86.3/86.7, Science58.3/63.3(w/fallbacks)/57.0/68.1, TB4.0 50.3/미표시/55.9/58.2 확인(열 Terra/Opus/Sol/Astra). max는 동일 계산량 아님. shell 원문 요청은 프록시403으로 차단되어 재시도 안 함; 부모 독립 수집 HTML Vega-Lite 값·Max·tooltip .1% receipt 수신, artifacts/qa-v2/parent-chart-evidence.json에 수집주체와 필요한 행 보존. web 본문50.3 직접확인. 기존 C3의 절대점수 미확보 서술은 이전 버전 기록이며 새 표의 부모 원자료 receipt 및 로컬 전사 검수로 대체.
