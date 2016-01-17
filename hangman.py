#Hangman
#chra94

import random

#wordList = ['football', 'america', 'internet', 'boston'] #List of words for Hangman
#secretWord = wordList[random.randint(0, (len(wordList)-1))] #Selects random word from list
secretWord = 'car' #for testing purposes
#print(secretWord)
correctGuess = []
for i in secretWord:
    correctGuess.append('_')
wrongGuess = []
wrongGuesses = 0
print('Welcome to hangman. You are going to figure out what the secret word is by guessing letters. You can guess wrong 10 times.')
print('The word has this many letters : ' + str(correctGuess))
while wrongGuesses <= 9: #Until 10 wrong guesses by user
    guess = input('Guess a letter.\n') #Makes the user guess a letter.
    #if guess in wrongGuess or correctGuess:
    #    print('Already guessed.')
    if guess in secretWord: #for correct guesses
        print('Correct')
        correctGuess.insert(secretWord.index(guess), guess) ##replaces guess with '_'
        del correctGuess[(secretWord.index(guess) + 1)] #deletes the space to the right of the newly insertet letter
        print(correctGuess)
        if '_' not in correctGuess: #If there are equally many characters in correctGuess and wrongGuess the word is guessed
            break
    elif guess not in secretWord: #for wrong guesses
        print('Wrong')
        wrongGuess.append(guess)
        print('Letters not in the word: ' + str(wrongGuess))
        wrongGuesses += 1
        print('Guesses left: ' + str(10 - wrongGuesses))
if '_' not in correctGuess:
    print('You won!')
else:
    print('You lost :(')
