import random
import json


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
                 "location": (0, 0), "level": 1, "current_hp": 10, "max_hp": 10, "xp": 10, "attack": 2}
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
    print("========================================")
    for key, value in occupations.items():
        print(f"{key}: {value}")
    print("========================================")
    print("HINT: You can enter just number or full name of occupations.")
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
            print("Please re-enter your occupation by number or full name of occupations.")
            # TODO: print occupations list one more time here
    return character_information


def describe_current_location(game_board, character):
    print(f"{character['name']} is now currently in {game_board[character['level']][character['location']]}")


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
            print(f"Your input `{user_input} is not valid.`")
            print("Please select from the below.")
            print(valid_direction_inputs)
            print(valid_feature_inputs)


def validate_movement(user_input, character, board):
    current_location = list(character["location"])
    location_after_movement = current_location
    print(location_after_movement)
    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1
    print(tuple(location_after_movement))
    if tuple(location_after_movement) in board[character["level"]]:
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

    while True:
        character["current_hp"] -= foe["attack"]
        print(f"Foe attacked you. Now your hp is {character['current_hp']}")
        if character["current_hp"] <= 0:
            return False
        foe["HP"] -= character["attack"]
        print(f"You attacked foe. Now foe's hp is {foe['HP']}")
        if foe["HP"] <= 0:
            return True


def check_for_quiz():
    #  25% of chance to get a quiz
    there_is_a_quiz = random.randint(1, 4)
    if there_is_a_quiz == 2:
        return True
    else:
        return False


def solve_quiz():
    # Load quiz json file and store in dictionary
    quiz_file = "game_data/quiz.json"
    with open(quiz_file) as quiz_json:
        quizzes = json.load(quiz_json)
    chosen_quiz = random.choice(quizzes)

    # get the key for the chosen quiz
    quiz_key = list(chosen_quiz.keys())[0]

    question = chosen_quiz[quiz_key]["question"]
    options = chosen_quiz[quiz_key]["option"]
    answer = chosen_quiz[quiz_key]["answer"]

    # print question and options
    print("You've encountered a quiz challenge! 🧠\n")
    print(f"Question 🧐❔\n{question}")
    for option in options:
        print(option.strip())

    user_answer = input("Enter your answer >>>").strip()
    if user_answer not in ['1', '2', '3']:
        raise ValueError("Invalid choice!\nPlease select one of the following options:")
    elif user_answer == answer:
        print("You are right! You get 1 HP 🥳")
        return True
    else:
        print(f"Oops! The answer is {answer}")
        return False


def increase_hp():
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character = {"name": "momo", "occupation": "Otaku",
                 "location": (2, 4), "level": 0, "current_hp": 5, "max_hp": 10, "xp": 100,
                 "attack": 3}
    character["current_hp"] += 1

    print("========================================")
    print("Current Status:")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("========================================")


def increase_xp(character, foe):
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    if character["xp"] <= 0:
        print("Congratulations! You've reached maximum XP so Your level went up!")
        return True
    else:
        character["xp"] -= foe['xp']
        print("========================================")
        print("Current Status:")
        for key, value in character.items():
            print(f"{key}: {value}")
        print("========================================")
        return False


def increase_level(character):
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character["level"] += 1
    print("========================================")
    print("Current Status:")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("========================================")


def main():
    game_map = create_map()

    # Create Character
    character_information = get_user_input_for_character()
    character = create_character(character_information)

    # Create Foes
    foes = create_foe()

    print_initial_story(character["name"])

    is_not_alive = False
    is_achieved_goal = False

    while not is_achieved_goal:
        describe_current_location(game_map, character)
        user_input = get_general_user_input()
        is_valid_input = validate_movement(user_input, character, game_map)
        if is_valid_input:
            move_character(user_input, character)
            describe_current_location(game_map, character)
            there_is_a_challenger = check_for_foe()
            there_is_a_quiz = check_for_quiz()

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
                    print("Your XP is initialized and you are returned to the initial place.")
                    continue

            # deal with quiz
            if there_is_a_quiz:
                pass
        else:
            print("------------------------------------------------------")
            print("❌Warning!!❌")
            print("You reached the boundary of the game board.")
            print("You cannot move to that direction!")
            print("------------------------------------------------------")

    # there_is_a_challenger = check_for_foe()
    # if there_is_a_challenger:
    #     fight_with_foe()
    #     check_for_quiz()
    #     if check_for_quiz():
    #         try:
    #             quiz_result = solve_quiz()
    #             if quiz_result:
    #                 increase_hp() # character will be inside ()
    #         except ValueError as e:
    #             print(e)

    # new_xp = increase_xp()
    # if new_xp:
    #     increase_level()


if __name__ == "__main__":
    main()
