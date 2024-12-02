"""
Khai Phan
Overwatch Kingdom
"""
import time
from colorama import Fore, init
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
    init()
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    doom = make_final_boss()
    time.sleep(1)
    print(Fore.YELLOW + "Story:\n" +
          Fore.RESET + "Overwatch Kingdom was once a peaceful land with bliss and joy.\n"
          "Then Master Doom came and disrupted the harmony of the kingdom.\n"
          "You are Reinhardt Wilhelm, a watchful guardian who vowed to protect the kingdom at all costs.")
    time.sleep(1)
    print(Fore.YELLOW + "Mission:\n" +
          Fore.RESET + "Navigate through the map and overcome challenges on the way.\n"
          "Every time you win a challenge, you'll gain 100 XP for levelling up.\n"
          "The milestones to level up are 300 XP for level 2 and 600 XP (max) for level 3.\n"
          "You are now at Level 1 with 0 XP, 5 HP, and holding a Dragon Blade as your weapon.\n"
          "Each time you level up, your HP limit and weapon will be upgraded.\n"
          "When reaching level 3 AND arrive at the bottom right location, "
          "you will face Master Doom - the final boss.\n"
          "You must kill him before he drains all your HP. Defeat him to complete the mission.\n"
          "Let your journey begin. Overwatch citizens are relying on you. Good luck!")
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
            print(Fore.RED + "Sorry you can't go in that direction.")
    if not is_alive(character):
        print(Fore.RED + "Sorry, you died. You will need another effort to save the Overwatch Kingdom.")
        time.sleep(1)
        print(Fore.RED + """
            ██╗    ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
            ████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
            ██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║
            ██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║
            ██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║
            ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ ██╗      
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗██║      
            █████╗  ███████║██║██║     █████╗  ██║  ██║██║      
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║╚═╝      
            ██║     ██║  ██║██║███████╗███████╗██████╔╝██╗      
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝ 
              """)
    else:
        print(Fore.YELLOW + "Congratulations! Peace has finally returned to Overwatch Kingdom!")
        time.sleep(1)
        print(Fore.YELLOW + """
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
