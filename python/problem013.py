""" 
Work out the first ten digits of the sum of the following 100 50-digit
numbers (see the associated data file)

>>> total = 0
>>> with open('../data/problem13_100_nums.txt') as fd:
...     for line in fd:
...         total += int(line)
>>> int(str(total)[:10])
5537376230
"""

pass
