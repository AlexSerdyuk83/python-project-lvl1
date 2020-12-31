import prompt


def welcome_user():
    """The function asks for the user's name, displays
    a welcome message, and returns the name"""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
