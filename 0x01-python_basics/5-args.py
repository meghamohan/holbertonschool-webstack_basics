#!/usr/bin/python3
"""
prints all the arguments
"""
import sys


def args(a):
    """
    prints number and the arg
    """
    l = len(a)
    if l is 1:
        print("{} arguments.".format(l - 1))
    elif l is 2:
        print("{} argument.".format(l - 1))
        print("{}: {}".format(l - 1, a[1]))
    else:
        print("{} arguemnts:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, a[i]))
if __name__ == "__main__":
    args(sys.argv)
