from unittest import TestCase
from unittest.mock import patch
import io
from challenges import hostage_rescue


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hostage_rescue_correct_guess_at_lower_bound(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = mock_output.getvalue()
        expected = ("Master Doom's minions are holding a number of citizens as hostage.\n"
                    "Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.\n"
                    "Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!\n"
                    "Correct! You just rescued the victims and gained 100 XP (max 600 XP)! Your current XP is 200.\n")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hostage_rescue_correct_guess_at_upper_bound(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = mock_output.getvalue()
        expected = ("Master Doom's minions are holding a number of citizens as hostage.\n"
                    "Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.\n"
                    "Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!\n"
                    "Correct! You just rescued the victims and gained 100 XP (max 600 XP)! Your current XP is 200.\n")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hostage_rescue_correct_guess_between_bounds(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = mock_output.getvalue()
        expected = ("Master Doom's minions are holding a number of citizens as hostage.\n"
                    "Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.\n"
                    "Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!\n"
                    "Correct! You just rescued the victims and gained 100 XP (max 600 XP)! Your current XP is 200.\n")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hostage_rescue_wrong_guess_lower_than_result(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = mock_output.getvalue()
        expected = ("Master Doom's minions are holding a number of citizens as hostage.\n"
                    "Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.\n"
                    "Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!\n"
                    "Wrong! The correct number of hostage is 3. "
                    "You just lost 1 HP. Your current HP is 4.\n")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hostage_rescue_wrong_guess_higher_than_result(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = mock_output.getvalue()
        expected = ("Master Doom's minions are holding a number of citizens as hostage.\n"
                    "Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.\n"
                    "Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!\n"
                    "Wrong! The correct number of hostage is 2. "
                    "You just lost 1 HP. Your current HP is 4.\n")
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    @patch('random.randint', return_value=2)
    def test_hostage_rescue_wrong_guess_update_HP(self, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = char['HP']
        expected = 4
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    @patch('random.randint', return_value=3)
    def test_hostage_rescue_correct_guess_update_XP(self, _, __):
        char = {'HP': 5, 'XP': 100}
        hostage_rescue(char)
        actual = char['XP']
        expected = 200
        self.assertEqual(expected, actual)
