import random
import json


# def print_character_status(character):
#     {"name": character_information["name"], "occupation": character_information["occupation_title"],
#      "location": (0, 0), "level": 1, "current_hp": 10, "max_hp": 10, "xp": 10, "attack": 2}
#     print_value = ""
#     print_value += "Name"


def print_initial_story(name):
    print(f"Hello {name}!")
    print("Your journey to become Japanese Emperor Starts Here.")


def create_map():
    # Load map name json file and store in dictionary
    location_file = "game_data/location_names.json"
    with open(location_file, encoding="utf-8") as location_names_json:
        location_names = json.load(location_names_json)

    # Shuffle map list expect first and last items
    for level, maps in location_names.items():
        middle_map = maps[1:-1]
        random.shuffle(middle_map)
        location_names[level] = [maps[0]] + middle_map + [maps[-1]]

    # Initialize maps
    maps = {1: {(x, y): "" for x in range(5) for y in range(4)},
            2: {(x, y): "" for x in range(5) for y in range(4)},
            3: {(x, y): "" for x in range(5) for y in range(4)},
            4: {(x, y): "" for x in range(5) for y in range(4)},
            5: {(x, y): "" for x in range(5) for y in range(4)}}

    # Assign location name to maps
    for level, locations in zip(maps.keys(), location_names.values()):
        for index, each_map in enumerate(maps[level]):
            maps[level][each_map] = locations[index]

    return maps


def create_character(character_information):
    character = {"name": character_information["name"], "occupation": character_information["occupation_title"],
                 "location": (0, 0), "level": 1, "current_hp": 1000, "max_hp": 1000, "xp": 10, "attack": 2}
    # TODO: Add "attack": character_information.skills into character dictionary
    return character


def create_foe():
    foe_file = "game_data/foe.json"
    with open(foe_file) as foe_json:
        foes = json.load(foe_json)
    return foes


def select_foe(foes, level):
    return random.choice(foes[level])


def get_user_input_for_character():
    # Get username from user
    print("Welcome User! Enter your name to start")
    character_information = {}
    while True:
        user_name = input(">> ").strip()
        if len(user_name) >= 3:
            character_information["name"] = user_name
            print(f"Nice to meet you {user_name}!")
            break
        else:
            print("Your name must be longer than or equal to 3 letters.")
            print("Please re-enter your name.")

    occupations = {"1": "occupation1", "2": "occupation2", "3": "occupation3", "4": "occupation4"}
    print("Now, let's select your occupation!")
    print("Please select one occupation from below.")

    def print_occupation():
        print("========================================")
        for key, value in occupations.items():
            print(f"{key}: {value}")
        print("========================================")
        print("HINT: You can enter just number or full name of occupations.")

    print_occupation()

    while True:
        user_occupation = input(">> ")
        if user_occupation in occupations or user_occupation in occupations.values():
            try:
                user_occupation = int(user_occupation)
            except ValueError:
                character_information["occupation_title"] = user_occupation
            else:
                character_information["occupation_title"] = occupations[str(user_occupation)]
            finally:
                break
        else:
            print(f"{user_occupation} is not valid occupation.")
            print("Please re-enter your occupation again.")
            print_occupation()
    return character_information


def describe_current_location(game_board, character):
    print()
    print(f"|INFO| {character['name']} is now currently in {game_board[character['location']]}")
    print()


def get_general_user_input():
    valid_direction_inputs = ["1", "2", "3", "4", "north", "south", "east", "west"]
    valid_feature_inputs = ["help", "map", "status"]
    valid_inputs = valid_direction_inputs + valid_feature_inputs
    print("Where do you want to go?")
    print("Enter the number or full direction name.")
    print("[1: North, 2: East, 3: South, 4: West]")
    while True:
        user_input = input(">> ").lower()
        if user_input in valid_inputs:
            return user_input
        else:
            print()
            print("------------------------------------------------------")
            print("❌Warning!!❌")
            print(f"Your input `{user_input} is not valid.`")
            print("Please select from the below.")
            print(valid_direction_inputs)
            print(valid_feature_inputs)
            print("------------------------------------------------------")


def validate_movement(user_input, character, board):
    current_location = list(character["location"])
    location_after_movement = current_location
    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1
    if tuple(location_after_movement) in board:
        return True
    else:
        return False


def move_character(user_input, character):
    current_location = list(character["location"])
    location_after_movement = current_location

    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1

    character["location"] = tuple(location_after_movement)


def check_for_foe():
    #  25% of chance to encounter a foe
    there_is_a_foe = random.randint(1, 4)
    if there_is_a_foe == 1:
        return True
    else:
        return False


def fight_with_foe(character, foe):
    print(f"A wild {foe['name']} appears!")
    print("")

    while True:
        character["current_hp"] -= foe["attack"]
        print("")
        print(f"|FIGHT🔥| Foe attacked you. Now your hp is {character['current_hp']}")
        print("")

        if character["current_hp"] <= 0:
            return False
        foe["HP"] -= character["attack"]
        print(f"|FIGHT🔥| You attacked foe. Now foe's hp is {foe['HP']}")
        print("")
        if foe["HP"] <= 0:
            print("You WIN!!")
            return True


def check_for_quiz(character):
    #  25% of chance to get a quiz
    if not(character["current_hp"] == character["max_hp"]):
        there_is_a_quiz = random.randint(1, 4)
        if there_is_a_quiz == 2:
            return True
        else:
            return False
    else:
        return False


def create_quizzes():
    quiz_file = "game_data/quiz.json"
    with open(quiz_file, encoding="utf-8") as quiz_json:
        quizzes = json.load(quiz_json)
    return quizzes


def select_quiz(quizzes, level):
    quiz_len = len(quizzes[level]) - 1
    if quiz_len != -1:
        return quizzes[level].pop(random.randint(0, quiz_len))


def solve_quiz(chosen_quiz):
    question = chosen_quiz["question"]
    options = chosen_quiz["option"]
    answer = chosen_quiz["answer"]

    # print question and options
    print("You've encountered a quiz challenge! 🧠\n")
    print(f"Question 🧐❔\n{question}")
    for option in options:
        print(option.strip())
    print("")

    user_answer = input("Enter your answer >>>").strip()
    if user_answer not in ['1', '2', '3']:
        raise ValueError("Invalid choice!\nPlease select one of the following options:")
    elif user_answer == answer:
        print("You are right! You get 1 HP 🥳")
        print("")
        return True
    else:
        print(f"Oops! The answer is {answer}")
        print("")
        return False


def increase_hp(character):
    # character info will be taken from an argument eventually
    character["current_hp"] += 100

    print("========================================")
    print(f"Current Status: HP {character['current_hp']} / {character['max_hp']}")
    print("========================================")
    print("")


def increase_xp(character, foe):
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    if character["xp"] <= 0:
        print("Congratulations! You've reached maximum XP so Your level went up!")
        print("")
        return True
    else:
        character["xp"] -= foe['xp']
        # print("========================================")
        # print("Current Status: ")
        # for key, value in character.items():
        #     print(f"{key}: {value}")
        # print("========================================")
        # print("")
        return False


def increase_level(character):
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character["level"] += 1
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"You reached level {character['level']}")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    # print("========================================")
    # print("Current Status:")
    # for key, value in character.items():
    #     print(f"{key}: {value}")
    # print("========================================")
    # print("")


def get_current_map_level(character, entire_board, current_map):
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            return map_level


def is_enough_level_to_proceed_to_next_map(character, entire_board, current_map):
    current_map_level = None
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            current_map_level = map_level
    if character["level"] > current_map_level:
        return True
    else:
        return False


def is_in_the_goal_destination_of_each_map(character, current_map):
    if sorted(current_map.keys())[-1] == character["location"]:
        return True
    else:
        return False


def is_achieved_goal(character, current_map):
    if character["level"] > 5 and is_in_the_goal_destination_of_each_map(character, current_map):
        return True
    else:
        return False



def main():
    game_map = create_map()

    # Create Character
    character_information = get_user_input_for_character()
    character = create_character(character_information)

    # Create Foes
    foes = create_foe()
    quizzes = create_quizzes()

    print_initial_story(character["name"])

    am_i_win = False
    current_map = game_map[character["level"]]
    print(current_map)

    describe_current_location(current_map, character)
    while not am_i_win:
        current_map_level = get_current_map_level(character, game_map, current_map)
        print("#" * 100)
        print(current_map_level)
        print("#" * 100)
        user_input = get_general_user_input()
        is_valid_input = validate_movement(user_input, character, current_map)
        if is_valid_input:
            move_character(user_input, character)
            describe_current_location(current_map, character)
            there_is_a_challenger = check_for_foe()
            there_is_a_quiz = check_for_quiz(character)
            am_i_win = is_achieved_goal(character, current_map)

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
                    # TODO: Handle no more quiz error
                    print(character["level"])
                    quiz = select_quiz(quizzes, str(character["level"]))
                    if quiz:
                        solve_quiz(quiz)

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
        else:
            print("------------------------------------------------------")
            print("❌Warning!!❌")
            print("You reached the boundary of the game board.")
            print("You cannot move to that direction!")
            print("------------------------------------------------------")


if __name__ == "__main__":
    main()
    # character = create_character({"name": "Anthony", "occupation_title": "NINJA"})
    # game_map = create_map()
    # current_map = game_map[character["level"]]
    # is_enough_level_to_proceed_to_next_map(character, game_map, current_map)