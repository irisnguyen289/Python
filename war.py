"""
File: war.py
Author: Iris Nguyen
Description: A game that player/user and computer have a card chosen
             randomly. The winner is the one who has a larger number
             card with A=1, J=11, Q=12, K=13. When the result is tie,
             the program will choose other cards for each player
             immediately until there is one winner and all the cards
             in the tie round are counted towards the winner's total
             scores.
"""
import random
print("Welcome to the game of war.")

uWin = 0
cWin = 0
uScore = 0
cScore = 0

myDict = {1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:\
          "J", 12:"Q", 13:"K"}

while True:
    task = input("Press e to Exit, p to Play, and s to show Score. ")
    ## check what the player wants to do
    if task == "p" or task == "P" or task == "s" or task == "S":
        True
    elif task == "e" or task == "E":
        print("Thank you for playing!")
        print("Goodbye!")
        break
    else:
        print("Invalid input.")

    ## player presses p (play)           
    if task == "p" or task == "P":
        u = random.randint(1,13)
        c = random.randint(1,13)
        ## tie situation
        tie = 0
        while u == c:
            tie = tie + 2 * u
            print()
            print("We tied.")
            print("Better go again...")
            print("You had:", myDict[u])
            print("Computer had:", myDict[c])
            u = random.randint(1,13)
            c = random.randint(1,13)
        ## player wins
        if u > c:
            print()
            print("You won!")
            uWin += 1
            uScore = uScore + u + c + tie
        ## computer wins
        elif u < c:
            print()
            print("Computer won.")
            cWin += 1
            cScore = cScore + u + c + tie
        ## number to A, J, Q, K output
        print("You had:", myDict[u])
        print("Computer had:", myDict[c])
        print()

    ## player presses s (show round win and score)       
    if task == "s" or task == "S":
        print()
        print("Your round wins:", uWin)
        print("Computer round wins:", cWin)
        print("Your card score:", uScore)
        print("Computer card score:", cScore)
        print()

