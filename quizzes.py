"""
Add Docstring
"""
import json
from random import randint


def create_quizzes():
    quiz_file = "game_data/quiz.json"
    with open(quiz_file, encoding="utf-8") as quiz_json:
        quizzes = json.load(quiz_json)
    return quizzes


def select_quiz(quizzes, level):
    quiz_len = len(quizzes[level]) - 1
    if int(level) <= 5 and quiz_len != -1:
        return quizzes[level].pop(randint(0, quiz_len))


def solve_quiz(chosen_quiz):
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
        user_answer = input("Enter your answer >>>").strip()
        if user_answer not in ['1', '2', '3']:
            print("Please select 1, 2, or 3.")
            continue
        elif user_answer == answer:
            print("You are right! You get 1 HP 🥳")
            print("")
            return True
        else:
            print(f"Oops! The answer is {answer}")
            print("")
            return False


def check_for_quiz(character):
    #  25% of chance to get a quiz
    if not(character["current_hp"] == character["max_hp"]):
        there_is_a_quiz = randint(1, 4)
        if there_is_a_quiz == 2:
            return True
        else:
            return False
    else:
        return False


def main():
    pass


if __name__ == "__main__":
    main()
