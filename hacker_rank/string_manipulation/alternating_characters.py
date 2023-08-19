#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


'''
AABB
- check index 0 & 1
- del
- check index 0 & 1
- increment
- check index 1 & 2
- increment
- check index 2 & 3
- stop (no index 4)
'''


def alternatingCharacters(s):
    s = list(s)
    del_cnt = 0
    i = 0
    j = 1

    while j < len(s):
        if s[i] == s[j]:
            del s[i]
            del_cnt += 1
        else:
            i += 1
            j += 1

    return del_cnt


tests = [
    'AAAA',         # 3
    'BBBBB',        # 4
    'ABABABAB',     # 0
    'BABABA',       # 0
    'AAABBB'        # 4
]

results = []

for s in tests:
    results.append(alternatingCharacters(s))

print(results)
