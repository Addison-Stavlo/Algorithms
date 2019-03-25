#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):

    pass


def number_of_permutations(list):
    # for list of size N with repeating elements of amounts A, B, etc..
    # number of permutations is given by N! / (A!B!...);
    N = len(list)
    A = list.count(3)
    B = list.count(2)
    C = list.count(1)
    return math.factorial(N) / (math.factorial(A)*math.factorial(B)*math.factorial(C))


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
