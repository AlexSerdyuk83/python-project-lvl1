from random import randint, choice


def get_random_int():
    """The function returns a random number in the specified range"""
    rand_int = randint(1, 10)
    return rand_int


def get_random_operator(list_operattor):
    return choice(list_operattor)
