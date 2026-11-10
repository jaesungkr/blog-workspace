"""Synthetic file-based queue verification, not an agent or automation.

No API calls, CLI agent calls, chat delivery, permission changes, or code edits.
The only filesystem writes are demo outputs under this script's directory.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
STATES = {'AI 작업 중', '내 판단 대기', '외부 요인 대기', '완료'}
FIELDS = ('ID', '상태', '돌아갈 대화', '마지막 갱신', '대기 시작', '마감',
          '다른 작업을 막음', '판단 질문', '결정', '다음 행동')
BEFORE_AT = '2026-11-10T09:10:00+00:00'
AFTER_AT = '2026-11-10T09:16:00+00:00'


def timestamp(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise ValueError('시각에는 시간대가 필요합니다: ' + value)
    return parsed.astimezone(timezone.utc)


def validate(card):
    missing = [key for key in FIELDS if not card.get(key)]
    if missing:
        raise ValueError('필수 항목 누락: ' + ', '.join(missing))
    if not re.fullmatch(r'T[0-9]+', card['ID']):
        raise ValueError('잘못된 작업 ID')
    if card['상태'] not in STATES:
        raise ValueError('정의하지 않은 상태: ' + card['상태'])
    if card['다른 작업을 막음'] not in {'예', '아니요'}:
        raise ValueError('막힘 값은 예 또는 아니요여야 합니다')
    timestamp(card['마지막 갱신'])
    for field in ('대기 시작', '마감'):
        if card[field] != '없음':
            timestamp(card[field])
    if card['상태'] == '내 판단 대기':
        if card['판단 질문'] == '없음' or card['대기 시작'] == '없음':
            raise ValueError('내 판단 대기에는 질문과 대기 시작 시각이 필요합니다')
    return card


def parse_card(text, relative_path):
    card = {'_text': text, '_path': relative_path}
    for key in FIELDS:
        matches = re.findall(r'^- ' + re.escape(key) + r': (.+)$', text, re.M)
        if len(matches) != 1:
            raise ValueError(key + ': 정확히 한 번 있어야 합니다')
        card[key] = matches[0]
    return validate(card)


def load_cards(workspace):
    cards = [parse_card(p.read_text(encoding='utf-8'),
                        p.relative_to(workspace).as_posix())
             for p in sorted((workspace / 'tasks').glob('*.md'))]
    ids = [c['ID'] for c in cards]
    if len(ids) != len(set(ids)):
        raise ValueError('중복 작업 ID')
    if not cards:
        raise ValueError('작업 카드가 없습니다')
    return cards


def queue(cards):
    ids = [c['ID'] for c in cards]
    if len(ids) != len(set(ids)):
        raise ValueError('중복 작업 ID')
    for card in cards:
        validate(card)
    infinity = datetime.max.replace(tzinfo=timezone.utc)
    def key(card):
        deadline = (timestamp(card['마감']) if card['마감'] != '없음'
                    else infinity)
        return (card['다른 작업을 막음'] != '예', deadline,
                timestamp(card['대기 시작']), card['ID'])
    return sorted((c for c in cards if c['상태'] == '내 판단 대기'), key=key)


def render_inbox(cards, generated_at):
    timestamp(generated_at)
    lines = ['# 내 판단 대기함', '', '마지막 갱신: ' + generated_at,
             '', '가상 fixture에서 생성한 스냅샷입니다. 자동 갱신되지 않습니다.', '',
             '정렬: 다른 작업을 막음 → 가까운 마감 → 오래 기다린 순서 → ID.', '']
    selected = queue(cards)
    for index, card in enumerate(selected, 1):
        lines.extend([
            '{}. **{}**: {}'.format(index, card['ID'], card['판단 질문']),
            '   - 카드·근거: [{}]({}#판단-근거)'.format(card['_path'], card['_path']),
            '   - 돌아갈 대화: ' + card['돌아갈 대화'],
        ])
    if not selected:
        lines.append('지금 판단을 기다리는 항목이 없습니다.')
    lines.extend(['', '판단 전 해당 카드를 다시 읽습니다. 한 건의 결정은 원래 작업 대화로',
                  '전달하고, 카드 저장 확인 뒤 대기함 갱신을 다시 요청합니다.', ''])
    return '\n'.join(lines)


def simulate_decision_return(card, decision):
    """Pure simulation: caller-provided delivery flag is NOT delivery evidence."""
    validate(card)
    if decision.get('fixture_only') is not True:
        raise ValueError('이 함수는 가상 fixture 전용입니다')
    if card['상태'] != '내 판단 대기':
        raise ValueError('현재 판단 대기 상태가 아닙니다')
    if decision.get('task_id') != card['ID']:
        raise ValueError('다른 카드에 대한 결정입니다')
    if decision.get('question') != card['판단 질문']:
        raise ValueError('대기 질문이 바뀌었습니다. 다시 확인해야 합니다')
    if decision.get('delivered') is not True:
        raise ValueError('원래 작업 대화에 전달되지 않은 결정입니다')
    if decision.get('delivered_to') != card['돌아갈 대화']:
        raise ValueError('다른 대화로 전달한 결정입니다')
    if timestamp(decision['returned_at']) < timestamp(card['마지막 갱신']):
        raise ValueError('카드보다 오래된 결정입니다')
    if not decision.get('decision') or not decision.get('next_action'):
        raise ValueError('결정과 다음 행동이 필요합니다')
    revised = deepcopy(card)
    updates = {'상태': 'AI 작업 중', '마지막 갱신': decision['returned_at'],
               '대기 시작': '없음', '판단 질문': '없음',
               '결정': decision['decision'], '다음 행동': decision['next_action']}
    for key, value in updates.items():
        revised[key] = value
        revised['_text'] = re.sub(r'^- ' + re.escape(key) + r': .+$',
                                 lambda m: '- ' + key + ': ' + value,
                                 revised['_text'], flags=re.M)
    revised['_text'] += ('\n## 결정 반환 뒤의 가상 기록\n'
                         '위 멈춘 지점과 판단 근거는 결정 전 기록입니다. '
                         '가상 입력에 따라 원래 작업 대화에 결정이 전달되고 '
                         '작업 AI가 카드에 반영했다고 가정했습니다. 실제 메시지를 보내거나 '
                         '버튼을 구현·검증하지 않았습니다. 다음 행동은 아직 미실행입니다.\n')
    return validate(revised)


def write(relative, text):
    path = (ROOT / relative).resolve()
    if ROOT not in path.parents:
        raise ValueError('예제 폴더 밖에는 쓰지 않습니다')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def main():
    cards = load_cards(ROOT / 'ai-work')
    originals = {c['_path']: hashlib.sha256(c['_text'].encode()).hexdigest()
                 for c in cards}
    before = render_inbox(cards, BEFORE_AT)
    write('ai-work/inbox.md', before)
    decision = json.loads((ROOT / 'decision-input.json').read_text(encoding='utf-8'))
    after_cards = [simulate_decision_return(c, decision) if c['ID'] == decision['task_id']
                   else deepcopy(c) for c in cards]
    after = render_inbox(after_cards, AFTER_AT)
    for label, current, inbox in [('before', cards, before), ('after', after_cards, after)]:
        prefix = Path('snapshots') / label / 'ai-work'
        for card in current:
            write(prefix / card['_path'], card['_text'])
        write(prefix / 'inbox.md', inbox)
    before_ids, after_ids = [c['ID'] for c in queue(cards)], [c['ID'] for c in queue(after_cards)]
    assert before_ids == ['T01', 'T02']
    assert after_ids == ['T02']
    for card in load_cards(ROOT / 'ai-work'):
        assert hashlib.sha256(card['_text'].encode()).hexdigest() == originals[card['_path']]
    result = {'kind': 'synthetic_rule_verification', 'actor': 'Codex',
              'input_cards': len(cards), 'before_queue': before_ids,
              'after_simulated_return': after_ids,
              'excluded_in_progress': ['T03'],
              'source_cards_unchanged': True, 'agent_cli_invoked': False,
              'messages_delivered': False, 'product_tests_run': False,
              'productivity_measured': False, 'passed': True}
    write('results.json', json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
