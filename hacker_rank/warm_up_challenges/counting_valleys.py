#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    depth = 0
    num_valleys = 0
    start_valley = False
    for step in list(path):
        if step == 'U':
            depth+=1
        elif step == 'D':
            if depth == 0:
                num_valleys+=1
            depth-=1
    
    return num_valleys

    

steps = 8
path = 'UDDDUDUU'
result = countingValleys(steps, path)

print(result)