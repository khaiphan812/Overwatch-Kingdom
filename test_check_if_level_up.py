from unittest import TestCase
from characters import check_if_level_up


class Test(TestCase):
    def test_check_if_level_up_not_level_2_yet(self):
        char = {'HP': 5, 'XP': 200, 'Level': 1, 'Weapon': 'Dragon Blade'}
        actual = check_if_level_up(char)
        expected = {'HP': 5, 'XP': 200, 'Level': 1, 'Weapon': 'Dragon Blade'}
        self.assertEqual(expected, actual)

    def test_check_if_level_up_level_2_reached(self):
        char = {'HP': 5, 'XP': 300, 'Level': 1, 'Weapon': 'Dragon Blade'}
        actual = check_if_level_up(char)
        expected = {'HP': 10, 'XP': 300, 'Level': 2, 'Weapon': 'Rocket Hammer'}
        self.assertEqual(expected, actual)

    def test_check_if_level_up_not_level_3_yet(self):
        char = {'HP': 8, 'XP': 500, 'Level': 2, 'Weapon': 'Rocket Hammer'}
        actual = check_if_level_up(char)
        expected = {'HP': 8, 'XP': 500, 'Level': 2, 'Weapon': 'Rocket Hammer'}
        self.assertEqual(expected, actual)

    def test_check_if_level_up_level_3_reached(self):
        char = {'HP': 7, 'XP': 600, 'Level': 2, 'Weapon': 'Rocket Hammer'}
        actual = check_if_level_up(char)
        expected = {'HP': 12, 'XP': 600, 'Level': 3, 'Weapon': 'Biotic Rifle'}
        self.assertEqual(expected, actual)
