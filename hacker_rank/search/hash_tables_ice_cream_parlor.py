
'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor,
they pool their money to buy ice cream. On any given day, 
the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of "money" and the "cost" of each flavor for t trips
to the Ice Cream Parlor, help Sunny and Johnny choose
two distinct flavors such that they spend their entire pool of money during each visit.
ID numbers are the 1- based index number associated with a "cost".

For each trip to the parlor, print the ID numbers for the two types of ice cream
that Sunny and Johnny purchase as two space-separated integers on a new line.
You must print the smaller ID first and the larger ID second.

Proposed algorithm --> two pointers
- enumerate cost array
- sort by cost
- remove duplicate cost icecreams?
- find max cost lower than money
- add min
  - if equal to money, return indexes
  - if less than money, find next cheapest
  - if greater than money, find next expensive
'''


def whatFlavors(cost, money):
    # track indices and sort by price
    cost = [[idx, c]for idx, c in enumerate(cost)]
    cost.sort(key=lambda x: x[1])
    l = 0
    r = len(cost) - 1

    while l != r:
        li = cost[l][0] + 1
        ri = cost[r][0] + 1
        price = cost[l][1] + cost[r][1]

        if price == money:
            indices = [li,ri]
            indices.sort()
            print(' '.join([str(i) for i in indices]))
            break
        elif price < money:
            l += 1
        else:  # price > money
            r -= 1


tests = [
    [[2, 1, 3, 5, 6], 5],   # 1 3
    [[4, 3, 2, 5, 7], 8],   # 2 4
    [[7, 2, 5, 4, 11], 12]   # 1 3
]

for c, m in tests:
    whatFlavors(c, m)
