from unittest import TestCase
from movement import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        user_input_direction = "1"
        character_info = {"location": (0, 1)}
        expect = (0, 0)
        move_character(user_input_direction, character_info)
        actual = character_info["location"]
        self.assertEqual(expect, actual)

    def test_move_character_east(self):
        user_input_direction = "2"
        character_info = {"location": (0, 1)}
        expect = (1, 1)
        move_character(user_input_direction, character_info)
        actual = character_info["location"]
        self.assertEqual(expect, actual)


    def test_move_character_south(self):
        user_input_direction = "3"
        character_info = {"location": (0, 1)}
        expect = (0, 2)
        move_character(user_input_direction, character_info)
        actual = character_info["location"]
        self.assertEqual(expect, actual)


    def test_move_character_west(self):
        user_input_direction = "4"
        character_info = {"location": (2, 2)}
        expect = (1, 2)
        move_character(user_input_direction, character_info)
        actual = character_info["location"]
        self.assertEqual(expect, actual)
