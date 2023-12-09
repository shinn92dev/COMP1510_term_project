"""
Add Docstring
"""
def print_map(current_map, character):
    max_x_coordinate = max(coord[0] for coord in current_map.keys())
    max_y_coordinate = max(coord[1] for coord in current_map.keys())
    current_x_coord, current_y_coord = character["location"]
    print("-----------------------------------")
    for y_coord in range(max_y_coordinate + 1):
        for x_coord in range(max_x_coordinate + 1):
            if x_coord == current_x_coord and y_coord == current_y_coord:
                print("| 👨 |", end=" ")
            else:
                print("| 🟪 |", end=" ")
        print()
        print("-----------------------------------")


def print_initial_story(name):
    """
    Print out initial story of the game

    :param name: a string
    :precondition: a name should be a username that the user inputted
    :postcondition: print out correct initial story with username
    """
    print(f"Hello {name}!")
    print("Your journey to become Japanese Emperor Starts Here.")


def describe_current_location(game_board, character):
    print()
    print(f"|INFO| {character['name']} is now currently in {game_board[character['location']]}")
    print()


def main():
    pass


if __name__ == "__main__":
    main()
