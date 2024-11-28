def make_character():
    """
    Create a dictionary containing "X-coordinate": 0, "Y-coordinate": 0, and "Current HP": 5.

    :postcondition: create the X & Y coordinates, HP, XP, and Weapon of the character
    :return: a dictionary containing X & Y coordinates, HP, XP, and Weapon of the character

    >>> player = make_character()
    >>> player
    {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Weapon': 'Magic Sword'}
    """
    return {'X-coordinate': 0, 'Y-coordinate': 0, 'HP': 5, 'XP': 0, 'Level': 1, 'Weapon': 'Dragon Blade'}


def make_final_boss():
    """
    Create a dictionary containing the boss' HP level and weapon name.

    :postcondition: create the HP level and weapon name for the final boss
    :return: a dictionary containing HP level and weapon name for the final boss

    >>> doom = make_final_boss()
    >>> doom
    {'HP': 10, 'Weapon': 'Destructive Flail'}
    """
    return {'HP': 10, 'Weapon': 'Destructive Flail'}


def is_alive(character):
    """
    Check if the character is still alive.

    :param character: a dictionary containing the character's stats
    :precondition: character is a dictionary
    :postcondition: check if the character's HP reaches zero
    :return: True if character's HP is greater than zero, else False

    >>> is_alive({'HP': 0})
    False
    >>> is_alive({'HP': 1})
    True
    """
    return character['HP'] > 0


def check_if_level_up(character):
    """
    Check if the character reaches the next level.

    :param character: a dictionary containing the character's stats
    :precondition: character is a dictionary
    :postcondition: check if the character reaches the next level
    :return: the character's updated Level, HP, Weapon stats

    >>> char = check_if_level_up({'HP': 5, 'XP': 400, 'Level': 1, 'Weapon': 'Dragon Blade'})
    You just reached level 2. Your HP increases by 5. Your current HP is 10.
    Your weapon has been upgraded to a Rocket Hammer.
    >>> char = check_if_level_up({'HP': 7, 'XP': 600, 'Level': 2, 'Weapon': 'Rocket Hammer'})
    You just reached level 3. Your HP increases by 5. Your current HP is 12.
    Your weapon has been upgraded to a Biotic Rifle.
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
