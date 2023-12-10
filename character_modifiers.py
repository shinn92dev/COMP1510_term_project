"""
Add Docstring
"""
from game_printer import print_colored_text
import time


def increase_attack(character, current_map):
    """
    Increases the attack power of the character if they are in a specific location
    :param character: a dictionary representing character
    :param current_map: a dictionary representing current map
    :precondition: character should be a dictionary containing correct character information
    :precondition: current_map should be a dictionary containing correct current map information
    :postcondition: increase character attack power when character is in CoCo Curry and print corresponding message
    """
    current_location_name = current_map[character["location"]]
    if current_location_name[-8:-1] == "CoCo壱番屋":
        character["attack"] += 2
        print_colored_text("|🎉 Congrats!|", "YELLOW", False)
        print("Luckily, you came to the CoCo Curry.")
        print("You are eating CoCo Curry now.🍛")
        for _ in range(3):
            print("...")
            time.sleep(0.7)
        print("Now, you got stronger! Your attack power increased because you are full!")
        print()


def increase_hp(character):
    """
    Increases the character's current health points (HP) up to the maximum HP.

    The function adds 5 HP to the character's current HP. If the resulting current HP exceeds
    the character's maximum HP, it sets the current HP to the maximum HP

    :param character: a dictionary representing character
    :precondition: character should be a dictionary containing correct character information
    :postcondition: The character's current HP is increased, and if it exceeds the maximum HP, it is set to the maximum
    :return: None
    """
    current_hp = character["current_hp"]
    hp = 5
    if current_hp + hp >= character["max_hp"]:
        character["current_hp"] = character["max_hp"]
    else:
        character["current_hp"] += hp

    print()
    print_colored_text("|🎉 Congrats!|", "YELLOW", False)
    print(f"Your Current HP: {character['current_hp']} / {character['max_hp']}")
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
        return False


def increase_level(character):
    # character info will be taken from an argument eventually
    # so this is a temporary variable
    each_level_status = {2: {"max_hp": 40, "xp": 20}, 3: {"max_hp": 50, "xp": 30},
                         4: {"max_hp": 60, "xp": 40}, 5: {"max_hp": 70, "xp": 50}}
    next_level = character["level"] + 1
    character["level"] = next_level
    character["current_hp"] = character["max_hp"] = each_level_status[next_level]["max_hp"]
    character["xp"] = each_level_status[next_level]["xp"]
    print_colored_text("|🎉 Congrats!|", "YELLOW", False)
    print(f"You reached level {character['level']}")


def main():
    pass


if __name__ == "__main__":
    main()
