# 근거: AI 추론 레벨 비교

확인일: 2026-11-02 UTC. 실제 모델 평가를 새로 실행하지 않았다. 공급자 실험·원평가기관 데이터와 Codex가 재계산한 산술을 분리한다. 로컬 복제한 연구노트는 `artifacts/research/`에 있다.

## 검증된 주장과 출처

| claim ID | 본문 주장 | 1차 출처 | 조건·판정 |
|---|---|---|---|
| effort-accounting | effort는 soft guidance, 토큰량은 과제에 적응, 숨은 추론은 출력 과금 | https://developers.openai.com/api/docs/guides/reasoning | verified; 고정 시간·고정 배수 아님 |
| model-versus-effort | 모델 변경과 노력 변경 구분, 세대별 effort 대응 불가 | https://learn.chatgpt.com/docs/models | verified; user account UI를 직접 확인한 주장은 없음 |
| verbosity | 노력과 답변 상세함 별도 설정 | https://learn.chatgpt.com/docs/config-file/config-reference | verified; 출력 길이=실제 추론량으로 쓰지 않음 |
| claude-support | Sonnet/Opus5.5 모두5단계, Sonnet API high | https://platform.claude.com/docs/en/build-with-claude/effort | verified; 과거Sonnet max미지원과 구분 |
| claude-code-default | Code의 Sonnet/Opus5.5 기본medium | https://code.claude.com/docs/en/model-config | verified; 환경/조직 override 가능 |
| claude-terminal | Sonnet5.5max70.6 vs Opus5.5high64.2 | https://www.anthropic.com/claude-sonnet-5-5 | verified SVG aria-label; 당시 benchmark curve; 비용은현행견적아님 |
| claude-frontier2 | Sonnet5.5max41.0 vs Opus5.5high34.5 | https://cognition.com/frontiercode | verified current2.0; weighted composite, pass rate와 구별; 두행Claude Code |
| frontier2-method |132개; 합리적 추가수정 탈락시키던 범위기준 조정 | https://cognition.com/blog/frontier-code-2.0 | verified10/27; 다른 문제집이라 순위변화 원인을rubric 하나로 단정안함 |
| claude-cursor |55.5 vs56.0;작은차이 유의성 경고 | https://cursor.com/en-US/cursorbench | verified Cursor자체평가; CI미공개 |
| claude-methods |TB4=66×5;Cursor production harness | https://assets.claude.com/870c8f525702625d2c62fc6dd04c857e3250bec1.pdf | verifiedpp109–115. production safeguards/fallback 있음. max SE를high에붙이지 않음 |
| frontier1-history |1.1 Main46.2 vs54.0 | https://www.anthropic.com/claude-sonnet-5-5 | verified historical9/28; 현재2.0과동일시험재측정아님 |
| opus-sweep | low87.4/.11 medium92.8/.21 high95.3/.29 xhigh96.7/.74 | https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence | verified 내부SWEPro478;비용per attempt;2/2/2/1회;16384cap xhigh2회 잘림 |
| engineering-example |LP0/5→5/5;검증행동,앱제작1.5/4/11/67및16/22/33/79분 | https://claude.dev/blog/spending-your-effort/ | verified9/25;선정사례·소수평가,평균latency나품질등급표아님;TB3.0 cli-2ph-simplex |
| aa-method |v5.0,9평가,4분야 각25%,가중비용 | https://artificialanalysis.ai/methodology/intelligence-benchmarking | verified; 주로영어/text,한국어글쓰기우위 주장안함 |
| claude-aa |54/52,10.02/3.46,285k/60k;TB64/57,HLE53/56 | https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-claude-opus-5-5-high | verifiedv5.0 동일DefaultFallback. compositeCI미공개;taskcost구독청구아님 |
| fallback |DefaultFallback안전분류거절시대체모델 | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | verified; overload failover아님. fallback빈도 동일 추정안함 |
| subscription |구독사용량은 모델·effort·도구·대화길이 영향 | https://support.claude.com/en/articles/9797557-usage-limit-best-practices | verifiedactualopen11/2;API bill과분리 |
| codex-ui |Power는 모델×effort 묶음preset;Max단일추론/Ultra보조에이전트 | https://learn.chatgpt.com/docs/models?surface=app | verified doc example;실제사용자UI단정안함; samepage source budget 합산 |
| sol-default |Sol6.1API기본medium | https://developers.openai.com/api/docs/models/gpt-6.1-sol | verified API,clientdefault와구분 |
| sol-low |AA v5 low35/$0.16 | https://artificialanalysis.ai/models/gpt-6-1-sol-low | verifiedtitleLow,versionv5.0동시확인 |
| sol-medium-xhigh |medium46/.36,xhigh52/.76 | https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-1-sol-xhigh | verifiedAAreferenceharness. Codex앱/CLI실험아님 |
| sol-high-max |high50/.59,max55/1.27;TB52/56,FC37/41,GDP32/31 | https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol | verifiedv5.0,effort수준공식지원교차검증 |
| decision-framework |기본값/상향/실패비용별권고;같은초기조건/입력/도구로비교 | 본문의자료를분리·종합한dev.log판단틀 | inference,검증된보편정책이나새실험결과로표시하지않음 |

## 산술 재현
- 입력: `artifacts/published-values.json`.
- 실행: `python3 artifacts/recalculate.py` (해당 bundle에서 실행하거나 절대경로 사용).
- 결과: `artifacts/calculated-results.json`.
- 실제 실행 주체: Codex. 네트워크/모델호출/결제 없음.
- %p 차이와 합성지수의 점수 차이를 구분. 지수비율로 지능상승률을 만들지 않음.
- 반올림가격$.74/$.29는2.5517배;본문의약2.5배는공급자가원값으로계산한표현.
- AA비용10.02/3.46=2.8960,출력285k/60k=4.75;Sol1.27/.59=2.1525.

## 채택하지 않은 결과
- AA v4.x/9월출시가격·token counts는 v5와 섞지 않음.
- AA Time per Task는 토큰출력률 기반 가중decode 추정치로 wallclock완료시간이 아니므로 본문 제외.
- Sonnet1.1 xhigh→max 하락은 최신평가와scope규칙의영향이커 본문일반화근거에서제외.
- Sonnet max TerminalBench현재가격과9월Opus가격을 섞은 배수 제외.
- GPT-5 Tau-Bench API/state 변경결과는 effort효과가아니므로 제외.
- 한국어작문품질,앱계정별배포상태,모든프로젝트의일반승자 주장없음.

## 미디어
- `claude-terminal`: 공식 페이지 실제 화면의 crop;원본·SVG source·hash 보존. 비용축은로그이며출시당시수치,캡션명시. 360px에서는720px폭수평스크롤로라벨보존.
- `sol-effort`: AA v5공개값을재구성한원작성도표.두패널독립0기준;지수와달러단위;원SVG및코드·SHA·측정bounds보존. 실제Codex앱실험아님을캡션명시.
- source image의귀속은manifest+inlineURL에보존. 사용자의실제제품화면으로표시하지않음.

## 저작권·출처 분량 점검
본문은 직접 장문 인용 없이 새 한국어로 작성. 단일source의정성요약·관련표·캡션·반복설명을함께보며 기본200words범위로제한. URL query가다른같은Codex모델문서는하나로합산.
- Sonnet발표: 주로TB행·이전FC1.1·공식그림설명·역사적비용캡션,약150words이하.
- Codex모델문서: effort비대응·Power·Max/Ultra·기본값 관련문단합산,약180words이하.
- Opusoptimization: 표·조건·단계별해석약160words이하.
- Thariq사례: 두문단약135words이하.
- AA Claude직접비교: 표·비율·세부두평가약170words이하.
- Sol자료: 각source별표행·도표숫자·해석합산100words이하.
- 나머지source는각100words미만. 계산의수학적결과도연관source분량에보수적으로포함.

## 한계와 미완료 게이트
- 자료검증·원고·로컬리뷰용. 게시승인없음;Tistory이미지첨부·remoteCDN검증·네이티브preview·공개게시미진행.
- repository는Git메타데이터없는부분복제.원문가이드는GitHub읽기API로복구,publicpush없음.
- 로컬Chromium시작은socket권한오류.1회escalation은환경bwrap읽기전용경로생성오류로실패.그경로읽기/우회시도하지않음.도표는실제Pillow생성;페이지최종QA는CUA로별도기록.

## 2026-11-02 편집 개정의 근거 배치
- 숫자·실험 데이터 자체의 변경 없음. 기존 claim table은 검증된 전체 연구 목록이며 모든 행이 최신 본문에 노출되는 것은 아니다.
- 본문1: claude-aa, claude-frontier2, claude-cursor, claude-terminal. AA 표에서 출력 토큰 절대값은 제거하고 계산 비율만 유지한다.
- 본문2: sol-low, sol-medium-xhigh, sol-high-max, codex-ui. 표는 제거하되 두 패널 도표에 5단계 원값 유지.
- 본문3: engineering-example 중 운동 앱 low/high/max 시간, decision-framework.
- 부록: opus-sweep, aa-method, fallback, subscription, claude-methods, frontier2-method, frontier1-history, LP 체감 사례, claude-support, claude-code-default.
- 삭제한 공개 서술: verbosity, Sol API default, 나머지 모델 기본값 목록, AA 세부평가 두 줄, Sol TB/FC/GDP 개별점수, 운동 앱 medium 및 상세 명세 조건. 검증 기록은 연구에 보존.
- 모든 source 파생 분량은 첫 버전보다 줄었으며 단일 source 기본 200-word 한도를 넘지 않는다. 현행 source review 승인 대기.

## 자연스러운 문체 개정의 사실 경계
- 연구 수치·모델 조합·평가 버전·입력 데이터 변경 없음. source bytes와 계산 결과는 유지한다.
- 본문·캡션의 ‘Codex 앱 직접 실험 아님’ 문구는 삭제하고 AA가 기반 모델을 평가했다는 긍정적 attribution으로 동일한 정직성을 확보한다.
- API 비용을 표의 정의로 표시하고 구독과의 차이는 기존 부록에 둔다. Default Fallback 조건도 동일 부록에 유지한다.
- Thariq 시간은 ‘운동 앱 제작 사례’ 및 ‘앱 하나’로 범위를 한정한다. 기능 추가라는 실제 행동을 시간 차이와 연결하며 일반 응답 평균이나 품질등급으로 확대하지 않는다.
- user 실제 진술인 max 선택·Sonnet/Opus 비교의 궁금증을 서론에 반영. 새 저자 경험·사용 로그·심정·대화는 추가하지 않는다.
- 공식 그래프 caption은 9월 28일 발표 당시 비용을 직접 명시. 현재 가격이라고 쓰지 않는다. Sol caption은 AA v5 재구성, 확인일, 독립 눈금을 유지한다.
