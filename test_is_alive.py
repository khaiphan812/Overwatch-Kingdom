from unittest import TestCase
from game import is_alive


class Test(TestCase):

    def test_is_alive_0_HP(self):
        char = {'HP': 0}
        actual = is_alive(char)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_1_HP(self):
        char = {'HP': 1}
        actual = is_alive(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_2_HP(self):
        char = {'HP': 2}
        actual = is_alive(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_3_HP(self):
        char = {'HP': 3}
        actual = is_alive(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_10_HP(self):
        char = {'HP': 10}
        actual = is_alive(char)
        expected = True
        self.assertEqual(expected, actual)
