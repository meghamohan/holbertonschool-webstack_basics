#!/usr/bin/python3
"""
prints all the arguments
"""
from  sys import argv


if __name__ == "__main__":
    l = len(argv)
    if l is 1:
        print("{} arguments.".format(l - 1))
    elif l is 2:
        print("{} argument.".format(l - 1))
        print("{}: {}".format(l - 1, argv[1]))
    else:
        print("{} arguemnts:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, argv[i]))