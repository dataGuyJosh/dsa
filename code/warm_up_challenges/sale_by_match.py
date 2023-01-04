#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # sort array
    ar.sort()
    # group by colour, count groups, halve, round down then sum
    return sum([(int(len(list(j))/2)) for i, j in groupby(ar)])

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)

print(str(result))