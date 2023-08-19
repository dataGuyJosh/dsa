#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    pos = 0
    steps = 0
    while pos < len(c) - 1:
        if pos == len(c) - 1:
            break
        pos += 2
        if pos > len(c) - 1 or c[pos]:
            pos -= 1
        steps += 1

    return steps


c = [0, 0, 0, 1, 0, 0]

result = jumpingOnClouds(c)
print(result)
