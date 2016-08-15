#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The Descent

Description:

The enterprise is in danger: drawn towards the surface of an unknown
planet, it is at risk of crashing against towering mountains.

Help Kirk and Spock destroy the mountains... Save the enterprise!

Topic: search in an array
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
