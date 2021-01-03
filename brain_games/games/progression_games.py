import prompt
from random import randint
from brain_games.cli import welcome_user
from brain_games.question import get_question_for_even
from brain_games.answer import get_answer_for_user
from brain_games.task import task_description_for_progression
from brain_games.random import get_random_int
"""Realization of the logic of the game brain-progression.
The user must guess the number missing in the given arithmetic progression"""


def get_creates_progression_list(start, stop, step, len_prog=10):
    """creates an arithmetic progression of a given length and step"""
    return list(range(start, stop, step))[:len_prog]


def get_replacing_number(list_num, start=0, stop=9):
    """in a given list range, replaces an element at an
    random position with two points"""
    position = randint(start, stop)
    element = list_num.pop(position)
    list_num.insert(position, '..')
    return list_num, element


def get_creates_progression_string(li):
    """converts a list to a string"""
    result = ''
    for item in li:
        result += '{} '.format(item)
    return result


def get_progression_games():
    count = 0
    limit = 3
    name = welcome_user()
    task_description_for_progression()
    while count < limit:
        start = get_random_int(1, 40)
        stop = get_random_int(60, 100)
        step = get_random_int(2, 4)
        progression_list = (
            get_creates_progression_list(start, stop, step)
        )
        riddle_list, element = get_replacing_number(progression_list)
        result_progression = get_creates_progression_string(riddle_list)
        get_question_for_even(result_progression)
        answer = prompt.string('Your answer: ')
        answer = int(answer)
        if element == answer:
            print('Correct!')
            count += 1
        else:
            get_answer_for_user(answer, element, name)
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
