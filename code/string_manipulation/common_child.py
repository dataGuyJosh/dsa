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


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def commonChild(s1, s2):
    uc1 = set(powerset(s1))
    uc2 = set(powerset(s2))

    itrsct = uc1.intersection(uc2)
    return len(max(itrsct, key=len)) if itrsct else 0


# Dynamic Programming implementation of LCS problem
 
def commonChild(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)
 
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
 
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of s1[0..i-1]
    and s2[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # L[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    return L[m][n]

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
