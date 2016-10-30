""" 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

PRIMES_FILE = '../data/primes.txt'
VALUE_CAP = 2e6

def solve():
    """
    >>> solve()
    142913828922
    """
    total = 0
    with open(PRIMES_FILE) as fd:
        for prime in fd:
            value = int(prime.strip())
            if value > VALUE_CAP:
                break
            total += int(prime.strip())
        return total
