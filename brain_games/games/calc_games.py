import prompt
from brain_games.cli import welcome_user
from brain_games.random import get_random_int, get_random_operator
from brain_games.question import get_question_for_calc
from brain_games.answer import get_answer_for_user
from brain_games.task import task_description_for_calc
"""Realization of the logic of the game brain-calc.
The user must execute the operation"""


def is_equal(num1, num2):
    """the function compares two numbers and returns True,
    if they are equal and False, if they are not"""
    return num1 == num2


def operation_calc(num1, num2, operator):
    """the function takes two numbers and an operator, and
    returns the result of an expression using the operator"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def get_calc_result():
    count = 0
    limit = 3
    name = welcome_user()
    task_description_for_calc()
    while count < limit:
        random_int1 = get_random_int(1, 10)
        random_int2 = get_random_int(1, 10)
        random_operator = get_random_operator(['+', '-', '*'])
        result = operation_calc(random_int1, random_int2, random_operator)
        get_question_for_calc(random_int1, random_int2, random_operator)
        answer = prompt.string('Your answer: ')
        answer = int(answer)
        if is_equal(result, answer):
            print('Correct!')
            count += 1
        else:
            get_answer_for_user(answer, result, name)
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
