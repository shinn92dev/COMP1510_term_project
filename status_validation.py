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
