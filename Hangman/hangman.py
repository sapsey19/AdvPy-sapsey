import random

def find_all(string, substring):
    start = 0
    while(1):
        start = string.find(substring, start)
        if(start == -1):
            return
        yield start                 #credit to https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring for help with yield
        start += len(substring)

f = open('words.txt', 'r')
wordList = f.read().split('\n')
word = random.choice(wordList)
<<<<<<< HEAD
guesses, usedWords = list(), list()

dashes = ''
for i in range(0, len(word)):
    dashes += '-'                   #creates a dashes version of the word

r = open('hangmanPics.txt', 'r')
hangmanPics = r.read().split(',')   #inits ascii hangman pictures, credit to https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c for the ascii art
state = 0                           #state, or stage of the game. Effectively the 'lives'

while(1): 
    print(hangmanPics[state])
    print(dashes)
    print ('Letters tried: ', ', '.join(guesses))
=======
guesses = list()
dashes = ''
for i in range(0, len(word)):
    dashes += '-'
print(word)
print(dashes)
i = 6
while(i > 0):  
    print('You have ', i, ' guesses left.')
>>>>>>> 995b7bfaa51f34018eeee339b7b67d7405b697ed
    guess = input('Enter a guess: ')
    print('\n')
    if(len(guess) > 1):
        print('Please only enter one character at a time. Try again.')
<<<<<<< HEAD
        continue      
    if(guess in word):
        if(guess in usedWords):
             print('You already got "{}"! Pick another letter.'.format(guess))
             continue
        occurences = list(find_all(word, guess))
        for i in range(0, len(occurences)):
            dashes = dashes[:occurences[i]] + guess + dashes[occurences[i]+1:]
        print('Correct!')
        usedWords.append(guess)      
    else:
        if(guess in guesses):
            print('Already tried "{}". Try again.'.format(guess))
            continue
        guesses.append(guess)
        print('Incorrect.')
        state += 1
    if(dashes == word):
        print('\n')
        print('Congratulations, you won! The word was: "{}"'.format(word))
        break
    if(state == 6):
        print(hangmanPics[6])
        print('Sorry, game over. The word was: "{}"'.format(word))        
        break
print('\n')
input('Thanks for playing! Press any key to quit.')
=======
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


    
>>>>>>> 995b7bfaa51f34018eeee339b7b67d7405b697ed
