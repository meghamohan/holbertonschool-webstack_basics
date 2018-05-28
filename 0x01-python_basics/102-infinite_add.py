#!/usr/bin/python3
from sys import argv


def infinite_add():
    """
    for infinite addition
    """
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)

if __name__ == "__main__":
    infinite_add()
