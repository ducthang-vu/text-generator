import unittest
from textgenerator.state import State


class StateTestCase(unittest.TestCase):
    def test_constructor(self):
        state = State('mock_value')
        self.assertEqual(str(state), 'mock_value')

    def test_add_linked_state_first_time(self):
        state = State('mock_value')
        state.add_linked_state('other')
        self.assertEqual(len(state._linked_states), 1)
        self.assertEqual(state._linked_states['other'], 1)

    def test_add_linked_state_multiple_times(self):
        state = State('mock_value')
        state.add_linked_state('other')
        state.add_linked_state('other')
        self.assertEqual(len(state._linked_states), 1)
        self.assertEqual(state._linked_states['other'], 2)

    def test_get_transition_value(self):
        state = State('mock_value')
        state.add_linked_state('other')
        result = state.get_transition_value()
        self.assertEqual(result, 'other')

    def test_get_transition_value_should_raise_error(self):
        state = State('mock_value')
        with self.assertRaises(IndexError):
            state.get_transition_value()


if __name__ == '__main__':
    unittest.main()