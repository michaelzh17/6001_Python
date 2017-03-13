# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lst = []
    for l in secretWord:
        for i in range(len(lettersGuessed)):
            if l == lettersGuessed[i]:
                lst.append(True)
                break
    if len(lst) == len(secretWord):
        result = True
    else:
        result = False
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    lst_secretWord = list(secretWord)
    for l in range(len(lst_secretWord)):
        flag = False
        for i in range(len(lettersGuessed)):
            if lst_secretWord[l] == lettersGuessed[i]:
                flag = True
                break
        if flag == False:
            lst_secretWord[l] = '_'
    word_guessed = ''.join(lst_secretWord)
    return word_guessed


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lettersGuessed_copy = lettersGuessed.copy()
    lst = list(letters)
    lst_copy = lst.copy()
    for l in lst:
        for i in lettersGuessed_copy:
            if l == i :
                lst_copy.remove(l)
                lettersGuessed_copy.remove(l)
                break
    letters_available = ''.join(lst_copy)
    return letters_available 
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    guess = 8
    lettersGuessed = []
    flag = False
    while guess > 0 and flag == False:
        print("------------")
        print("You have", guess, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess_letter = input('Please guess a letter: ')
        guess_letter_low = guess_letter.lower()
        #
        
        if guess_letter_low in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess_letter_low in secretWord:
            lettersGuessed.append(guess_letter_low)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            flag = isWordGuessed(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess_letter_low)
            guess -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
    print("------------")
    if flag == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")
            





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
