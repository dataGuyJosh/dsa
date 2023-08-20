'''
Fast & Slow Pointers
The fast and slow pointer approach (AKA the Hare & Tortoise algorithm)
is a pointer algorithm that uses two pointers which move through an array at different speeds.
This approach is especially useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds, the algorithm proves that the two pointers are bound to meet.
The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

When slow = 1 m/s & fast = 2 m/s,
all distances between two pointers reduce to two possibilities:
- fast is one step behind slow
- fast is two steps behind slow

Two scenarios:
- if fast is 1 step behind slow; fast moves 2 steps, slow moves 1 and they meet
- if fast is 2 steps behind slow; fast moves 2, slow moves 1 and we get the first scenario
  i.e. they will meet next iteration
'''

'''
Given the head of a Singly LinkedList,
write a function to determine if the LinkedList has a cycle in it or not.

Singly LinkedList
- every node contains a pointer to the next node
- allows traversal of data in one direction only
'''

# Classless Solution
# def hasCycle(arr):
#     slow = 0
#     fast = 0
#     while arr[fast] != None:
#         if fast + 2 > len(arr) - 1 :
#             fast = len(arr) - fast
#         else:
#             fast += 2

#         slow += 1
#         if arr[slow] == arr[fast]:
#             return True
#     return False


# tests = [
#     [1, 2, 3, 4, 5, 3],  # True
#     [1, 2, 3, 4, 5, 1],  # True
#     [1, 2, 3, 4, None]   # False
# ]

# for arr in tests:
#     print(hasCycle(arr))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def hasCycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast.value == slow.value:
            return True
    return False


n6 = Node(6)
n5 = Node(5, n6)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
n6.next = n3

nf = Node('f')
ne = Node('e', nf)
nd = Node('d', ne)
nc = Node('c', nd)
nb = Node('b', nc)
na = Node('a', nb)
nf.next = nb

nylw = Node('ylw')
nblu = Node('blu', nylw)
nred = Node('red', nblu)
npur = Node('pur', nred)
nora = Node('ora', npur)

print(
    hasCycle(n1),   # True
    hasCycle(na),   # False
    hasCycle(nora),  # Fasle
    sep='\n'
)


'''
Given an integer, write a function to determine if after repeatedly
replacing it with an integer equal to the sum of the square of all of its digits,
leads us to the number 1.

Example
23 --> True
2^2 + 3^2 = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^1 + 0^2 = 1 + 0 = 1

12 --> False
1^2 + 2^2 = 1 + 4             = 5
5^2                           = 25
2^2 + 5^2 = 4 + 25            = 29
2^2 + 9^2 = 4 + 81            = 85
8^2 + 5^2 = 64 + 25           = 89
8^2 + 9^2 = 64 + 81           = 145
...
5^2 + 8^2 = 25 + 64           = 89 --> we've hit a cycle!!!

A cycle is found if slow == fast, a cycle is not found if slow or fast equal 1.
'''


def leadsToOne(num):
    slow = num
    fast = num
    while True:
        slow = sumDigitSquares(slow)
        fast = sumDigitSquares(sumDigitSquares(fast))
        if slow == fast:
            return False
        if slow == 1 or fast == 1:
            return True


def sumDigitSquares(num):
    squareSum = 0
    while num > 0:
        # in the decimal system, n % 10 returns the first digit of n!
        first_digit = num % 10
        squareSum += first_digit ** 2
        # divide by 10 rounding down to remove the first digit!!
        num = num // 10
    return squareSum


tests = [
    23,  # True
    12  # False
]

for num in tests:
    print(leadsToOne(num))


'''
You are given an array of positive/negative numbers.

Suppose the array contains a number m at a particular index.
We will move forwards/backwards if m is positive/negative respectively.

Write a method to determine if the array has a cycle.

Note: The cycle should have more than one element and follow one direction which means
cycles should not contain both forward and backward movements.
'''


def hasCycle(arr):
    for i in range(len(arr)):
        slow = i
        fast = i
        forward = arr[i] > 0

        while True:
            slow = nextIndex(arr, forward, slow)
            fast = nextIndex(arr, forward, fast)
            if fast != -1:
                fast = nextIndex(arr, forward, fast)

            '''
            What are our break cases?
            - fast/slow pointer equals -1
            - fast equals slow i.e. cycle
            '''
            if fast == -1 or slow == -1 or fast == slow:
                break

        if fast != -1 and slow != -1 and slow == fast:
            return True

    return False


def nextIndex(arr, forward, ci):
    currForward = arr[ci] > 0
    # if next direction is different from current direction i.e. no cycle; return false
    if currForward != forward:
        return -1

    # using modulus to loop back to start of array
    # e.g. [1,2,3] (0 + 1) % 3 = 1, (3 + 1) % 3 = 1
    ni = (ci + arr[ci]) % len(arr)
    if ni < 0:
        ni += len(arr)

    # no movement and we can't have 1 element in a cycle
    if ni == ci:
        return -1

    return ni


tests = [
    [1, 2, -1, 2, 2],   # True
    [2, 2, -1, 2],      # True
    [2, 1, -1, -2]      # False
]

for arr in tests:
    print(hasCycle(arr))
