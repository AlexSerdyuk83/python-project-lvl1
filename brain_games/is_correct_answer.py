def is_correct_answer(function, num, string):
    """The function checks the user's response and returns
    True if it is correct, and False if it is not"""
    return (function(num) and string == 'yes' or
            not function(num) and string == 'no')
