"""
Add Docstring
"""
def is_enough_level_to_proceed_to_next_map(character, entire_board, current_map):
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
