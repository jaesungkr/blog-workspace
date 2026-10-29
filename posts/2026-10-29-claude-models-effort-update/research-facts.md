# Claude 모델·Effort 업데이트 조사

확인일: 2026-10-29 UTC. 공식 Anthropic/Claude 원문만 기술 근거로 사용. 기존 글 URL 유지, 이 단계는 검토용 초안 제작이며 게시하지 않음.

## 가장 중요한 편집 결론

- API 파라미터 해설이 아니라 ‘지금 어떤 모델과 강도를 고르면 되나’를 중심으로 쓸 것.
- 현재 모델표에는 Haiku 5.5 / Sonnet 5.5 / Opus 5.5 / Fable 5.1. Fable는 어려운 장기 작업용 별도 선택지. 일반 독자는 앞의 3종부터 이해하면 충분하다.
- Effort는 low / medium / high / xhigh / max. 모든 버전이 다섯 단계를 지원하는 것은 아니지만 위 최신 4종은 전부 지원한다.
- 모델은 능력의 차이, Effort는 한 요청에 얼마나 공을 들이는지의 차이. Effort를 올린다고 다른 모델이 되는 것도, 답의 정확성이 보장되는 것도 아니다.
- **API 기본값과 앱/Code 기본값을 혼용하면 안 된다.** Sonnet 5.5는 앱/Code medium, API high.
- 표는 모델·어울리는 일·선택 시점 3열 정도. API단가·컨텍스트·모델ID 등은 독자에게 불필요하므로 이번 본문에 전부 넣지 않는 편이 좋다.

## 출처와 확인된 사실

### S1. 현재 모델 목록
https://platform.claude.com/docs/en/models/overview

현재 featured models: Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5. 모두 텍스트/이미지 입력, 텍스트 출력, 1M context, 최대 출력128K. 일반작업 출발점으로 Opus5.5, 어려운 추론·장기작업에Fable5.1을 안내한다.
API 입/출력 100만토큰 가격: Fable $10/$50, Opus $4/$20, Sonnet $2/$10, Haiku **부터** $0.10/$0.50. Haiku는 입력길이에따른tier이므로 단일고정가로쓰지말것.

### S2. 모델을 고르는 공식 가이드
https://platform.claude.com/docs/en/about-claude/models/choosing-a-model

빠르고반복적인작업은Haiku부터시험→부족한능력있을때상향. 복잡한작업은Opus5.5부터시험→effort조절→어려운추론/장기작업에서xhigh/max로도부족하면Fable5.1검토. 이는 API구현가이드 기준의 선택 전략이며, 모든사용자의채팅기본모델이라는뜻아님.

### S3. Effort API 문서
https://platform.claude.com/docs/en/build-with-claude/effort

- 최신4종 모두5단계지원. API기본: Opus5.5·Haiku5.5 medium / Sonnet5.5·Fable5.1 high.
- Effort는생각토큰만이아니라응답본문·도구호출·인수에도영향을준다. 토큰예산을숫자로딱고정하는기능은아님.
- low는효율/속도, medium균형, high복잡한추론/코딩, xhigh장기agent작업, max가장깊은검토.
- 같은이름의effort가모델마다동일한계산량/품질을뜻하지않는다. 특히Sonnet5.5는재조정됨.
- API상세 예외는 본문에서 빼도 됨: Opus5.5·Fable5.1 always-on thinking. Haiku5.5는high이하thinkingoff가능. Sonnet5.5는disabled불가, low~high에서between_tools 가능.

### S4. Claude 앱 UI
https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings

- 전송버튼옆 모델이름→모델선택, More models로추가목록.
- 전송버튼옆 모델이름→Effort→단계선택. 해당모델권장값에Default표시. 변경은다음응답부터적용.
- 높은effort는시간과토큰사용이늘어사용량한도에빨리도달할수있음.
- 최신 Haiku5.5·Sonnet5.5·Opus5.5·Fable5.1은 **Claude앱에서Thinking을끌수없음**. ‘간단한질문이면Thinking을끄세요’식옛가이드삭제.
- 펼쳐보이는Thinking은전체내부사고가아닌요약.

### S5. Claude Code 설정
https://code.claude.com/docs/en/model-config

- `/model` 모델선택, `/effort` 슬라이더, `/effort high`처럼직접설정.
- Code기본effort: Opus5.5·Sonnet5.5·Haiku5.5 medium, Fable5.1 high.
- `/effort status` 현재강도확인. `/effort auto` 저장설정해제.
- max는대체로현재세션만적용; low~xhigh는기본설정으로저장. 지엽적이므로본문생략가능.
- max는수익체감/과도한생각가능. 일괄최대설정권하지않음.
- ultrathink와ultracode는별개이며복잡한예외가있음. 이번첫이해글에는추가하지않는편권장.

### S6. 실용적인 구분 근거 (2026-07-07)
https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code

자료를충분히보며시도했는데도잘못판단하면능력높은모델을검토. 필요한파일을건너뛰거나테스트를생략하거나중간에멈추면effort상향검토. 모델/effort차이를독자에게설명할좋은핵심이다. 원문은Code맥락이므로일반챗에확대할땐‘예를들어코딩에서는’으로구분.

### S7. Sonnet5.5 발표 (2026-09-28)
https://www.anthropic.com/claude-sonnet-5-5

범위명확한일상업무,버그수정,문서·슬라이드·스프레드시트작성에강점. Opus5.5는복잡하고열린판단작업에강점. **앱·Code는medium, ClaudePlatform은high**라고명시. 발표당시Haiku미출시서술은현재낡았으므로재사용금지.

### S8. Opus5.5 발표 (2026-09-22)
https://www.anthropic.com/claude-opus-5-5

복잡한여러저장소작업/장기코딩/지식업무. 기본medium. 발표당시Sonnet/Haiku추후출시문장은이제낡음. 벤치마크표는일부xhigh·일부max,보호장치fallback조건있어한줄종합서열로쓰기부적절. 이번사용가이드에는점수표생략권장.

### S9. Haiku5.5 (2026-10-07)
https://www.anthropic.com/claude-haiku-5-5
https://www.anthropic.com/claude/haiku

빠른요약·분류·데이터추출·반복작업. Free/Pro/Max/Team/Enterprise에서선택가능. API입력100K이하$0.10/$0.50,초과$0.50/$2.50 perMTok. 가격표넣지않으면생략.

### S10. Fable 요금제 주의 (2026-09-02)
https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan

모든유료플랜접근가능하지만동일하게포함은아님. Pro·Teamstandard는처음부터사용량크레딧별도. Max·Teampremium는정규주간한도중50%까지Fable사용. ‘Max면무제한’,‘Pro에그냥포함’금지. 본문에는‘Pro에서는별도사용량크레딧이필요하므로,일상작업용기본추천과는구분했습니다’정도만있으면충분.

### S11. 오늘 변경되는 구형 모델 (필요시만)
https://support.claude.com/en/articles/17444146-claude-haiku-4-5-is-leaving-the-model-selector

2026-10-29 Free/Pro/Max 채팅·Cowork·Design에서Haiku4.5목록제거,Haiku5.5대체. Code·Team·Enterprise·API는영향없음. 따라서‘Haiku4.5완전종료’금지. 본문역사설명은삭제하고최신선택지로정리하면됨.

## 권장 구성

제목: Claude 모델 비교와 Effort, 어떻게 고를까? (SEO상기존URL유지)
1. 두설정이헷갈리는상황부터짧게도입. 핵심: 모델/공들이는강도는별개.
2. 지금고를모델 3종실용표+Fable짧은추가.
3. Effort5단계표. everydaymedium → 빠르면low / 확인이부족하면high. xhigh/max는정말어려운일.
4. 모델바꿀때vs강도올릴때 실제문서정리/코딩예시. 작성자가고안한상황예시임,실측후기처럼쓰지않기.
5. 앱3클릭사용법+Code짧은커맨드상자. API는Sonnet기본값다르다는한줄보충까지만.
6. 짧은결론: 처음부터최대보다는기본에서시작하고부족한부분에맞춰바꾸기.

## 아직 미확인

기존포스트웹fetch2회timeout. 별도브라우저담당capture_claude_effort_examples가실제본문읽는중. 기존글의특정문장문제는그결과수신후추가예정.

## 기존 글 실독 결과 (브라우저 담당 공유, 2026-10-29)

- 구형 Haiku4.5/Sonnet4.6/Opus4.8 중심, Fable5 접근중단 상태를 설명 중. 지금은 최신라인업/복구후Fable5.1 기준으로교체필요.
- 점수표 Opus4.8 88.6%와4.6 80.8%를섞어놓고1.2%p차이라서술. 버전/산술불일치. 현재글의목적상점수표전체삭제해실용표로대체추천.
- Effort는항상high기본, low거의생각생략, max5~10배등일괄단정수정필요.
- MAX_THINKING_TOKENS=8000 및/config thinkingoff를보편적인추천처럼설명. 최신4종에는적절하지않음.
- 9개섹션으로촘촘함. 핵심6개안쪽으로줄이고실제설정위치+사용예시강화.

## 구형 코드설정 제거의 직접근거

https://code.claude.com/docs/en/model-config#adaptive-reasoning-and-fixed-thinking-budgets
현재Fable,Sonnet5이후,Haiku5.5,Opus4.7이후는항상adaptive. 고정thinkingbudget 및 CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING은적용되지않는다. 구형Opus4.6/Sonnet4.6에서만해당환경변수로fixedbudget모드를돌리고MAX_THINKING_TOKENS제어가능.
https://code.claude.com/docs/en/model-config#extended-thinking
Code상Opus5.5/Sonnet5.5/Haiku5.5/Fable는thinkingoff불가. /config 및sessiontoggle에Thinking can't be turned off표시, 기존alwaysThinkingEnabled:false/MAX_THINKING_TOKENS=0효과없음. 최신모델은Effort로조절하도록정리해야함.
