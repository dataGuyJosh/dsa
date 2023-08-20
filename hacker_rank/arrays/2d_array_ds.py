#!/bin/python3

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    max_sum = -float('inf')
    for x in range(4):
        for y in range(4):
            current_sum = \
                sum(arr[x][y:y + 3]) + \
                arr[x + 1][y + 1] + \
                sum(arr[x + 2][y:y + 3])
            max_sum = max(max_sum, current_sum)

    return max_sum


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

result = hourglassSum(arr)

print(result)
