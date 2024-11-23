"""
Khai Phan
Overwatch Kingdom
"""
import itertools
import random


def make_board(rows, columns):
    """
    Create a dictionary containing key-value pairs of coordinate sets-strings.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive non-zero integers
    :postcondition: generate coordinates and location in a dictionary form
    :return: a dictionary containing key-value pairs of coordinate sets-strings

    >>> make_board(1, 1)    # doctest: +SKIP
    {(0, 0): 'Route 66'}
    >>> make_board(2, 2)    # doctest: +SKIP
    {(0, 0): 'Lijiang Tower', (0, 1): 'Route 66',
     (1, 0): 'Kings Row', (1, 1): 'Hanamura'}
    """
    board = {}
    locations = ['Dorado', 'Temple of Anubis', 'Circuit Royal', 'Junkertown',
                 'Lunar Colony', 'Eichenwalde', 'Numbani', 'Hanamura',
                 'Château Guillard', 'Havana', 'Ilios Ruins', 'Black Forest',
                 'Necropolis', 'Kings Row', 'Rialto', 'Lijiang Tower']
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(locations)

    print("This is the map of the Overwatch Kingdom:")
    for row in range(rows):
        for column in range(columns):
            print(f"({row}, {column}): {board[(row, column)]:<20}", end=" ")
        print()
    return board


def make_character():
    """
    Create a dictionary containing "X-coordinate": 0, "Y-coordinate": 0, and "Current HP": 5.

    :postcondition: create the X & Y coordinates and Current HP level for the character
    :return: a dictionary containing X & Y-coordinates and Current HP level of the character

    >>> player = make_character()
    >>> player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Weapon': 'Magic Sword'}
    """
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}


def describe_current_location(board, character):
    """
    Describe the current location of the player.

    :param board: a dictionary containing key-value pairs of coordinate sets-strings
    :param character: a dictionary containing the player's current location and HP
    :precondition: board is the game map
    :precondition: character is a dictionary containing the player's current location and HP
    :postcondition: print the current location of the character

    >>> gameboard = {(0, 0): 'Lijiang Tower', (0, 1): 'Circuit Royal',
    ...              (1, 0): 'Kings Row',     (1, 1): 'Hanamura'}
    >>> char = {"X-coordinate": 0, "Y-coordinate": 1}
    >>> describe_current_location(gameboard, char)
    You have arrived at Route 66.
    >>> gameboard = {(0 ,0): 'Necropolis', (0 ,1): 'Black Forest',
    ...              (1 ,0): 'Kings Row', (1 ,1): 'Eichenwalde'}
    >>> char = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> describe_current_location(gameboard, char)
    You have arrived at Kings Row.
    """
    x_coordinate = character["X-coordinate"]
    y_coordinate = character["Y-coordinate"]
    description = board[(x_coordinate, y_coordinate)]
    print(f"You have arrived at {description}.")
    return


def get_user_direction():
    """
    Return the direction the player wishes to go.

    :postcondition: acquire the direction the player wants to go
    :return: the direction the player wishes to go

    """
    directions = {
        "w": "North",
        "s": "South",
        "d": "East",
        "a": "West"
    }
    print("Below are the possible directions:")
    print("W - North\nS - South\nD - East\nA - West")
    while True:
        user_input = input("Which direction do you want to go? ")
        user_choice = user_input.lower()
        if user_choice in directions:
            return directions[user_choice]
        else:
            print("Invalid input. Please enter a valid direction.")


def validate_move(board, character, direction):
    """
    Determine if the player can make the desired move.

    :param board: a dictionary containing key-value pairs of coordinate sets-strings
    :param character: a dictionary containing the player's current location and HP
    :param direction: the direction the player wishes to go
    :precondition: character is a dictionary containing the player's current location and HP
    :precondition: check if the player can make the desired move
    :return: True if the player can make the move, else False

    >>> validate_move({(0, 0): 'Kings Row',     (0, 1): 'Lijiang Tower',
    ...                (1, 0): 'Eichenwalde',   (1, 1): 'Hanamura'},
    ...                {"X-coordinate": 0, "Y-coordinate": 1}, "North")
    False
    >>> validate_move({(0, 0): 'Hanamura',      (0, 1): 'Eichenwalde',
    ...                (1, 0): 'Circuit Royal', (1, 1): 'Kings Row'},
    ...                {"X-coordinate": 1, "Y-coordinate": 0}, "East")
    True
    """
    x_coordinate = character["X-coordinate"]
    y_coordinate = character["Y-coordinate"]

    if direction == "North" and x_coordinate > min(key[0] for key in board.keys()):
        return True
    elif direction == "South" and x_coordinate < max(key[0] for key in board.keys()):
        return True
    elif direction == "East" and y_coordinate < max(key[1] for key in board.keys()):
        return True
    elif direction == "West" and y_coordinate > min(key[1] for key in board.keys()):
        return True
    else:
        return False


def move_character(character, direction):
    """
    Update the character's new X- and Y-coordinates after the move.

    :param character: a dictionary containing the player's current location and HP
    :param direction: the direction the player wishes to go
    :precondition: direction must be a string that is either "North" or "South" or "East" or "West"
    :postcondition: character moves to a new location within board bounds
    :postcondition: update character's new X- and Y-coordinates

    >>> move_character({'X-coordinate': 0, 'Y-coordinate': 1}, 'South')
    {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> move_character({'X-coordinate': 1, 'Y-coordinate': 1}, 'East')
    {'X-coordinate': 1, 'Y-coordinate': 2}
    """
    if direction == "North":
        character["X-coordinate"] -= 1
    elif direction == "South":
        character["X-coordinate"] += 1
    elif direction == "East":
        character["Y-coordinate"] += 1
    elif direction == "West":
        character["Y-coordinate"] -= 1
    return character


def check_for_challenge():
    """
    Determine if the player encounters a foe.

    :postcondition: determine if the player will encounter a foe
    :return: True if the player encounters a foe, else False

    """
    return random.randint(1, 2) == 1


def challenge_picker(character):
    """

    :return:
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

    :return:
    """
    print("Welcome to Word Puzzle challenge. You must unscramble the given word to overcome this challenge.\n"
          "Hint: the word is VERY python-related!")
    words_list = ["python", "function", "aliases", "immutable", "itertools", "dictionary", "tuple", "variable"]
    chosen_word = random.choice(words_list)
    scrambled_list = random.sample(chosen_word, len(chosen_word))
    scrambled_word = "".join(scrambled_list)
    print("Unscramble the word:", scrambled_word)
    guess = input("Your guess: ")
    if guess == chosen_word:
        print(f"Correct! You gained 100 XP. Your current XP is {character['XP']}.")
        character['XP'] += 100
    else:
        print(f"Wrong! The correct word was: {chosen_word}\n"
              f"You just lost 1 HP. Your current HP is {character['HP']}.")
        character["HP"] -= 1
    return character


def hostage_rescue(character):
    """

    :param character:
    :return:
    """
    print("Doomfist's minions are holding a number of citizens as hostage.\n"
          "Guess the correct number of victims they're holding hostage to rescue them, otherwise you'll lose 1 HP.")
    user_guess = int(input('Guess the number of hostage between 1 and 5: '))
    hostage_roll = random.randint(1, 5)
    if user_guess == hostage_roll:
        print(f'Correct! You just rescued the victims and gained 100 XP! Your current XP is {character['XP']}.')
        character['XP'] += 100
    else:
        print(f'Wrong! The correct number is {hostage_roll}. You just lost 1 HP. Your current HP is {character['HP']}.')
        character['HP'] -= 1
    return character


def skill_cast(character):
    """

    :param character:
    :return:
    """
    print("Welcome to Skill Cast Battle!\n"
          "Your enemy and you will each cast a skill.\n"
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
          "If you win, you'll gain 100 XP. If you lose, you'll lose 1 HP. If you tie, no gain or loss.")
    options = ['fortify', 'burrow', 'soundwave', 'virus']
    user_choice = ""
    while user_choice not in options:
        user_input = input("It's time to cast your skill (lowercase acceptable): ")
        user_choice = user_input.lower().strip()
        if user_choice not in options:
            print("Invalid input. Recast a valid skill.")

    enemy_choice = random.choice(options)
    print(f'Your enemy casted {enemy_choice.title()}.')
    if user_choice == enemy_choice:
        print(f"It's a tie. You survive another day. You can move on.")
    elif (user_choice == "fortify" and enemy_choice == "burrow") or \
         (user_choice == "burrow" and enemy_choice == "soundwave") or \
         (user_choice == "soundwave" and enemy_choice == "virus") or \
         (user_choice == "virus" and enemy_choice == "fortify") or \
         (user_choice == "soundwave" and enemy_choice == "fortify") or \
         (user_choice == "virus" and enemy_choice == "burrow"):
        print(f'You won the fight. You gained 100 XP! Your current is {character['XP']}.')
        character['XP'] += 100
    else:
        print(f'You lost the fight. You also lost 1 HP. Your current HP is {character['HP']}.')
        character['HP'] -= 1
    return character


def check_if_level_up(character):
    """

    :param character:
    :return:
    """
    if character['XP'] >= 300 and character['Level'] == 1:
        character['Level'] = 2
        character['HP'] += 5
        character['Weapon'] = 'Rocket Hammer'
        print(f"You just reached level 2. Your HP increases by 5. Your current HP is {character['HP']}.\n"
              f"Your weapon has been upgraded to a {character['Weapon']}.")

    if character['XP'] == 600 and character['Level'] == 2:
        character['Level'] = 3
        character['HP'] += 5
        character['Weapon'] = 'Biotic Rifle'
        print(f"You just reached level 3. Your HP increases by 5. Your current HP is {character['HP']}.\n"
              f"Your weapon has been upgraded to a {character['Weapon']}.")
    return character


def check_if_final_boss(character):
    """

    :param character:
    :return:
    """
    return character['Level'] == 3


def final_boss_battle(character):
    """

    :param character:
    :return:
    """
    print("You are now ready to face the Final Boss - Doomfist! You must defeat him to finish the game. Good luck!")
    print("game rule-placeholder")
    riddle_dict = {'Q1': '1', 'Q2': '2', 'Q3': '3', 'Q4': '4', 'Q5': '5', 'Q6': '6', 'Q7': '7', 'Q8': '8'}
    cycle = itertools.cycle(riddle_dict.items())
    while character['HP'] > 0:
        riddle, answer = next(cycle)
        print(riddle)
        user_answer = input('Give your answer: ').lower().strip()
        if user_answer != answer:
            character['HP'] = max(0, character['HP'] - 2)
            print(f'You got it wrong. You lost 2 HP. Your have {character['HP']} left.')
        else:
            print('You have defeated Doomfist!')
            return
    print('Doomfist has defeated you!')
    return character


def is_alive(character):
    """
    Check if the character is still alive.

    :param character: a dictionary containing the player's current location and HP
    :precondition: character is a dictionary containing the player's current location and HP
    :postcondition: check if the Current HP reaches zero
    :return: True if character is still alive, else False

    >>> is_alive({"HP": 0})
    False
    >>> is_alive({"HP": 1})
    True
    """
    return character["HP"] > 0


def game():
    """
    Drive the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    print("Objective:\n"
          "Navigate through the Overwatch Land, find the final boss and defeat him to bring back peace for the land.\n"
          "Overcome challenges on the way to level up.\n"
          "Once reaching level 3, you will be ready to face Doomfist - the final boss.\n"
          "Defeat him to complete the mission. Don't let your HP drain out!\n"
          f"You are currently at Level {character['Level']}.\n"
          f"Every time you level up, your HP and weapon will be upgraded.\n"
          f"Your current HP is {character['HP']} and you're holding a {character['Weapon']} as your weapon.\n"
          f"Every time you overcome a challenge, you'll gain 100 XP.\n"
          f"You need 300 XP to level up.\n"
          f"Let's begin your mission. The citizens are relying on you!")
    mission_complete = False
    while is_alive(character) and not mission_complete:
        describe_current_location(board, character)
        direction = get_user_direction()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_challenge()
            if there_is_a_challenger:
                challenge_picker(character)
            check_if_level_up(character)
            final_boss = check_if_final_boss(character)
            if final_boss:
                final_boss_battle(character)
                if character['HP'] > 0:
                    mission_complete = True
        else:
            print("Sorry you can't go in that direction.")
    if not is_alive(character):
        print("Sorry, you have 0 HP left and died. Mission Failed.")
    else:
        print("Congratulations! Peace has finally returned on Overwatch Kingdom!")
        print("""
            ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗                    
            ████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║                    
            ██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║                    
            ██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║                    
            ██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║                    
            ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝                    
                                                                                    
             ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗██╗
            ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝██║
            ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  ██║
            ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  ╚═╝
            ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗██╗
             ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝                                                                                                                                                  
                """)


def main():
    """
    Drive the program.
    :return:
    """
    game()


if __name__ == '__main__':
    main()
