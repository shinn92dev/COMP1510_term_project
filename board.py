import json
from random import shuffle


def create_map():
    # Load map name json file and store in dictionary
    location_file = "game_data/location_names.json"
    with open(location_file, encoding="utf-8") as location_names_json:
        location_names = json.load(location_names_json)

    # Shuffle map list expect first and last items
    for level, maps in location_names.items():
        middle_map = maps[1:-1]
        shuffle(middle_map)
        location_names[level] = [maps[0]] + middle_map + [maps[-1]]

    # Initialize maps
    maps = {1: {(x, y): "" for x in range(5) for y in range(4)},
            2: {(x, y): "" for x in range(5) for y in range(4)},
            3: {(x, y): "" for x in range(5) for y in range(4)},
            4: {(x, y): "" for x in range(5) for y in range(4)},
            5: {(x, y): "" for x in range(5) for y in range(4)}}

    # Assign location name to maps
    for level, locations in zip(maps.keys(), location_names.values()):
        for index, each_map in enumerate(maps[level]):
            maps[level][each_map] = locations[index]

    return maps
