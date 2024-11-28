from unittest import TestCase
from game import make_character


class Test(TestCase):

    def test_make_character_contains_X_coordinate_key(self):
        result = make_character()
        self.assertIn('X-coordinate', result)

    def test_make_character_contains_Y_coordinate_key(self):
        result = make_character()
        self.assertIn('Y-coordinate', result)

    def test_make_character_contains_HP_key(self):
        result = make_character()
        self.assertIn('HP', result)

    def test_make_character_contains_XP_key(self):
        result = make_character()
        self.assertIn('XP', result)

    def test_make_character_contains_Level_key(self):
        result = make_character()
        self.assertIn('Level', result)

    def test_make_character_contains_Weapon_key(self):
        result = make_character()
        self.assertIn('Weapon', result)

    def test_make_character_X_coordinate_value_is_0(self):
        result = make_character()
        actual = result['X-coordinate']
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_Y_coordinate_value_is_0(self):
        result = make_character()
        actual = result['Y-coordinate']
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_HP_value_is_5(self):
        result = make_character()
        actual = result['HP']
        expected = 5
        self.assertEqual(expected, actual)

    def test_make_character_XP_value_is_0(self):
        result = make_character()
        actual = result['XP']
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_Level_value_is_1(self):
        result = make_character()
        actual = result['Level']
        expected = 1
        self.assertEqual(expected, actual)

    def test_make_character_Weapon_value_is_Dragon_Blade(self):
        result = make_character()
        actual = result['Weapon']
        expected = 'Dragon Blade'
        self.assertEqual(expected, actual)
