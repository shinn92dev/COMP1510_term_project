"""
Module for determining the level of the current map based on the character's location
"""
import json
from game_printer import print_colored_text


def get_user_input_for_character():
    """
    Prompt the user for character information

    :postconditon: get user input for character until user enters valid data
    :return: a dictionary containing the user's name and selected occupation
    """
    # Get username from user
    print("Welcome User! Enter your name to start")
    character_information = {}
    while True:
        user_name = input(">> ").strip()
        if len(user_name) >= 3:
            character_information["name"] = user_name
            print()
            print(f"Nice to meet you {user_name}!")
            print()
            break
        else:
            print_colored_text("|❌WARNING❌|", "RED", False)
            print("Your name must be longer than or equal to 3 letters. Please re-enter your name.")

    occupation_file = "game_data/occupation.json"
    with open(occupation_file, encoding="utf-8") as location_names_json:
        occupations = json.load(location_names_json)

    print("Now, let's select your occupation!")
    print("Please select one occupation from below.")
    print()

    def print_occupation():
        """
        Print the list of occupation with corresponding numbers and descriptions

        :postcondition: print out correct occupations and descriptions with corresponding number
        """
        print_colored_text("|OCCUPATION|".center(100, "="), "YELLOW")
        for key, value in occupations.items():
            print(f"{key}: {value[0]}")
            print(value[1])
        print("HINT: You can enter just number or full name of occupations.")
        print_colored_text("=".center(100, "="), "YELLOW")

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
            print()
            print_colored_text("|❌WARNING❌|", "RED", False)
            print(f"`{user_occupation}` is not valid occupation. Please re-enter your occupation again.")
            print("")
            print_occupation()
    return character_information


def get_general_user_input():
    """
    Prompt the user for general input, including movement directions and other features

    :postcondition: prompt the user for general input until user enters valid input
    :return: a list containing the type of input ("valid_destination_input" or "valid_feature_input") and
             the user's input value
    """
    valid_direction_inputs = ["1", "2", "3", "4", "north", "south", "east", "west"]
    valid_feature_inputs = ["5", "6", "map", "status"]
    print("Where do you want to go or What do you want to do?")
    print("Enter the number or full name.")
    print("[1: North, 2: East, 3: South, 4: West, 5: Map, 6: Status]")
    while True:
        user_input = input(">> ").lower()
        if user_input in valid_direction_inputs:
            return ["valid_destination_input", user_input]
        elif user_input in valid_feature_inputs:
            return ["valid_feature_input", user_input]
        else:
            print()
            print_colored_text("❌Warning!❌".center(100, "-"), "RED")
            print(f"Your input `{user_input}` is not valid.`")
            print("Please select from the below.")
            print("[1: North, 2: East, 3: South, 4: West, 5: Map, 6: Status]")
            print()


def main():
    pass


if __name__ == "__main__":
    main()
