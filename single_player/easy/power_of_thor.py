"""Power of Thor

Description:

Thor's hammer, Mjöllnir has lost all of its powers... Will you be able
to guide Thor towards the light of power to make the hammer whole again?

Topic: condition statements (if...).
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while 1:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW

    if thor_x > light_x:
        direction_x = "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction_x = "E"
        thor_x += 1
    else:
        direction_x = ""

    if thor_y > light_y:
        direction_y = "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction_y = "S"
        thor_y += 1
    else:
        direction_y = ""

    print(direction_y + direction_x)
