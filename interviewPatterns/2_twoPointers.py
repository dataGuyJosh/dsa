'''
Two Pointers
In many problems involving arrays or linked lists where you need to find
a set of elements that fulfil certain constraints, we can use the Two Pointers pattern 
to avoid looping over the array multiple times.

Because we use two pointers, we are able to process two elements per loop instead of one.
Common patterns in the Two Pointers approach are:
- each pointer starts at ither end of the array/linked list, meeting somewhere in the middle.
- both pointers start from the same position, with one pointer moving twice the rate of the other
'''

'''
Given an array of SORTED integers and a target sum,
find a pair in the array whose sum is equal to the given target.
'''


def findPair(arr, targetSum):
    # naive approach O(n^2)
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if i != j and arr[i] + arr[j] == targetSum:
    #             return [arr[i], arr[j]]

    # two pointer approach O(n)
    l = 0
    r = len(arr) - 1
    pair = None

    # get element at each pointer and check if they sum to target sum
    # pairSum == targetSum: return pair
    # pairSum < targetSum: increment l
    # pairSum > targetSum: decrement r

    while l != r:
        pairSum = arr[l] + arr[r]
        if pairSum == targetSum:
            pair = [arr[l], arr[r]]
            break
        elif pairSum < targetSum:
            l += 1
        else:
            r -= 1

    return pair


tests = [
    [[1, 2, 3, 4, 5], 7],       # [2, 5]
    [[1, 6, 8, 9, 10], 14],     # [6, 8]
    [[1, 3, 4, 6, 8, 10], 12],  # [4, 8]
    [[1, 2, 3, 4, 5], 10]       # None
]

for arr, sum in tests:
    print(findPair(arr, sum))


'''
Given an array of unsorted numbers,
find all UNIQUE triplets that add up to zero.

e.g. [-3,0,1,2,-1,1,-2]
- sort the array
- loop over array
  - take negative of array at i i.e. difference from zero
  - find pairs [l,r] which sum to dfz
    - if l + r = dfc --> record triplet
    - 
'''


def zeroTriplets(arr):
    if len(arr) < 3:
        return []
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        dfz = -arr[i]
        # we want to UNIQUE triplets and have a SORTED list
        # if we've already seen this element before, skip it
        if i > 0 and arr[i] == arr[i-1]:
            continue

        searchPair(arr, dfz, i + 1, triplets)

    return triplets


# two pointer implementation
def searchPair(arr, dfz, l, triplets):
    r = len(arr) - 1
    while l < r:
        cSum = arr[l] + arr[r]
        # we found a triplet!
        if cSum == dfz:
            # remember that dfz is just negative i, so we can invert it here to get i
            triplets.append([-dfz, arr[l], arr[r]])
            l+=1
            r-=1
            # move each pointer until we find the next unique number or run out of numbers
            while l < r and arr[l] == arr[l-1]:
                l+=1
            while l < r and arr[r] == arr[r+1]:
                r-=1
        elif dfz > cSum:
            l+=1
        elif dfz < cSum:
            r-=1


tests = [
    [-3, 0, 1, 2, -1, 1, -2],   # [[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]
    [-5, 2, -1, -2, 3],         # [[-5,2,3],[-2,-1,3]]
]

for arr in tests:
    print(zeroTriplets(arr))


'''
Given an array of unsorted numbers, find the length of the smallest subarray that
(when sorted) will sort the whole array.

e.g. [1,3,2,0,-1,7,10] --> 5 i.e. sort the first 5 numbers and the entire array is sorted

Solution:
- define a subarray by shrinking the window l - r until we find numbers out of order
[1,|3,2,0,-1|,7,10]
- sub_min = -1, sub_max = 3
- add from left if greater than sub_min, else stop searching
- add from right if less than sub_max, else stop searching
- note that we know values outside the subarray are sorted
[|1,3,2,0,-1|,7,10]
- sort subarray

Algorithm
- init l and r at either end of arr
- l++ until l < l - 1
- r-- until r < r + 1
- subArr = arr[l:r+1]
- extend subArr l when l - 1 > l
- extend subArr r when r + 1 > r
'''



def findMinSort(arr):
    l = 0
    r = len(arr) - 1
    
    while l < len(arr) - 1 and arr[l] < arr[l+1]:
        l+=1
    if l == len(arr) - 1:
        return 0
    while r > -1 and arr[r] > arr[r-1]:
        r-=1
    
    subArr = arr[l:r+1]
    sbArMn = min(subArr)
    sbArMx = max(subArr)

    # extend window left to include elements greater than sbArMx
    while l > 0 and arr[l - 1] > sbArMn:
        l-=1
    # extend window right to include elements less than sbArMn
    while r < len(arr) - 1 and arr[r + 1] < sbArMx:
        r+=1

    return r - l + 1


    
tests = [
    [1,3,2,0,-1,7,10],      # 5
    [1,2,5,7,3,10,11,12],   # 3
    [1,2,3],                # 0
    [4,3,2,1],              # 4
    [12,7,8,1,2,0,10,11]    # 8
]

for arr in tests:
    print(findMinSort(arr))