#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The Descent

The Goal:

Destroy the mountains before your starship collides with one of them.
For that, shoot the highest mountain on your path.
"""

import sys
import math

mountain = {}

while True:
    for i in range(8):
        # represents the height of one mountain, from 9 to 0.
        mountain_h = int(input())
        mountain[i] = mountain_h

    sorted_mountain = sorted(mountain, key=mountain.get, reverse=True)

    # The index of the mountain to fire on.
    print(sorted_mountain[0])
