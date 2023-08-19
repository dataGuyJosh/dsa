#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    s = list(s)
    ltr_cnts = list(dict(Counter(s)).values())
    # check if already valid string
    if len(set(ltr_cnts)) == 1:
        return 'YES'
    # need to use list function such that
    # these are two distinct copies rather than references to the same list
    mx = list(ltr_cnts)
    mn = list(ltr_cnts)
    # get max & min values
    max_cnt = max(mx)
    min_cnt = min(mn)
    # decriment first occurence i.e. remove one copy of this letter
    mx[mx.index(max_cnt)] -= 1
    mn[mn.index(min_cnt)] -= 1
    # remove zeros from min list
    mn = list(filter((0).__ne__, mn))
    # check all values in list are identical
    if len(set(mx)) == 1 or len(set(mn)) == 1:
        return 'YES'
    # if none of the steps above made the string valid, it is invalid
    return 'NO'


tests = [
    'abc',                  # YES
    'abcc',                 # YES
    'abccc',                # NO
    'aabbcd',               # NO
    'aabbccddeefghi',       # NO
    'abcdefghhgfedecba',    # YES
    'aabbccddd',            # YES
    'aabbc'                 # YES (remove 'c')
]

results = []

for s in tests:
    results.append(isValid(s))

print(results)
