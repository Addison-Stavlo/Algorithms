#!/usr/bin/python

import sys
import math


def rock_paper_scissors(n):
    ans_list = []
    permutations_made = 0
    # 3^n is the number of possibilities
    rps = ['rock', 'paper', 'scissors']
    while permutations_made < 3**n:
        permutation = [None]*n
        index = 1

        while index <= n:

            permutation[n -
                        index] = rps[math.floor(permutations_made/(3**(index-1))) % 3]

            index += 1

        ans_list.append(permutation)
        permutations_made += 1

    return ans_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
