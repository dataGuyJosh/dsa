'''
A group of friends want to buy a bouquet of flowers.
The florist wants to maximize his number of new customers and the money he makes.

To do this, he decides he'll multiply the price of each flower by
the number of THAT customer's previously purchased flowers plus 1.

The first flower will be original price, (0 + 1) * price,
the next will be (1 + 1) * price and so on.

Given the size of the group of friends k,
the number of flowers they want to purchase
and the original prices of the flowers,
determine the minimum cost to purchase all of the flowers.

The number of flowers they want equals the length of the c array.
'''


'''
- sort price array
- each friend takes turns buying flowers, starting with the most expensive
- return price
'''




from collections import Counter
def getMinimumCost(k, c):
    c.sort(reverse=True)
    flower_count = Counter()
    current_friend = 0
    total_price = 0

    for f in c:
        total_price += (flower_count[current_friend] + 1) * f
        flower_count[current_friend] += 1
        if current_friend < k - 1:
            current_friend += 1
        else:
            current_friend = 0

    return (total_price)


tests = [
    [3, [1, 2, 3, 4]],  # 11
    [3, [2, 5, 6]],     # 13
    [2, [2, 5, 6]]      # 15
]

for k, c in tests:
    print(getMinimumCost(k, c))
