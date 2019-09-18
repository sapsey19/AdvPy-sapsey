import random

def find_all(string, substring):
    start = 0
    while(1):
        start = string.find(substring, start)
        if(start == -1):
            return
        yield start                 #credit to https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring for help with yield
        start += len(substring)
def reInit(word, dashes, gueses, usedWords):    
    word = random.choice(wordList)
    guesses.clear()
    usedWords.clear()
    dashes = ''
    for i in range(0, len(word)):
        dashes += '-' 
    return word, dashes, guesses, usedWords

f = open('words.txt', 'r')
wordList = f.read().split('\n')
word = random.choice(wordList)
guesses, usedWords = list(), list()

dashes = ''
for i in range(0, len(word)):
    dashes += '-'                   #creates a dashed version of the word

r = open('hangmanPics.txt', 'r')
hangmanPics = r.read().split(',')   #inits ascii hangman pictures, credit to https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c for the ascii art
state = 0                           #state, or stage of the game. Effectively the 'lives'

while(1):   
    if(dashes == word):
        print('\n')
        print('Congratulations, you won! The word was: "{}"'.format(word))
        temp = input('If you want to play again, type "p". If you want to quit, type "q" ')
        if(temp == 'p'):
            state = 0
            word, dashes, guesses, usedWords = reInit(word, dashes, guesses, usedWords)           
            continue
        elif(temp == 'q'):            
            break
    if(state == 6):                 #fail state
        print(hangmanPics[6])
        print('Sorry, game over. The word was: "{}"'.format(word))   
        temp = input('If you want to play again, type "p". If you want to quit, type "q" ')
        if(temp == 'p'):
            state = 0
            word, dashes, guesses, usedWords = reInit(word, dashes, guesses, usedWords)            
            continue
        elif(temp == 'q'):
            break
    print(hangmanPics[state])
    print(dashes)
    print ('Letters tried: ', ', '.join(guesses))
    guess = input('Enter a guess: ')
    if(guess == ''):
        print('Please enter a character.')
        continue
    guess = guess.lower()
    print('\n')
    if(len(guess) > 1):
        print('Please only enter one character at a time. Try again.')
        continue    
    if(guess in usedWords):
        print('You already got "{}"! Pick another letter.'.format(guess))
        continue
    if(guess in word):    
        occurences = list(find_all(word, guess))
        for i in range(0, len(occurences)):
            dashes = dashes[:occurences[i]] + guess + dashes[occurences[i]+1:]      #replaces dashes with appropriate letter(s)
        print('Correct!')
        usedWords.append(guess)
        continue
    else:
        if(guess in guesses):
            print('Already tried "{}". Try again.'.format(guess))
            continue
        guesses.append(guess)
        print('Incorrect.')
        state += 1   

input('Thanks for playing! Press any key to quit. ')