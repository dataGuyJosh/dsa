#!/bin/python3

import math
import os
import random
import re
import sys

'''
Special Strings follow either of the following rules
- all characters are the same e.g. 'aaa'
- all characters except the middle one are the same e.g. 'aadaa'

The first condition can be checked after fulfilling the second,
potentially saving run time?
'''

# Complete the substrCount function below.


def substrCount(n, s):
    if n == 1:
        return 1
    # count all combinations
    str_cnts = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = ''.join(s[i:j+1])
            if sub_str in str_cnts:
                str_cnts[sub_str] += 1
            else:
                str_cnts[sub_str] = 1
    
    special_cnts = dict(str_cnts)
    # filter out non-special strings
    for ss in str_cnts:
        tmp_ss = list(ss)
        # all characters are the same
        cond_1 = len(set(tmp_ss)) != 1
        cond_2 = True
        if len(tmp_ss) != 1 and len(tmp_ss) % 2 != 0:
            m = len(tmp_ss) // 2
            del tmp_ss[m]
            # all characters are the same after removing middle
            cond_2 = len(set(tmp_ss)) != 1
        # if either condition is met, they are special,
        # therefore check that BOTH conditions are not met
        # hence 'and'
        if cond_1 and cond_2:
            del special_cnts[ss]

    # count special strings
    return sum(special_cnts.values())


tests = [
    'mnonopoo',     # 12
    'asasd',        # 7
    'abcbaba',      # 10
    'aaaa',         # 10
    'a',
    ''.join(['a'] * 10**3)
]

results = []

for s in tests:
    results.append(substrCount(len(s), s))

print(results)
