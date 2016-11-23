#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Mars Lander - Episode 1

The Goal:

The goal for your program is to safely land the "Mars Lander" shuttle,
the landing ship which contains the Opportunity rover.
Mars Lander is guided by a program, and right now the failure rate for landing
on the NASA simulator is unacceptable.

Note that it may look like a difficult problem, but in reality the problem is
easy to solve.
This puzzle is the first level among three, therefore, we need to present you
some controls you won't need in order to complete this first level.
"""

import sys
import math

# the number of points used to draw the surface of Mars.
surface_n = int(input())
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points
    #         together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # 2 integers: rotate power. rotate is the desired rotation angle (should be
    # 0 for level 1), power is the desired thrust power (0 to 4).
    if y > 1000:
        print("0 3")
    elif y > 0:
        print("0 4")
    else:
        print("0 0")
