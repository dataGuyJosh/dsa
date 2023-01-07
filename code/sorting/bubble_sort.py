#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print(
        'Array is sorted in ' + str(swaps) + ' swaps.',
        '\nFirst Element: ' + str(a[0]),
        '\nLast Element: ' + str(a[-1])
    )


a = [6, 4, 1]

countSwaps(a)
