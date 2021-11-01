import random

START_POSITION = 0
NO_PLAY_OPTION = 0
LADDER_OPTION = 1
SNAKE_OPTION = 2

player_position = START_POSITION
dice_rolls = 0
while player_position < 100:
    dice_number = random.randint(1, 6)
    dice_rolls += 1
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
    print("Dice roll: {} Current position: {}".format(dice_rolls, player_position))

print("Position in the end = {} with total {} dice rolls".format(player_position, dice_rolls))
