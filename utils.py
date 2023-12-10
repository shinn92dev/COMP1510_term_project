"""
Add Docstring
"""


def get_current_map_level(character, entire_board, current_map):
    """
    Get the level of the current map based on the character's location

    :param character: a dictionary representing character information
    :param entire_board: a dictionary representing entire game board information
    :param current_map: a dictionary representing the current map
    :precondition: character should be a dictionary representing character information
    :precondition: entire_board should be a dictionary representing entire game board information
    :precondition: current_map should be a dictionary representing the current map
    :postcondition: figure out correct level of the current mep
    :return: an int representing level of the current map
    >>> test_character = {"location": (0, 0)}
    >>> test_entire_board = {
    ...     1: {(0, 0): "Map 1A", (0, 1): "Map 1B"},
    ...     2: {(0, 0): "Map 2C", (0, 1): "Map 2D"}
    ... }
    >>> test_current_map = {(0, 0): "Map 1A", (0, 1): "Map 1B"}

    >>> get_current_map_level(test_character, test_entire_board, test_current_map)
    1

    >>> test_character = {"location": (0, 1)}
    >>> test_current_map = {(0, 0): "Map 2C", (0, 1): "Map 2D"}

    >>> get_current_map_level(test_character, test_entire_board, test_current_map)
    2
    """
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            return map_level


def main():
    pass


if __name__ == "__main__":
    main()
