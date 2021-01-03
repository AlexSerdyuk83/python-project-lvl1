from random import randint, choice


def get_random_int(start, stop):
    """The function returns a random number in the specified range"""
    return randint(start, stop)


def get_random_operator(list_operator):
    """Returns a random element of the passed sequence"""
    return choice(list_operator)
