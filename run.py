# Import generating random word
import random
from words import words


# Input name message
# Generates a welcome message with explanation of rules
# Start game button is below list of rules
player_name = input("Please enter your name:")
print("Welcome + player_name, read the rules below then hit the start button to begin")


# Hangman area is generated - This is where an illustration of the hangman is built with every
# incorrect letter that is guessed

# Computer generates random (hidden) word from a list, all below the hangman area

# Player guesses the letter from a keyboard provided

# If letter is contained in the word then letter fills the blank of
# where it appears within the word

# If letter is not contained in the word then that letter is blanked out on the keyboard and player loses 
# a try (total 5 tries)

# If full word is guessed, message appears, f"Congratulations {player_name}! You guessed the correct word"
# Play again? - Button below - Restarts game

# If numbers of tries is < 1 then message appears, f"Sorry {player_name}...You died!"
# Play again? - Button below - Restarts game
