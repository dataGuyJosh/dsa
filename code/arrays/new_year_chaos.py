#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    bribes = 0
    too_chaotic = False
    for (idx, sticker) in enumerate(q):
        if (sticker > idx + 3):
            too_chaotic = True
            break
        elif (sticker > idx + 2):
            bribes += 2
        elif (sticker > idx + 1):
            bribes += 1
    if (too_chaotic):
        print('Too chaotic')
    else:
        print(bribes)


'''
1, 2, 3, 4
1, 3, 2, 4 --> 1 bribe by 3
1, 4, 3, 2 --> 2 bribes by 4
3 bribes total
'''

q1 = [2, 1, 5, 3, 4]
q2 = [2, 5, 1, 3, 4]
q3 = [1, 2, 5, 3, 7, 8, 6, 4]
q4 = [1, 4, 3, 2]

minimumBribes(q1)
minimumBribes(q2)
minimumBribes(q3)
minimumBribes(q4)