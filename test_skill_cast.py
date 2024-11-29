from unittest import TestCase
from unittest.mock import patch
import io
from challenges import skill_cast


class Test(TestCase):
    @patch('random.choice', side_effect=['soundwave'])
    @patch('builtins.input', side_effect=['burrow'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skill_cast_win(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        skill_cast(char)
        actual = mock_output.getvalue()
        expected = ("You have a skill battle against Sigma - Master Doom's sidekick.\n"
                    "You and Sigma will each cast a skill.\n"
                    "Whoever casts a more powerful skill wins the battle.\n"
                    "Here are the skills you can cast:\n"
                    "Fortify: Gain temporary health, reducing all damage taken.\n"
                    "Burrow: Move underground and then emerge to deal damage.\n"
                    "Soundwave: Create a blast wave to knock enemies away from you.\n"
                    "Virus: Infect enemies with a projectile that deals damage over time.\n"
                    "Here are the rules:\n"
                    "Fortify beats Burrow.\n"
                    "Burrow beats Soundwave.\n"
                    "Soundwave beats Virus.\n"
                    "Virus beats Fortify.\n"
                    "Soundwave beats Fortify.\n"
                    "Virus beats Burrow.\n"
                    "If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. "
                    "If you tie, no gain or loss.\n"
                    "Your enemy casted Soundwave.\n"
                    "You won the fight. You gained 100 XP (max 600 XP)! Your current XP is 200.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['soundwave'])
    @patch('builtins.input', side_effect=['soundwave'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skill_cast_tie(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        skill_cast(char)
        actual = mock_output.getvalue()
        expected = ("You have a skill battle against Sigma - Master Doom's sidekick.\n"
                    "You and Sigma will each cast a skill.\n"
                    "Whoever casts a more powerful skill wins the battle.\n"
                    "Here are the skills you can cast:\n"
                    "Fortify: Gain temporary health, reducing all damage taken.\n"
                    "Burrow: Move underground and then emerge to deal damage.\n"
                    "Soundwave: Create a blast wave to knock enemies away from you.\n"
                    "Virus: Infect enemies with a projectile that deals damage over time.\n"
                    "Here are the rules:\n"
                    "Fortify beats Burrow.\n"
                    "Burrow beats Soundwave.\n"
                    "Soundwave beats Virus.\n"
                    "Virus beats Fortify.\n"
                    "Soundwave beats Fortify.\n"
                    "Virus beats Burrow.\n"
                    "If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. "
                    "If you tie, no gain or loss.\n"
                    "Your enemy casted Soundwave.\n"
                    "It's a tie. You survive another day. You can move on.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['soundwave'])
    @patch('builtins.input', side_effect=['fortify'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skill_cast_loss(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        skill_cast(char)
        actual = mock_output.getvalue()
        expected = ("You have a skill battle against Sigma - Master Doom's sidekick.\n"
                    "You and Sigma will each cast a skill.\n"
                    "Whoever casts a more powerful skill wins the battle.\n"
                    "Here are the skills you can cast:\n"
                    "Fortify: Gain temporary health, reducing all damage taken.\n"
                    "Burrow: Move underground and then emerge to deal damage.\n"
                    "Soundwave: Create a blast wave to knock enemies away from you.\n"
                    "Virus: Infect enemies with a projectile that deals damage over time.\n"
                    "Here are the rules:\n"
                    "Fortify beats Burrow.\n"
                    "Burrow beats Soundwave.\n"
                    "Soundwave beats Virus.\n"
                    "Virus beats Fortify.\n"
                    "Soundwave beats Fortify.\n"
                    "Virus beats Burrow.\n"
                    "If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. "
                    "If you tie, no gain or loss.\n"
                    "Your enemy casted Soundwave.\n"
                    "You lost the fight. You also lost 1 HP. Your current HP is 4.\n")
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['soundwave'])
    @patch('builtins.input', side_effect=['abc', 'burrow'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skill_cast_invalid_input_at_first(self, mock_output, _, __):
        char = {'HP': 5, 'XP': 100}
        skill_cast(char)
        actual = mock_output.getvalue()
        expected = ("You have a skill battle against Sigma - Master Doom's sidekick.\n"
                    "You and Sigma will each cast a skill.\n"
                    "Whoever casts a more powerful skill wins the battle.\n"
                    "Here are the skills you can cast:\n"
                    "Fortify: Gain temporary health, reducing all damage taken.\n"
                    "Burrow: Move underground and then emerge to deal damage.\n"
                    "Soundwave: Create a blast wave to knock enemies away from you.\n"
                    "Virus: Infect enemies with a projectile that deals damage over time.\n"
                    "Here are the rules:\n"
                    "Fortify beats Burrow.\n"
                    "Burrow beats Soundwave.\n"
                    "Soundwave beats Virus.\n"
                    "Virus beats Fortify.\n"
                    "Soundwave beats Fortify.\n"
                    "Virus beats Burrow.\n"
                    "If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. "
                    "If you tie, no gain or loss.\n"
                    "Invalid input. Recast a valid skill.\n"
                    "Your enemy casted Soundwave.\n"
                    "You won the fight. You gained 100 XP (max 600 XP)! Your current XP is 200.\n")
        self.assertEqual(expected, actual)
