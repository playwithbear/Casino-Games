# Basic Roulette Mechanics
#
# Key attributes:
# 1. Provide a player with a balance
# 2. Take a player bet
# 3. 'Spin' Roulette wheel
# 4. Return result to player and update balance if necessary with winnings
# 
# NB. This roulette generator only assumes a bet on one of the evens i.e. red of black to test a gambling strategy

# Import modules
import random

# Initialise game
balance = 1000
playing = "y"

print("Welcome to The Oversimplified Roulette Machine.")
print("This game will assume you always bet on evens.")
print("Your current balance is: " + str(balance))

# Game loop
while playing == "y":

    # Take bet
    bet = int(input("\nHow much would you like to bet? "))

    balance -= bet

    # Spin wheel
    result = random.randrange(36)
    print("The result is: " + str(result))

    # Assess winning
    if result == 0:
        # i.e. no winning or losing
        balance += bet 
        print("\nZero. Player stands.")
    elif result % 2 == 0:
        # Result is even
        balance += (bet*2)
        print("\nCongratulations, you win " + str(bet*2))
    else:
        # You lose
        print("\nSorry, you lose.")

    # Inform player of their current balance
    print("\nYour current balance is: " + str(balance))

    # Invite to play again
    playing = str.lower(input("\nWould you like to play again? Y/N: "))

input("\nThank you for playing The Oversimplified Roulette Machine. \nPress any key to exit.")