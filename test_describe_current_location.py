from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location
import io


class Test(TestCase):

    @patch('random.choice', side_effect=['Rialto'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_at_start_point(self, mock_output, _):
        gameboard = {(0, 0): 'Rialto'}
        char = {"X-coordinate": 0, "Y-coordinate": 0}
        describe_current_location(gameboard, char)
        actual = mock_output.getvalue()
        expected = "You have arrived at Rialto.\n"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Rialto', 'Havana', 'Circuit Royal', 'Junkertown',])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_at_boundary(self, mock_output, _):
        gameboard = {(0, 0): 'Rialto', (0, 1): 'Havana',
                     (1, 0): 'Circuit Royal',       (1, 1): 'Black Forest'}
        char = {"X-coordinate": 1, "Y-coordinate": 0}
        describe_current_location(gameboard, char)
        actual = mock_output.getvalue()
        expected = "You have arrived at Circuit Royal.\n"
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Rialto', 'Havana', 'Circuit Royal',
                                         'Junkertown', 'Black Forest', 'Necropolis',
                                         'Eichenwalde', 'Numbani', 'Hanamura'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_at_non_boundary(self, mock_output, _):
        gameboard = {(0, 0): 'Rialto', (0, 1): 'Havana', (0, 2): 'Circuit Royal',
                     (1, 0): 'Junkertown',    (1, 1): 'Black Forest',    (1, 2): 'Necropolis',
                     (2, 0): 'Eichenwalde', (2, 1): 'Numbani', (2, 2): 'Hanamura'}
        char = {"X-coordinate": 1, "Y-coordinate": 1}
        describe_current_location(gameboard, char)
        actual = mock_output.getvalue()
        expected = "You have arrived at Black Forest.\n"
        self.assertEqual(expected, actual)
