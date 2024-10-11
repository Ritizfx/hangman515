import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))  # Number of unique letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Step 1: Define the check_guess method
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()
        
        # Check if the guess is in the word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            # Step 2: Loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Check if the letter matches the guess
                if letter == guess:
                    # Replace the corresponding "_" in word_guessed with the guess
                    self.word_guessed[i] = guess
            
            # Reduce the number of unique letters left to guess
            self.num_letters -= 1
            
            # Print the updated word_guessed list
            print(f"Current word: {' '.join(self.word_guessed)}")
            
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    # Step 2: Define the ask_for_input method
    def ask_for_input(self):
        while True:
            # Ask the user to guess a letter
            guess = input("Please guess a letter: ")
            
            # If the guess is not a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # If the guess has already been tried
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            # If the guess is valid and has not been tried yet
            else:
                # Call the check_guess method and pass the guess
                self.check_guess(guess)
                
                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)
                break

# Step 3: Test the code
word_list = ['apple', 'banana', 'grape', 'orange', 'mango']
game = Hangman(word_list)
game.ask_for_input()



