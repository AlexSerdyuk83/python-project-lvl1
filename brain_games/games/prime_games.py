import prompt
from brain_games.cli import welcome_user
from brain_games.random import get_random_int
from brain_games.question import get_question_for_even
from brain_games.task import task_description_for_prime_games
from brain_games.is_correct_answer import is_correct_answer
from brain_games.opposite import get_opposite_answer
from brain_games.answer import get_answer_for_user
"""Implementation of the logic of the game brain-prime.
The user should be a Prime number or not"""


def is_prime(num):
    """the function returns True if the number is prime and False if not"""
    i = 2
    while num % i != 0:
        i += 1
    return i == num


def get_prime_games():
    count = 0
    limit = 3
    start = 1
    stop = 100
    name = welcome_user()
    task_description_for_prime_games()
    while count < limit:
        random = get_random_int(start, stop)
        get_question_for_even(random)
        answer = prompt.string('Your answer: ')
        if is_correct_answer(is_prime, random, answer):
            print('Correct!')
            count += 1
        else:
            get_answer_for_user(answer, get_opposite_answer(answer), name)
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
