from unittest import TestCase
from game import move_character


class Test(TestCase):

    def test_move_character_North(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 0}
        direction = 'North'
        actual = move_character(char, direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 0}
        self.assertEqual(expected, actual)

    def test_move_character_South(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'South'
        actual = move_character(char, direction)
        expected = {'X-coordinate': 2, 'Y-coordinate': 1}
        self.assertEqual(expected, actual)

    def test_move_character_East(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 0}
        direction = 'East'
        actual = move_character(char, direction)
        expected = {'X-coordinate': 1, 'Y-coordinate': 1}
        self.assertEqual(expected, actual)

    def test_move_character_West(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'West'
        actual = move_character(char, direction)
        expected = {'X-coordinate': 1, 'Y-coordinate': 0}
        self.assertEqual(expected, actual)
