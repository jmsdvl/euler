#! /usr/bin/env python3
"""
The four adjacent digits in the 1000-digit number that have the greatest product
are 9 × 9 × 8 × 9 = 5832.

    # see NUM below

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""
from collections import deque
from functools import reduce
from itertools import islice, tee
from operator import mul


NUM = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

## Use a special sentinel object instead of None for next calls
_SENTINEL = object()


def consume(iterator, n):
    """ From the doc's itertools examples """
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), _SENTINEL)


def chunks(stream, size=13, pred=lambda v: True):
    """
    Return tuple chunks from the stream of size ``size``.  If ``pred`` is
    given, skip any chunks for which ``pred`` returns false.
    """
    iterators = tee(stream, size)

    # prime the iterators
    for index, iterator in enumerate(iterators):
        consume(iterator, index)

    # prime the while loop
    values = tuple(next(it, _SENTINEL) for it in iterators)
    while not any(val is _SENTINEL for val in values):
        if pred(values):
            yield values
        values = tuple(next(it, _SENTINEL) for it in iterators)


def main(chunk_size):
    """
    >>> main(chunk_size=4)
    5832
    >>> main(chunk_size=13)
    23514624000
    """
    values = (int(c) for c in NUM if c in '0123456789')
    chunked_vals = chunks(values, size=chunk_size, pred=lambda vals: 0 not in vals)
    products = (reduce(mul, chunk) for chunk in chunked_vals)
    return max(products)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
