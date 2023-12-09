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
                 "location": (0, 0), "level": 1, "current_hp": 1000, "max_hp": 1000, "xp": 10, "attack": 2}
    # TODO: Add "attack": character_information.skills into character dictionary
    return character

def main():
    create_character()


if __name__ == "__main__":
    main()
