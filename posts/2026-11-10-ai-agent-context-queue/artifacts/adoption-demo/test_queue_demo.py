from copy import deepcopy
import json
import unittest
import queue_demo as demo


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.cards = demo.load_cards(demo.ROOT / 'ai-work')
        self.decision = json.loads((demo.ROOT / 'decision-input.json').read_text(encoding='utf-8'))

    def ids(self, cards):
        return [c['ID'] for c in demo.queue(cards)]

    def test_three_fixtures_two_decisions(self):
        self.assertEqual(len(self.cards), 3)
        self.assertEqual(self.ids(self.cards), ['T01', 'T02'])

    def test_all_states_only_human_wait_is_selected(self):
        for state in demo.STATES:
            card = deepcopy(self.cards[0])
            card['상태'] = state
            self.assertEqual(self.ids([card]), ['T01'] if state == '내 판단 대기' else [])

    def test_blocking_precedes_deadline(self):
        self.assertEqual(self.ids(self.cards), ['T01', 'T02'])

    def test_deadline_precedes_wait_age_when_blocking_tied(self):
        self.cards[0]['다른 작업을 막음'] = '아니요'
        self.assertEqual(self.ids(self.cards), ['T02', 'T01'])

    def test_oldest_wait_when_blocking_and_deadline_tied(self):
        self.cards[0]['다른 작업을 막음'] = '아니요'
        self.cards[1]['마감'] = '없음'
        self.assertEqual(self.ids(self.cards), ['T02', 'T01'])

    def test_id_is_stable_tie_breaker(self):
        self.cards[0]['다른 작업을 막음'] = '아니요'
        self.cards[1]['마감'] = '없음'
        self.cards[1]['대기 시작'] = self.cards[0]['대기 시작']
        self.assertEqual(self.ids(list(reversed(self.cards))), ['T01', 'T02'])

    def test_empty_inbox_message(self):
        self.assertIn('지금 판단을 기다리는 항목이 없습니다.',
                      demo.render_inbox([self.cards[2]], demo.BEFORE_AT))

    def test_pending_without_question_is_rejected(self):
        self.cards[0]['판단 질문'] = '없음'
        with self.assertRaises(ValueError):
            demo.queue(self.cards)

    def test_duplicate_id_is_rejected(self):
        with self.assertRaises(ValueError):
            demo.queue(self.cards + [deepcopy(self.cards[0])])

    def test_unknown_status_is_rejected(self):
        self.cards[0]['상태'] = '아마 완료'
        with self.assertRaises(ValueError):
            demo.queue(self.cards)

    def test_timezone_required(self):
        with self.assertRaises(ValueError):
            demo.timestamp('2026-11-10T09:00:00')

    def test_render_preserves_cards_and_keeps_details_in_card(self):
        original = deepcopy(self.cards)
        inbox = demo.render_inbox(self.cards, demo.BEFORE_AT)
        self.assertEqual(self.cards, original)
        self.assertIn('마지막 갱신: ' + demo.BEFORE_AT, inbox)
        self.assertIn('tasks/T01-login.md#판단-근거', inbox)
        self.assertIn('돌아갈 대화: 로그인 수정', inbox)
        self.assertNotIn('추천: B입니다.', inbox)
        self.assertNotIn('T03', inbox)

    def test_unreturned_decision_does_not_remove_question(self):
        self.decision['delivered'] = False
        with self.assertRaises(ValueError):
            demo.simulate_decision_return(self.cards[0], self.decision)
        self.assertEqual(self.ids(self.cards), ['T01', 'T02'])

    def test_wrong_destination_is_rejected(self):
        self.decision['delivered_to'] = '검토 대화'
        with self.assertRaises(ValueError):
            demo.simulate_decision_return(self.cards[0], self.decision)

    def test_stale_question_is_rejected(self):
        self.decision['question'] = '질문이 바뀌었습니다'
        with self.assertRaises(ValueError):
            demo.simulate_decision_return(self.cards[0], self.decision)

    def test_older_decision_is_rejected(self):
        self.decision['returned_at'] = '2026-11-10T08:00:00+00:00'
        with self.assertRaises(ValueError):
            demo.simulate_decision_return(self.cards[0], self.decision)

    def test_return_updates_status_decision_next_action_and_excludes(self):
        original = deepcopy(self.cards[0])
        revised = demo.simulate_decision_return(self.cards[0], self.decision)
        self.assertEqual(revised['상태'], 'AI 작업 중')
        self.assertEqual(revised['결정'], self.decision['decision'])
        self.assertEqual(revised['다음 행동'], self.decision['next_action'])
        self.assertEqual(self.cards[0], original)
        self.assertEqual(self.ids([revised] + self.cards[1:]), ['T02'])
        reparsed = demo.parse_card(revised['_text'], revised['_path'])
        self.assertEqual(reparsed['결정'], self.decision['decision'])
        self.assertEqual(reparsed['상태'], 'AI 작업 중')

    def test_repeated_return_is_rejected(self):
        revised = demo.simulate_decision_return(self.cards[0], self.decision)
        with self.assertRaises(ValueError):
            demo.simulate_decision_return(revised, self.decision)


if __name__ == '__main__':
    unittest.main(verbosity=2)
