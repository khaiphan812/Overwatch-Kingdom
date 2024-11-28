from unittest import TestCase
from unittest.mock import patch
from game import get_user_direction


class Test(TestCase):

    @patch('builtins.input', side_effect=['w'])
    def test_get_user_direction_North(self, _):
        actual = get_user_direction()
        expected = 'North'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['s'])
    def test_get_user_direction_South(self, _):
        actual = get_user_direction()
        expected = 'South'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_get_user_direction_East(self, _):
        actual = get_user_direction()
        expected = 'East'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    def test_get_user_direction_West(self, _):
        actual = get_user_direction()
        expected = 'West'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2', 's'])
    def test_get_user_direction_invalid_input_number(self, _):
        actual = get_user_direction()
        expected = 'South'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['p', 'a'])
    def test_get_user_direction_invalid_input_letter(self, _):
        actual = get_user_direction()
        expected = 'West'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['k', '3.7', 'd'])
    def test_get_user_direction_invalid_input_letter_and_number(self, _):
        actual = get_user_direction()
        expected = 'East'
        self.assertEqual(expected, actual)

