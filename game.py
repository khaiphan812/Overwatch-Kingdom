"""
Khai Phan
Overwatch Kingdom
"""
import time
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
    time.sleep(1)
    print("Story:\n"
          "Overwatch Kingdom was once a peaceful land with bliss and joy.\n"
          "Then Master Doom came and disrupted the harmony of the kingdom.\n"
          "You are Reinhardt Wilhelm, a watchful guardian who vowed to protect the kingdom at all costs.")
    time.sleep(1)
    print("Mission:\n"
          "Navigate through the map and overcome challenges on the way.\n"
          "Every time you win a challenge, you'll gain 100 XP for levelling up.\n"
          "You need to obtain 300 and 600 XP to reach level 2 and 3 respectively.\n"
          "You are now at Level 1 with 0 XP, 5 HP, and holding a Dragon Blade as your weapon.\n"
          "Each time you level up, your HP limit and weapon will be upgraded.\n"
          "When reaching level 3 AND arrive at the bottom right location,"
          "you will face Master Doom,the final boss, in a super challenging battle.\n"
          "You must kill him before he kills you. Defeat him to complete the mission.\n"
          "Let your journey begin. The citizens are relying on you. Good luck!")
    time.sleep(1)
    mission_complete = False
    while is_alive(character) and not mission_complete:
        describe_current_location(board, character)
        time.sleep(1)
        direction = get_user_direction()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            time.sleep(1)
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
        time.sleep(1)
    if not is_alive(character):
        print("Sorry, you died. Mission Failed.")
    else:
        print("Congratulations! Peace has finally returned to Overwatch Kingdom!")
        time.sleep(1)
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
