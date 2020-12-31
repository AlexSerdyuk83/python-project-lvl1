import prompt
from random import randint
from brain_games.cli import welcome_user
"""Realization of the logic of the game brain-even.
The user must surmise the parity of the number"""


def task_description():
    """The function displays a description of the task"""
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(task)


def get_random_int():
    """The function returns a random number in the specified range"""
    rand_int = randint(1, 40)
    return rand_int


def get_question(num):
    """The function displays a question"""
    print('Question: {}'.format(num))


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
        get_question(random)
        answer = prompt.string('Your answer: ')
        if is_correct_answer(random, answer):
            print('Correct!')
            count += 1
        else:
            print('Sorry! This is the incorrect answer! Please, try again!')
            break
    if count == 3:
        print('Congratulations, {}'.format(name))
