#! /usr/bin/env python3
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
# This is essentially finding the least common multiple for the set {2,3,...,20}
from functools import reduce
from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_many(numbers):
    """
    Finds the least common multiple of the set of numbers

    >>> lcm_many(range(1,11))
    2520
    >>> lcm_many(range(1,21))
    232792560
    """
    return reduce(lcm, numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
