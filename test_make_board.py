from unittest import TestCase
from unittest.mock import patch
from board import make_board


class Test(TestCase):

    @patch('random.choice', side_effect=['Rialto'])
    def test_make_board_one_by_one_size(self, _):
        actual = make_board(1, 1)
        expected = {(0, 0): 'Rialto'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Rialto', 'Havana', 'Circuit Royal', 'Junkertown'])
    def test_make_board_square_size(self, _):
        actual = make_board(2, 2)
        expected = {(0, 0): 'Rialto',           (0, 1): 'Havana',
                    (1, 0): 'Circuit Royal',    (1, 1): 'Junkertown'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Rialto', 'Havana', 'Circuit Royal',
                                         'Junkertown', 'Black Forest', 'Necropolis'])
    def test_make_board_two_rows_three_columns_size(self, _):
        actual = make_board(2, 3)
        expected = {(0, 0): 'Rialto',       (0, 1): 'Havana',       (0, 2): 'Circuit Royal',
                    (1, 0): 'Junkertown',   (1, 1): 'Black Forest', (1, 2): 'Necropolis'}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Rialto', 'Havana', 'Circuit Royal',
                                         'Black Forest', 'Necropolis', 'Kings Row'])
    def test_make_board_three_rows_two_columns_size(self, _):
        actual = make_board(3, 2)
        expected = {(0, 0): 'Rialto',         (0, 1): 'Havana',
                    (1, 0): 'Circuit Royal',  (1, 1): 'Black Forest',
                    (2, 0): 'Necropolis',     (2, 1): 'Kings Row'}
        self.assertEqual(expected, actual)
