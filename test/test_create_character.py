from unittest import TestCase
from character import create_character


class TestCreateCharacter(TestCase):
    def test_create_character_ninja_class(self):
        character_info = {"name": "Tommy", "occupation_title": "Ninja"}
        expect = {"name": "Tommy", "occupation": "Ninja", "location": (0, 0), "level": 1, "current_hp": 1000,
                     "max_hp": 1000, "xp": 10, "attack": 5, "luck": 5}
        actual = create_character(character_info)
        self.assertEqual(expect, actual)

    def test_create_character_samurai_class(self):
        character_info = {"name": "Matthew", "occupation_title": "Samurai"}
        expect = {"name": "Matthew", "occupation": "Samurai", "location": (0, 0), "level": 1, "current_hp": 1000,
                  "max_hp": 1000, "xp": 10, "attack": 5, "luck": 0}
        actual = create_character(character_info)
        self.assertEqual(expect, actual)
