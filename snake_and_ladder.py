import random

START_POSITION = 0
NO_PLAY_OPTION = 0
LADDER_OPTION = 1
SNAKE_OPTION = 2

player_position = START_POSITION
dice_number = random.randint(1, 6)

option = random.randint(0, 2)

if option == NO_PLAY_OPTION:
    print("NO PLAY!")
    player_position = player_position
elif option == LADDER_OPTION:
    print("YIPPEE! ITS A LADDER")
    player_position += dice_number
elif option == SNAKE_OPTION:
    print("UH NO! ITS A SNAKE")
    player_position -= dice_number

print("Position after dice roll = {}".format(player_position))
