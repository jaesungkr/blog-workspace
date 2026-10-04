"""Render this user-requested text-only body with the existing v2 renderer.

The user explicitly requested a separate thumbnail and no body images.
Only the three media-required checker errors are excluded. Repository tools
and their global contracts remain unchanged. Run while lifecycle is reviewing.
"""
from pathlib import Path
import hashlib
import json
import sys

POST = Path(__file__).resolve().parents[1]
REPO = POST.parents[1]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from render_rich_post_v2 import render_outputs
from rich_post_v2_common import validate_bundle

ALLOWED = {
    'media.json `items` must be a non-empty array',
    'media.json `lead_id` must reference a registered item',
    'exactly one media item must use role `lead` and match lead_id',
}
result = validate_bundle(POST)
if result['meta'].get('status') != 'reviewing':
    raise SystemExit('Render the candidate while reviewing.')
unexpected = set(result['errors']) - ALLOWED
if unexpected:
    raise SystemExit('\n'.join(sorted(unexpected)))
if result['manifest'] != {'version': 2, 'lead_id': None, 'items': []}:
    raise SystemExit('This exception applies only to the empty body manifest.')
if '{{media:' in result['body'] or '![' in result['body']:
    raise SystemExit('Body media is incompatible with the user exception.')
slug = result['meta']['slug']
qa = POST / 'artifacts/qa-v2'
hashes = {}
last_fragment = None
for theme, dirname in [('light', 'final-rendered'), ('dark', 'final-dark-rendered')]:
    target = qa / dirname
    target.mkdir(parents=True, exist_ok=True)
    preview, fragment = render_outputs(result, target, preview_theme=theme)
    if '<img' in fragment or '<h1' in fragment or '{{media:' in fragment:
        raise SystemExit('Unexpected media, H1 or unresolved token.')
    if last_fragment is not None and fragment != last_fragment:
        raise SystemExit('Theme-dependent fragment bytes.')
    last_fragment = fragment
    for name, content in [(f'{slug}-rich-preview.html', preview), (f'{slug}-tistory-fragment.html', fragment)]:
        (target / name).write_text(content)
        hashes[str((target / name).relative_to(POST))] = hashlib.sha256(content.encode()).hexdigest()
record = {
    'version': 2,
    'scope': 'user-requested-thumbnail-only',
    'user_instruction': '이미지는 썸네일에 넣을거라서 따로 본문에는 추가안해도되고. 썸네일 이미지만 만들어주면되는거야.',
    'excluded_checks': sorted(result['errors']),
    'body_media_count': 0,
    'body_remote_media': 'not_applicable',
    'strict_v2_media_gate': 'not_applicable_by_user_instruction',
    'hashes': hashes,
}
(qa / 'thumbnail-only-render.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(hashes, indent=2))
