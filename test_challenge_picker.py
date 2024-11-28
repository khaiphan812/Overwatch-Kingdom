from unittest import TestCase
from unittest.mock import patch
from game import challenge_picker


class Test(TestCase):

    @patch('random.randint', return_value=1)
    @patch('challenges.skill_cast')
    def test_challenge_picker_random_int_is_1(self, mock_output, _):
        char = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}
        challenge_picker(char)
        mock_output.assert_called_once_with(char)

    @patch('random.randint', return_value=2)
    @patch('challenges.hostage_rescue')
    def test_challenge_picker_random_int_is_2(self, mock_output, _):
        char = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}
        challenge_picker(char)
        mock_output.assert_called_once_with(char)

    @patch('random.randint', return_value=3)
    @patch('challenges.word_puzzle')
    def test_challenge_picker_random_int_is_3(self, mock_output, _):
        char = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}
        challenge_picker(char)
        mock_output.assert_called_once_with(char)

    @patch('random.randint', return_value=4)
    @patch('challenges.word_puzzle')
    def test_challenge_picker_random_int_is_4(self, mock_output, _):
        char = {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}
        challenge_picker(char)
        mock_output.assert_called_once_with(char)
