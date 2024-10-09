import random as rnd

word_list = ['Apple', 'Banana', 'Mango', 'Grapes', 'Cherry']
word = rnd.choice(word_list)
guess = input(str('Enter a single letter of your word: '))

if len(guess) == 1 and guess.isalpha():
    print('Good Guess')

else:
    print('Oops! That is not a valid input.')
