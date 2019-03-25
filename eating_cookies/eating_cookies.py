#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    num_permutations = 0
    solutions = []
    # find solution with most 3's
    if n % 3 == 0:
        sol = [3]*int(n/3)
        solutions.append(sol)
    elif n % 3 == 1:
        sol = [3]*(math.floor(n/3))
        sol.append(1)
        solutions.append(sol)
    else:
        sol1 = [3]*math.floor(n/3)
        sol1.append(2)
        solutions.append(sol1)
        sol2 = [3]*math.floor(n/3)
        sol2.append(1)
        sol2.append(1)
        solutions.append(sol2)
    return solutions


print(eating_cookies(2))


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
