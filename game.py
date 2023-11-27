import random
import json


def create_map():
    # Load map name json file and store in dictionary
    location_file = "game_data/location_names.json"
    with open(location_file) as location_names_json:
        location_names = json.load(location_names_json)

    # Shuffle map list expect first and last items
    for level, maps in location_names.items():
        middle_map = maps[1:-1]
        random.shuffle(middle_map)
        location_names[level] = [maps[0]] + middle_map + [maps[-1]]

    # Initialize maps
    maps = {"level_1_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_2_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_3_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_4_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_5_map": {(x, y): "" for x in range(5) for y in range(4)}}

    # Assign location name to maps
    for level, locations in zip(maps.keys(), location_names.values()):
        for index, each_map in enumerate(maps[level]):
            maps[level][each_map] = locations[index]

    return maps


def create_character(character_information):
    character = {"name": character_information.name, "occupation": character_information.occupation_title,
                 "location": (0, 0), "level": 0, "current_hp": 10, "max_hp": 10, "xp": 100,
                 "attack": character_information.skills}
    return character


def get_user_input_for_character():
    # Get username from user
    print("Welcome User! Enter your name to start")
    character_information = {}
    while True:
        try:
            name = input("Your name: ")
            if len(name.strip()) <= 2:
                pass
                # TODO: raise appropriate error
                # raise
        except:
            print("Character name should be longer than 2 letters.😥")
            print("Please re-enter your name🙏")
        else:
            character_information["name"] = name
            break

    # Get user occupation
    occupation_list = ["Otaku", "Salaryman", "Ninja", "Samurai"]


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

    # Load foe name json file and store in dictionary
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


def main():
    print("I'm ready for the term project! 🙌")
    game_map = create_map()
    get_user_input_for_character()
    there_is_a_challenger = check_for_foe()
    if there_is_a_challenger:
        fight_with_foe()





if __name__ == "__main__":
    main()
