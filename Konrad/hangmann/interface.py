"""
The console interface is used to run this program
During the game loop program creates an game object - the WordHangman class object,
then it runs the game using created object. If player win, or loose, inner loop ends
And destructor of class returns information about score, and word to guess
The endgame screen is shown for 5 seconds, and then next round begins.

"""
import class_word
import user_input
from time import sleep

while True:
    word = class_word.WordHangman()
    while not word.number_of_remaining_fails == 0:
        print('\n')
        print(*word.word_to_guess_public)
        print("Score is: " + str(word.score))
        print("You still have: " + str(word.number_of_remaining_fails) + " chances")
        print("You have typed these letters already: ")
        print(*word.already_given)
        Letter = user_input.user_input_letter(input("Guess a letter: "))
        if Letter == 1:
            print("Sorry, it's not a letter")
        elif Letter == 2:
            print("Sorry, string too long, or blank")
        else:
            word.check_if_input_in(Letter)
        if '.' not in word.word_to_guess_public:
            break
    print(word.word_to_guess_private)
    print("Game over")
    if word.number_of_remaining_fails != 0:
        print("You won")
    else:
        print("You lose")
    print("Score: " + str(word.score))
    sleep(5)
    print('\n' * 30)
