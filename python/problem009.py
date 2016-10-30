"""
Special Pythagorean Triplets.

A Pythagorean Triplet is a set of natural numbers a, b, and c such that:
    a^2 + b^2 = c^2

There exists exactly one Pythagorean Triplet such that a + b + c = 1000.
What is the value of a * b * c for that Triplet?

Handy discussion of how to generate triples:
    http://mathforum.org/library/drmath/view/55811.html
"""


def triples(m=2,n=1): 
    """ 
    Infinitly returns all (not just primitive) 
    Pythagorean Triplets as a tuple of ints, (a, b, c)
    for a^2 + b^2 = c^2.

    If m, n are given, changes the point of generation.
    """
    while True:
        while m > n:
            yield (m**2 - n**2), (2*m*n), (m**2 + n**2)
            n += 1
        m += 1
        n = 1


def solve():
    """
    >>> solve()
    31875000
    """
    for a, b, c in triples():
        assert a**2 + b**2 == c**2
        if a + b + c == 1000:
            return a*b*c
