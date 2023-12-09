"""
Add Docstring
"""
def validate_movement(user_input, character, board):
    current_location = list(character["location"])
    location_after_movement = current_location
    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1
    if tuple(location_after_movement) in board:
        return True
    else:
        return False


def move_character(user_input, character):
    current_location = list(character["location"])
    location_after_movement = current_location

    if user_input == "1" or user_input == "north":
        location_after_movement[1] -= 1
    elif user_input == "3" or user_input == "south":
        location_after_movement[1] += 1
    elif user_input == "4" or user_input == "west":
        location_after_movement[0] -= 1
    elif user_input == "2" or user_input == "east":
        location_after_movement[0] += 1

    character["location"] = tuple(location_after_movement)

def main():
    pass


if __name__ == "__main__":
    main()
