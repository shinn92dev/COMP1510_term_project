"""
Add Docstring
"""


def get_current_map_level(character, entire_board, current_map):
    for map_level in range(1, 6):
        if current_map[character["location"]] in entire_board[map_level].values():
            return map_level


def main():
    pass


if __name__ == "__main__":
    main()
