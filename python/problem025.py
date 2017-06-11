"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

# with every order of magnitude, the number of digits increases by one
# therefore the digit length of a number is equal to the power to which we must
# raise 10 to reduce that number to 0 plus one.


def fibo():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a+b


def find_term():
    """
    >>> find_term()
    4782
    """
    magnitude = 10
    digit_len = 1
    for i, fib in enumerate(fibo()):
        while fib > magnitude:
            magnitude *= 10
            digit_len += 1
            if digit_len == 1000:
                return i
