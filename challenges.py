import random
import itertools
import time


def check_for_challenge():
    """
    Determine if the player encounters a challenge.

    :postcondition: determine if the player encounters a challenge
    :return: True if the randomized result is equal to 1, else False

    """
    return random.randint(1, 2) == 1


def challenge_picker(character):
    """
    Determine the challenge the player is going to face.

    :param character: a dictionary containing the player's stats
    :precondition: character is a dictionary
    :postcondition: call the function based on the randomized result
    :return: character's stats

    """
    challenge = random.randint(1, 4)
    if challenge == 1:
        skill_cast(character)
    elif challenge == 2:
        hostage_rescue(character)
    else:
        word_puzzle(character)
    return character


def word_puzzle(character):
    """
    Ask the player to re-arrange a scrambled word back to the correct order.

    :param character: a dictionary containing the character's stats
    :precondition: character is a dictionary
    :postcondition: update the character's stats based on challenge's result
    :return: the character's updated XP and/or HP stats

    """
    time.sleep(1)
    print("This location is passcode-protected by Master Doom's guards.")
    time.sleep(1)
    print("You received a passcode from a spy but the letters are scrambled.")
    time.sleep(1)
    print("You must give the correct passcode to hide your identity and safely get through the gate.")
    time.sleep(1)
    print("Hint: the passcode is VERY python-related!")
    time.sleep(1)
    words_list = ['pythonic', 'function', 'aliases',
                  'immutable', 'itertools', 'iteration',
                  'dictionary', 'tuple', 'variable',
                  'decorator', 'package', 'exception',
                  'module', 'argument', 'parameter',
                  'recursion', 'closure', 'readability',
                  'reusability', 'compiler', 'debugger',
                  'decomposition', 'abstraction', 'algorithm',]
    chosen_word = random.choice(words_list)
    scrambled_list = random.sample(chosen_word, len(chosen_word))
    scrambled_word = "".join(scrambled_list)
    print("Here is scrambled passcode:", scrambled_word)
    time.sleep(1)
    guess = input("Enter the correct passcode: ")
    time.sleep(1)
    if guess == chosen_word:
        character['XP'] = min(600, character['XP'] + 100)
        print(f"Correct! You gained 100 XP. Your current XP is {character['XP']}.")
    else:
        character["HP"] -= 1
        print(f"Wrong! The passcode was: {chosen_word}.")
        time.sleep(1)
        print(f"Your undercover is exposed and the guards attack you.")
        time.sleep(1)
        print(f"You lost 1 HP. Your current HP is {character['HP']}.")
    return character


def hostage_rescue(character):
    """
    Ask the player to guess the correct number of victims held hostage by the enemy.

    :param character: a dictionary containing the character's stats
    :precondition: character is a dictionary
    :postcondition: update the character's stats based on challenge's result
    :return: the character's updated XP and/or HP stats

    """
    time.sleep(1)
    print("Master Doom's guards are holding a number of innocent people hostage.")
    time.sleep(1)
    print("Guess the correct number of victims held hostage to rescue them, otherwise you'll lose 1 HP.")
    time.sleep(1)
    print("Luck is an underrated factor for success. You'll need it to overcome this challenge. Good luck!")
    time.sleep(1)
    hostage_roll = random.randint(1, 5)
    options = ['1', '2', '3', '4', '5']
    user_guess = ""
    while user_guess not in options:
        try:
            user_guess = input("Guess the number of hostage between 1 and 5: ")
        except ValueError:
            print("You must enter a positive integer!")
        if user_guess not in options:
            print("Invalid input. Please enter an integer between 1 and 5.")
    time.sleep(1)
    if int(user_guess) == hostage_roll:
        character['XP'] = min(600, character['XP'] + 100)
        print(f"Correct! You successfully rescued the victims and gained 100 XP! "
              f"Your current XP is {character['XP']}.")
    else:
        character['HP'] -= 1
        print(f"Wrong! The correct number of hostage is {hostage_roll}. "
              f"You just lost 1 HP. Your current HP is {character['HP']}.")
    return character


def skill_cast(character):
    """
    Ask the player to select a skill to fight against the enemy.

    :param character: a dictionary containing the character's stats
    :precondition: character is a dictionary
    :postcondition: update the character's stats based on challenge's result
    :return: the character's updated XP and/or HP stats

    """
    time.sleep(1)
    print("Here comes a skill battle against Sigma - Master Doom's sidekick.\n"
          "You and Sigma will each cast a skill.\n"
          "Whoever casts a more powerful skill wins the battle.")
    time.sleep(1)
    print("Here are the skills you can cast:\n"
          "Fortify: Gain temporary health, reducing all damage taken.\n"
          "Burrow: Move underground and then emerge to deal damage.\n"
          "Soundwave: Create a blast wave to knock enemies away from you.\n"
          "Virus: Infect enemies with a projectile that deals damage over time.")
    time.sleep(1)
    print("And here are the rules:\n"
          "Fortify beats Burrow.\n"
          "Burrow beats Soundwave.\n"
          "Soundwave beats Virus.\n"
          "Virus beats Fortify.\n"
          "Soundwave beats Fortify.\n"
          "Virus beats Burrow.")
    time.sleep(1)
    print("If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. If it's a tie, no gain or loss.")
    time.sleep(1)
    options = ['fortify', 'burrow', 'soundwave', 'virus']
    user_choice = ""
    while user_choice not in options:
        user_input = input("Pick a skill and cast it: ")
        user_choice = user_input.lower().strip()
        if user_choice not in options:
            print("Invalid input. Recast a valid skill.")
    time.sleep(1)
    enemy_choice = random.choice(options)
    print(f"Your enemy casted {enemy_choice.title()}.")
    time.sleep(1)
    if user_choice == enemy_choice:
        print(f"It's a tie. You survive another day. You can move on.")
    elif (user_choice == 'fortify' and enemy_choice == 'burrow') or \
         (user_choice == 'burrow' and enemy_choice == 'soundwave') or \
         (user_choice == 'soundwave' and enemy_choice == 'virus') or \
         (user_choice == 'virus' and enemy_choice == 'fortify') or \
         (user_choice == 'soundwave' and enemy_choice == 'fortify') or \
         (user_choice == 'virus' and enemy_choice == 'burrow'):
        character['XP'] = min(600, character['XP'] + 100)
        print(f"You won the fight. You gained 100 XP! Your current XP is {character['XP']}.")
    else:
        character['HP'] -= 1
        print(f"You lost the fight. You also lost 1 HP. Your current HP is {character['HP']}.")
    return character


def check_if_final_boss(board, character):
    """
    Check if the character is ready to face the final boss.

    :param board: a dictionary containing tuple-string pairs describing coordinates and locations
    :param character: a dictionary containing the character's stats
    :precondition: board is a dictionary
    :precondition: character is a dictionary
    :postcondition: check if the character is ready to face the final boss
    :return: True if the character's level is 3 and the character is at the bottom right location, else False

    >>> gameboard = {
    ...      (0, 0): 'Havana',
    ...      (0, 1): 'Rialto',
    ...      (4, 4): 'Dorado',
    ... }
    >>> char = {'X-coordinate': 0, 'Y-coordinate': 1, 'Level': 3}
    >>> check_if_final_boss(gameboard, char)
    False
    >>> gameboard = {
    ...      (0, 0): 'Havana',
    ...      (0, 1): 'Rialto',
    ...      (4, 4): 'Dorado',
    ... }
    >>> char = {'X-coordinate': 4, 'Y-coordinate': 4, 'Level': 2}
    >>> check_if_final_boss(gameboard, char)
    False
    >>> gameboard = {
    ...      (0, 0): 'Havana',
    ...      (0, 1): 'Rialto',
    ...      (4, 4): 'Dorado',
    ... }
    >>> char = {'X-coordinate': 4, 'Y-coordinate': 4, 'Level': 3}
    >>> check_if_final_boss(gameboard, char)
    True
    """
    max_row = max(key[0] for key in board.keys())
    max_col = max(key[1] for key in board.keys())
    if (character['X-coordinate'] == max_row and
            character['Y-coordinate'] == max_col and
            character['Level'] == 3):
        return True
    else:
        return False


def final_boss_battle(character, doom):
    """
    Ask the player to answer a sequence of riddles from the final boss.

    :param character: a dictionary containing the character's stats
    :param doom: a dictionary containing Master Doom's stats
    :precondition: character is a dictionary
    :precondition: doom is a dictionary
    :postcondition: update the character's stats based on challenge's result
    :return: the character's updated stats

    """
    time.sleep(1)
    print("You are now ready to face the final boss - Master Doom!\n"
          "You must defeat him to complete your journey.")
    time.sleep(1)
    print("Master Doom is a riddle master. He fights using a series of conundrums.\n"
          "Everytime you get a question right, you'll strip 2 HP off him.\n"
          "If you get it wrong, he'll strike you and take away 2 HP.\n"
          "Only one-word answers, no articles (a/an/the) required.\n"
          "To kill or to be killed. Let's begin!")
    time.sleep(1)
    riddles = {'Riddle: I speak without a mouth and hear without ears. '
               'I have no body, but I come alive with the wind. What am I? (4 letters)': 'echo',
               'Riddle: I am not alive, but I can grow; I don’t have lungs, but I need air; '
               'I don’t have a mouth, and yet I drown. What am I? (4 letters)': 'fire',
               'Riddle: The more you take, the more you leave behind. What am I? (9 letters)': 'footsteps',
               'Riddle: What is so fragile that saying its name breaks it? (7 letters)': 'silence',
               'Riddle: What has a heart that doesn’t beat, a mouth that doesn’t speak, '
               'and a head that doesn’t think? (9 letters)': 'artichoke',
               'Riddle: I’m always in front of you but can never be seen. What am I? (6 letters)': 'future',
               'Riddle: The more you take out of me, the bigger I get. What am I? (4 letters)': 'hole',
               'Riddle: I have many teeth but cannot bite. What am I? (4 letters)': 'comb',
               'Riddle: What has no beginning, end, or middle? (6 letters)': 'circle',
               'Riddle: I can be cracked, made, told, and played. What am I? (4 letters)': 'joke',
               'Riddle: What is harder to catch the faster you run? (6 letters)': 'breath',
               'Riddle: The maker doesn’t want it. The buyer doesn’t use it. '
               'The user doesn’t know it. What am I? (6 letters)': 'coffin',
               'Riddle: The more you have of me, the less you see. What am I? (8 letters)': 'darkness'
               }
    cycle = itertools.cycle(riddles.items())
    while character['HP'] > 0 and doom['HP'] > 0:
        riddle, answer = next(cycle)
        print(riddle)
        time.sleep(1)
        user_answer = input("Your answer: ").lower().strip()
        time.sleep(1)
        if user_answer != answer:
            character['HP'] = max(0, character['HP'] - 2)
            print(f"Wrong answer! Master Doom just struck you with his {doom['Weapon']}.")
            time.sleep(1)
            print(f"You lost 2 HP. You have {character['HP']} HP left.")
        else:
            doom['HP'] = max(0, doom['HP'] - 2)
            print(f"Correct! You just shot Master Doom with your {character['Weapon']}.")
            time.sleep(1)
            print(f"He lost 2 HP and has {doom['HP']} HP left.")
        time.sleep(1)
    if character['HP'] == 0:
        print("You have fallen before Master Doom.")
    elif doom['HP'] == 0:
        print("You have defeated Master Doom!")
    time.sleep(1)
    return character
