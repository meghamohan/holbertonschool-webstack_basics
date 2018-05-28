#!/usr/bin/python3
"""
to print diagonals
"""


def print_diagonal(n):
    """
    prints a diagonal
    """
    if n <= 0:
        print()
    else:
        [print((' ' * i) + '\\') for i in range(n)]
        print()
