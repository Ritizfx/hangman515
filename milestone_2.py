import random as rnd

word_list = ['Apple', 'Banana', 'Mango', 'Grapes', 'Cherry']
word = rnd.choice(word_list)

while True:
    guess = input('Enter a single letter: ')

    if len(guess) == 1 and guess.isalpha():
        print('Good Guess!')
    break
    
    else:
    print('Opps! That is not a valid input')
    


