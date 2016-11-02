"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math


def digits(num):
    while num > 0:
        num, digit = divmod(num, 10)
        yield digit


def sum_digits(num):
    """
    >>> sum_digits(math.factorial(100))
    648
    """
    return sum(digits(num))
