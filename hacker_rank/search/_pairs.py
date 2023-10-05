from collections import Counter
'''
Given an array of integers and a target value,
determine the number of pairs of array elements that have
a difference equal to the target value.

For example:
k = 1
arr = [1, 2, 3, 4]
There are 3 pairs which differ by k, so we return 3.
'''

# def pairs(k, arr):
#     pairs = set()
#     for i in arr:
#         if abs(i - k) in arr:
#             pairs.add(abs(i - k))
#     return len(pairs)


def pairs(k, arr):
    pairs = set()
    num_cnts = Counter(arr)
    for num in num_cnts.keys():
        while num_cnts[num] > 0:
            diff = abs(num - k)
            if diff in num_cnts.keys():
                pairs.add(f'{[num, diff]}')
            num_cnts[num] -= 1
    return len(pairs)


tests = [
    [1, [1, 2, 3, 4]],      # 3
    [2, [1, 5, 3, 4, 2]]    # 3
]


for k, arr in tests:
    print(pairs(k, arr))
