#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

'''
In mathematics, a geometric progression, also known as a geometric sequence,
is a sequence of non-zero numbers where each term after the first is found by
multiplying the previous one by a fixed, non-zero number called the common ratio.

We want to count the number of geometric progressions of length 3 in each list.
'''

# Complete the countTriplets function below.

# terrible brute force method :c
def countTriplets(arr, r):
    geo_pro_cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                vj = arr[j]
                if i >= j or j >= k or i >= k or arr[i] * r != vj or vj * r != arr[k]:
                    continue

                geo_pro_cnt += 1

    return geo_pro_cnt


def countTriplets(arr, r):
    # using defaultdict as it returns 0 for nonexistent keys
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    # for each number
    for k in arr:
        # increment count by number of triplets ending in k
        count += v3[k]
        # increment potential TRIPLETS ending in k * r
        v3[k*r] += v2[k]
        # increment potential PAIRS ending in k * r
        v2[k*r] += 1
    return count


tests = [
    [[1, 4, 16, 64], 4],        # 2
    [[1, 2, 2, 4], 2],          # 2
    [[1, 3, 9, 9, 27, 81], 3],  # 6
    [[1, 5, 5, 25, 125], 5],    # 4
    [[1, 2], 2],                # 0
    [[1] * 100, 1],             # 161700
    [[69] * 420, 1]
]

result = []

for a, r in tests:
    result.append(countTriplets(a, r))

print(result)
