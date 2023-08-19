#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

'''
Known constraints
- list is consecutive
- list always starts at 1
'''


def minimumSwaps(arr):
    swaps = 0
    i = 0

    # we don't want to increment the index every iteration
    # only when a given index is the correct value
    # hence while loop instead of for loop
    while i < len(arr):
        # check if element is in correct position
        # i.e. element should equal index plus one given our constraints
        
        # if wrong position, swap values with correct position and increment
        if arr[i] != i + 1:
            tmp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[tmp - 1] = tmp
            swaps += 1
        # if right position, check next index
        else:
            i += 1

    return swaps


a1 = [2, 3, 4, 1, 5]
'''
Three Swaps:
    0   [2, 3, 4, 1, 5]
    1   [2, 3, 1, 4, 5]
    2   [3, 2, 1, 4, 5]
    3   [1, 2, 3, 4, 5]
'''

a2 = [1, 3, 5, 2, 4, 6, 7]

result = []

for i in [a1, a2]:
    result.append(minimumSwaps(i))

print(result)
