import unittest
from textgenerator.markov_chain import MarkovChain


class MarkovChainTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.words = ['word1', 'word2', 'word3', 'word2', 'word3', 'word2', 'word4']
        self.chain = MarkovChain(self.words)

    def test_constructor(self):
        with self.subTest(mgs='test that single words are stored by chain'):
            self.assertEqual(len(self.chain._states), 4)
            self.assertEqual(set(self.chain._states.keys()), set(self.words))
        with self.subTest(mgs='test that word1 is followed by only word2'):
            self.assertEqual(set(self.chain._states['word1']._linked_states), {'word2'})
            self.assertEqual(self.chain._states['word1']._linked_states['word2'], 1)
        with self.subTest(mgs='test that word2 is followed by only word3 and word4'):
            self.assertEqual(set(self.chain._states['word2']._linked_states), {'word3', 'word4'})
            self.assertEqual(self.chain._states['word2']._linked_states['word3'], 2)
            self.assertEqual(self.chain._states['word2']._linked_states['word4'], 1)
        with self.subTest(mgs='test that word3 is followed by only word2'):
            self.assertEqual(set(self.chain._states['word3']._linked_states), {'word2'})
            self.assertEqual(self.chain._states['word3']._linked_states['word2'], 2)
        with self.subTest(mgs='test that word4 is followed by no words'):
            self.assertEqual(set(self.chain._states['word4']._linked_states), set())

    def test_get_sequence(self):
        with self.subTest(mgs='should return a 100 string list'):
            text = self.chain.get_sequence()
            self.assertEqual(len(text), 100)

        with self.subTest(mgs='should return a 50 string list'):
            text = self.chain.get_sequence(50)
            self.assertEqual(len(text), 50)

        with self.subTest(mgs='should return a 15000 string list'):
            text = tuple(map(str, self.chain.get_sequence(500)))
            self.chain.get_sequence(500)
            for index, word in enumerate(text[1:], 1):
                if word in ('word3', 'word4'):
                    self.assertIn(text[index - 1], ('word2', 'word4'))
                if word == 'word2':
                    self.assertIn(text[index - 1], ('word1', 'word3', 'word4'))

        with self.subTest(mgs='should return a 250 string list (numeric string)'):
            words = ['1', '2', '3', '4', '5', '6', '7']
            chain = MarkovChain(words)
            sequence = chain.get_sequence(250)
            for index, state in enumerate(sequence[1:], 1):
                if word != '1' and str(sequence[index - 1]) != '7':
                    self.assertEqual(int(str(state)), int(str(sequence[index - 1])) + 1)
                if word == '1':
                    self.assertEqual(str(sequence[index - 1]), '7')


if __name__ == '__main__':
    unittest.main()