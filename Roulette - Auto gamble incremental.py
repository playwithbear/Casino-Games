# ROULETTE - AUTO-GAMBLE - INCREMENTAL
#
# Key attributes:
# 1. Ask a player for number of loops required
# 2. Incrementally increase bet by 1.5 if win.
# 3. Initial balance is 0 to easily identify gains/losses.
# 
# NB. This roulette generator only assumes a bet on one of the evens i.e. red of black to test a gambling strategy

# Import modules
import random

# Initialise game
balance = 0
initialbet = 10
bet = initialbet
betcount = 1

print("Welcome to The Oversimplified Roulette Machine - Auto-Gambling Mode")
print("This game will assume you always bet on evens.")
loopcount = int(input("How many loops do you want to test? "))

# Game loop
for lp in range(loopcount):

    # Take bet from balance
    print("\nBet number " + str(betcount))
    print("Current balance: " +str(balance))
    print("Current bet: " +str(bet))
    balance -= bet
    betcount += 1

    # Spin wheel
    result = random.randrange(36)

    # Assess winning
    if result == 0:
        # i.e. no winning or losing
        balance += bet 
        print("Zero. Player stands.")
    elif result % 2 == 0:
        # Result is even
        balance += (bet*2)
        print("Congratulations, you win.")
        bet = round(bet * 1.5)
    else:
        # You lose
        print("Sorry, you lose.")
        bet = initialbet

# Inform player of results
print("\nThank you for using The Oversimplified Roulette Machine - Auto-Gambling Mode")
print("\nAfter " + str(loopcount) + " bets on the roulette wheel, your final balance is: " + str(balance))

input("\nPress any key to exit.")