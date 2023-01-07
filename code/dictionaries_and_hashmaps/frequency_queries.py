#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.


def freqQuery(queries):
    num_freqs = Counter()
    q3 = []
    for opr, val in queries:
        if opr == 1:
            num_freqs[val] += 1
        elif opr == 2 and num_freqs[val]:
            num_freqs[val] -= 1
        elif opr == 3:
            if val in num_freqs.values():
                q3.append(1)
            else:
                q3.append(0)
    return q3


# 0
# 1
q1 = [[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]

# 0
# 1
q2 = [[3, 4],  [2, 1003],  [1, 16],  [3, 1]]

# 0
# 1
# 1
q3 = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5],
      [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
results = []

for q in [q1, q2, q3]:
    results.append(freqQuery(q))

print(results)