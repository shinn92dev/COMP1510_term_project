import random
import json


def create_map():
    # Load map name json file and store in dictionary
    location_file = "game_data/location_names.json"
    with open(location_file) as location_names_json:
        location_names = json.load(location_names_json)

    # Shuffle map list expect first and last items
    for level, maps in location_names.items():
        middle_map = maps[1:-1]
        random.shuffle(middle_map)
        location_names[level] = [maps[0]] + middle_map + [maps[-1]]

    # Initialize maps
    maps = {"level_1_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_2_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_3_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_4_map": {(x, y): "" for x in range(5) for y in range(4)},
            "level_5_map": {(x, y): "" for x in range(5) for y in range(4)}}

    # Assign location name to maps
    for level, locations in zip(maps.keys(), location_names.values()):
        for index, each_map in enumerate(maps[level]):
            maps[level][each_map] = locations[index]

    return maps


def create_character(name, occupation):
    character = {"name": name, "occupation": occupation.title, "location": (0, 0), "level": 0,
                 "current_hp": 10, "max_hp": 10, "xp": 100, "attack": occupation.skills}
    return character


def main():
    print("I'm ready for the term project! 🙌")
    game_map = create_map()
    print(game_map)


if __name__ == "__main__":
    main()
