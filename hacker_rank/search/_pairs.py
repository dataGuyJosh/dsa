'''
Given an array of integers and a target value,
determine the number of pairs of array elements that have
a difference equal to the target value.

For example:
k = 1
arr = [1,2,3,4]
There are 3 pairs which differ by k, so we return 3.
'''

def pairs(k, arr):
    pair_cnt = set()
    for i in arr:
        if abs(i - k) in arr:
            pair_cnt.add(abs(i - k))
    return len(pair_cnt)


tests = [
    [1, [1, 2, 3, 4]],      # 3
    [2, [1, 5, 3, 4, 2]]    # 3
]

for k, arr in tests:
    print(pairs(k, arr))
