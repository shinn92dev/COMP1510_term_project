"""
Add Docstring
"""
def increase_attack(character, current_map):
    current_location_name = current_map[character["location"]]
    print(current_location_name)
    if current_location_name[-8:-1] == "CoCo壱番屋":
        character["attack"] += 1
        print("|🎉 Congrats!| You got stronger")


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


def main():
    pass


if __name__ == "__main__":
    main()
