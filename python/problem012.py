"""
What is the value of the first Triangle Number to have over 500 divisors?
The sequence of triangle numbers is generated by adding the natural numbers.
So the seventh triangle number is 28 = 1 + 2 + 3 + 4 + 5 + 6 + 7, and it is
also the first to have over five divisors.
"""

from itertools import count
from functools import reduce
from math import sqrt

def triangle_num():
    """ Generator: iterates over the sequence of triangle nums. """
    tnum = 1
    for num in count(2):
        yield tnum
        tnum += num


# TODO: find the original stackoverflow that got me this version
# TODO: speed this sucker up, its slow
def factors(n):
    return set(reduce(list.__add__, 
                      ([i, n//i] 
                       for i in range(1, int(n**0.5)+1)
                       if n % i == 0)))


def solve():
    """
    >>> solve()
    76576500
    """
    for tnum in triangle_num():
        f = factors(tnum)
        if len(f) > 500:
            return tnum
