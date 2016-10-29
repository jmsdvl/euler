"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""
# Uses the pre-generated table of primes. See ../prime_gen.py
from os.path import abspath, dirname, join
PRIME_FILE = abspath(join(dirname(__file__), '..', 'data', 'primes.txt'))
TARGET_PRIME_INDEX = 10001

def solve():
    """
    >>> solve()
    104743
    """
    try:
        with open(PRIME_FILE) as fd:
            for index, prime in enumerate(fd, start=1):
                if index == TARGET_PRIME_INDEX:
                    return int(prime.strip())
            else:
                raise RuntimeError('Not enough primes in prime file: only {} primes present'.format(index))
    except (FileNotFoundError, IOError):
        print('Prime file not found or not at {}'.format(PRIME_FILE))
        raise

if __name__ == '__main__':
    solve()
