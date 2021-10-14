# Import generating random word
import random
from words import words


# Input name message
# Generates a welcome message with explanation of rules
# Start game button is below list of rules
player_name = input("Please enter your name:")
print("Welcome + player_name, read the rules below then hit the start button to begin")




# Computer generates random word from a list

def get_random_word(random):
    """This function generates the word that needs to be guessed """

    word = random.choice(words)

return word


def game():
    word = get_random_word(words) 
    word_letters = letter(word) #letters in the word
    used_letters = letter() #letters the user has guessed
    letters = ('abcdefghijklmnopqrstuvwxyz')
    tries = 5 #number of tries the user has to guess word
    