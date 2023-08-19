#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# https://www.youtube.com/watch?v=7z_v54Zk3Bk


def sherlockAndAnagrams(s):
    str_cnts = {}
    ana_cnt = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = ''.join(sorted(s[i:j+1]))
            if sub_str in str_cnts:
                str_cnts[sub_str] += 1
            else:
                str_cnts[sub_str] = 1

    for i in str_cnts:
        sc = str_cnts[i]
        # formula for anagram count given string counts
        ana_cnt += sc * (sc - 1) / 2

    return int(ana_cnt)

strs = [
    'mom',          # 2
    'abba',         # 4
    'abcd',         # 0
    'ifailuhkqq',   # 3
    'kkkk',         # 10
    'cdcd'          # 5
]

results = []

for s in strs:
    results.append(sherlockAndAnagrams(s))

print(results)
