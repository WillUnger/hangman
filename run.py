import random
from words import word_list

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
    

def guess_input():

    while True:
        player_input = input("Guess A Letter: ")
        if player_input in alphabet:
            if player_input in guess_letters:
                print("You Have Already Guessed That Letter, Try Again")
           


