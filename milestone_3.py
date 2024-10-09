
import random as rnd

# Secret word list and randomly choosing one
words = ['apple', 'banana', 'grape', 'orange', 'mango']
secret_word = rnd.choice(words)

# Define the check_guess function
def check_word(guess):
    
    '''
    Function to check if the guess letter is in the secret list of words.
    :param guess: the letter guessed by the user
    '''
# Converts the guess to lower case 

    guess = guess.lower()

# Checks if the guess is in the secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():

    """
    Function to prompt the user for input and validate the guess.
    Calls the check_guess function to check if the guess is in the word.
    """

    while True:
        # Ask the user to guess a letter of the word
        guess = input('Please Guess a Letter of the Secret Word: ')

        if len(guess) == 1 and guess.isalpha():
            # Call check_guess to validate the guess
            check_word(guess)
            break
        else:
            # Outputs invalid input
          print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to run the game
ask_for_input()


