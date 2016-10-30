"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""
# I've always hated these problems; off-by-one errors are very easy to make and
# not quite so easy to track down

DEBUG = False

NUMBER_DICT_FILE = '../data/number_word_dict.txt'
DICTIONARY = {}

with open(NUMBER_DICT_FILE) as fd:
    for line in fd:
        num, word = line.strip().split(' ')
        DICTIONARY[int(num)] = word

DICTIONARY[0] = ''  # don't count zeros
HUNDRED = 'HUNDRED'
AND = 'AND'


if DEBUG:
    for k, v in DICTIONARY.items():
        print(k, ':\t', len(v))


def num_to_words(num):
    """
    >>> num_to_words(0)
    ('',)
    >>> num_to_words(12)
    ('TWELVE',)
    >>> num_to_words(89)
    ('EIGHTY', 'NINE')
    >>> num_to_words(200)
    ('TWO', 'HUNDRED')
    >>> num_to_words(675)
    ('SIX', 'HUNDRED', 'AND', 'SEVENTY', 'FIVE')
    >>> num_to_words(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError
    """
    if num < 0:
        raise ValueError('Number less than 0 is not supported')
    elif num < 20:
        return (DICTIONARY[num], )  # 1-tuple
    elif num < 100:
        tens, ones = divmod(num, 10)
        return (DICTIONARY[tens*10], DICTIONARY[ones])
    elif num < 1000:
        hundreds, rest = divmod(num, 100)
        output = (DICTIONARY[hundreds], HUNDRED)
        if rest > 0:
            output += (AND,)
            output += num_to_words(rest)
        return output


def count_letters(word_seq):
    """
    >>> count_letters(num_to_words(0))
    0
    >>> count_letters(num_to_words(89))
    10
    >>> count_letters(num_to_words(342))
    23
    >>> count_letters(num_to_words(115))
    20
    >>> count_letters(['ONE', 'THOUSAND'])
    11
    """
    return sum(len(word) for word in word_seq)


def solve():
    """
    Deals with the edge case (1000) in a pretty dumb way.
    >>> solve()
    21124
    """
    count = sum(count_letters(num_to_words(num)) for num in range(1000))
    count += count_letters(['one', 'thousand'])
    return count


if __name__ == '__main__':
    if DEBUG:
        for num in range(1000):
            words = num_to_words(num)
            print(num, words, count_letters(words))
    print(solve())
