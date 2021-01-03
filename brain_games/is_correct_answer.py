def is_correct_answer(function, num, string):
    """The function checks the user's response and returns
    True if it is correct, and False if it is not"""
    result = function(num)
    return result and string == 'yes' or not result and string == 'no'
