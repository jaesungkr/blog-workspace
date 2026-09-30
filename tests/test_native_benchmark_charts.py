import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from render_rich_post_v2 import benchmark_chart_markup, render_lines


class NativeBenchmarkChartTests(unittest.TestCase):
    def payload(self, **row_changes):
        row = {'model': 'Sol <6.1>', 'score': 31.7, 'cost': 0.19, 'tone': 'sol'}
        row.update(row_changes)
        return json.dumps({'title': 'PDF <test>', 'caption': 'Official & attributed',
                           'groups': [{'label': 'medium', 'rows': [row]}]})

    def test_labels_and_bar_use_same_score_and_escape_source_text(self):
        markup = benchmark_chart_markup(self.payload())
        self.assertIn('31.7%', markup)
        self.assertIn('width:31.7%', markup)
        self.assertIn('$0.19', markup)
        self.assertIn('Sol &lt;6.1&gt;', markup)
        self.assertIn('Official &amp; attributed', markup)
        self.assertIn('0–100', markup)
        self.assertNotIn('<script', markup)

    def test_rejects_invalid_numeric_data_and_unsupported_tones(self):
        for changes in [{'score': -1}, {'score': 101}, {'score': True},
                        {'score': float('nan')}, {'cost': -1},
                        {'cost': float('inf')}, {'cost': False}, {'tone': '"onclick'}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                benchmark_chart_markup(self.payload(**changes))

    def render(self, lines):
        return render_lines(lines, {}, '', 'fragment', ROOT, ROOT)

    def test_chart_is_rendered_and_following_text_survives(self):
        markup = self.render(['before', '', '```benchmark-chart', self.payload(),
                              '```', '', 'after'])
        self.assertIn('devlog-rich__benchmark', markup)
        self.assertIn('before', markup)
        self.assertIn('after', markup)
        self.assertNotIn('"groups"', markup)

    def test_marker_inside_ordinary_fence_stays_code(self):
        for fence in ['````', '~~~~']:
            with self.subTest(fence=fence):
                markup = self.render([fence, '```benchmark-chart', self.payload(),
                                      '```', fence])
                self.assertNotIn('<figure', markup)

    def test_unclosed_chart_fails_instead_of_silently_omitting_data(self):
        with self.assertRaises(ValueError):
            self.render(['```benchmark-chart', self.payload()])
