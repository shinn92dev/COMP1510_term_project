def is_enough_level_to_proceed_to_next_map(character, entire_board, current_map):
    """
    Check if character has reached a high enough level to proceed the next level on map.

    :param character: a dictionary containing character's information
    :param entire_board: a dictionary containing all maps
    :param current_map: a dictionary containing the current map where the character is located
    :precondition: character is a dictionary with at least the keys 'level' and 'location'
    :precondition: entire_board is a dictionary all game maps with map levels as keys.
    :precondition: current_map is a dictionary representing the current map with character's location.
    :postcondition: determine if the character's current level is greater than the current map's level
    :return: True if the character's current level is greater than the current map's level, otherwise False
    >>> character_info = {"level": 3, "location": (1, 1)}
    >>> entire_map = {1: {(0, 0): "room1", (1, 1): "room2"},
    ...     2: {(0, 0): "room3", (1, 1): "room4"},
    ...     3: {(0, 0): "room5", (1, 1): "room6"},
    ...     4: {(0, 0): "room7", (1, 1): "room8"},
    ...     5: {(0, 0): "room9", (1, 1): "room10"},}
    >>> current_position_in_map = {(0, 0): "room3", (1, 1): "room4"}
    >>> is_enough_level_to_proceed_to_next_map(character_info, entire_map, current_position_in_map)
    True
    >>> character_info = {"level": 2, "location": (0, 0)}
    >>> is_enough_level_to_proceed_to_next_map(character_info, entire_map, current_position_in_map)
    False
    """
    current_map_level = None
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            current_map_level = map_level
    if character["level"] > current_map_level:
        return True
    else:
        return False


def is_in_the_goal_destination_of_each_map(character, current_map):
    """
    Check if the character has reached the goal of each map.

    :param character: a dictionary containing the character's information
    :param current_map: a dictionary containing which map the character is on
    :precondition: character is a dictionary containing name, occupation_title as keys with values from the user
    :precondition: current_map have keys that represent valid location coordinates as tuples (x, y)
    :postcondtion: determines if the character is at the goal location on the current map
    :return: True if the character location matches the goal location, otherwise False
    """
    if sorted(current_map.keys())[-1] == character["location"]:
        return True
    else:
        return False


def is_achieved_goal(character, current_map):
    if character["level"] > 5 and is_in_the_goal_destination_of_each_map(character, current_map):
        return True
    else:
        return False


def main():
    pass


if __name__ == "__main__":
    main()
