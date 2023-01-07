#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#


def maximumToys(prices, k):
    prices.sort()

    idx = 0
    toy_cnt = 0

    while k > 0 and idx < len(prices):
        if k - prices[idx] >= 0:
            k -= prices[idx]
            toy_cnt += 1
        idx += 1
    return toy_cnt

tests = [
    [[1, 2, 3, 4], 7],                      # 3
    [[1, 12, 5, 111, 200, 1000, 10], 50]    # 4
]

results = []

for p, b in tests:
    results.append(maximumToys(p, b))

print(results)