"""Recalculate differences from cited published numbers; does not run AI models."""
from decimal import Decimal as D
from pathlib import Path
import json
p=Path(__file__).resolve().parent
inputs=json.loads((p/'published-values.json').read_text())
def sub(a,b):return str(D(str(a))-D(str(b)))
def div(a,b):return round(float(D(str(a))/D(str(b))),4)
out={
 'actor':'Codex arithmetic on published values; no model trial',
 'terminal_sonnet_max_minus_opus_high_pp':sub(70.6,64.2),
 'frontier2_sonnet_max_minus_opus_high_pp':sub(41,34.5),
 'cursor_opus_high_minus_sonnet_max_pp':sub(56,55.5),
 'opus_medium_to_high_pp':sub(95.3,92.8),
 'opus_high_to_xhigh_pp':sub(96.7,95.3),
 'opus_high_to_xhigh_cost_ratio_rounded_inputs':div(.74,.29),
 'opus_cost_note':'Article uses source stated approximately 2.5x from unrounded costs; rounded inputs yield 2.5517x.',
 'claude_aa_sonnet_to_opus_cost_ratio':div(10.02,3.46),
 'claude_aa_sonnet_to_opus_output_ratio':div(285000,60000),
 'sol_high_to_max_index_delta':sub(55,50),
 'sol_high_to_max_cost_ratio':div(1.27,.59),
 'index_note':'Index points are not percentages and ratios are not IQ comparisons.'}
(p/'calculated-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
