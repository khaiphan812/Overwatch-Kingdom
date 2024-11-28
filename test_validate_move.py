from unittest import TestCase
from game import validate_move


class Test(TestCase):

    def test_validate_move_out_of_North_bound(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = 'North'
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_South_bound(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 1, 'Y-coordinate': 0}
        direction = "South"
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_East_bound(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 1}
        direction = "East"
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_out_of_West_bound(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "West"
        actual = validate_move(board, character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_valid_North_move(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 1, 'Y-coordinate': 0}
        direction = "North"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_valid_South_move(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "South"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_valid_East_move(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = "East"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_valid_West_move(self):
        board = {(0, 0): 'Eichenwalde', (0, 1): 'Dorado',
                 (1, 0): 'Havana',      (1, 1): 'Black Forest'}
        character = {'X-coordinate': 0, 'Y-coordinate': 1}
        direction = "West"
        actual = validate_move(board, character, direction)
        expected = True
        self.assertEqual(expected, actual)
