#! /usr/bin/env python3
"""
Edit distance funcs
"""


def min_edits(A:str, B:str) -> int:
    """
    Returns the minimum edit distance between strings A and B

    >>> min_edits('intention', 'execution')
    8
    """
    # compute a table of distances
    table = [[0 for _ in range(len(A)+1)]   # rows correspond to A
             for _ in range(len(B)+1)]      # cols correspond to B

    # initialize the top row and left column of the table
    table[0][1:] = list(range(1, len(A)+1))
    for x in range(1, len(B)+1):
        table[x][0] = x

    for i, _ in enumerate(A, start=1):
        for j, _ in enumerate(B, start=1):
            table[j][i] = min(table[i-1][j] + 1,
                              table[i][j-1] + 1,
                              table[i-1][j-1] + (0 if A[i-1] == B[j-1] else 2))

    return table


if __name__ == '__main__':
    import sys
    A, B = sys.argv[1:3]
    print('      ', end='')
    print(''.join(['{:>3}'.format(ch) for ch in A]))
    for ch, row in zip(' '+B, min_edits(A, B)):
        print('{:>3}{}'.format(ch, ''.join(['{:>3}'.format(n) for n in row])))
