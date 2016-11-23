#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The Bridge - Episode 1

The Goal:

The goal for your program is to make a motorbike jump across a gap and land on
a platform then stop.
"""

import sys
import math

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

bgap = road - 1
bplatform = road + gap

# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    if coord_x == bgap:
        print("JUMP")
    elif coord_x >= bplatform:
        print("SLOW")
    elif speed <= gap:
        print("SPEED")
    elif speed > gap + 1:
        print("SLOW")
    else:
        print("WAIT")
