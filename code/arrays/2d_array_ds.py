#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    max_sum = -math.inf
    for x in range(4):
        for y in range(4):
            sum = \
                arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + \
                arr[x + 1][y + 1] + \
                arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2]
            max_sum = max((max_sum, sum))

    return max_sum


arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

result = hourglassSum(arr)

print(result)
