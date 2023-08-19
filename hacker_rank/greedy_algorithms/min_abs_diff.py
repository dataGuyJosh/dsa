#!/bin/python3

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
Given an array of integers, 
find the minimum absolute difference between any two elements in the array.

Proposed algorithm:
- sort arr
- check difference between adjacent values
- return minimum difference
'''


def minimumAbsoluteDifference(arr):
    arr.sort()
    mnAbDf = float('Inf')
    for i in range(1, len(arr)):
        abDf = arr[i] - arr[i-1]
        mnAbDf = min(mnAbDf, abDf)
    return mnAbDf


tests = [
    [-2, 2, 4],     # 2
    [3, -7, 0],     # 3
    [1, 2, 3, 4]    # 1
]

for arr in tests:
    print(minimumAbsoluteDifference(arr))
