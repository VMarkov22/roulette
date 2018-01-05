# Roulette Game.
# Test Push.

import random

players = []
guesses = []
winning_number = random.randint(0, 36)
print("\nThe winning number is {}.".format(winning_number))

print("\n\t\t\t$$$$$$$$$$$$$$$$\n\t\t\t$$$ ROULETTE $$$\n\t\t\t$$$$$$$$$$$$$$$$")

num_players = int(input("\nEnter the number of players: "))

for i in range(0, num_players):
    players.append(str(input("\nEnter Player {}'s name: ".format(i + 1))).lower().title())
    guesses.append("")

while winning_number not in guesses:
    print("\n================")

    for i in range(0, num_players):
        guesses[i] = int(input("\n{} choose a number: ".format(players[i])))

    for i in range(len(guesses)):
        if guesses[i] == winning_number:
            print("\n$$$$$$$$$$$$$$$$\n\n{} wins.".format(players[i]))

input("\n$$$$$$$$$$$$$$$$\n\nPress ENTER to exit.")
