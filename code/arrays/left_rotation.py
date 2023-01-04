#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


def rotLeft(a, d):
    new_arr = list(range(len(a)))
    for (idx, val) in enumerate(a):
        new_idx = idx - d
        if new_idx < 0:
            new_idx += len(a)
        new_arr[new_idx] = val
    return new_arr
    


d = 4
a = [1, 2, 3, 4, 5]

result = rotLeft(a, d)

print(result)
