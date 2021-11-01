import random

START_POSITION = 0
NO_PLAY_OPTION = 0
LADDER_OPTION = 1
SNAKE_OPTION = 2

player1_position = START_POSITION
player2_position = START_POSITION
player1_chance = True

while player1_position < 100 and player2_position < 100:
    if player1_chance:
        player_position = player1_position
    else:
        player_position = player2_position

    dice_number = random.randint(1, 6)
    option = random.randint(0, 2)
    if option == NO_PLAY_OPTION:
        player_position = player_position
    elif option == LADDER_OPTION:
        player_position += dice_number
        if player_position > 100:
            player_position -= dice_number
    elif option == SNAKE_OPTION:
        player_position -= dice_number
        if player_position < 0:
            player_position = 0

    if player1_chance:
        player1_position = player_position
    else:
        player2_position = player_position

    print("Player 1 position is {} and player 2 position is {}".format(player1_position, player2_position))
    if option != LADDER_OPTION:
        if player1_chance:
            player1_chance = False
        else:
            player1_chance = True

if player1_position == 100:
    print("Player 1 has won!")
else:
    print("Player 2 has won!")
