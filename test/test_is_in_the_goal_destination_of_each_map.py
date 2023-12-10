from unittest import TestCase
from status_validation import is_in_the_goal_destination_of_each_map

class TestIsInTheGoalDestinationOfEachMap(TestCase):
    def test_is_in_the_goal_destination_of_each_map_result_is_yes(self):
        character_info = {'name': 'Alberto', 'location': (2, 2)}
        current_board = {(0, 0): 'start', (1, 1): 'empty room', (2, 2): 'goal'}
        expect = True
        actual = is_in_the_goal_destination_of_each_map(character_info, current_board)
        self.assertEqual(expect, actual)


    def test_is_in_the_goal_destination_of_each_map_result_is_no(self):
        character_info = {'name': 'Kenny', 'location': (1, 2)}
        current_board = {(0, 0): 'start', (1, 1): 'empty room', (2, 2): 'goal'}
        expect = False
        actual = is_in_the_goal_destination_of_each_map(character_info, current_board)
        self.assertEqual(expect, actual)
