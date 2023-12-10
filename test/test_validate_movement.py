from unittest import TestCase
from movement import validate_movement
class TestValidateMovement(TestCase):
    def test_validate_movement_north_valid(self):
        user_input = "1"
        character_info = {"name": "Jonny", "occupation": "Ninja", "location": (0, 1), "level": 1}
        board = {(0, 0): "room1", (0, 1): "room2", (0, 2): "room3", (1, 0): "room4", (1, 1): "room5", (1, 2): "room6"}
        expect = True
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)


    def test_validate_movement_north_invalid(self):
        user_input = "1"
        character_info = {"name": "Alex", "occupation": "Samurai", "location": (0, 0), "level": 1}
        board = {(0, 0): "room", (0, 1): "a_room", (0, 2): "b_room", (1, 0): "c_room", (1, 1): "d_room", (1, 2): "e_room"}
        expect = False
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)

    def test_validate_movement_east_valid(self):
        user_input = "2"
        character_info = {"name": "Conny", "occupation": "Otaku", "location": (0, 0), "level": 1}
        board = {(0, 0): "room", (0, 1): "room2", (0, 2): "room3", (1, 0): "room4", (1, 1): "room5", (1, 2): "room6"}
        expect = True
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)


    def test_validate_movement_east_invalid(self):
        user_input = "2"
        character_info = {"name": "Alice", "occupation": "Samurai", "location": (1, 2), "level": 1}
        board = {(0, 0): "room", (0, 1): "a_room", (0, 2): "room", (1, 0): "c_room", (1, 1): "d_room", (1, 2): "e_room"}
        expect = False
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)


    def test_validate_movement_south_valid(self):
        user_input = "3"
        character_info = {"name": "Peter", "occupation": "Otaku", "location": (0, 0), "level": 1}
        board = {(0, 0): "room", (0, 1): "room2", (0, 2): "room3", (1, 0): "room", (1, 1): "room5", (1, 2): "room6"}
        expect = True
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)

    def test_validate_movement_south_invalid(self):
        user_input = "3"
        character_info = {"name": "Alice", "occupation": "Samurai", "location": (0, 2), "level": 1}
        board = {(0, 0): "room", (0, 1): "room", (0, 2): "room", (1, 0): "c_room", (1, 1): "d_room", (1, 2): "e_room"}
        expect = False
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)


    def test_validate_movement_west_valid(self):
        user_input = "4"
        character_info = {"name": "Bob", "occupation": "Otaku", "location": (2, 0), "level": 1}
        board = {(0, 0): "room", (0, 1): "room2", (0, 2): "room3", (1, 0): "room", (1, 1): "room", (1, 2): "room6"}
        expect = True
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)

    def test_validate_movement_west_invalid(self):
        user_input = "4"
        character_info = {"name": "Alice", "occupation": "Samurai", "location": (0, 0), "level": 1}
        board = {(0, 0): "room", (0, 1): "room", (0, 2): "room", (1, 0): "room", (1, 1): "d_room", (1, 2): "e_room"}
        expect = False
        actual = validate_movement(user_input, character_info, board)
        self.assertEqual(expect, actual)
