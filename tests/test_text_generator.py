import unittest
from pathlib import Path
from unittest.mock import patch, mock_open

from textgenerator.markov_chain import MarkovChain
from textgenerator.text_generator import TextGenerator


class StateTestCase(unittest.TestCase):
    @patch.object(Path, 'glob')
    @patch('builtins.open', new_callable=mock_open, read_data='a1 (a2, a3\nb1 {b2 )b3 c\n d')
    def test_constructor(self, mock, path_mock):
        path_mock.return_value = ['abc', 'def']
        text_generator = TextGenerator('lady_gaga')
        self.assertEqual(set(text_generator._chain._states), {'a', 'b', 'c', 'd'})
        self.assertEqual(type(text_generator._chain), MarkovChain)

    def test_constructor_raise_KeyError(self):
        def create_text_generator_fake_author():
            return TextGenerator('fakeAuthor')
        self.assertRaises(KeyError, create_text_generator_fake_author)

    def test_constructor_raise_TypeError(self):
        self.assertRaises(TypeError, TextGenerator)

    @patch.object(MarkovChain, 'get_sequence')
    def test_get_new_text(self, mock):
        mock.return_value = ['abc', 'def']
        text_generator = TextGenerator('lady_gaga')
        result = text_generator.get_new_text()
        self.assertTrue(mock.called)
        self.assertEqual(result, 'abc def')

        with self.subTest(mgs='text should be of 100 words'):
            text_generator.get_new_text()
            mock.assert_called_with(100)

        with self.subTest(mgs='text should be of 75 words'):
            text_generator.get_new_text(75)
            mock.assert_called_with(75)


if __name__ == '__main__':
    unittest.main()