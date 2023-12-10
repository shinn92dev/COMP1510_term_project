"""
Add Docstring
"""
from dashtable import data2rst
from cfonts import render
import time
from colorama import init, Fore


init(autoreset=True)


def print_colored_text(text, color, new_line=True):
    if new_line:
        print(getattr(Fore, color) + text)
    else:
        print(getattr(Fore, color) + text, end=" ")


def print_with_delay(lines, delay, required_strip=False):
    for line in lines:
        if required_strip:
            print(line.strip(), flush=True)
        else:
            print(line, flush=True)
        time.sleep(delay)


def print_map(current_map, character):
    max_x_coordinate = max(coord[0] for coord in current_map.keys())
    max_y_coordinate = max(coord[1] for coord in current_map.keys())
    current_x_coord, current_y_coord = character["location"]
    print_colored_text("MAP".center(35, "-"), "BLUE")
    for y_coord in range(max_y_coordinate + 1):
        for x_coord in range(max_x_coordinate + 1):
            if x_coord == current_x_coord and y_coord == current_y_coord:
                print_colored_text("| 🧔🏻 |", "BLUE", False)
            else:
                print_colored_text("| 🟦 |", "BLUE", False)
        print()
        print_colored_text("".center(35, "-"), "BLUE")


def print_start_message(character):
    print()
    print_colored_text("|WELCOME|".center(100, "-"), "YELLOW")
    print(f"Hello!! {character['name']} [{character['occupation'][0]}]!!👋🏻")
    print("Your journey to become Japanese Emperor starts here!")
    print("Good Luck with You!🤞")
    print()


def print_initial_story():
    """
    Print out initial story of the game

    :postcondition: print out correct initial story
    """
    rendered_title_first_column = render("The Path", gradient=["red", "yellow"], align="center")
    rendered_title_second_column = render("of", gradient=["red", "yellow"], align="center")
    rendered_title_third_column = render("Japan", gradient=["red", "yellow"], align="center")
    titles = [rendered_title_first_column, rendered_title_second_column, rendered_title_third_column]
    print_with_delay(titles, 1.2)
    with open("game_data/game_story.txt", 'r', encoding='utf-8') as story:
        story_lines = story.readlines()
    print_with_delay(story_lines, 0.6, True)


def describe_current_location(game_board, character):
    print()
    print(f"|INFO| {character['name']} is now currently in {game_board[character['location']]}")
    print()


def print_status(character, current_map_level, current_map):
    map_names_for_each_level = {1: "沖縄 (Okinawa)", 2: "福岡 (Fukuoka)", 3: "京都 (Kyoto)",
                                4: "富士山 (Fuji Mountain)", 5: "東京 (Tokyo)"}
    name = f"Name: {character['name']}"
    level = f"Level: {character['level']}"
    occupation = f"Occupation: {character['occupation'][0]}"
    attack = f"Attack Power: {character['attack']}"
    luck = f"Luck: {character['luck']}"
    hp = f"Current HP: {character['current_hp']} / {character['max_hp']}"
    xp = f"Current XP Left: {character['xp']}"
    map_name = f"Current Map: {map_names_for_each_level[current_map_level]}"
    location = f"Current Locations: {current_map[character['location']]}"
    title = "🎌BECOME JAPANESE EMPEROR🤴"
    max_length = max([len(name), len(level), len(occupation), len(attack), len(luck), len(hp), len(xp), len(xp),
                     len(map_name), len(location), len(title)]) * 2

    title = title.center(max_length, " ")
    table = [
        [title, "", "", "", "", ""],
        [name, "", level, "", occupation, ""],
        [attack, "", "", luck, "", ""],
        [hp, "", "", xp, "", ""],
        [map_name, "", "", location, "", ""],
    ]
    span_first_column = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    span_second_column_left = [[1, 0], [1, 1]]
    span_second_column_middle = [[1, 2], [1, 3]]
    span_second_column_right = [[1, 4], [1, 5]]
    span_third_column_left = [[2, 0], [2, 1], [2, 2]]
    span_third_column_right = [[2, 3], [2, 4], [2, 5]]
    span_fourth_column_left = [[3, 0], [3, 1], [3, 2]]
    span_fourth_column_right = [[3, 3], [3, 4], [3, 5]]
    span_fifth_column_left = [[4, 0], [4, 1], [4, 2]]
    span_fifth_column_right = [[4, 3], [4, 4], [4, 5]]

    spans = [span_first_column, span_second_column_left, span_second_column_middle, span_second_column_right,
             span_third_column_left, span_third_column_right, span_fourth_column_left, span_fourth_column_right,
             span_fifth_column_left, span_fifth_column_right]
    print(data2rst(table, spans=spans, use_headers=True))


def main():
    pass


if __name__ == "__main__":
    main()
