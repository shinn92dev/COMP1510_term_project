"""
Module containing functions related to game quiz logic
"""
import json
from random import randint


def create_quizzes():
    """
    Create quizzes' dictionary from JSON file containing quiz information.

    :postcondition: get quizzes information from JSON file and create dictionary from the given information
    :return: a dictionary containing quizzes information
    """
    quiz_file = "game_data/quiz.json"
    with open(quiz_file, encoding="utf-8") as quiz_json:
        quizzes = json.load(quiz_json)
    return quizzes


def select_quiz(quizzes, level):
    """
    Select one random quiz that has the same level with the location level.

    :param quizzes: a dictionary
    :param level: an integer representing current location level
    :precondition:  quizzes should be a dictionary containing 'quizzes' level as keys and list of information as values
    :postcondition: randomly choose a foe that has the same level with the character
    :return: a dictionary containing a quiz's information
    """
    try:
        quiz_len = len(quizzes[level]) - 1
    except KeyError:
        return
    else:
        if int(level) <= 5 and quiz_len != -1:
            return quizzes[level].pop(randint(0, quiz_len))


def solve_quiz(chosen_quiz):
    """
    Present a quiz question to the player and check the answer.

    :param chosen_quiz: a dictionary containing a quiz question, select options, and the correct answer
    :precondition: chosen_quiz must have keys 'question', 'options', and 'answer',
                   where 'question' is a string, 'options' is a list of strings, and 'answer' is a string
    :postcondition: inform the player whether they have answered correctly
    :return: True if the player's answer matches the correct answer, otherwise False
    """
    question = chosen_quiz["question"]
    options = chosen_quiz["option"]
    answer = chosen_quiz["answer"]

    # print question and options
    print("You've encountered a quiz challenge! 🧠\n")
    print(f"Question 🧐❔\n{question}")
    for option in options:
        print(option.strip())
    print("")

    while True:
        print("Enter Your Answer🖌")
        user_answer = input(">> ").strip()
        if user_answer not in ['1', '2', '3']:
            print("Please enter 1, 2, or 3.")
            continue
        elif user_answer == answer:
            print()
            print("You are right! Your HP increased! 🥳")
            return True
        else:
            print(f"Oops!😲 Wrong Answer! The answer was {answer}.")
            print("")
            return False


def check_for_quiz(character, luck_stat):
    """
    Determine if the character encounters a quiz based on luck stat of player's class and character's current HP.

    :param character: a dictionary representing the player's character
    :param luck_stat: an integer representing the character's luck attribute
    :precondition: character must have 'current_hp' and 'max_hp' keys with integer values, luck_stat must be an integer
    :return: True if a randomly selected number within a range falls below the character's luck-adjusted chance,
             otherwise False
    """
    base_chance = 15

    # If luck_stat is 5, increase chance to 25
    if luck_stat == 5:
        base_chance = 25

    #  Check for a quiz
    #  If the character's current HP are at their maximum, no quiz for sure
    if not (character["current_hp"] == character["max_hp"]):
        there_is_a_quiz = randint(1, 100)  # Use a range from 1 to 100 for percentage
        if there_is_a_quiz <= base_chance:
            return True
    return False


def main():
    pass


if __name__ == "__main__":
    main()
