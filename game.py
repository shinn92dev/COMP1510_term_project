import random
import json


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
                 "location": (0, 0), "level": 1, "current_hp": 10, "max_hp": 10, "xp": 100}
    # TODO: Add "attack": character_information.skills into character dictionary
    return character


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
    print(location_after_movement)
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

def fight_with_foe():
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character = {"name": "momo", "occupation": "Otaku",
                 "location": (2, 4), "level": 0, "current_hp": 10, "max_hp": 10, "xp": 100,
                 "attack": 3}

    # Load foe json file and store in dictionary
    foe_file = "game_data/foe.json"
    with open(foe_file) as foe_json:
        foes = json.load(foe_json)
    chosen_foe = random.choice(foes)

    print(f"A wild {chosen_foe['name']} appears!")

    while character['current_hp'] > 0 and chosen_foe['HP'] > 0:
        print()
        try:
            action = input("Choose your action:\n1. Attack\n2. Defend\n")
            if action == "1":
                chosen_foe['HP'] -= character['attack']
                print(f"You attacked the {chosen_foe['name']}")
                print(f"Your current status: {character}\nThe {chosen_foe['name']}'s current status{chosen_foe}")
                is_defending = False
            elif action == "2":
                print(f"You defend yourself so you didn't get any damage from {chosen_foe['name']}!")
                print(f"Your current status: {character}\nThe {chosen_foe['name']}'s current status{chosen_foe}")
                is_defending = True
            else:
                print("Invalid input. Please enter 1 or 2!")
                continue

            print()
            if chosen_foe['HP'] >= 0 and not is_defending:
                character['current_hp'] -= chosen_foe['attack']
                print(f"The {chosen_foe['name']} attacked you!")
                print(f"Your current status: {character}\nThe {chosen_foe['name']}'s current status{chosen_foe}")
        except ValueError:
            print("Invalid input. Please enter 1 or 2!")
            continue

    print()
    if character['current_hp'] <= 0:
        print("You have been defeated...")
        return False
    else:
        print(f"You defeated the {chosen_foe['name']}!")
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

    #get the key for the chosen quiz
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
        raise ValueError("Invalid choice!\nPlease select one of the following options:" )
    elif user_answer == answer:
        print("You are right! You get 1 HP 🥳")
        return True
    else:
        print(f"Oops! The answer is {answer}")
        return False

def increase_hp():
    #character info will be taken from an argument eventually
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


def increase_xp():
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character = {"name": "momo", "occupation": "Otaku",
                 "location": (2, 4), "level": 0, "current_hp": 5, "max_hp": 10, "xp": 100,
                 "attack": 3}
    if character["xp"] == 100:
        print("Congratulations! You've reached maximum XP so Your level went up!")
        return True
    else:
        character["xp"] += 1
        print("========================================")
        print("Current Status:")
        for key, value in character.items():
            print(f"{key}: {value}")
        print("========================================")
        # return False


def increase_level():
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    character = {"name": "momo", "occupation": "Otaku",
                 "location": (2, 4), "level": 0, "current_hp": 5, "max_hp": 10, "xp": 100,
                 "attack": 3}
    character["level"] += 1
    print("========================================")
    print("Current Status:")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("========================================")


def main():
    print("I'm ready for the term project! 🙌")
    game_map = create_map()
    get_user_input_for_character()
    there_is_a_challenger = check_for_foe()
    if there_is_a_challenger:
        fight_with_foe()
        check_for_quiz()
        if check_for_quiz():
            try:
                quiz_result = solve_quiz()
                if quiz_result:
                    increase_hp() # character will be inside ()
            except ValueError as e:
                print(e)

    # new_xp = increase_xp()
    # if new_xp:
    #     increase_level()


if __name__ == "__main__":
    board = create_map()
    # character_information = get_user_input_for_character()
    character_information = {"occupation_title": "Occupation 1", "name": "Anthony"}
    character = create_character(character_information)
    describe_current_location(board, character)
    user_input = get_general_user_input()

    if validate_movement(user_input, character, board):
        move_character(user_input, character)

    print(character["location"])
    # main()
