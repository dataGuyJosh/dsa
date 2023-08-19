#!/bin/python3
import math
#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    pattern_cnt = s.count('a')
    
    if(pattern_cnt == 0):
        return 0

    # calculate minimum repetitions before hitting character limit
    reps = math.floor(n/len(s))

    # calculate extra letters between string size and limit
    extra_letters = n % len(s)
    # sum 'a' characters in extras
    extras = s[:extra_letters].count('a')

    return pattern_cnt * reps + extras
    

s = 'a'
n = 1000000000000
s = 'aba'
n = 10
s = 'ceebbcb'
n = 817723
s = 'gfcaaaecbg'
n = 547602

result = repeatedString(s, n)

print(result)