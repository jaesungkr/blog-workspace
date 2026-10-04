"""Deliver the reviewed text-only candidate under the user's media exception."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

POST = Path(__file__).resolve().parents[1]
REPO = POST.parents[1]
QA = POST / 'artifacts/qa-v2'
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from rich_post_v2_common import article_content_sha256, split_frontmatter

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

output = Path(sys.argv[1]).expanduser().resolve()
article = POST / 'article.md'
source_path = QA / 'source-pass.json'
source = json.loads(source_path.read_text())
review_path = QA / 'thumbnail-only-final-page.json'
review = json.loads(review_path.read_text())
meta, body = split_frontmatter(article.read_text())
assert meta['status'] == 'reviewing'
assert source['result'] == review['result'] == 'pass'
assert source['article_content_sha256'] == article_content_sha256(article)
assert source['brief_sha256'] == digest(POST / 'brief.md')
assert source['evidence_sha256'] == digest(POST / 'evidence.md')
assert review['source_pass_sha256'] == digest(source_path)
assert review['article_content_sha256'] == article_content_sha256(article)
slug = meta['slug']
light = QA / 'final-rendered' / f'{slug}-rich-preview.html'
dark = QA / 'final-dark-rendered' / f'{slug}-rich-preview.html'
fragment = QA / 'final-rendered' / f'{slug}-tistory-fragment.html'
dark_fragment = QA / 'final-dark-rendered' / f'{slug}-tistory-fragment.html'
assert review['preview_sha256'] == digest(light)
assert review['dark_preview_sha256'] == digest(dark)
assert review['fragment_sha256'] == digest(fragment) == digest(dark_fragment)
assert fragment.read_bytes() == dark_fragment.read_bytes()
thumbnail = json.loads((POST / 'thumbnail.json').read_text())
assert thumbnail['status'] == 'validated'
assert thumbnail['sha256'] == digest(POST / thumbnail['publish_path'])
assert '<img' not in fragment.read_text() and '<h1' not in fragment.read_text()
assert '{{media:' not in fragment.read_text() and '/Users/' not in fragment.read_text()
subprocess.run([sys.executable, str(REPO / 'scripts/blog.py'), 'check', str(POST)], check=True)
output.mkdir(parents=True, exist_ok=True)
copies = [
    (fragment, output / f'{slug}-tistory-fragment.txt'),
    (light, output / f'{slug}-preview.html'),
    (dark, output / f'{slug}-preview-dark.html'),
    (POST / 'artifacts/thoughts-polished.md', output / f'{slug}-thoughts.md'),
]
for src, dst in copies:
    shutil.copyfile(src, dst)
    assert digest(src) == digest(dst)
readable = output / f'{slug}-final.md'
readable.write_text(f'# {meta["title"]}\n\n' + body.lstrip())
original = article.read_text()
assert original.count('status: reviewing') == 1
article.write_text(original.replace('status: reviewing', 'status: ready', 1))
assert article_content_sha256(article) == source['article_content_sha256']
record = {
    'version': 2,
    'result': 'pass',
    'scope': 'user-requested-thumbnail-only',
    'ready_basis': 'independent source, separate thumbnail, actual light/dark desktop/mobile page approval',
    'strict_v2_media_gate': 'not_applicable_by_user_instruction',
    'source_pass_sha256': digest(source_path),
    'page_pass_sha256': digest(review_path),
    'fragment_sha256': digest(fragment),
    'paste_file_sha256': digest(copies[0][1]),
    'output_files': [str(dst) for _, dst in copies] + [str(readable)],
}
(QA / 'thumbnail-only-delivery.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
