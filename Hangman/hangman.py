import random

f = open('words.txt', 'r')
wordList = f.read().split('\n')
word = random.choice(wordList)
guesses = list()
dashes = ''
for i in range(0, len(word)):
    dashes += '-'
print(word)
print(dashes)
i = 6
while(i > 0):  
    print('You have ', i, ' guesses left.')
    guess = input('Enter a guess: ')
    print('\n')
    if(len(guess) > 1):
        print('Please only enter one character at a time. Try again.')
        continue  
    if(guess in word):    
       dashes = dashes[:word.find(guess)] + guess + dashes[word.find(guess)+1:]
       print('Correct! ', dashes)
       print('\n')
    else:
        guesses.append(guess)            
        print ('Incorrect. Letters tried: ', ', '.join(guesses))
        print(dashes)
        i -= 1;
    if(dashes == word):
        print('Congratulations, you won!')
        break
    if(i == 0):
        print('Sorry, game over.')










#print out all dashes that represents the word to guess
#print out how many guesses the user has remaining
#read in a guess
#if the guess is in the word
    #replace the dashes with the appropriate letter/s
#else 
    #print out that the guess is not in the word, take away an attemp








# print(word)
# while(i < 6):
#     toDashes(word)
#     guess = input('Enter one character to guess: ')
#     if(len(guess) > 1):
#         print('I said enter ONE character... Try again.')
#         continue
#     else:
#         guess = guess.lower()
#     if(guess in word):
#         print ('correct')
#     else:
#         if(guess in guesses):
#             print('Already tried ', guess, ', pick another letter.')
#             continue
#         guesses.append(guess)
#         print ('Incorrect. Letters tried: ', ', '.join(guesses))
#         print ('Attempts remaining: ', tries-1)        
#         i += 1
#         tries -= 1


    