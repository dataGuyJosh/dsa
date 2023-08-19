#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

'''
Constraints
- all letters are lowercase
- words can be 1 to 10^5 letters long

We only really need to know 1 letter substrings for this to work I think.
'''


def twoStrings(s1, s2):
    con_sub_str = 'NO'
    
    for l1, l2 in zip(list(s1), list(s2)):
        if l1 in s2 or l2 in s1:
            con_sub_str = 'YES'
            break

    return con_sub_str


result = []

words = [['and', 'art'],        # YES
         ['be', 'cat'],         # NO
         ['hello', 'world'],    # YES
         ['hi', 'world']]       # NO

for s1, s2 in words:
    result.append(twoStrings(s1, s2))

print(result)
