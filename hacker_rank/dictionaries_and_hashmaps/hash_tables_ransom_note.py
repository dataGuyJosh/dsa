#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    can_use = True
    
    m_word_count = dict.fromkeys(magazine, 0)

    for mw in magazine:
        m_word_count[mw] += 1
    
    for nw in note:
        if not nw in m_word_count or m_word_count[nw] == 0:
            can_use = False
            break
        m_word_count[nw] -= 1

    print('Yes' if can_use else 'No')


# No
m1 = 'attack at dawn'
n1 = 'Attack at dawn'

# Yes
m2 = 'give me one grand today night'
n2 = 'give one grand today'

# No
m3 = 'two times three is not four'
n3 = 'two times two is four'

# No
m4 = 'ive got a lovely bunch of coconuts'
n4 = 'ive got some coconuts'

for maga, note in [[m1, n1], [m2, n2], [m3, n3], [m4, n4]]:
# for maga, note in [[m2, n2]]:
    checkMagazine(maga.split(), note.split())