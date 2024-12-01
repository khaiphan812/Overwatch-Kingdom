from unittest import TestCase
from unittest.mock import patch
import io
from challenges import word_puzzle


class Test(TestCase):
    @patch('random.choice', side_effect=['tuple'])
    @patch('random.sample', side_effect=['euplt'])
    @patch('builtins.input', side_effect=['tuple'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_word_puzzle_correct_answer(self, mock_output, _, __, ___):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = mock_output.getvalue()
        expected = ("Welcome to Word Puzzle challenge. "
                    "You must unscramble the given word to overcome this challenge.\n"
                    "Hint: the word is VERY python-related!\n"
                    "Unscramble the word: euplt\n"
                    "Correct! You gained 100 XP (max 600 XP). Your current XP is 200.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['recursion'])
    @patch('random.sample', side_effect=['insoerucr'])
    @patch('builtins.input', side_effect=['curresion'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_word_puzzle_wrong_answer_with_valid_letters(self, mock_output, _, __, ___):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = mock_output.getvalue()
        expected = ("Welcome to Word Puzzle challenge. "
                    "You must unscramble the given word to overcome this challenge.\n"
                    "Hint: the word is VERY python-related!\n"
                    "Unscramble the word: insoerucr\n"
                    "Wrong! The correct word was: recursion\n"
                    "You just lost 1 HP. Your current HP is 4.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['dictionary'])
    @patch('random.sample', side_effect=['ctiioyrand'])
    @patch('builtins.input', side_effect=['dfg%s#fdsa@42'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_word_puzzle_wrong_answer_with_invalid_characters(self, mock_output, _, __, ___):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = mock_output.getvalue()
        expected = ("Welcome to Word Puzzle challenge. "
                    "You must unscramble the given word to overcome this challenge.\n"
                    "Hint: the word is VERY python-related!\n"
                    "Unscramble the word: ctiioyrand\n"
                    "Wrong! The correct word was: dictionary\n"
                    "You just lost 1 HP. Your current HP is 4.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['tuple'])
    @patch('random.sample', side_effect=['euplt'])
    @patch('builtins.input', side_effect=['tupel'])
    def test_word_puzzle_loss_updated_HP(self, _, __, ___):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = char['HP']
        expected = 4
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['tuple'])
    @patch('random.sample', side_effect=['euplt'])
    @patch('builtins.input', side_effect=['tuple'])
    def test_word_puzzle_win_updated_XP(self, _, __, ___):
        char = {'HP': 5, 'XP': 100}
        word_puzzle(char)
        actual = char['XP']
        expected = 200
        self.assertEqual(expected, actual)
