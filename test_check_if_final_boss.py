from unittest import TestCase
from challenges import check_if_final_boss


class Test(TestCase):
    def test_check_if_final_boss_insufficient_location_insufficient_level(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 0, 'Level': 1}
        board = {(0, 0): 'Rialto',           (0, 1): 'Havana',
                 (1, 0): 'Circuit Royal',    (1, 1): 'Junkertown'}
        actual = check_if_final_boss(board, char)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_final_boss_insufficient_location_sufficient_level(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 0, 'Level': 3}
        board = {(0, 0): 'Ilios Ruins',      (0, 1): 'Hanamura',
                 (1, 0): 'Circuit Royal',    (1, 1): 'Dorado'}
        actual = check_if_final_boss(board, char)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_final_boss_sufficient_location_insufficient_level(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 2}
        board = {(0, 0): 'Havana',         (0, 1): 'Hanamura',
                 (1, 0): 'Ilios Ruins',    (1, 1): 'Rialto'}
        actual = check_if_final_boss(board, char)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_final_boss_sufficient_location_sufficient_level(self):
        char = {'X-coordinate': 1, 'Y-coordinate': 1, 'Level': 3}
        board = {(0, 0): 'Havana',         (0, 1): 'Rialto',
                 (1, 0): 'Ilios Ruins',    (1, 1): 'Kings Row'}
        actual = check_if_final_boss(board, char)
        expected = True
        self.assertEqual(expected, actual)
