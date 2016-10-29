#! /usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime_factor(n=600851475143):
    """
    >>> largest_prime_factor(n=13195)
    29
    >>> largest_prime_factor()
    6857
    """
    # factor out all the twos
    if n % 2 == 0:
        last_factor = 2
        while n % 2 == 0:
            # NOTE: you will get the correct answer using truediv, but it will
            # be of type `float`, which makes no sense in the context and causes
            # the doctests to fail
            n //= 2
    else:
        last_factor = 1

    # deal with larger odd nums
    factor = 3
    max_factor = int(n**0.5)
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            last_factor = factor
            while n % factor == 0:
                # see above NOTE on floordiv vs truediv
                n //= factor
            max_factor = int(n**0.5)
        factor += 2

    return last_factor if n == 1 else n


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
