'''
Sliding Windows
In many problems involving an array or linked list,
we are asked to calculate something among subarrays of a given size.

Often these subarrays overlap, which allows us to optimize our algorithm
and not recompute the overlapping sections.

We can use a "sliding window" to discern what might be overlapping between subarrays
as oppose to what is a new element to be computed.
'''

'''
Given an array, find the average of all contiguous subarrays of size "k".
The word "contiguous" means adjacent numbers, not necessarily consecutive.
In the array [1,4,2], 1 & 2 are consecutive but not contiguous (as 4 is between them).

e.g. [1,2,3,4,5], k = 3 --> [2, 3, 4]
'''
# naive approach, we're summing the same numbers multiple times




from collections import Counter
def subMeans(nums, k):
    means = []
    window = []
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        means.append(sum(window)/k)
    return means

# sliding window approach, we're adding/subtracting each number once
# this avoids adding the same numbers multiple times


def subMeans(nums, k):
    means = []
    start = 0
    windowSum = 0
    for end in range(len(nums)):
        windowSum += nums[end]
        if end >= k - 1:
            means.append(windowSum/k)
            windowSum -= nums[start]
            start += 1
    return means


tests = [
    [[1, 2, 3, 4, 5], 3],               # [2.0, 3.0, 4.0]
    [[1, 3, 2, 6, -1, 4, 1, 8, 2], 5]   # [2.2, 2.8, 2.4, 3.6, 2.8]
]

for nums, k in tests:
    print(subMeans(nums, k))


'''
Given an array of positive integers and a positive number s,
find the length of the smallest contiguous subarray whose sum is greater than or equal to s.
Return 0 when no such subarray exists.

e.g. [1,3,2,2,4,5], s = 6 --> [2,4] --> 2
'''


def sumGreaterThan(lst, s):
    wstart, wend, wsum = 0, 0, 0
    minLength = float('inf')
    for wend in range(len(lst)):
        # grow window
        wsum += lst[wend]
        # until wsum is less than s
        while (wsum >= s):
            # shrink window, decrement wstart, remove first element

            # update minLength if necessary
            curLength = wend - wstart + 1
            if curLength < minLength:
                minLength = curLength

            # shrink window by removing first element from wsum
            wsum -= lst[wstart]
            # advance wstart
            wstart += 1

    if minLength == float('inf'):
        return 0
    return minLength


tests = [
    [[1, 3, 2, 2, 4, 5], 6],    # 2
    [[2, 1, 5, 2, 8], 7],       # 1
    [[4, 2, 0], 69]             # 0
]

for lst, s in tests:
    print(sumGreaterThan(lst, s))


'''
Given a string, find the length of the LONGEST substring
which contains no more than k distinct characters.

e.g. 'acccpbbebi', k = 3 --> 'cccpbb' --> 6

Algorithm
1. init start/end at 0th index
2. add char to charFreqs
3. are there more keys in charFreqs than k?
  - yes
    - shrink window until charFreqs keys < k
    - repeat from step 2
  - no
    - grow window by incrementing end
    - capture llen
    - repeat from step 2
'''


def longestSS(str, k):
    wstart, llen = 0, 0
    charFreqs = Counter()

    for wend in range(len(str)):
        # grow window
        charFreqs[str[wend]] += 1
        # if we meet condition k
        while len(charFreqs) > k:
            # remove character from window
            charFreqs[str[wstart]] -= 1
            # remove key if no longer present in window
            if charFreqs[str[wstart]] == 0:
                del charFreqs[str[wstart]]
            # shrink window
            wstart += 1

        # sum characters in substring
        # adding 1 compensates for the fact that we're counting indices which start from 0
        # e.g. if wstart = 0 & wend = 4, there are 5 characters in the substring, but 4 - 0 = 4
        llen = max(llen, wend - wstart + 1)
    return llen


tests = [
    ['acccpbbebi', 3],  # 6 (cccpbb)
    ['aaaabbccd', 1],   # 4 (aaaa)
    ['abcdefg', 10]     # 7 (abcdefg)
]

for str, k in tests:
    print(longestSS(str, k))
