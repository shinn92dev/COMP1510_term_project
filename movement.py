def validate_movement(user_input, character, board):
    """
    Check if the character's movement based on user input is valid within the board boundaries.

    :param user_input: a string
    :param character: a dictionary containing the character's information
    :param board: a dictionary representing the board
    :precondition: user_input is a string representing the direction of movement, either a cardinal direction or
                   a corresponding number '1' for north, '2' for east, '3' for south, '4' for west
    :precondition: character is a dictionary containing the character's current location with the key 'location'
    :precondition: board must have keys that represent valid location coordinates as tuples (x, y)
    :postcondition: determine if the user's input is valid or not
    :return: True if the user's input is valid, otherwise False
    """
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
