import sys
import unittest
from io import StringIO
from unittest.mock import patch

from main import generate_text, main
from textgenerator.text_generator import TextGenerator


class MainTestCase(unittest.TestCase):
    @patch.object(TextGenerator, 'get_new_text')
    @patch('builtins.print')
    def test_generate_text(self, mock_print, mock_text_generator):
        generate_text('lady_gaga', 100)
        self.assertEqual(mock_print.called, True)

    @patch('main.generate_text')
    def test_main(self, mock):
        arg = ['prog', '-a', 'katy_perry', '-l', '100']
        with patch.object(sys, 'argv', arg):
            main()
            self.assertEqual(mock.called, True)
            mock.assert_called_with('katy_perry', 100)

    @patch('sys.stderr', new_callable=StringIO)
    def test_main_missing_cli_arguments(self, mock):
        args = [
            ['prog'],
            ['prog', '-a', 'mock'],
            ['prog', '-l', 'mock']
        ]
        for arg in args:
            with patch.object(sys, 'argv', arg):
                self.assertRaises(SystemExit, main)
                self.assertRegex(mock.getvalue(), r'the following arguments are required')

    @patch('sys.stderr', new_callable=StringIO)
    def test_main_invalid_cli_arguments(self, mock):
        with patch.object(sys, 'argv', ['prog', '-a', 'mock', '-l', '100']):
            self.assertRaises(SystemExit, main)
            self.assertRegex(mock.getvalue(), r"invalid choice: 'mock'")

        with patch.object(sys, 'argv', ['prog', '-a', 'lady_gaga', '-l', 'ooo']):
            self.assertRaises(SystemExit, main)
            self.assertRegex(mock.getvalue(), r"invalid int value")


if __name__ == '__main__':
    unittest.main()
