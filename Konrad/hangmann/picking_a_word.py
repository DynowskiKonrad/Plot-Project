from dictionary import dictionary
from random import randint


def picking_a_word():
    length = len(dictionary)
    return dictionary[randint(0, length) - 1].lower()
# returns random string from dictionary
