#! /usr/bin/env python3
"""
The sum of the squares of the first ten natural numbers is,
            12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sum_squares(nums):
    return sum(n**2 for n in nums)


def square_sum(nums):
    return sum(nums) ** 2


def difference(nums):
    """
    >>> difference(range(11))
    2640
    >>> difference(range(101))
    25164150
    """
    return abs(sum_squares(nums) - square_sum(nums))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
