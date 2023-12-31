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
    for player_index in range(players):
        print("\nIt is player {}'s turn.".format(player_index + 1))
        print("Your current total score is {}.\n".format(player_scores[player_index]))
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is over.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a {}!".format(value))

            print("Your current score is {}.".format(current_score))
        player_scores[player_index] += current_score
        print("Your total score is {}.".format(player_scores[player_index]))

max_score = max(player_scores)
# winning_player = player_scores.index(max_score) # Causes a bug if there are two players with the same score
winning_player = player_scores.index(max(player_scores))
print("\nPlayer {} has won with {} points.".format(winning_player + 1, max_score))
