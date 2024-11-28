from unittest import TestCase
from unittest.mock import patch
from game import check_for_challenge


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_check_for_challenge_random_int_is_1(self, _):
        actual = check_for_challenge()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_check_for_challenge_random_int_is_2(self, _):
        actual = check_for_challenge()
        expected = False
        self.assertEqual(expected, actual)
