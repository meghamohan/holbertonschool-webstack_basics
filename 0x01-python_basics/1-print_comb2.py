#!/usr/bin/python3
"""
programs to print numbers from 0 to 99
"""
for i in range(0, 10):
    for j in range(0, 10):
        if i is 9 and j is 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
