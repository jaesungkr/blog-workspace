# 전면 개정 원문 독립 검토

검토자는 `/root/revision_source_review`이며, 검토일은 2026-09-06입니다. 판정은 원문 단계 `pass`입니다. 현재 원고의 `reviewing` 상태를 유지합니다. 신규 공식 화면의 CDN 검증과 최종 페이지 검토는 이번 판정에 포함하지 않습니다.

## 선행 원문 읽기

다른 검토 기록보다 `article.md`를 먼저 읽었습니다. 사용자가 요구한 비교 시리즈 제목과 출시 사건으로 시작하는 첫 문장을 존중했습니다. 첫 화면에서 대상 독자는 코드와 문서를 만드는 최신 AI를 고르는 사람이고, 제안은 코딩·분석에 Astra를 먼저 시험하되 긴 프로젝트와 기존 Claude 환경에서는 Fable을 함께 비교하는 것으로 읽힙니다. 제조사 평가와 외부 종합 평가가 엇갈린다는 이유가 그 제안에 앞서 제시됩니다. 사용자 피드백으로 선택한 뉴스형 첫 문장을 일반적인 업무 질문으로 되돌릴 이유는 없습니다.

제목과 소제목만 읽었을 때도 모델 소개, 개별 성능, 외부 순위의 차이, 긴 작업 기능, 비용, 시험 순서를 비교하는 글이라는 점을 알 수 있습니다. 소제목은 서로 다른 문장 형식을 사용하며, 별도 절을 읽어야만 드러나는 숨은 절차나 일반 생산성 주제로의 확장이 없습니다.

## 원문 대조

- [OpenAI 공식 발표](https://openai.com/index/gpt-6-astra/)의 두 모델 열을 직접 대조했습니다. Terminal-Bench 4.0의 57.9/55.8, DeepSWE의 74.1/67.4, FrontierCode Extended의 64.5/63.6, AutomationBench의 41.4/31.4, Science의 64.6/52.6, FrontierMath의 97.6/87.8, GPQA의 96.0/93.7, HLE 도구 사용의 57.2/65.0, ARC-AGI-2의 95.0/90.0이 일치합니다. 최고 추론 강도 결과, 연구/API와 ChatGPT 환경의 차이, FrontierCode 개발자 지시의 요약도 각주와 일치합니다. BenchCAD·OSWorld·ARC-AGI-3를 제외한 설명에 근거가 있습니다.
- [Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)에서 같은 기반 모델과 안전장치·접근 대상의 차이 및 과학 평가의 표준오차 범위를 확인했습니다. [Fable 안내](https://www.anthropic.com/claude/fable)의 9월 1일과 [Astra 평가 발표](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)의 9월 3일이 이틀 간격이라는 설명을 지지합니다.
- [AA v4.2 개편 안내](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2)에서 9월 4일 개편, 새 문서·업무 과제, 가중치 변경과 GDP.pdf의 모든 조건 충족 기준을 확인했습니다. GDP.pdf 33.2/26.2가 일치합니다. [Astra 모델 페이지](https://artificialanalysis.ai/models/gpt-6-astra)의 55와 $2.57, [Fable 모델 페이지](https://artificialanalysis.ai/models/claude-fable-5-1)의 57과 $6.12도 일치하며, 양쪽 v4.2와 max, Fable 기본 fallback 조건을 확인했습니다. 과제당 비용을 가중평균으로 설명한 문장도 평가 기관의 정의와 일치합니다.
- [9월 3일 코딩 평가](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra)에서 Codex 67과 Claude Code 70을 확인했습니다. 원고가 모델 단독 평가와 도구 환경을 포함한 지수, 서로 다른 발표일을 구분합니다.
- [Astra 사양](https://developers.openai.com/api/docs/models/gpt-6-astra)과 [Fable 사양](https://platform.claude.com/docs/en/models/fable-5-1/overview)에서 컨텍스트·출력·모달리티·모델 ID를 확인했습니다. [Astra 가이드](https://developers.openai.com/api/docs/guides/latest-model)의 비동기 도구 호출과 작업 도중 지시 변경, [Fable 변경 사항](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)의 캐시를 유지하는 추론 강도 변경 및 진행 텍스트 베타도 원고의 범위와 일치합니다. 앱에서 자동 제공되는 기능으로 일반화하지 않았습니다.
- [Astra 가격](https://developers.openai.com/api/docs/models/gpt-6-astra), [Claude 가격](https://platform.claude.com/docs/en/about-claude/pricing), [Claude 컨텍스트 안내](https://platform.claude.com/docs/en/build-with-claude/context-windows)에서 표준 단가, 캐시 읽기·쓰기, 1시간 보존 요금, Astra의 272K 초과 시 요청 전체 할증과 Fable의 장문 표준 요금을 확인했습니다. [Fable 플랜 안내](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)의 Code 최소 버전과 Pro 별도 크레딧·Max 제한도 원고와 일치합니다.

## 판단과 한국어 문장

Astra를 먼저 시험하라는 문장은 코딩·과학의 개별 결과와 평가 비용에 근거한 시험 순서입니다. 모든 작업의 품질 우위나 데이터 분석을 직접 비교 측정했다는 결론으로 제시되지 않습니다. Fable의 외부 종합·코딩 지수 우위와 기존 작업 환경이라는 예외가 앞부분과 해당 근거 곁에 남아 있습니다. 한국어 글쓰기의 승자는 정하지 않았으며, 같은 원문으로 직접 비교하라는 조언이 미평가 범위와 연결됩니다.

모든 본문 문장은 존대어를 사용합니다. 벤치마크·API·토큰·컨텍스트·캐시를 독자가 결과를 해석할 수 있는 수준으로 설명합니다. 표의 요약을 다시 길게 반복하거나 일반적인 예고만 하는 문단은 발견하지 못했습니다. 수치의 주 담당 표, 실제 청구와 가상 계산의 경계, 필요한 조건과 예외를 유지했습니다. 마지막 문단은 같은 작업 조건에서 검증하는 다음 행동으로 끝납니다. 원고에는 모델을 직접 사용한 경험이나 사용자가 수행한 실험을 꾸민 문장이 없습니다.

`brief.md`, `evidence.md`, `audit.md`, 매체 캡션을 추가로 읽었습니다. 과거 ready 기록은 이전 릴리스 이력임을 마지막 개정 기록에서 구분합니다. 캡션의 사실 설명은 원문 근거와 일치합니다. 실제 그림의 가독성과 최종 배치는 별도 페이지 단계에서 확인해야 합니다.

## 실행 결과와 범위

`python3 scripts/blog.py check posts/2026-09-06-gpt-6-astra-vs-fable-5-1`은 오류 0개, 경고 0개로 통과했습니다. `artifacts/cost_scenarios.py`를 재실행하여 $1.50/$1.50, $0.70/$0.625, $6.75/$3.50을 재현했습니다. 계산 코드를 읽고 추론 토큰을 포함한 출력, 캐시 최초 쓰기 제외, 도구 비용·세금·할인 제외 조건을 확인했습니다.

수정이 필요한 원문 결함은 발견하지 못했습니다. 원문·brief·evidence는 수정하지 않았습니다. 실제 검토자 이름으로 source-pass를 기록하며, ready 전환과 Git 작업은 수행하지 않습니다.
