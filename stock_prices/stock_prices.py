#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # for each number
    # find the largest value that comes after it in list
    # take difference
    # set difference as answer if difference is bigger than answer
    largest_gain = prices[1] - prices[0]

    i = 0
    while i < len(prices)-1:
        largest_successor = prices[i+1]
        for price in prices[i+1:]:
            if price > largest_successor:
                largest_successor = price
        temp_largest_gain = largest_successor - prices[i]
        if largest_gain < temp_largest_gain:
            largest_gain = temp_largest_gain
        i += 1
    return largest_gain


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
