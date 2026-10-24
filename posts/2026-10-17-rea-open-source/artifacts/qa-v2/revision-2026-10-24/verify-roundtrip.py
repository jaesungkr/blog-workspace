from pathlib import Path
import csv
import io
import json
import subprocess

root = Path(__file__).resolve().parent
process = subprocess.run(['node', str(root / 'verify-csv.cjs')], check=True, text=True, capture_output=True)
(root / 'csv-results.json').write_text(process.stdout)
results = json.loads(process.stdout)['results']
checks = []
for case in results:
    actual = list(csv.reader(io.StringIO(case['actual'], newline='')))
    expected = [['id', 'title']] + [[str(note['id']), note['title']] for note in case['input']]
    checks.append({'name': case['name'], 'exact_output_pass': case['pass'], 'parsed_rows': actual, 'roundtrip_pass': actual == expected})
    assert case['pass'] and actual == expected, case['name']
(root / 'csv-roundtrip.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n')
print(f'{len(checks)} cases passed exact output and CSV roundtrip checks.')
