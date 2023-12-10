"""
Anthony Shin (A01299201)
Momona Wada (A01348325)

This is our game! I hope you enjoy this. Thank you for the entire term. We could have learned a lot.
We can't wait for learning OOP with you!😉
"""
from character import create_character
from foes import create_foe, select_foe, fight_with_foe, check_for_foe
from board import create_map
from user_input import get_user_input_for_character, get_general_user_input
from quizzes import select_quiz, create_quizzes, solve_quiz, check_for_quiz
from character_modifiers import increase_level, increase_attack, increase_xp, increase_hp
from game_printer import (print_map, print_initial_story, describe_current_location,
                          print_status, print_start_message, print_colored_text, print_ending_message)
from status_validation import (is_enough_level_to_proceed_to_next_map, is_achieved_goal,
                               is_in_the_goal_destination_of_each_map)
from movement import move_character, validate_movement
from utils import get_current_map_level


def main():
    """
    Run the game
    """
    print_initial_story()
    game_map = create_map()

    # Create Character
    character_information = get_user_input_for_character()
    character = create_character(character_information)

    # Create Foes
    foes = create_foe()
    quizzes = create_quizzes()

    am_i_win = False
    current_map = game_map[character["level"]]

    print_start_message(character)

    describe_current_location(current_map, character)
    while not am_i_win:
        current_map_level = get_current_map_level(character, game_map, current_map)
        user_input = get_general_user_input()
        is_valid_movement = validate_movement(user_input[1], character, current_map)
        if user_input[0] == "valid_destination_input" and is_valid_movement:
            move_character(user_input[1], character)
            describe_current_location(current_map, character)
            am_i_win = is_achieved_goal(character, current_map)
            if am_i_win:
                break
            there_is_a_challenger = check_for_foe()
            there_is_a_quiz = check_for_quiz(character, character["luck"])
            increase_attack(character, current_map)

            if current_map_level + 1 > character["level"]:
                # deal with foe
                if there_is_a_challenger:
                    foe = select_foe(foes, str(character["level"]))
                    result_of_fight = fight_with_foe(character, foe)

                    # if character wins, increase xp
                    if result_of_fight:
                        result_of_level = increase_xp(character, foe)
                        # if xp is full, increase the level
                        if result_of_level:
                            increase_level(character)
                    # if character loses, initialize the character status
                    else:
                        print_colored_text("|❌Warning❌|".center(100, "-"), "RED")
                        print("You Died🧨")
                        print("But don't worry! Your journey is not finished!")
                        print("Your XP is initialized and you are returned to the initial place of the map.")
                        character["location"] = (0, 0)
                        character["xp"] = 300
                        character["current_hp"] = character["max_hp"]
                        continue

                # deal with quiz
                if there_is_a_quiz:
                    quiz = select_quiz(quizzes, str(character["level"]))
                    if quiz:
                        if solve_quiz(quiz):
                            increase_hp(character)

            is_enough_level = is_enough_level_to_proceed_to_next_map(character, game_map, current_map)
            is_in_goal = is_in_the_goal_destination_of_each_map(character, current_map)
            if is_enough_level and is_in_goal:
                level_for_map = character["level"] if int(character["level"]) <= 5 else 5
                current_map = game_map[level_for_map]
                character["location"] = (0, 0)
                print_colored_text("|INFO|".center(100, "-"), "YELLOW")
                print("You are going Next Map!!")
            elif is_in_goal:
                print_colored_text("|❌Warning❌|".center(100, "-"), "RED")
                print("You reached destination, but your level is not high enough to move to the next map.")
                print("Please travel around the map more, fight with foes and reach next level to get next map!")
                print()
        elif user_input[0] == "valid_feature_input":
            if user_input[1] == "5" or user_input[1] == "map":
                print_map(current_map, character)
                continue
            elif user_input[1] == "6" or user_input[1] == "status":
                print_status(character, current_map_level, current_map)
                continue
        else:
            print_colored_text("|❌Warning❌|".center(100, "-"), "RED")
            print("You reached the boundary of the game board!")
            print("You cannot move to the direction!")
            print()
    print_ending_message()


if __name__ == "__main__":
    main()
