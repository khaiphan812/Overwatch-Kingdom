from unittest import TestCase
from game import is_alive


class Test(TestCase):

    def test_is_alive_0_HP(self):
        character = {'HP': 0}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_1_HP(self):
        char = {'HP': 1}
        actual = is_alive(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_2_HP(self):
        character = {'HP': 2}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_3_HP(self):
        character = {'HP': 3}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_10_HP(self):
        character = {'HP': 10}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)
