# 근거 지도: Fable 5.2 vs Fable 5.1 vs Opus 5.5 - 클로드 모델 비교

확인일: 2026-11-10. 웹 직접 열람과 원문 표시값을 사용했다. 제품 모델 자체를 실행한 테스트는 없다.

| ID | 본문 주장 | 유형·상태 | 출처·측정 조건 | 한계 |
|---|---|---|---|---|
| C-release | 2026-11-09 Fable/Mythos 5.2 발표, 같은 기반 모델/접근 조건 차이 | 공식·확인 | https://www.anthropic.com/claude-fable-and-mythos-5-2 , https://platform.claude.com/docs/en/models/fable-5-2/overview | Fable 일반 제공은 Free 무료 사용을 뜻하지 않음 |
| C-models | Fable 안전분류와 Claude 앱 fallback, API는 별도 구성 | 공식·확인 | https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2 , 발표 Safeguards | 사이버 Opus 4.8, 생물 Opus 5이며 본문은 통칭만 사용 |
| C-benchmark | FrontierCode 49.1/32.4/45.5/42.8, FrontierSWE 69.9/56.3/62.3/65.5, Automation 51.4/31.4/42.5/41.4, Chartography 73.4/44.8/64.4/71.0 | 벤더 발표·확인 | 발표 표, 순서 Fable 5.2/5.1/Opus5.5/Astra | 최고 이용가능 effort, Fable FrontierCode xhigh 예외, Chartography no tools. 자체 실험 결과 아님 |
| C-counter | Automation에서 Carbon 53.9 > Fable51.4 | 벤더 발표·확인 | 같은 공식 비교표 | Carbon의 가용성 비교는 하지 않음 |
| C-fermat | 페르마 정리의 Lean 형식화: 초기 Fable 5.2 에이전트 1,000개가 28.7시간에 완료. Opus 5.5는 18시간에 진행률 26%. | 공식 실험·확인 | https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/ 및 공식 발표 Mathematics. 아래 첨부 검증 기록 참조. | Lean·Mathlib·명제와 보조정리 제공. 모델별 단회, 18시간 후 재개. 이전 11일 실험과 인원·도구가 달라 속도 배수로 비교하지 않음 |
| C-hardware | 세 전자기기 설계·엔지니어 제작, 회로 수정 없이 동작, 조립각 제약 고려 | 연구진 발표·확인 | https://www.anthropic.com/research/claude-electronics-design | 시제품, 내구성과 인증 미확인. AI가 물리적으로 제조했다는 문장 금지 |
| C-aa | AA v5.0.1 9개 평가. Fable medium56/$3.80/8.3m, high62/$9.08/17.7m, max65/$26.54/46.4m. Opus max59/$10.04/25.2m, Astra max57/$6.24/22.8m | 독립 평가·확인 | https://artificialanalysis.ai/leaderboards/models , https://artificialanalysis.ai/models/claude-fable-5-2 | 11/10 스냅샷, 정수 지수, 모델별 다른 effort, Default Fallback. 예전 v4.3.2 점수와 혼합 금지 |
| C-vals | Vals2.2 Fable71.31%/$17.94 vs Opus70.14%/$24.77 | 독립 평가·확인 | https://www.vals.ai/benchmarks/vals_index , Updated11/9 | 금융/코딩/법률/세무 GDP 비중. AA와 과제·실행 조건이 달라 표 안에서만 비교 |
| C-price | 5.1 $10/$50, 5.2 $8/$40, fast$16/$80, Opus$4/$20 per1M | 공식·확인 | https://www.anthropic.com/claude-fable-and-mythos-5-1 의 Cost & availability; 5.2 overview/발표 | 캐시·도구·할인·구독·재시도 제외한 기본 단가 |
| C-cost | 같은 입력10만/출력1만 가정 1.50/1.20/2.40/0.60달러, 20% 인하, 점수차16.7/13.6pp, high→max 비용2.9배/시간2.6배 | Codex 계산·확인 | artifacts/cost_checks.py, artifacts/cost_checks.json | 모델 실행비용 실측 아님. 공개 값을 산술 검산 |
| C-efficiency | FrontierCode High Fable45.3 vs Max Opus45.5, 약 절반 과제비용 | 벤더 발표·확인 | 5.2 공식 발표 FrontierCode cost graph 설명 | 이 평가·설정 한정, 일반적 반값으로 확대하지 않음 |
| C-speed | 일반 출력 최대30%↑, fast 토큰생성 최대2.5배 | 벤더 발표·확인 | 공식 발표 | 전체 과제시간과 분리 |
| C-spec | 1M context,128K max output,text/image→text,API id | 공식·확인 | Fable5.2 overview | 모델 사양은 앱 사용 한도와 다름 |
| C-effort | 앱/Code 기본medium,APIhigh,low/medium의 조기종료·subagent 비용 가능 | 공식·확인 | 발표, what's new | 본문은 기본 설정과 조절만 설명. API 구현 가이드 범위 제외 |
| C-access | Pro/Team standard 11/9→11/16 23:59PT,50%주간 한도,이후 enabled usage credits 과금,Free 제외 | 공식·확인 | https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers | reset billing cutoff 11/9 10:00PT, 좌석조건 별도. 혜택과 영구 구독조건 혼동 금지 |
| C-data | 기본30일보관,ZDR별도승인 | 공식·확인 | Fable5.2 overview와 발표 EFS 설명 | 승인 예외 존재. 'ZDR 절대 불가' 아님 |

## 직접 검증
- 실행 주체: Codex. 환경: 사용자 Mac의 blog-workspace. 모델 API 호출 없음.
- 입력: 공식 표·AA v5.0.1·Vals2.2 표시값. 원본 화면은 assets 및 artifacts/captures/raw에 캡처 담당자가 저장한다.
- 산술: Decimal로 고정 입력/출력 사용료, 가격 감소율, 점수 차이, 설정별 비용·시간 비율을 계산하고 assertion으로 결과 확인.
- 실행: python3 artifacts/cost_checks.py. 결과는 artifacts/cost_checks.json.
- 원자료가 정수 표시한 지수에 소수 정밀도를 만들지 않았다.

## 반례와 한계
- 공식 업무 자동화는 Carbon이 앞선다. 모든 과제에서 1위라는 결론을 막는 반례로 유지한다.
- Fable max의 AA 과제비용은 Opus max보다 높지만 Vals 표시비용은 낮다. 비용 순위의 평가 의존성을 본문에서 드러낸다.
- AA 비교 URL 두 개는 웹 도구에서 열리지 않았다. 개별 모델 페이지와 공개 리더보드로 확인하고 실패 URL은 출처로 쓰지 않는다.
- 시스템카드 전문은 읽지 않았고 세부 안전 수치를 본문에 쓰지 않는다. 공식 요약·명시 문서만 사용한다.
- 기존 블로그의 개인 Astra 사용 선호는 이번 글의 새로운 제품 교체 의사로 옮기지 않는다.
- 모든 공표 사실은 공개 자료 기준이며 앱 실사용·한국어 품질 평가는 아니다. 이 한계는 제목과 해당 주장 범위로 반영한다.

## 미해결 항목
본문에 남은 미확인 주장은 없다. 실제 캡처/미디어 검토와 독립 원고 검토는 별도 단계에서 완료할 예정이다.

## 수정본 추가 검증 (2026-11-10)
| ID | 주장 | 출처 및 확인 | 범위 |
|---|---|---|---|
| C-51-spec | 5.1 9/1 출시,5.2 11/9,두 모델1M/128K,텍스트·이미지→텍스트,지식2026.6 | https://platform.claude.com/docs/en/models/fable-5-1/overview 및5.2 overview | 현재 사양표. 지식기준일이 최신웹자료 접근을 뜻하지 않음 |
| C-aa-51 | 5.1max(Default Fallback)49/$12.99/22.5분 | https://artificialanalysis.ai/models/claude-fable-5-1 | 같은v5.0.1 9평가 직접 확인. 과거66점 재사용안함 |
| C-aa-opus-medium | Opus5.5medium48/$2.45/7.2분 | https://artificialanalysis.ai/leaderboards/models | 11/10 동일표. high/max비교를 일상기본설정의 비용으로 일반화하지 않도록 포함 |
| C-plan | Max/Ultra/Team premium 주간50%포함,Pro/Team standard는별도크레딧,Code2.1.321+,Cowork최신Desktop | https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan | Enterprise는 계약별. 프로모션과 상시조건 분리 |
| C-effort-choice | API high권장,xhigh는어려운과제추가성능확인시,max는최대성능한정,앱·Codemedium | https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2 및 공식발표 | low/medium 조기종료,쉬운요청effort낮추기. 프롬프트로생각줄이기효과제한 |
| C-migration | 이전system/tools/messages 변경후thinking재전송prefix검사모든계정400가능,앱CodeSDK자동요청수동대응없음 | https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2 , /migration-guide | 5.2→5.1/Opus5.5 추론내용이어받기불가. Mythos5.2는호환예외이므로본문에다른모델전체라고쓰지않음 |

권장 범위: 공식 문서가 대부분의 업무에서 최신Opus를먼저쓰고 높은effort로도요구사항미달일때Fable로올리도록명시. 이 선택은 공개평가 기반이며 직접실사용후기·한국어문장품질비교는 없음.

## 첨부 내용 검증과 추가 (2026-11-10)
- C-fermat: 사용자 첨부 author-provided source의 형식화 실험을 공식 발표 Mathematics와 상세 보고서 https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/ 로 대조했다. 이미 증명된 페르마 정리의 Lean 형식화이며 새로운 정리의 발견으로 표현하지 않는다.
- 초기 Fable 5.2 에이전트 1,000개, 28.7시간(발표 약30시간). 각 모델1회 실행,18시간에저장상태재개+12시간. Opus5.5 동일1,000구성18시간26% 진행률,30시간까지추가진전거의없음. 정답률 아님.
- 상세 보고서는 Lean/Mathlib,60개명제,증명경로개요·정의,이전형식화의47개보조정리 제공 명시. 발표의 no mathematical references를 그대로 반복하지 않고 인터넷 차단·연구자 지속지휘 없음으로 한정한다. 자료/사전지식 전혀없음, no Mathlib는 사용하지 않는다.
- 앞선11일 결과는Fable5.1과대략비슷한내부연구모델,수십에이전트,연구자·Prove2Me 도움. 인원과도구달라모델속도배수계산안함. 이전보고서 https://www.anthropic.com/research/formalizing-fermats-last-theorem .
