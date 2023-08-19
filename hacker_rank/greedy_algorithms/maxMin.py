'''
You will be given a list of integers arr and a single integer k.

You must create an array of length k from elements of arr such that 
its unfairness is minimized. Call that array arr'.

Unfairness of an array is calculated as max(arr') - min(arr').
'''

'''
Sounds like a sliding window problem.
- sort arr
- create a window of size k
- check unfairness
- 
'''

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    arr.sort()
    l = 0
    r = k - 1
    minUnfairness = float('inf')

    while r < len(arr):
        minUnfairness = min(minUnfairness, arr[r] - arr[l])
        l += 1
        r += 1

    return minUnfairness


tests = [
    [2, [1, 4, 7, 2]],                              # 1
    [3, [10, 100, 300, 200, 1000, 20, 30]],         # 20
    [4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]],    # 3
    [2, [1, 2, 1, 2, 1]],                           # 0
]

for k, arr in tests:
    print(maxMin(k, arr))
