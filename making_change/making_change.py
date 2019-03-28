#!/usr/bin/python

import sys

# ways to get values up to 10
# 1 - with only pennies
# [1,1,1,1,1,1,1,1,1,1,1]
# 2 - with pennies and nickels
# [1,1,1,1,1,2,2,2,2,2,2]
# 3 - with pennies and nickels and dimes
# [1,1,1,1,1,2,2,2,2,2,3]
#  use this pattern to build the solution


def making_change(amount, denominations):
    # initialize placeholder list
    ways_to_get_amount = [0]*(amount+1)

    # base case
    ways_to_get_amount[0] = 1

    # loop through our denominations
    for denomination in denominations:
        # loop through values to update
        for i in range(denomination, amount+1):
            # for each value, we can add X more ways to get that value
            # where X is the amount of ways to get the smaller value corresponding to
            # our current value - the value of the denomination we are updating for
            # ex- there is 1 way to get 5-10c with only pennies
            # when we introduce nickels, there becomes 1 new way to get values
            # 5-9c and 2 new ways to get value 10c
            # since value@(5) + value@(5-5=0) = 1 + 1 = 2
            # and value@(10) + value@(10-5=5) = 1 + 2...etc...
            ways_to_get_amount[i] += ways_to_get_amount[i-denomination]

    return ways_to_get_amount[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
