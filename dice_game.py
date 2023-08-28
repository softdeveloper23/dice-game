import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of people playing (2-4 players): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("You must enter between 2 - 4 players.")
    else:
        print("You must enter a number between 2 and 4.")


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    current_score = 0

    should_roll = input("Would you like to roll? (y)? ")
    if should_roll.lower() != "y":
        break

    value = roll()
    if value == 1:
        print("You rolled a 1! Your turn is over.")
        break
    else:
        current_score += value
        print("You rolled a {}!".format(value))

    print("Your current score is {}.".format(current_score))
