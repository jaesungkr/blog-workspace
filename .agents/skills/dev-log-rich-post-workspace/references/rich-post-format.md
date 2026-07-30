# Rich-post format

Use this profile when the finished artifact must behave like a designed Tistory
page rather than a generic Markdown conversion.

## Editorial model

- Lead with the product, reader task, and retained result.
- Follow the real user journey. A common sequence is
  `concept -> setup -> action -> result -> failure or limitation -> decision`.
- Give each paragraph one job and each visual one evidence role.
- Use official media for product direction, direct captures for actions and
  observations, GIFs for time-dependent change, and tables for decisions.
- Keep claims, test actor, environment, duration, failures, and untested scope
  explicit.
- Do not repeat visible UI labels in prose unless the label is the instruction.
- Write captions as `what the screen shows + what to notice + why it matters`.
- Use a checklist or FAQ only when it removes a likely follow-up question.
- Do not target a fixed article length, section count, or image count.

## HTML contract

- Emit a full preview document and a Tistory paste fragment.
- Namespace every selector under `.devlog-rich`.
- Put no page-level H1 inside the Tistory fragment; the Tistory skin owns it.
- Use semantic `article`, `nav`, `section`, `figure`, `figcaption`, headings,
  lists, tables, and links.
- Generate stable, unique heading IDs and a TOC that targets every major
  article section.
- Wrap wide tables and code blocks so only the component can scroll.
- Keep every section self-contained so an injected advertisement cannot split
  a paragraph, figure, or grid dependency.
- Keep critical styles inside the fragment. Do not depend on a particular
  Tistory skin class.
- Never emit a local absolute path or unresolved media directive.

## Layout system

Use these defaults unless the subject requires a documented exception:

| Token | Value |
|---|---|
| Media canvas | `980px` maximum |
| Reading measure | `760px` maximum |
| Desktop section padding | `56px 32px` |
| Mobile section padding | `48px 20px` |
| Body | `17px / 1.72` |
| Section heading | `34px / 1.25` |
| Mobile heading | `30px / 1.25` |
| Image radius | `18px` |
| Border | `#e0e0e0` |
| Text | `#1d1d1f` and `#333333` |
| Muted text | `#636366` or darker |
| Link | `#0066cc` |
| Section backgrounds | `#ffffff` and `#f5f5f7` |
| Mobile breakpoint | `735px` |

Keep prose on the reading measure while allowing an evidence image to use the
media canvas. Set an intentional `display_width` for narrow dialogs, mobile
screens, popovers, or terminal crops instead of stretching every asset.

## Media behavior

- Reserve layout space with real `width` and `height` attributes.
- Load the lead image eagerly and below-fold images lazily.
- Preserve aspect ratio and never use a fixed-height crop for evidence.
- Pair a GIF of at most five seconds with a static poster. Hide motion and show
  the exact extracted poster frame when `prefers-reduced-motion: reduce`
  applies. Use a static sequence when the meaningful motion takes longer; this
  profile does not render video.
- Prefer a static sequence when motion does not change meaning.
- Recapture an unreadable full screen as a focused crop. Pinch-to-zoom is not a
  mobile pass.
- Preserve enough surrounding UI to prove location and state.

## Responsive gate

Inspect at `1280px`, `390px`, and `360px`; add `768px` for complex layouts.
Pass only when:

- page `scrollWidth` equals its client width;
- content order and meaning remain the same;
- no capture, caption, table, code block, or link is clipped;
- important UI text is readable without zoom;
- every caption remains attached to its figure;
- tables scroll or transform without compressing into unreadable columns;
- GIF poster and motion frames share the same crop;
- TOC links resolve to exactly one heading;
- the full preview contains one H1 and the paste fragment contains none.

## Publication flow

1. Render a local preview with publishable local assets.
2. Perform a preliminary desktop and mobile inspection.
3. Run `tistory_media_map.py plan`; upload only with explicit authority, or
   receive the final CDN URLs from the user.
4. Bind each HTTPS URL to its media ID with
   `tistory_media_map.py set-url`.
5. Fetch every final URL and create `remote-media.json`.
6. Render a remote-media candidate without the strict flag directly under
   `artifacts/qa/rendered/`; use `capture_rich_qa.py --mode creator` for
   `1280×900`, `390×844`, and `360×800`, then add the human visual decisions
   and write the hash-bound creator QA record.
7. Let the independent article validator refetch the CDN media, strict-render
   a fresh candidate under `artifacts/qa/independent-rendered/`, repeat the
   browser review, and persist `independent-final-page.json`.
8. Set `ready`, then run exactly:

   ```bash
   python3 scripts/blog.py check posts/YYYY-MM-DD-slug --strict
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/check_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls \
     --require-remote-verification \
     --require-independent-pass
   python3 .agents/skills/dev-log-rich-post-workspace/scripts/render_rich_post.py \
     posts/YYYY-MM-DD-slug \
     --require-publish-urls \
     --preview-media-source remote \
     --output-dir dist
   ```
9. Paste into Tistory HTML mode and inspect the actual preview.
10. Let the user perform the final publish action unless explicitly authorized.
11. Validate the supplied live URL and CDN bytes before setting `published`.

## Reject these defects

- duplicated inner title or page H1;
- generic HTML that loses the designed section system;
- official material described as direct use;
- generated or simulated UI presented as product evidence;
- unrecorded crop, annotation, redaction, or format conversion;
- fixed-width content or advertisements causing mobile clipping;
- media without alt, caption, provenance, dimensions, or a claim role;
- an infinite-motion experience with no static equivalent;
- a paste fragment containing local paths, media IDs, or upload placeholders.
