#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

'''
- For each action
  - add k to index a - 1
  - minus k from index b
- sum by index
- running sum across previous sum
- max value is answer
'''


def arrayManipulation(n, queries):
    arr = [0] * n
    max_int = 0
    cur_int = 0

    for a, b, k in queries:
        arr[a - 1] += k
        if (b < n):
            arr[b] -= k

    # iterate over array only storing running max to save space
    for i in range(len(arr)):
        cur_int += arr[i]
        if max_int < cur_int:
            max_int = cur_int

    return max_int

# 10
n1 = 10
q1 = [[1, 5, 3],
      [4, 8, 7],
      [6, 9, 1]]

# 200
n2 = 5
q2 = [[1, 2, 100],
      [2, 5, 100],
      [3, 4, 100]]

# 31
n3 = 10
q3 = [[2, 6, 8],
      [3, 5, 7],
      [1, 8, 1],
      [5, 9, 15]]

# 882
n4 = 4
q4 = [[2, 3, 603],
      [1, 1, 286],
      [4, 4, 882]]


result = []

# for i in [[n1, q1], [n2, q2], [n3, q3]]:
for i in [[n4, q4]]:
    result.append(arrayManipulation(i[0], i[1]))

print(result)
