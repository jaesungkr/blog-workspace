"""Exercise canonical quote boxes against skin overrides in local Chromium."""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'
sys.path.insert(0, str(SCRIPTS))
from render_rich_post_v2 import render_outputs


class RichPromptDefaultsTests(unittest.TestCase):
    def render(self, directory, theme='light'):
        result = {
            'post_dir': directory,
            'meta': {'title': 'Format regression'},
            'body': 'Intro.\n\n### Request\n\n> Keep this request unchanged.\n> https://example.com/' + 'x' * 180 + '\n\n### Quotation\n\n> An attributed quotation, not a command.\n\nOrdinary prose.\n',
            'manifest': {'lead_id': ''}, 'items_by_id': {},
        }
        return render_outputs(result, directory, preview_theme=theme)

    def test_canonical_structure_preserves_quote_content_without_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            preview, fragment = self.render(Path(tmp))
        self.assertIn('<article class="devlog-rich">', fragment)
        self.assertEqual(1, fragment.count('<nav class="devlog-rich__toc"'))
        self.assertIn('devlog-rich__section is-alt', fragment)
        self.assertEqual(2, fragment.count('<blockquote>'))
        self.assertIn('Keep this request unchanged.', fragment)
        self.assertIn('An attributed quotation, not a command.', fragment)
        self.assertNotIn('class="prompt-label"', fragment)

    def test_theme_color_pairs_meet_text_contrast_and_mobile_rule_is_included(self):
        with tempfile.TemporaryDirectory() as tmp:
            for theme in ('light', 'dark'):
                preview, fragment = self.render(Path(tmp), theme)
                self.assertIn('padding: 16px !important;', fragment)
                self.assertIn('overflow-wrap: anywhere !important;', fragment)
                rules = re.search(r'(?:\.dark )?\.devlog-rich \{(.*?)\}', fragment, re.S)
                if theme == 'dark':
                    rules = re.search(r'\.dark \.devlog-rich \{(.*?)\}', fragment, re.S)
                values = dict(re.findall(r'(--[\w-]+):\s*(#[0-9a-f]{6});', rules.group(1)))
                def luminance(color):
                    rgb = [int(color[i:i+2], 16)/255 for i in (1,3,5)]
                    v = [x/12.92 if x <= .04045 else ((x+.055)/1.055)**2.4 for x in rgb]
                    return sum(x*y for x,y in zip(v,(.2126,.7152,.0722)))
                low, high = sorted(luminance(values[k]) for k in ('--rich-body','--rich-pre-bg'))
                self.assertGreaterEqual((high+.05)/(low+.05), 4.5)

    @unittest.skipUnless(os.environ.get('RUN_RICH_BROWSER_TESTS') == '1' and shutil.which('chromium'), 'opt-in local browser test: RUN_RICH_BROWSER_TESTS=1')
    def test_computed_boxes_in_both_themes_at_desktop_and_mobile(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            frames = []
            for theme in ('light', 'dark'):
                for width in (1280, 360):
                    preview, _ = self.render(directory, theme)
                    # Deliberately later skin declarations reproduce the original defect.
                    preview = preview.replace('</head>', '<style>blockquote{color:#666;background:transparent;padding:0;border:0;margin:20px 0 0}</style></head>')
                    frames.append(f'<iframe data-theme="{theme}" width="{width}" height="900" srcdoc="{html.escape(preview, quote=True)}"></iframe>')
            js = '''
window.onload=()=>{
 const rows=[...document.querySelectorAll('iframe')].map(f=>{
  const d=f.contentDocument, q=d.querySelector('blockquote'), s=f.contentWindow.getComputedStyle(q);
  const parent=q.parentElement.getBoundingClientRect();
  return {theme:f.dataset.theme,width:+f.width,color:s.color,bg:s.backgroundColor,padding:s.paddingLeft,border:parseFloat(s.borderLeftWidth),radius:s.borderRadius,overflow:q.scrollWidth>q.clientWidth,contained:q.getBoundingClientRect().right<=parent.right};
 });
 document.getElementById('report').textContent=JSON.stringify(rows);
};'''
            path = directory / 'test.html'
            path.write_text(''.join(frames) + '<pre id="report"></pre><script>' + js + '</script>')
            run = subprocess.run([shutil.which('chromium'), '--headless', '--user-data-dir=' + str(directory / 'browser-profile'), '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--virtual-time-budget=3000', '--dump-dom', path.as_uri()], capture_output=True, text=True, timeout=30)
            self.assertEqual(0, run.returncode, run.stderr[-1000:])
            match = re.search(r'<pre id="report">(.*?)</pre>', run.stdout, re.S)
            self.assertIsNotNone(match)
            rows = json.loads(html.unescape(match.group(1)))
            self.assertEqual(4, len(rows))
            for row in rows:
                with self.subTest(**row):
                    self.assertEqual('rgb(209, 209, 214)' if row['theme']=='dark' else 'rgb(51, 51, 51)', row['color'])
                    self.assertEqual('rgb(37, 38, 41)' if row['theme']=='dark' else 'rgb(246, 246, 246)', row['bg'])
                    self.assertEqual('16px' if row['width']==360 else '20px', row['padding'])
                    self.assertGreaterEqual(row['border'], 2)
                    self.assertEqual('12px', row['radius'])
                    self.assertFalse(row['overflow'])
                    self.assertTrue(row['contained'])
                    def lum(rgb):
                        nums=[int(x)/255 for x in re.findall(r'\d+',rgb)]
                        vals=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in nums]
                        return sum(a*b for a,b in zip(vals,(.2126,.7152,.0722)))
                    a,b=sorted((lum(row['color']),lum(row['bg'])))
                    self.assertGreaterEqual((b+.05)/(a+.05),4.5)
