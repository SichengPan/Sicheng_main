'''
How to play Hangman: https://www.wikihow.com/Play-Hangman
'''

from operator import truediv
from random import randint
import time, os

'''These pictures are from: https://github.com/imwithye/Hangman-in-Python/blob/master/Hangman.py'''
def hangmanInterface(index):
    if index==0:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('        /|\  | ')
            print('        / \  | ')
            print('             | ')
            print('     ________|_')
            return
    if index==1:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('        /|\  | ')
            print('        /    | ')
            print('             | ')
            print('     ________|_')
            return
    if index==2:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('        /|\  | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==3:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('        /|   | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==4:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('         |   | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==5:
            print('         _____ ')
            print('         |   | ')
            print('         O   | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==6:
            print('         _____ ')
            print('         |   | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==7:
            print('         _____ ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==8:
            print('               ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('             | ')
            print('     ________|_')
            return
    if index==9:
            print('               ')
            print('               ')
            print('               ')
            print('               ')
            print('               ')
            print('               ')
            print('     ________|_')
            return

def setWordLength(diff_level):
    word_length = 0
    if (diff_level == 1):
        word_length = int(input("Enter a number longer than 10 to choose the word length: "))
        while (word_length <= 10):
            word_length = int(input("Enter a number longer than 10 to choose the word length: "))

    elif (diff_level == 2):
        word_length = int(input("Enter a number ranging from 6 to 9 to choose the word length: "))
        while (word_length > 9 or word_length < 6):
            word_length = int(input("Enter a number ranging from 6 to 9 to choose the word length: "))

    elif (diff_level == 3):
        word_length = int(input("Enter a number lower than or equal to 5 to choose the word length: "))
        while (word_length > 5 or word_length <= 0):
            word_length = int(input("Enter a number lower than or equal to 5 to choose the word length: "))

    print(word_length)
    return word_length


def word_Selector():
    fhandler = open("words.txt", "r") # you can replace it with any file consisting English words you want
    lines = fhandler.readlines() # readlines read all lines in a file, and stores them in a list
    # We just need to operate on a list as followes
    lines_num = len(lines)
    word_index = randint(0, lines_num-1)
    word = lines[word_index].strip()
    return word

def difficulty_level_selector():
    word = ""
    print("Enter a difficulty level.")
    print("If you enters 1, the chosen word is longer than 10 characters.")
    print("If you enters 2, the chosen word is of length 6-9 characters.")
    print("If you enters 3, the chosen word is of length 5 or less characters.")
    diff_level = int(input("Enter the number of the difficulty level here: "))

    while (diff_level>3 or diff_level<=0):
        diff_level = int(input("Enter the number of the difficulty level here: "))

    if (diff_level == 1):
        word_length = setWordLength(diff_level)
        word = word_Selector()
        count = 0
        while (len(word) != word_length):
            word = word_Selector()
            count += 1
            if (count > 100):
                word_length = setWordLength(diff_level)

    elif (diff_level == 2):
        word_length = setWordLength(diff_level)
        word = word_Selector()
        while (len(word) != word_length):
            word = word_Selector()

    elif (diff_level == 3):
        word_length = setWordLength(diff_level)
        word = word_Selector()
        while (len(word) != word_length):
            word = word_Selector()

    return word



def answer_start_generator(word):
    answer = ""
    for i in range(0,len(word)):
        answer = answer + "_"
    return answer

def guess_the_word(word):
    count = 0
    win = False
    guesses = ""
    answer = answer_start_generator(word)

    while (count < 10 and win == False):
        count += 1
        guess = input("Enter guess " + str(count) + ": ")
        guesses = guesses + guess
        tmp = ""
        i = 0

        while (i<len(word)):
            if (word[i] == guess):
                tmp = tmp + guess
            else:
                tmp = tmp + answer[i]
            i += 1

        index = 10 - count
        print()

        if (answer != tmp):
            print("Good guess.")
            print("You move a step forward to save Hangman.")
            count -= 1
            answer = tmp
        else:
            print("Not a good guess.")
            print("The situation gets worse.")

        if (answer == word):
            print("Well done you win! Hangman is saved!")
            win = True

        print("Now the Hangman situation is: ")
        hangmanInterface(index)
        print()
        print(str(10-count)+"/10 guesses left.")
        print("your guesses: "+ guesses)
        print("The word so far: "+answer)
        print("======================================================================")
        print()

        # if the user fails, show the answer
        if (count == 10 and win == False):
            print("The man is dead.")
            print("You failed, try better next time.")
            print("The intended word is: " + word)

'''main algorithm of the game'''
play = True
name = os.getlogin()

print("Hello " + name + " let's play Hangman!")
print("Loading ... ")
print()
time.sleep(2)

while (play):
    word_chosen = difficulty_level_selector()
    guess_the_word(word_chosen)

    # ask if the user wants to re-play
    choice = input("Do you want to play again? [y/n]: ")
    while (choice != "y" and choice != "n"):
        choice = input("Do you want to play again? [y/n]: ")

    if (choice == "y"):
        play = True
    else:
        play = False









