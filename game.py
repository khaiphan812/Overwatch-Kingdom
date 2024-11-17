"""
Khai Phan
Overwatch League
"""

import random


def make_board(rows, columns):
    """
    Create a dictionary containing key-value pairs of coordinate sets-strings.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive non-zero integers
    :postcondition: generate sets of coordinates and strings in a dictionary form
    :return: a dictionary containing key-value pairs of coordinate sets-strings

    >>> make_board(1, 1)    # doctest: +SKIP
    {(0, 0): 'Route 66'}
    >>> make_board(2, 2)    # doctest: +SKIP
    {(0, 0): 'Lijiang Tower', (0, 1): 'Route 66',
     (1, 0): 'Kings Row', (1, 1): 'Hanamura'}
    """
    board = {}
    descriptions = ['Dorado', 'Havana', 'Route 66', 'Circuit Royal', 'Junkertown',
                    'Lunar Colony', 'Gibraltar', 'Suravasa', 'Eichenwalde', 'Numbani',
                    'New Queen Street', 'Hanamura', 'Château Guillard', 'Temple of Anubis', 'Ilios Ruins',
                    'Black Forest', 'Eco-point', 'Necropolis', 'Ayutthaya', 'Oasis University',
                    'Esperança', 'Colosseo', 'Kings Row', 'Rialto', 'Lijiang Tower']
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(descriptions)
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
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Weapon': 'Magic Sword'}


def describe_current_location(board, character):
    """
    Describe the current location of the player.

    :param board: a dictionary containing key-value pairs of coordinate sets-strings
    :param character: a dictionary containing the player's current location and HP
    :precondition: board is the game map
    :precondition: character is a dictionary containing the player's current location and HP
    :postcondition: print the current location of the character

    >>> gameboard = {(0, 0): 'Lijiang Tower', (0, 1): 'Route 66',
    ...              (1, 0): 'Kings Row', (1, 1): 'Hanamura'}
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


def get_user_direction():
    """
    Return the direction the player wishes to go.

    :postcondition: acquire the direction the player wants to go
    :return: the direction the player wishes to go

    """
    directions = {
        "1": "North",
        "2": "South",
        "3": "East",
        "4": "West"
    }
    print("Below are the possible directions:")
    print("1. North\n2. South\n3. East\n4. West")
    while True:
        user_choice = input("Which direction do you want to go? Input number: ")
        if user_choice in directions:
            return directions[user_choice]
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

    >>> validate_move({(0, 0): 'Secret Chamber', (0, 1): 'Dark Tunnel',
    ...                (1, 0): 'Joy Park',       (1, 1): 'Scary Cave'},
    ...                {"X-coordinate": 0, "Y-coordinate": 1}, "North")
    False
    >>> validate_move({(0, 0): 'Secret Chamber', (0, 1): 'Dark Tunnel',
    ...                (1, 0): 'Joy Park',       (1, 1): 'Scary Cave'},
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


def check_if_goal_attained(board, character):
    """
    Check if the character has reached the destination.

    :param board: a dictionary containing the coordinates and location descriptions of the board
    :param character: a dictionary containing the player's current location and HP
    :precondition: board is a dictionary containing key-value pairs of coordinate sets-strings
    :precondition: character is a dictionary containing the player's current location and HP
    :postcondition: check if the character has reached the destination
    :return: True if the character has reached the destination, else False

    >>> gameboard = {
    ...      (0 ,0): 'Scary Cave',
    ...      (0 ,1): 'Dark Tunnel',
    ...      (4 ,4): 'Safe Haven',
    ... }
    >>> char = {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> check_if_goal_attained(gameboard, char)
    False
    >>> char = {"X-coordinate": 4, "Y-coordinate": 4}
    >>> check_if_goal_attained(gameboard, char)
    True
    """
    max_row = max(key[0] for key in board.keys())
    max_col = max(key[1] for key in board.keys())
    if character["X-coordinate"] == max_row and character["Y-coordinate"] == max_col:
        return True
    return False


def check_for_challenge():
    """
    Determine if the player encounters a foe.

    :postcondition: determine if the player will encounter a foe
    :return: True if the player encounters a foe, else False

    """
    return random.randint(1, 4) == 1 or 2 or 3


def challenge_picker():
    """

    :return:
    """
    challenge = random.randint(1, 3)
    if challenge == 1:
        word_scramble()
    elif challenge == 2:
        roll_dice()
    else:
        rock_paper_scissors()


def rock_paper_scissors(character):
    """

    :param character:
    :return:
    """
    options = ['rock', 'paper', 'scissors']
    user_input = input('Pick between "rock", "paper", or "scissors": ')
    user_choice = user_input.lower().strip()
    enemy_choice = random.choice(options)
    print(f'Your enemy chose {enemy_choice}.')

    if user_choice == enemy_choice:
        print(f"It's a tie. You survive another day. You can move on.")
    elif (user_choice == "rock" and enemy_choice == "scissors") or \
         (user_choice == "paper" and enemy_choice == "rock") or \
         (user_choice == "scissors" and enemy_choice == "paper"):
        character['XP'] += 1
        print(f'You won the fight. You gained 100 XP! Your current is {character['XP']}.')
    else:
        character['XP'] -= 1
        print(f'You lost the fight. You also lost 1 HP. Your current HP is {character['HP']}.')


def guessing_game(character):
    """
    Make the player play a guessing game.

    :param character: a dictionary containing the player's current location and HP
    :precondition: character is a dictionary containing the player's current location and HP
    :postcondition: reduce the character's HP by 1 if guessing incorrectly

    """
    secret_number = (random.randint(1, 5))
    guess = int(input("Enemy alert! Guess an integer between 1 and 5 (inclusive): "))
    if guess == secret_number:
        print("You are correct! You may continue your journey.")
    else:
        character["Current HP"] -= 1
        print(f"Wrong! The correct number was {secret_number}. "
              f"You just lost 1 HP. You now have {character["HP"]} HP left.")


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
    print("Objective: Move to the bottom right corner of the board without dying.")
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_direction()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_challenge()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Sorry you can't go in that direction.")
    if not is_alive(character):
        print("Sorry, no HP left, you just died. Very sad :(")
    else:
        print("Congratulations! You have finally reached the Promise Land!")


def main():
    game()


if __name__ == '__main__':
    main()

