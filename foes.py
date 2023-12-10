"""
Add Docstring
"""
import json
from random import choice, randint
from game_printer import print_colored_text
import time


def create_foe():
    """
    Create foes' dictionary from JSON file containing foes information.

    :postcondition: get foes information from JSON file and create dictionary from the given information
    :return: a dictionary containing foe information
    """
    foe_file = "game_data/foe.json"
    with open(foe_file, encoding="utf-8") as foe_json:
        foes = json.load(foe_json)
    return foes


def select_foe(foes, level):
    """
    Select one random foe that has the same level with the character.

    :param foes: a dictionary
    :param level: an integer representing current character level
    :precondition: foes should be a dictionary containing foes' level as keys and list of foes information as values
    :postcondition: randomly choose a foe that has the same level with the character
    :return: a dictionary containing a foe's information
    """
    return choice(foes[level])


def fight_with_foe(character, foe):
    """
    Simulate a fight between character and foe.

    :param character: a dictionary representing the player's character
    :param foe: a dictionary representing the foe
    precondition: a dictionary representing the player's character, with keys for 'current_hp' and 'attack'
    precondition: a dictionary representing the foe, with keys for 'name', 'HP', and 'attack'
    :postcondition: determine which one wins
    :return: True if the character wins, otherwise False
    >>> character_info = {"name": "momo", "level": 1, "current_hp": 10, "xp": 10, "attack": 2, "luck": 0}
    >>> foe_info = {"name": "virus", "HP": 2, "attack": 1, "xp": 5}
    >>> fight_with_foe(character_info, foe_info)
    A wild virus appears!
    <BLANKLINE>
    <BLANKLINE>
    |FIGHT🔥| Foe attacked you. Now your hp is 9
    <BLANKLINE>
    |FIGHT🔥| You attacked foe. Now foe's hp is 0
    <BLANKLINE>
    You WIN!!
    True
    """
    print(f"A wild {foe['name']} appears!")
    print("")

    count = 1
    while True:
        character["current_hp"] -= foe["attack"]
        print(f"Round {count}")
        print_colored_text("|FIGHT🔥|", "RED", False)
        print(f"Foe attacked you. Now your hp is {character['current_hp']}")

        if character["current_hp"] <= 0:
            return False
        foe["HP"] -= character["attack"]
        print_colored_text("|FIGHT🔥|", "RED", False)
        print(f"You attacked foe. Now foe's hp is {foe['HP'] if foe['HP'] >= 0 else 0}")
        if foe["HP"] <= 0:
            print("You WIN!!")
            print()
            return True
        count += 1
        time.sleep(0.7)


def check_for_foe():
    """
    Check if there is a foe.

    :return: True if a randomly selected number from 1 to 4 is 1, else False.
    """
    #  25% of chance to encounter a foe
    there_is_a_foe = randint(1, 4)
    if there_is_a_foe == 1:
        return True
    else:
        return False

def main():
    pass


if __name__ == "__main__":
    main()
