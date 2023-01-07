#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
The trick might be to not actually perform the swaps, but count them another way?
'''


def countInversions(arr):
    swaps = 0

    def merge(a):
        nonlocal swaps
        if len(a) < 2:
            return a

        # determine mid point (rounded down)
        m = len(a)//2
        # split and recurse until arrays are singular
        l = merge(a[:m])
        r = merge(a[m:])

        i = j = 0
        sub_list = []

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                sub_list.append(l[i])
                i += 1
            else:
                sub_list.append(r[j])
                j += 1
                swaps += len(l) - i

        return sub_list + l[i:] + r[j:]

    merge(arr)
    return swaps


rand_list = []

for i in range(1_000_000):
    rand_list.append(random.randint(0, 10))

tests = [
    [1, 1, 1, 2, 2],    # 0
    [2, 1, 3, 1, 2],    # 4
    rand_list
]

results = []

for arr in tests:
    results.append(countInversions(arr))

print(results)
