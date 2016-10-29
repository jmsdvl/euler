#! /usr/bin/env python3
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def split_digits(num):
    """
    Splits an integral number into a tuple of its digits

    >>> split_digits(1234)
    (1, 2, 3, 4)
    """
    # I feel like this is somehow cheating, but it is kind of nice:
    # return tuple(str(num))
    output = []
    while num > 0:
        num, digit = divmod(num, 10)
        output.append(digit)
    return tuple(reversed(output))


def combine_digits(digits):
    """
    Combines a sequence of digits into an integral number

    >>> combine_digits([1, 2, 3, 4])
    1234
    """
    return sum(digit * (10**factor) for factor, digit in enumerate(reversed(digits)))


def is_palindrome(seq):
    """
    Basic predicate: True if the seq is palindromic

    >>> is_palindrome('samaroid dioramas')
    True
    """
    return seq == seq[::-1]


def largest_palindrome(digit_length=3):
    """
    >>> largest_palindrome(digit_length=2)
    9009
    >>> largest_palindrome()
    906609
    """
    start = 10 ** (digit_length - 1)
    stop = 10 ** digit_length
    #  Not the fastest or cleverest, but tolerable
    return max(product
               for product in (i*j for i in range(start, stop)
                                   for j in range(i, stop))
               if is_palindrome(split_digits(product)))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
