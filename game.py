"""
Khai Phan
Overwatch Kingdom
"""
from board import make_board
from board import describe_current_location
from characters import make_character
from characters import make_final_boss
from characters import is_alive
from characters import check_if_level_up
from directions import get_user_direction
from directions import validate_move
from directions import move_character
from challenges import check_for_challenge
from challenges import challenge_picker
from challenges import check_if_final_boss
from challenges import final_boss_battle


def game():
    """
    Drive the game.
    """
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    doom = make_final_boss()
    print("Objective:\n"
          "Navigate through the Overwatch Kingdom, overcome challenges on the way to level up.\n"
          "Upon reaching level 3 and arrive at the bottom right of the map,"
          "you will face Master Doom - the final boss.\n"
          "You must kill him before he kills you. Defeat him to complete the mission.\n"
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
            final_boss = check_if_final_boss(board, character)
            if final_boss:
                final_boss_battle(character, doom)
                if character['HP'] > 0:
                    mission_complete = True
        else:
            print("Sorry you can't go in that direction.")
    if not is_alive(character):
        print("Sorry, you died. Mission Failed.")
    else:
        print("Congratulations! Peace has finally returned to Overwatch Kingdom!")
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
    """
    game()


if __name__ == '__main__':
    main()
