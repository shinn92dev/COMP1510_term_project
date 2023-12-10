"""
Momona Wada
A01348325
"""
from unittest import TestCase
from status_validation import is_enough_level_to_proceed_to_next_map

class TestIsEnoughLevelToProceedToNextMap(TestCase):
    def test_is_enough_level_to_proceed_to_next_map_result_is_yes(self):
        character_info = {"level": 3, "location": (1, 1)}
        entire_map = {1: {(0, 0): "room1", (1, 1): "room2"}, 2: {(0, 0): "room3", (1, 1): "room4"}, 3: {(0, 0): "room5",
                      (1, 1): "room6"}, 4: {(0, 0): "room7", (1, 1): "room8"}, 5: {(0, 0): "room9", (1, 1): "room10"},}
        current_position_in_map = {(0, 0): "room3", (1, 1): "room4"}
        expect = True
        actual = is_enough_level_to_proceed_to_next_map(character_info, entire_map, current_position_in_map)
        self.assertEqual(expect, actual)


    def test_is_enough_level_to_proceed_to_next_map_result_is_no(self):
        character_info = {"level": 2, "location": (1, 1)}
        entire_map = {1: {(0, 0): "room1", (1, 1): "room3"}, 2: {(0, 0): "room3", (1, 1): "room4"}, 3: {(0, 0): "room5",
                      (1, 1): "room6"}, 4: {(0, 0): "room7", (1, 1): "room8"}, 5: {(0, 0): "room9", (1, 1): "room10"},}
        current_position_in_map = {(0, 0): "room3", (1, 1): "room4"}
        expect = False
        actual = is_enough_level_to_proceed_to_next_map(character_info, entire_map, current_position_in_map)
        self.assertEqual(expect, actual)
