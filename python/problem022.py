"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import re
from string import ascii_uppercase


NAMES_F = '../data/p022_names.txt'
VALUES = {ch:num for ch, num in zip(ascii_uppercase, range(1,27))}


def score_names():
    """
    >>> score_names()
    871198282
    """
    with open(NAMES_F) as fd:
        names = sorted(re.sub(r'"|\s', '', fd.read()).split(','))
    return sum(i * sum(VALUES[ch] for ch in name)
               for i, name in enumerate(names, start=1))
