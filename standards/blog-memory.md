# dev.log persistent blog memory

Use this file for topic selection, full-post planning, AdSense or traffic
strategy, and portfolio review. Treat metrics as dated snapshots and refresh
them when decisions depend on current state.

## Status snapshot - 2026-07-25

- Public URL: `https://dop3n.tistory.com`
- User-reported average daily visitors: about 200.
- User-reported AdSense result: three failed reviews. The exact rejection reason
  is unknown and must not be inferred.
- Public inventory observed on 2026-07-25: 48 posts. Of these, 45 were published
  from 2026-05-27 through 2026-07-25.
- Parent-category mix: Log 18, Trends 14, Health 7, Reflections 9, spread across
  11 current subcategories.
- Human feedback received by the user: many informational posts feel as though
  AI produced them. Treat this as a perception signal, not a proven AdSense
  cause.
- Public navigation exposed categories but no prominent author/about destination
  in the inspected layout.

## Working diagnosis

- Content volume is not the clearest constraint. The stronger risks are a broad
  topic mix, rapid publishing cadence, source-summary posts with little
  first-party value, and weak visibility of who writes the site and why.
- AI use itself is not the working diagnosis. The editorial test is whether
  experience, evidence, judgment, and accountability remain when polished prose
  is removed.
- Health and finance raise a higher trust burden. Do not choose them
  autonomously without relevant first-hand evidence, qualified review, or
  unusually strong primary-source value.
- A single post cannot guarantee AdSense approval or explosive traffic. Never
  promise either outcome.

## Editorial feedback memory - 2026-09-02

- The user rejected the first OpenClaw 2.0 title and opening because the prose
  described abstractions before explaining the product in recognizable terms.
  Treat this as a recurring quality signal for all technical posts.
- Reject titles built around vague combinations such as `시작과 운영이 달라진
  이유`, `사용 환경의 변화`, or `새 구조` when the title can name the actual
  object, task, conflict, or decision instead.
- After the greeting, explain the subject with concrete nouns and direct verbs
  before introducing architecture. For a software product, name what the user
  can connect, inspect, change, or delegate. Do not make the reader translate
  `Gateway`, `흐름`, `경계`, or `운영` into an everyday benefit.
- Do not compress several audience branches into the first screen. A new-user
  benefit, existing-user migration warning, collaboration summary, and security
  boundary do not belong in one short paragraph merely because they are all
  important. Keep one main benefit and at most one decision-changing caution;
  move the other branches to their owner sections.
- Phrases such as `모델 자체의 성능보다 사용 환경에 있습니다` and `필요한
  순간에 권한을 승인하는 흐름을 한곳으로 모았습니다` fail unless the next
  words immediately name who does what and what changes for the reader.
- Read the title and opening aloud as a standalone pair. Return them for rewrite
  when they sound like a release-note classification, could introduce many
  unrelated products, or leave a cold reader unable to answer `그래서 이걸로
  무슨 일을 하는가?`.

## Proven strengths

- `게임 내 한글 채팅 오류 해결 방법`: exact Windows environment and a
  concrete fix; visible in the site's popular-post list during the audit.
- `텍스트 유사도 파이썬 실전 (2)`: a connected series with 12 sentence-pair
  tests, explicit method differences, and observed failures.
- `AI 파인튜닝 (1)`: a reproducible transformation with before/after accuracy
  and artifact size.
- AI model comparisons are strongest when they expose test conditions, cost,
  failure cases, and scope limits rather than restating vendor claims.
- Reflections contains authentic personal voice, but its reader intent is
  separate from the monetized technical growth pillar.

## Portfolio direction

- Default growth pillar: `Log`, especially connected experiments,
  troubleshooting, AI mechanisms, and reproducible technical comparisons.
- For the next publishing phase, prefer roughly 7 of 10 new posts in Log until
  the site's primary purpose is obvious. This is a planning target, not a
  permanent quota.
- Build clusters before adding categories. Continue an existing series or link
  to at least two relevant posts when natural.
- Pause autonomous generic Health, finance, and daily-news topics unless the
  post adds first-party evidence or a defensible expert contribution.
- Do not mass-delete existing posts solely to look fresh. Strengthen the best
  posts, author identity, navigation, internal links, and evidence first.

## Tistory publication ownership

- Codex never performs Tistory's final public-publish action. The user always
  pastes the delivered HTML, checks the Tistory preview, and publishes the post.
- This is a permanent workflow boundary, not an approval question. Do not ask
  whether Codex should publicly publish a post.
- Codex may prepare paste-ready HTML, validate mapped CDN media, and complete
  repository delivery at `ready`. After the user publishes and supplies the
  live URL, Codex may validate the live page and update publication metadata.
- The user's preferred final handoff is a `.txt` file containing only the raw
  paste-ready Tistory HTML, matching the Kimi K3 delivery. Always provide this
  file as the primary final artifact and give the title separately.
- Do not show media-origin labels such as `사용자 제공`, `직접 캡처`, or
  `공식 자료` beside images in the public article. Keep provenance in
  `media.json` and the audit only; public captions contain the useful image
  explanation unless the user explicitly requests a visible source label.

## Current Reflections series direction

- `Reflections > 성경 인물 시리즈` is written from the stated position of a
  reader who has not yet read the Bible cover to cover and does not know most
  biblical figures.
- Use the series name `성경 인물 알아가기`. Its purpose is to meet one person
  at a time, not to produce a definitive personality analysis or revisionist
  argument.
- Public titles use one short, passage-grounded modifier before the person's
  name. Keep the series name and episode order in the article context or bundle,
  not as a title suffix.
- Explain first who the person is, what scene most Christians associate with
  the person, and two or three other representative moments.
- Keep the visible article warm, light, and easy to follow. Preserve exhaustive
  passage checks, disputed details, and evidence boundaries in the post bundle,
  but bring them into the article only when they prevent a misleading claim.
- Build each post around one defining biblical event with a readable
  before -> tension -> encounter or choice -> after sequence. Supporting scenes
  stay short.
- Use `쉬운성경` (YouVersion's `읽기 쉬운 성경`, KOERV) by default for the
  public article unless the user requests another translation. Keep
  `책 장:절 (쉬운성경)`, one blank quote line, and the numbered verse text
  inside the same blockquote. Do not use a Bible link in place of the text:
  quote only the few decisive verses and keep source URLs in frontmatter or
  evidence notes.

## Autonomous topic scoring

Score each candidate from 0 to 2 on the five criteria below. Prefer topics
scoring at least 8/10, with no zero for first-party evidence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| First-party evidence | none | evidence can be added | test or artifact can be produced now |
| Search intent | vague | timely or narrow | clear evergreen problem |
| Cluster fit | isolated | fits a category | directly extends a strong existing post |
| Reader action | only learns a fact | gains a checklist | can reproduce or fix something |
| Trust and scope | risky or broad | manageable caveats | precise, bounded, verifiable |

## Topic-selection rules

- Prefer a smaller test with preserved inputs and failures over a broad
  definitive guide.
- If a test cannot actually be run, do not use a title that implies direct
  testing.
- Avoid a news rewrite as the next best post when an evergreen Log experiment
  is available.
- Preserve raw inputs, environment, code, outputs, scoring rules, and
  limitations for reproducible posts.
- Connect the opening and internal links to what dev.log has already tested,
  not merely to a high-volume keyword.

## Required honesty

- Do not invent a personal experience, a test the user ran, an AdSense rejection
  label, or a future result.
- Distinguish user-reported facts, Codex-run analysis, official sources, vendor
  claims, and estimates.
- When AI materially helped create a post, disclose the useful role when readers
  would reasonably ask; do not use disclosure as a substitute for verification.

## Model-comparison series format

- For head-to-head Claude posts, default to the title pattern
  `<Model A> vs <Model B> - 클로드 모델 비교`. Do not add a separate
  clickbait-style question unless the user requests it.
- Use a consistent split comparison thumbnail: a luminous ivory-and-gold left
  world, a deep charcoal-and-violet right world, a thin glowing diagonal seam,
  and a centered metallic `VS`.
- Give each model one large equal-weight heading, one short Korean role line,
  and one premium rounded-square 3D symbol. Choose different symbols that
  express the models' roles; do not reuse a generic brain icon or copy a
  reference image's exact emblem.
- Keep the composition polished and cinematic with controlled reflections,
  subtle background linework, clear hierarchy, and crop-safe margins. Omit
  multi-row feature lists, benchmark numbers, winner marks, and decorative
  clutter.
- Keep both models visually equal in status. The thumbnail communicates a
  comparison rather than a fight, ranking podium, or predetermined winner.
- In-image text is allowed for this recurring comparison series when it is
  exact, concise, and inspected for spelling before delivery.
- End model-comparison articles with `### 참고 자료`, ordered as official
  sources, independent evaluations, and hands-on tests. This series-level
  reference list is required even when the same links already appear beside
  claims in the body.
