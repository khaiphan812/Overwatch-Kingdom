import random


def make_board(rows, columns):
    """
    Create a dictionary containing tuple-string pairs describing coordinates and locations.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows and columns must be positive non-zero integers
    :postcondition: generate coordinates and location in a dictionary form
    :return: a dictionary containing tuple-string pairs describing coordinates and locations

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


def describe_current_location(board, character):
    """
    Describe the current location of the player.

    :param board: a dictionary containing tuple-string pairs describing coordinates and locations
    :param character: a dictionary containing the player's stats
    :precondition: board is a dictionary
    :precondition: character is a dictionary
    :postcondition: print the current location of the character

    >>> gameboard = {(0, 0): 'Lijiang Tower', (0, 1): 'Circuit Royal',
    ...              (1, 0): 'Kings Row',     (1, 1): 'Hanamura'}
    >>> char = {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> describe_current_location(gameboard, char)
    You have arrived at Circuit Royal.
    >>> gameboard = {(0 ,0): 'Necropolis', (0 ,1): 'Black Forest',
    ...              (1 ,0): 'Kings Row', (1 ,1): 'Eichenwalde'}
    >>> char = {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> describe_current_location(gameboard, char)
    You have arrived at Kings Row.

    """
    x_coordinate = character["X-coordinate"]
    y_coordinate = character["Y-coordinate"]
    description = board[(x_coordinate, y_coordinate)]
    print(f"You have arrived at {description}.")
    return
