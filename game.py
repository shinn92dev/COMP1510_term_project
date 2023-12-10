from character import create_character
from foes import create_foe, select_foe, fight_with_foe, check_for_foe
from board import create_map
from user_input import get_user_input_for_character, get_general_user_input
from quizzes import select_quiz, create_quizzes, solve_quiz, check_for_quiz
from character_modifiers import increase_level, increase_attack, increase_xp, increase_hp
from game_printer import print_map, print_initial_story, describe_current_location, print_status, print_start_message
from status_validation import (is_enough_level_to_proceed_to_next_map, is_achieved_goal,
                               is_in_the_goal_destination_of_each_map)
from movement import move_character, validate_movement


def get_current_map_level(character, entire_board, current_map):
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            return map_level


def main():
    # print_initial_story()
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
        print("#" * 100)
        print(f"current_map_level {current_map_level}")
        print("#" * 100)
        user_input = get_general_user_input()
        is_valid_movement = validate_movement(user_input[1], character, current_map)
        if user_input[0] == "valid_destination_input" and is_valid_movement:
            move_character(user_input[1], character)
            describe_current_location(current_map, character)
            there_is_a_challenger = check_for_foe()
            there_is_a_quiz = check_for_quiz(character, character["luck"])
            am_i_win = is_achieved_goal(character, current_map)
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
                        print("You died.")
                        character["location"] = (0, 0)
                        character["xp"] = 100
                        character["current_hp"] = character["max_hp"]
                        print("Your XP is initialized and you are returned to the initial place.")
                        continue

                # deal with quiz
                if there_is_a_quiz:
                    print("character level {character['level']}")
                    quiz = select_quiz(quizzes, str(character["level"]))
                    if quiz:
                        if solve_quiz(quiz):
                            increase_hp(character)

            is_enough_level = is_enough_level_to_proceed_to_next_map(character, game_map, current_map)
            is_in_goal = is_in_the_goal_destination_of_each_map(character, current_map)
            if is_enough_level and is_in_goal:
                current_map = game_map[character["level"]]
                character["location"] = (0, 0)
                print("Next level!!")
            elif is_in_goal:
                print("------------------------------------------------------")
                print("")
                print("You reached destination, but not enough level")
                print("Please walk around the map and reach next level to get next map!")
        elif user_input[0] == "valid_feature_input":
            if user_input[1] == "5" or user_input[1] == "map":
                print_map(current_map, character)
                continue
            elif user_input[1] == "6" or user_input[1] == "status":
                print_status(character, current_map_level, current_map)
                continue
        else:
            print("------------------------------------------------------")
            print("❌Warning!!❌")
            print("You reached the boundary of the game board.")
            print("You cannot move to that direction!")
            print("------------------------------------------------------")


if __name__ == "__main__":
    main()
