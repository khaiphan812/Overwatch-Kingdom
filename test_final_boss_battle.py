from unittest import TestCase
from unittest.mock import patch
import io
from challenges import final_boss_battle


class Test(TestCase):
    @patch('builtins.input', side_effect=['echo', 'fire', 'footsteps', 'silence', 'artichoke'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_battle_correct_answer_print_output(self, mock_output, _):
        char = {'HP': 12, 'XP': 600, 'Level': 3, 'Weapon': 'Biotic Rifle'}
        boss = {'HP': 10, 'Weapon': 'Destructive Flail'}
        riddles = {'Riddle: I speak without a mouth and hear without ears. '
                   'I have no body, but I come alive with the wind. What am I? (4 letters)': 'echo',
                   'Riddle: I am not alive, but I can grow; I don’t have lungs, but I need air; '
                   'I don’t have a mouth, and yet I drown. What am I? (4 letters)': 'fire',
                   'Riddle: The more you take, the more you leave behind. What am I? (9 letters)': 'footsteps',
                   'Riddle: What is so fragile that saying its name breaks it? (7 letters)': 'silence',
                   'Riddle: What has a heart that doesn’t beat, a mouth that doesn’t speak, '
                   'and a head that doesn’t think? (9 letters)': 'artichoke'}

        with patch('itertools.cycle', return_value=iter(riddles.items())):
            final_boss_battle(char, boss)
        actual = mock_output.getvalue()
        expected = "Correct! You just shot Master Doom with your Biotic Rifle.\nHe lost 2 HP and has 8 HP left.\n"
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['cloud', 'fire', 'footsteps', 'silence', 'artichoke'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_battle_wrong_answer_print_output(self, mock_output, _):
        char = {'HP': 11, 'XP': 600, 'Level': 3, 'Weapon': 'Biotic Rifle'}
        boss = {'HP': 8, 'Weapon': 'Destructive Flail'}
        riddles = {'Riddle: I speak without a mouth and hear without ears. '
                   'I have no body, but I come alive with the wind. What am I? (4 letters)': 'echo',
                   'Riddle: I am not alive, but I can grow; I don’t have lungs, but I need air; '
                   'I don’t have a mouth, and yet I drown. What am I? (4 letters)': 'fire',
                   'Riddle: The more you take, the more you leave behind. What am I? (9 letters)': 'footsteps',
                   'Riddle: What is so fragile that saying its name breaks it? (7 letters)': 'silence',
                   'Riddle: What has a heart that doesn’t beat, a mouth that doesn’t speak, '
                   'and a head that doesn’t think? (9 letters)': 'artichoke'}

        with patch('itertools.cycle', return_value=iter(riddles.items())):
            final_boss_battle(char, boss)
        actual = mock_output.getvalue()
        expected = ("Wrong answer! Master Doom just struck you with his Destructive Flail.\n"
                    "You lost 2 HP. You have 9 HP left.\n")
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=['echo', 'fire', 'footsteps', 'silence', 'artichoke'])
    def test_final_boss_battle_character_defeats_boss(self, _):
        char = {'HP': 9, 'XP': 600, 'Level': 3, 'Weapon': 'Biotic Rifle'}
        boss = {'HP': 10, 'Weapon': 'Destructive Flail'}
        final_boss_battle(char, boss)
        actual = boss['HP']
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['easd', 'akde', 'fgss', 'sdgfe'])
    def test_final_boss_battle_character_dies(self, _):
        char = {'HP': 8, 'XP': 600, 'Level': 3, 'Weapon': 'Biotic Rifle'}
        boss = {'HP': 10, 'Weapon': 'Destructive Flail'}
        final_boss_battle(char, boss)
        actual = char['HP']
        expected = 0
        self.assertEqual(expected, actual)
