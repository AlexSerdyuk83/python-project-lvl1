import prompt
from brain_games.cli import welcome_user
from brain_games.random import get_random_int
from brain_games.question import get_question_for_even
"""Realization of the logic of the game brain-even.
The user must surmise the parity of the number"""


def task_description():
    """The function displays a description of the task"""
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(task)


def is_even(num):
    """The function checks the number for parity and returns
    True if the number is even and False if it is not"""
    return num % 2 == 0


def is_correct_answer(num, string):
    """The function checks the user's response and returns
    True if it is correct, and False if it is not"""
    return ((is_even(num) and string == 'yes')
            or (not is_even(num) and string == 'no'))


def get_check_parity():
    count = 0
    limit = 3
    name = welcome_user()
    task_description()
    while count < limit:
        random = get_random_int()
        get_question_for_even(random)
        answer = prompt.string('Your answer: ')
        if is_correct_answer(random, answer):
            print('Correct!')
            count += 1
        else:
            print('Sorry! This is the incorrect answer! Please, try again!')
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
