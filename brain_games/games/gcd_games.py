import prompt
from brain_games.cli import welcome_user
from brain_games.random import get_random_int
from brain_games.question import get_question_for_gcd
from brain_games.answer import get_answer_for_user
from brain_games.task import task_description_for_gcd
"""Realization of the logic of the game brain-gcd.
The user must calculate the greatest common divisor
of two given numbers"""


def get_gcd(num1, num2):
    """the function gets two numbers and returns the greatest common divisor"""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_gcd_games():
    count = 0
    limit = 3
    start = 2
    stop = 40
    name = welcome_user()
    task_description_for_gcd()
    while count < limit:
        random_int1 = get_random_int(start, stop)
        random_int2 = get_random_int(start, stop)
        result = get_gcd(random_int1, random_int2)
        get_question_for_gcd(random_int1, random_int2)
        answer = prompt.string('Your answer: ')
        answer = int(answer)
        if result == answer:
            print('Correct!')
            count += 1
        else:
            get_answer_for_user(answer, result, name)
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
