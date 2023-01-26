#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain, combinations
#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

'''
A string is said to be a child of a another string if
it can be formed by deleting 0 or more characters from the other string. 
- letters cannot be rearranged.
- input is two strings of EQUAL LENGTH

It looks like "powersets" could be useful here.

To fulfil performance requirements, this is an LCS problem:
https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
'''


def commonChild(s1, s2):
    # find the intersect of both strings i.e. characters found in both
    common_characters = set(s1).intersection(set(s2))

    # remove all characters not found in intersect
    s1 = [c for c in s1 if c in common_characters]
    s2 = [c for c in s2 if c in common_characters]

    l1, l2 = len(s1), len(s2)
    # create a 2D list with dimensions
    lcs = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    # interate over all character combinations
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            # if characters are equal, 
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    
    return lcs[l1 - 1][l2 - 1]

tests = [
    ['HARRY', 'SALLY'],         # 2
    ['AA', 'BB'],               # 0
    ['SHINCHAN', 'NOHARAAA'],   # 3
    ['ABCDEF', 'FBDAMN'],       # 2
                                # 15
    ['WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS',
        'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC']
]

results = []

for s1, s2 in tests:
    results.append(commonChild(s1, s2))

print(results)
