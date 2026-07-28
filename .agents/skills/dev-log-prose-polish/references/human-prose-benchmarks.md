# Korean technical prose benchmark notes

Use these observations to guide editorial judgment, not to imitate a writer.
The examples have public bylines and concrete operating details, but a public
page cannot prove that no editorial or AI assistance was used. This benchmark
therefore compares the published writing surface and accountable authorship,
not biological authorship or AI-detector scores.

Checked on 2026-07-28.

## Local dev.log pre-polish baseline

The figures below are the baseline captured at commit
`7990b0a34b48dcdac93b7446627a806332725796` before this skill changed any
article on 2026-07-28. They are intentionally not a live repository inventory.
The six posts inspected were the then-current prompt-injection experiment, WSL
containers, ccshare/manycode, Nicodemus, PER/PBR/EPS, and Mary Magdalene posts.

- All four non-Reflections titles used the same `search term - explanatory
  hook` skeleton.
- Fourteen of 45 headings ended in broad labels such as `정체`, `관계`, `구조`,
  `이유`, `결과`, `경계`, `기준`, `순서`, `진단`, `방어`, `용도`, `경우`,
  or `것`.
- The prompt-injection post used a particularly visible sequence:
  `정체 -> 이유 -> 실험 -> 결과 -> 폐기한 파일럿 -> 이유 -> 방어`.
- `한 번 폐기한 파일럿` was more concrete than the surrounding generic
  headings, but it still fails the scan-only clarity test: the heading does not
  say what contaminated the pilot or whether the test was rerun. A revision
  should name the invalidating condition and the rerun.
- The most natural paragraph runs followed time, action, and consequence:
  a contaminated pilot led to isolation and rerunning; two failed attempts led
  to cause tracing and another run.
- The denser passages chained abstract nouns and repeated corrective frames
  such as `A가 아니라 B`, even when a single concrete boundary would suffice.
- A quota-like bold takeaway near every section ending made the posts feel more
  symmetrical than the underlying material.

These are corpus observations, not automatic rejection thresholds.

## Public bylined examples

### Toss - legacy infrastructure and hybrid cloud

- Article: [레거시 인프라 작살내고 하이브리드 클라우드 만든 썰](https://toss.tech/article/payments-legacy-9)
- Authors: 박명순, 정상현
- Useful observation: the title combines searchable objects with a real
  conflict. Headings reveal a sequence of discovery and reversal, while
  operating counts and installation attempts keep the story concrete.
- Do not transfer its slang unless the target author's material already has
  that voice.

### Kakao Pay - removing a fashionable architecture

- Article: [Hexagonal Architecture, 진짜 하실 건가요?](https://tech.kakaopay.com/post/home-hexagonal-architecture/)
- Author: 도리
- Useful observation: the headings follow changing judgment over time, from
  initial goals through a collision between ideal and operation to removal.
  System counts and integration constraints explain the decision.

### Woowahan Brothers - exception mapping

- Article: [IllegalArgumentException은 400 Bad Request인가?](https://techblog.woowahan.com/21686/)
- Author: 허용선
- Useful observation: the title narrows the whole article to one choice. A
  small counterexample carries the abstract distinction, and the following
  paragraph repeatedly picks up the exact term established just before it.

### Woowahan Brothers - Kafka replacement

- Article: [장시간 비동기 작업, Kafka 대신 RDB 기반 Task Queue로 해결하기](https://techblog.woowahan.com/23625/)
- Author: 박민규
- Useful observation: the opening begins with a duplicate-delivery incident,
  then the headings follow the actual response: issue, hotfix, doubt about
  Kafka, and a replacement design. Plain labels work because the causal
  sequence is concrete.

### Kurly - two discarded RAG designs

- Article: [AI에게 도메인을 가르치다 두 번 갈아엎은 이야기](https://helloworld.kurly.com/blog/2026-delivery-domain-rag)
- Author: 김태훈
- Useful observation: each stage records an expectation, a measured failure,
  and the clue that motivates the next design. The most memorable headings
  name the discovery rather than merely saying `한계` or `개선`.

### Kurly - regular-expression troubleshooting

- Article: [개발자들이 꺼려하는 까칠한 규식이 형](https://helloworld.kurly.com/blog/reg-exp-01/)
- Author: 김세윤
- Useful observation: a concrete ticket, first deployment failure, and a
  changed framing create the rhythm. Humor is an author-specific surface, not
  the source of credibility.

### LINE - technical-debt work

- Article: [기술 부채를 갚기 위한 첫 발을 떼기까지](https://engineering.linecorp.com/ko/blog/about-messaging-hub-1/)
- Author: 송재욱
- Useful observation: the author states a working belief, enters a specific
  project, and lets the project's resistance test that belief. The transition
  comes from the author's changed situation rather than a generic connector.

### NAVER D2 - earthquake response

- Article: [네이버 검색 SRE - 지진과 비상 대응 시스템](https://d2.naver.com/helloworld/1623894)
- Author: 이선규
- Useful observation: a timestamped alert and a normal service outcome open a
  restrained systems explanation. Exact time and operating conditions show
  that natural prose need not be chatty.

### 44BITS - choosing a technical article form

- Article: [좋은 기술 블로그를 만들어 나가기 위한 8가지 제언](https://www.44bits.io/posts/8-suggestions-for-tech-programming-blog/)
- Author: nacyot
- Useful observation: writers and readers do not automatically share context.
  Choose the article form and intended reader before shaping the explanation;
  do not use one universal outline for tutorials, explanations, news, and
  retrospectives.

### Toss - sentence-level writing principles

- Article: [토스의 8가지 라이팅 원칙들](https://toss.tech/article/21022)
- Author: 김자유
- Useful observation: remove words and sentences that add no information,
  focus on the reader's next need, and read sentences as spoken Korean. Shorter
  is not automatically clearer.

## Transferable findings

1. Build the outline from a real causal chain. Strong prose shows how a
   constraint caused a choice and how an observation changed the next choice.
2. Let the title carry a searchable object plus a genuine tension, decision,
   incident, or result. Make only promises the body repays.
3. Let headings do different jobs as the article changes: scene, failed
   expectation, mechanism, observation, decision, or useful navigation.
4. Connect paragraphs by carrying forward a concrete noun, question, decision,
   or consequence. Connector variety alone does not create flow.
5. Anchor important claims with an available number, log, code line, timestamp,
   rejected alternative, or observed limitation.
6. Recover author voice from accountable judgment: what was expected, what was
   wrong, what was chosen, and why. Do not confuse voice with casual endings.
7. Use a short sentence after a dense explanation when it states a real
   decision or reversal, not merely for artificial rhythm.

## Mechanical repairs to avoid

- Do not ban `결국`, `하지만`, `들어가며`, `결과`, or `마치며` by keyword.
- Do not force every heading into a question, number, reversal, or joke.
- Do not insert rhetorical questions, analogies, anecdotes, emojis, or
  self-deprecation at fixed intervals.
- Do not make every paragraph the same size or optimize sentence length to a
  quota.
- Do not replace established 존대어 with unsupported `~죠`, `~거든요`, or
  `~했어요` merely to sound human.
- Do not invent emotion, conversation, failure, or personal experience.
- Do not chase an AI-detector score. Optimize for reader understanding,
  evidence density, and honest editorial responsibility.
