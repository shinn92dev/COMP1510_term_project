"""
Add Docstring
"""
from game_printer import print_colored_text
import time


def increase_attack(character, current_map):
    current_location_name = current_map[character["location"]]
    print(current_location_name)
    if current_location_name[-8:-1] == "CoCo壱番屋":
        character["attack"] += 1
        print_colored_text("|🎉 Congrats!|", "YELLOW", False)
        print("Luckily, you came to the CoCo Curry.")
        print("You are eating CoCo Curry now.🍛")
        for _ in range(3):
            print("...")
            time.sleep(0.7)
        print("Now, you got stronger! Your attack power increased because you are full!")
        print()


def increase_hp(character):
    # character info will be taken from an argument eventually
    current_hp = character["current_hp"]
    hp = 100
    if current_hp + hp >= character["max_hp"]:
        character["current_hp"] = character["max_hp"]
    else:
        character["current_hp"] += hp

    print()
    print_colored_text("|🎉 Congrats!|", "YELLOW", False)
    print(f"Your Current HP {character['current_hp']} / {character['max_hp']}")
    print()

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


def main():
    pass


if __name__ == "__main__":
    main()
