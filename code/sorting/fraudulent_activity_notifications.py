#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from statistics import median
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

'''
if today_spending >= 2 * median_spending then notify()

Don't sort every index every iteration, only one new index needs sorting per iteration after the first!
'''

import bisect


def activityNotifications(expenditure, d):
    hist = sorted(expenditure[:d])

    # a & b describe the index of the median
    # if d is odd; median == hist[a] == hist[b]
    # if d is even; median == (hist[a] + hist[b]) / 2
    a = math.ceil((d-1)/2)
    b = math.floor((d-1)/2)

    not_cnt = 0

    for i in range(len(expenditure) - d):
        # if the sum of the median values is less than or equal to
        # today's expenditure a notification is sent!
        not_cnt += (hist[a] + hist[b] <= expenditure[i+d])
        
        # bisect allows the list to be updated while remaining sorted
        # this cuts runtime down significantly
        hist.pop(bisect.bisect_left(hist, expenditure[i]))
        bisect.insort(hist, expenditure[i+d])
    return not_cnt


tests = [
    [[2, 3, 4, 2, 3, 6, 8, 4, 5], 5],   # 2
    [[1, 2, 3, 4, 4], 4],               # 0
    [[69] * 10**6, 10]
]

results = []

for e, d in tests:
    results.append(activityNotifications(e, d))

print(results)
