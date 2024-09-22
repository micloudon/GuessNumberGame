# Guess a random number between 1 - 10
# number must be guessed in 3 guesses
# On each unsuccessful guess a less than or greater than is given

# Take in user input (number 1 - 10)
    # Validate user input; user input must be a number between 1-10
# Generate a random number between 1 - 10
# Compare a users guess to users Generated number, 
    # determine if it is greater or less than the users guess
    # If the user guesses the number, declare the game a win and end the game
#Count the number of times a user has guessed, 
    # declare the game a loss and end the game if they guess more than 3 times
#Output the gamestate
    # number of guesses left
    # a victory or a loss
    # The success of a guess
        # If a guess is greater than or less than the number
#Control the flow of the program
    # quiting the program in a loss or victory event
    # repeating input prompts in the event of an invalid input
    # repeating input prompts in the event of an invalid guess

import random

randnum = random.randrange(1, 11)
guessesLeft = 4


# print(randnum)
# guess = input()
# print(type(guess))
# print(parm)

def verifyEntry():
    while True:
        print("randnum: ",randnum)
        parm = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        guess = input("Enter a number between 1 - 10: ")
        print("you guessed :", guess)
        if guess in parm:
            guess = int(guess)
            # break
            return guess
        else:
            print("invalid entry, enter a number between 1 - 10")

# guess = verifyEntry()
# print("randnum: ",randnum)
# print("randnum type: ",type(randnum))


def checkGuess(guess):
    if guess == randnum:
        print("you win")
        return
    if guess > randnum:
        print("Too high")
        return driver()
    if guess < randnum:
        print("Too low")
        return driver()
    # guessesLeft -= 1



def driver():
    v = verifyEntry()
    global guessesLeft
    guessesLeft = guessesLeft - 1
    print("Guesses Left: ", guessesLeft)
    if guessesLeft <= 0:
        return print("You lose :(")
        
    checkGuess(v)
    

driver()

    


