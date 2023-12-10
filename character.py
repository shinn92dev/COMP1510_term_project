"""
Add Docstring
"""


def create_character(character_information):
    """
    Create character dictionary

    :param character_information: a dictionary
    :precondition: character_information should be a dictionary containing name, occupation_title as keys with values
                   from the user
    :postcondition: create initial character information with correct user information
    :return: a dictionary containing character information
    """
    character = {"name": character_information["name"], "occupation": character_information["occupation_title"],
                 "location": (0, 0), "level": 4, "current_hp": 1000, "max_hp": 1000, "xp": 10, "attack": 5, "luck": 0}
    if character["occupation"][0] == "Ninja":
        character["luck"] = 5
    if character["occupation"][0] == "Samurai":
        character["attack"] = 5
    return character


def main():
    pass


if __name__ == "__main__":
    main()
