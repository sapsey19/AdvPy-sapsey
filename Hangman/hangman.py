import random

f = open('words.txt', 'r')
wordList = f.read().split('\n')
word = random.choice(wordList)
guesses = list(range())
i = 0
tries = 6
print(word)
while(i < 6): 
    guess = input('Enter one character to guess: ')
    if(len(guess) > 1):
        print('I said enter ONE character... Try again.')
        continue
    else:
        guess = guess.lower()
    if(guess in word):
        print ('correct')
    else:
        guesses = guess
        print ('Incorrect. Letters tried: ', guesses)
        print ('Attempts remaining: ', tries)        
        i += 1
        tries -= 1





















