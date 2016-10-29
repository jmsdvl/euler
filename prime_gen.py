#! /usr/bin/env python
"""
Many Project Euler problems require primes in some way; generating huge
arrays of primes is slow and boring. So use this script to pre-generate
any primes needed and save them to `./data`; these can then be read by
problem answer scripts as needed
"""
from itertools import compress, count, cycle, islice

def erat3():
    # http://stackoverflow.com/a/3796442
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0) 
    MODULI = frozenset([1, 7, 11, 13, 17, 19, 23, 29])

    for q in compress(islice(count(7), 0, None, 2), cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x % 30) not in MODULI:
                x += 2*p
            D[x] = p


def gen_until(generator, num):
    """ Produces ``num`` values from ``generator`` """
    #next(generator)  # prime the generator
    counter = count(1)
    while next(counter) < num:
        yield next(generator)


def write_primes(fd, num, delimiter='\n'):
    for value in gen_until(erat3(), num):
        fd.write(str(value))
        fd.write(delimiter)


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('num', nargs='?', type=int, default=1e6, help='Number of primes to generate')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default='data/primes.txt', help='File to write primes to')
    parser.add_argument('-d', '--delimiter', default='\n', help='Delimits primes')

    args = parser.parse_args()
    write_primes(args.output, args.num, args.delimiter)
