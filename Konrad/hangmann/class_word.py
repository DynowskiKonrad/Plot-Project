"""
This class is written for game purpose. It is designed for console interface, although only
class does not use console directly.

During creating a class the __init__ method is called. It creates class objects:
    - The word to display - as dots, and during a game as letters
    - The given letter table, which collects data about given letters
    - Score - integer value which will grow as player will guess correctly and will
      decrease whenever player inputs same letter again (already given will be visible)
    - The number of fails is maximum amount of mistakes during game loop and depends on word length
    - length of word is a tuple, because it will be used only to determine number of rounds in loops

Method check_if_input_in checks if its argument was already given, and if it is in word to guess
It is designed for string inputs. This method appends letter to already given, affects score, and
the number of remaining fails.
"""

import picking_a_word


class WordHangman:
    def __init__(self):
        self.word_to_guess_public = []
        self.already_given = []
        self.score = 0
        self.word_to_guess_private = picking_a_word.picking_a_word()
        self.number_of_remaining_fails = len(self.word_to_guess_private) + 1
        self.length_of_word = range(len(self.word_to_guess_private))
        for i in self.length_of_word:
            self.word_to_guess_public.append('.')

    def check_if_input_in(self, given_input):
        if given_input in self.word_to_guess_private and given_input not in self.already_given:
            self.score += 10
            self.already_given.append(given_input)
            for i in self.length_of_word:
                if given_input == self.word_to_guess_private[i - 1]:
                    self.word_to_guess_public[i-1] = given_input
        elif given_input not in self.already_given:
            self.already_given.append(given_input)
            self.number_of_remaining_fails -= 1
        else:
            self.score -= 5
