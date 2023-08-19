#!/bin/python3

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

'''
Lena is preparing for an important coding competition that is preceded by
a number of sequential preliminary contests.

Initially, her luck balance is 0. She believes in "saving luck", 
and wants to check her theory. Each contest is described by two integers, L and T:
- L is the amount of luck associated with a contest.
  If Lena wins the contest, her luck balance will decrease by L; 
  if she loses it, her luck balance will increase by L.
- T denotes the contest's importance rating. It's equal to 1 if the contest is important,
  and it's equal to 0 if it's unimportant.

If Lena loses no more than k important contests,
what is the MAXIMUM amount of luck she can have
after competing in all the preliminary contests?
This value may be negative.

Example:
k = 2
L = [5,1,4]
T = [1,1,0]
max_luck = 5 + 1 + 4 = 10

k = 1
L = [5,1,4]
T = [1,1,0]
max_luck = 5 - 1 + 4 = 8


If important and k
- lose
If important not k
- win
If not important
- lose
'''


def luckBalance(k, contests):
    luck = 0
    contests.sort(reverse=True)
    for i in range(len(contests)):
        L = contests[i][0]
        T = contests[i][1]
        if not T:
            luck += L
        elif (T and k > 0):
            luck += L
            k -= 1
        else:  # T and k == 0
            luck -= L
    return luck


tests = [
    [2, [[5, 1], [1, 1], [4, 0]]],                          # 10
    [1, [[5, 1], [1, 1], [4, 0]]],                          # 8
    [3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]]  # 29
]

for k, contests in tests:
    print(luckBalance(k, contests))
