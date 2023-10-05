'''
Merge Intervals
This pattern is about efficient techniques to deal with overlapping intervals.
In these types of problems, we're asked to find and/or merge overlapping intervals.

Given 2 intervals A & B, there will be 6 different ways 2 intervals relate to each other:
(understanding this will help us understand all possible scenarios for this problem)
- A & B don't overlap, A occurs 1st
- A & B don't overlap, B occurs 1st
- A & B overlap, B ends after A
- A & B overlap, A ends after B
- A overlaps B completely, A starts before and ends after B
- B overlaps A completely, B starts before and ends after A
'''

'''
Problem
Given a list of intervals, merge all overlapping intervals
to produce a list of mutually exclusive intervals.

Example
Intervals: [[1,4], [2,5], [7,9]]
Mutually Exclusive Intervals: [[1,5], [7,9]]

Approach
- sort intervals by start time
- if we reduce our scenarios such that A.start <= B.start we are left with 4 scenarios
  1. A & B don't overlap
  2. A & B overlap, B ends after A
  3. A completely overlaps B, A starts before and ends after B
  4. B completely overlaps A but they share start time
- in scenario 2, 3 & 4 we merge according to different rules (1 has no overlaps so no merge)
  1. no merge
  2. A.start - B.end
  3. A.start - A.end
  4. A.start - B.end

Pseudo Code
If A overlaps B i.e. A.start >= B.start, we merge into new interval C such that:
- C.start == A.start
- C.end == max(A.end, B.end)

In other words:
- always take A.start
- always take the larger end
'''


def mergeIntervals(arr):
    # sort intervals by start time
    arr.sort()

    # init stack of merged intervals
    mi = [arr.pop(0)]
    i = 0
    while (len(arr)):
        # always compare the
        a = mi.pop()    # last interval seen to the
        b = arr.pop(0)  # next available interval in arr

        # ES60 structuring
        [aS, aE] = a
        [bS, bE] = b

        # scenarios
        # a & b don't overlap
        if bS > aE:
            mi.append(a)
            mi.append(b)
        else:  # merging --> always take A.start, always take larger end
            c = [aS, max(aE, bE)]
            mi.append(c)

    return mi


tests = [
    [[2, 5], [1, 4], [7, 9]],   # [[1, 5], [7, 9]]
    [[6, 7], [2, 4], [5, 9]],   # [[2, 4], [5, 9]]
    [[1, 4], [2, 6], [3, 5]]    # [[1, 6]]
]

for i in tests:
    print(mergeIntervals(i))
