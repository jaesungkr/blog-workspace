"""Local review render honoring this author's explicit request for no caption.

The shared validator requires a caption. Record that exact, user-authorized
exception; all other errors remain fatal. This does not approve publication.
"""
from pathlib import Path
import json
import sys
bundle=Path(__file__).resolve().parents[1]
repo=bundle.parents[1]
sys.path.insert(0,str(repo/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from rich_post_v2_common import validate_bundle
from render_rich_post_v2 import render_outputs
result=validate_bundle(bundle)
allowed='smoking-cessation-month-3-hero: `caption` must be a non-empty string'
assert json.loads((bundle/'media.json').read_text())['items'][0]['caption']=='', 'Caption exception requires an intentionally empty caption'
other=[e for e in result['errors'] if e!=allowed]
assert not other,other
qa=bundle/'artifacts/qa-v2'
(qa/'caption-exception.json').write_text(json.dumps({'scope':'local author-review candidate','reason':'Author explicitly requested removal of the abstract image explanation; caption is intentionally omitted.','standard_validator_errors':result['errors'],'accepted_exception':allowed,'other_errors':other,'warnings':result['warnings'],'publication_approved':False},ensure_ascii=False,indent=2)+'\n')
for theme,directory in [('light','preflight'),('dark','preflight-dark')]:
 out=qa/directory;out.mkdir(parents=True,exist_ok=True)
 preview,fragment=render_outputs(result,out,preview_media_source='local',preview_theme=theme)
 for suffix,markup in [('rich-preview',preview),('tistory-fragment',fragment)]:
  # This article has one short, two-column table; keep both columns visible.
  markup=markup.replace('min-width: 620px;', 'min-width: 0; table-layout: fixed;')
  markup=markup.replace('</style>', '.devlog-rich .rich-table-wrap th:first-child { width: 36%; }\n</style>')
  markup=markup.replace('<figcaption class="devlog-rich__caption"></figcaption>','')
  (out/f'smoking-cessation-month-3-{suffix}.html').write_text(markup)
 print(theme+': rendered without caption; no other validation errors')
