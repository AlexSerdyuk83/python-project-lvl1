import prompt
from brain_games.cli import welcome_user
from brain_games.random import get_random_int
from brain_games.question import get_question_for_even
from brain_games.task import task_description_for_even_games
from brain_games.is_correct_answer import is_correct_answer
"""Realization of the logic of the game brain-even.
The user must surmise the parity of the number"""


def is_even(num):
    """The function checks the number for parity and returns
    True if the number is even and False if it is not"""
    return num % 2 == 0


def get_check_parity():
    count = 0
    limit = 3
    start = 1
    stop = 100
    name = welcome_user()
    task_description_for_even_games()
    while count < limit:
        random = get_random_int(start, stop)
        get_question_for_even(random)
        answer = prompt.string('Your answer: ')
        if is_correct_answer(is_even, random, answer):
            print('Correct!')
            count += 1
        else:
            print('Sorry! This is the incorrect answer! Please, try again!')
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
