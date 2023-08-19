#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


'''
Two strings are anagrams of each other
if the first string's letters can be rearranged
to form the second string.

In other words, both strings must contain
the same exact letters in the same exact frequency.

- create a frequency count of each letter
- find all distinct letters across both strings (union)
- number of deletions is the sum of differences in frequency for each letter between strings
  - for 'cde' and 'dcf'
  - distinct letters are 'cdef'
    - for 'e', deletions = |1 - 0| = 1
    - for 'f', deletions = |0 - 1| = 1
    - all other letters are present in both so no deletion necessary
    - therefore 2 deletes total
'''
from collections import Counter

def makeAnagram(a, b):
    del_cnt = 0

    a_cnt = Counter(list(a))
    b_cnt = Counter(list(b))

    # for each distinct letter in the union between a & b
    for i in set(a).union(set(b)):
        # number of deletes is difference in letter frequency between a & b
        del_cnt += abs(a_cnt[i] - b_cnt[i])

    return del_cnt


tests = [
    ['cde', 'dcf'], # 2
    ['cde', 'abc']  # 4
]

results = []

for a, b in tests:
    results.append(makeAnagram(a, b))

print(results)
