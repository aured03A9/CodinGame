#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Power of Thor - Episode 1

The Goal:

Your program must allow Thor to reach the light of power.
"""

import sys
import math

# Hint: You can use the debug stream to print initialTX and initialTY,
# if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

# game loop
while 1:
    # The remaining amount of turns Thor can move.
    remaining_turns = int(input())

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
