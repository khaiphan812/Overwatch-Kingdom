from unittest import TestCase
from game import make_final_boss


class Test(TestCase):

    def test_make_final_boss_contains_HP_key(self):
        result = make_final_boss()
        self.assertIn('HP', result)

    def test_make_final_boss_contains_Weapon_key(self):
        result = make_final_boss()
        self.assertIn('Weapon', result)

    def test_make_final_boss_HP_value_is_10(self):
        result = make_final_boss()
        actual = result['HP']
        expected = 10
        self.assertEqual(expected, actual)

    def test_make_final_boss_Weapon_value_is_Destructive_Flail(self):
        result = make_final_boss()
        actual = result['Weapon']
        expected = 'Destructive Flail'
        self.assertEqual(expected, actual)
