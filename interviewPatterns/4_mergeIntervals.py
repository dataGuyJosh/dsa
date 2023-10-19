'''
Merge Intervals
This pattern is about efficient techniques to deal with overlapping intervals.
In these types of problems, we're asked to find and/or merge overlapping intervals.

Given 2 intervals A & B, there will be 6 different ways 2 intervals relate to each other:
(understanding this will help us understand all possible scenarios for this problem)
- A & B don't overlap, A occurs 1st                         {A}[B]
- A & B don't overlap, B occurs 1st                         [B]{A}
- A & B overlap, B ends after A                             {A[B}]
- A & B overlap, A ends after B                             [B{A]}
- A overlaps B completely, A starts before and ends after B {A[B]}
- B overlaps A completely, B starts before and ends after A [{A}B]
'''

'''
Problem
Given a list of intervals, merge all overlapping intervals
to produce a list of mutually exclusive intervals.

Example
Intervals: [[1,4], [2,5], [7,9]]
Mutually Exclusive Intervals: [[1,5], [7,9]]

Approach
- sort intervals by start time such that A.start is always <= B.start, leaving 4 scenarios
  1. A & B don't overlap                                        {A}[B]
  2. A & B overlap, B ends after A                              {A[B}]
  3. A completely overlaps B, A starts before and ends after B  {A[B]}
  4. B completely overlaps A BUT they share start time          [{A}B] <-- more specific than scenario 6 above
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


'''
Problem
Given a list of jobs, each with a start/end time and CPU load (while running),
find the max CPU load at any time if all jobs are running on the same machine.

Example
Jobs: [
    {start: 1, end: 4, load: 3},
    {start: 2, end: 5, load: 4},
    {start: 7, end: 9, load: 6}
]
Output: 7 i.e. the first two jobs are the only overlap, summing their load equals 7

Approach
- sort intervals by start time such that A.start is always <= B.start, leaving 4 scenarios
  1. A & B don't overlap                                        {A}[B]
  2. A & B overlap, B ends after A                              {A[B}]
  3. A completely overlaps B, A starts before and ends after B  {A[B]}
  4. B completely overlaps A BUT they share start time          [{A}B] <-- more specific than scenario 6 above
- in scenario 2, 3 & 4 we merge according to different rules (1 has no overlaps so no merge)
  1. no merge
  2. A.start - B.end
  3. A.start - A.end
  4. A.start - B.end
- when combining 2 intervals, add load times to compare against our running max CPU
'''


def maxCPULoad(jobs):

    pass


tests = [
    [
        {'start': 1, 'end': 4, 'load': 3},
        {'start': 2, 'end': 5, 'load': 4},
        {'start': 7, 'end': 9, 'load': 6}
    ],  # 7 i.e. jobs 1 & 2
    [
        {'start': 6, 'end': 7,  'load': 10},
        {'start': 2, 'end': 4,  'load': 11},
        {'start': 8, 'end': 12, 'load': 15}
    ],   # 15 i.e. no overlap
    [
        {'start': 1, 'end': 4, 'load': 2},
        {'start': 2, 'end': 4, 'load': 1},
        {'start': 3, 'end': 6, 'load': 5}
    ]   # 8 i.e. jobs 1, 2 & 3
]

for i in tests:
    print(maxCPULoad(i))
