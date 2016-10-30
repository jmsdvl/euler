"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# NOTE: we're moving along the *edges* of the grid, not from square to square.
# Essentially we're being asked to find the number of "lattice paths" from the
# point (0, 0) to (20, 20); which is the binomial coefficient
#       20 + 20 Choose 20 == 40 C 20 == 40!/20!20! == 40*39*...*21/20!
#

import math

class MathException(Exception):
    pass


def lattice_paths(x, y):
    """
    >>> lattice_paths(20, 20)
    137846528820
    """
    n = x+y 
    k = x or y
    n_choose_k = math.factorial(n) / (math.factorial(n-k) * math.factorial(k))
    if n_choose_k.is_integer():
        return int(n_choose_k)
    else:
        raise MathException('Expected Binomial Coefficent to be an Integer')
