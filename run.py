import random
from words import words_list

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

guess_word = random.choice(words_list)
secret_word = []
for i in range(0, len(guess_word)):
    secret_word.append(guess_word[i])
word_space = []
for i in secret_word:
    word_space.append('_')
guess_letters = []
tries = 0     


def gallows_pole_area(tries):
    if tries == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif tries == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")

def guess_input():
    """
    This function is for the player to input a letter in order to try and guess the word
    """

    while True:
        player_input = input("Guess A Letter: ")
        if player_input in alphabet:
            if player_input in guess_letters:
                print("You Have Already Guessed That Letter, Try Again")
            else:
                guess_letters.append(player_input)
                if player_input in secret_word:
                    print("Excellent! You Guessed A Correct Letter")
                    for i in range(0, len(secret_word)):
                        if secret_word[i] == player_input:
                            word_space[i] = player_input
                else:
                    print("Wrong! That Letter Is Not In This Word")
                    tries = tries + 1

        else:
            print("You Need To Input A Valid Character... A Letter")

        if tries > 5:
            gallows_pole_area(tries)
            break
        elif "_" in word_space:
            gallows_pole_area(tries)
        else:
            gallows_pole_area(-1)
            break

