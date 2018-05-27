#!/usr/bin/python3
def add_integer(a, b):
    """
    adds 2 integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a + b)
