# 2026-07-28 source notes

## OWASP GenAI Security Project

- URL: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- 확인 범위: 프롬프트 인젝션의 넓은 정의, 외부 파일·웹사이트를 통한 간접
  인젝션, 보이지 않는 입력도 모델이 파싱하면 영향을 줄 수 있다는 설명
- 방어 범위: 명확한 모델 역할, 출력 검증, 최소 권한, 고위험 행동의 사람 승인,
  외부 콘텐츠 분리, 적대적 테스트
- 한계: 제품별 구현이나 실제 공격 성공률을 제공하는 문서가 아님

## OpenAI - Understanding prompt injections

- URL: https://openai.com/safety/prompt-injections/
- 확인 범위: 제3자가 문맥에 지시를 넣어 사용자가 요청하지 않은 행동을 시키는
  사회공학 공격이라는 설명
- 사용자 권고: 필요한 데이터만 접근, 중요 행동 확인, 넓고 모호한 지시 대신
  구체적인 작업 지시
- 한계: OpenAI 제품의 공개 설명이며 모든 에이전트 구현의 독립 평가가 아님

## OpenAI - Instruction hierarchy

- URL: https://openai.com/index/instruction-hierarchy-challenge/
- 확인 범위: 공개 지시 계층 `system > developer > user > tool`, 신뢰가 낮은
  도구 출력의 지시는 높은 수준의 지시와 충돌할 때 무시해야 한다는 원리
- 한계: 공개 연구의 평가 결과를 이번 Codex 실행 내부 구조와 동일하다고
  단정하지 않음

## OpenAI - Designing agents to resist prompt injection

- URL: https://openai.com/index/designing-agents-to-resist-prompt-injection/
- 확인 범위: 외부 콘텐츠라는 공격 출처와 정보 전송·도구 행동이라는 위험
  목적지의 결합, 입력 필터 하나보다 조작 성공 시 영향까지 제한하는 설계
- 한계: OpenAI의 자체 시스템 설계 설명

## Microsoft Learn

- URL:
  https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection
- 확인 범위: 문서·메일·웹·플러그인의 외부 지시를 정상 명령으로 오인하는
  간접 인젝션, 격리·최소 권한·짧은 권한·사람 승인·런타임 감시의 다층 방어
- 한계: 여러 구현 선택지를 묶은 아키텍처 패턴이며 단일 조합의 효과 수치는 없음

## Anthropic

- URL: https://www.anthropic.com/research/prompt-injection-defenses
- 확인 범위: 브라우저 에이전트는 모든 페이지와 문서가 공격 표면이며, 자체
  내부 평가에서 낮은 공격 성공률도 의미 있는 위험이라고 명시
- 한계: Anthropic의 내부 적응형 공격 평가로, 이번 Codex 실험과 직접 비교하지
  않음
