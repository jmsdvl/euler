"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
from itertools import permutations, islice


def nth(iterable, n):
    return next(islice(iterable, n, None), None)


def combine(digits):
    return sum(d * 10**i for i, d in enumerate(reversed(digits)))


def brute_force_solution():
    """
    >>> brute_force_solution()
    2783915460
    """
    # 999999, not 1000000, because zero-indexing
    return combine(nth(permutations(range(10)), 999999)) 
