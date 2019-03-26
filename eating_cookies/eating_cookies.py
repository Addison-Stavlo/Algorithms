#!/usr/bin/python

import sys
import math
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def number_of_permutations(solution):
        # for list of size N with repeating elements of amounts A, B, etc..
        # number of permutations is given by N! / (A!B!...);
    N = len(solution)
    A = solution.count(3)
    B = solution.count(2)
    C = solution.count(1)
    return math.factorial(N) / (math.factorial(A)*math.factorial(B)*math.factorial(C))


def eating_cookies(n, cache=None):
    num_permutations = 0
    solutions = []

    most_3s = math.floor(n/3)
    # find solution(s) with most 3's
    if n % 3 == 0:
        sol = [3]*most_3s
        solutions.append(sol)
    elif n % 3 == 1:
      # 3s with a 1
        sol = [3]*most_3s
        sol.append(1)
        solutions.append(sol)
    else:
      # 3s with 1,1 or 3s with a 2
        sol1 = [3]*most_3s
        sol1.append(2)
        solutions.append(sol1)
        sol2 = [3]*most_3s
        sol2 = sol2 + [1, 1]
        solutions.append(sol2)

    # extract possible solutions from top level solutions found above
    while most_3s > 0:
        for solution in solutions:
            if solution.count(3) == most_3s:
                # assign new solutions for replacing 3 with 2,1 and 1,1,1
                newSol1 = solution[:]
                newSol2 = solution[:]
                newSol1.remove(3)
                newSol1 = newSol1 + [2, 1]
                newSol2.remove(3)
                newSol2 = newSol2 + [1, 1, 1]
                newSol1.sort(reverse=True)
                newSol2.sort(reverse=True)
                if newSol1 not in solutions:
                    solutions.append(newSol1)
                if newSol2 not in solutions:
                    solutions.append(newSol2)

                # assign new solution for replacing 3 and 1 with 2,2
                if solution.count(1) > 0:
                    newSol3 = solution[:]
                    newSol3.remove(3)
                    newSol3.remove(1)
                    newSol3 = newSol3 + [2, 2]
                    newSol3.sort(reverse=True)
                    if newSol3 not in solutions:
                        solutions.append(newSol3)

        most_3s -= 1

    # add the number of permutations possible for each solution
    for solution in solutions:
        num_permutations += number_of_permutations(solution)

    return int(num_permutations)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
