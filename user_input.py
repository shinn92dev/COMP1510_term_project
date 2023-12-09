"""
Add Docstring
"""
import json


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

    occupation_file = "game_data/occupation.json"
    with open(occupation_file, encoding="utf-8") as location_names_json:
        occupations = json.load(location_names_json)

    print("Now, let's select your occupation!")
    print("Please select one occupation from below.")

    def print_occupation():
        print("========================================")
        for key, value in occupations.items():
            print(f"{key}: {value[0]}")
            print(value[1])
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


def get_general_user_input():
    valid_direction_inputs = ["1", "2", "3", "4", "north", "south", "east", "west"]
    valid_feature_inputs = ["help", "map", "status"]
    valid_inputs = valid_direction_inputs + valid_feature_inputs
    print("Where do you want to go?")
    print("Enter the number or full direction name.")
    print("[1: North, 2: East, 3: South, 4: West, 5: Map, 6: Status]")
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

def main():
    pass


if __name__ == "__main__":
    main()
