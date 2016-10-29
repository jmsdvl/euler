"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_in_range(start, stop, *mults):
    """
    >>> sum_multiples_in_range(1, 10, 3, 5)
    23
    >>> sum_multiples_in_range(1, 1000, 3, 5)
    233168
    """
    return sum(n for n in range(start, stop) if any(n % m == 0 for m in mults))
