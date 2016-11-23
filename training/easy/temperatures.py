#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Temperatures

The Goal:

You have to analyze records of temperature to find the closest to zero.
"""

import sys
import math

# the number of temperatures to analyse
n = int(input())
# the n temperatures expressed as integers ranging from -273 to 5526
temps = input().split(' ')

if n == 0:
    print(0)
else:
    p = 0
    for i in range(n):
        temps[i] = int(temps[i])
        if p == 0:
            p = temps[i]
        elif abs(p) == abs(temps[i]):
            if p < temps[i]:
                p = temps[i]
        elif abs(p) > abs(temps[i]):
            p = temps[i]
    print(p)
