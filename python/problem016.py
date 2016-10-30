"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

def iterative(num):
    """
    >>> iterative(2**1000)
    1366
    """
    total = 0
    while num > 0:
        num, digit = divmod(num, 10) 
        total += digit
    return total


def recursive(inp):
    """
    >>> recursive(2**1000)
    1366
    """
    if inp == 0:
        return 0
    num, digit = divmod(inp, 10)
    return recursive(num) + digit
