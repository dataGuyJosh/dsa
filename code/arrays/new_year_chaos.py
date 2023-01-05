#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

'''
input: list of stickers in their final order
output: total number of bribes or 'Too chaotic' if not possible

This kind of looks like a bubble sort, so let's do that?

Starting from index 0, check
- if sticker is greater than adjacent sticker
  - if so, swap and add one to that sticker's bribe count
- else move to next sticker
'''


def minimumBribes(q):
    # track bribes separately to make checking TC easier
    bribes = {}
    for i in q:
        bribes[i] = 0

    for i in range(len(q)-1):
        swapped = False
        # reduce search space after each iteration
        for j in range(len(q) - 1 - i):
            # compare adjacent values
            if q[j] > q[j + 1]:
                # swap (sort)
                q[j], q[j + 1] = q[j + 1], q[j]
                # increase bribe count
                bribes[q[j + 1]] += 1
                swapped = True
        # if no swap occured, continue to next person
        if not swapped:
            break

    if max(bribes.values()) > 2:
        print('Too chaotic')
    else:
        print(sum(bribes.values()))


'''
1, 2, 3, 4
1, 3, 2, 4 --> 1 bribe by 3
1, 4, 3, 2 --> 2 bribes by 4
3 bribes total
'''

q1 = [2, 1, 5, 3, 4]  # 3
q2 = [2, 5, 1, 3, 4]  # TC
q3 = [5, 1, 2, 3, 7, 8, 6, 4]  # TC
q4 = [1, 2, 5, 3, 7, 8, 6, 4]  # 7
q5 = [1, 4, 3, 2]  # 3
q6 = [1, 2, 3, 4]

for i in [q1, q2, q3, q4, q5, q6]:
    minimumBribes(i)
