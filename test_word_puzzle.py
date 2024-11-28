from unittest import TestCase
from unittest.mock import patch
import io
from challenges import word_puzzle


class Test(TestCase):
    @patch('random.choice', side_effect=['tuple'])
    @patch('builtins.input', side_effect=['tuple'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_word_puzzle_correct_answer(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = mock_output.getvalue()
        expected =
        self.assertEqual(expected, actual)
