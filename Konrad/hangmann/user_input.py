"""
This function takes string as argument - it may be an input function
If a letter is given it returns this letter in lowercase
If it is not, it returns one of two numbers, which are different for further decisions
For instance 1 means that value is not alphabetical
Then 2 means that string is not a letter but letters
"""


def user_input_letter(given_string):
    not_alpha = 1
    too_long = 2
    if len(given_string) == 1:
        if given_string.isalpha():
            return given_string.lower()
        return not_alpha
    return too_long
