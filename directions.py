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
