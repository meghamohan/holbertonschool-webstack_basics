#!/usr/bin/python3
"""
program to print alphabet from a to z
"""
for l in range(ord('a'), ord('z') + 1):
    if chr(l) is not 'q' and chr(l) is not 'e':
        print("{}".format(chr(l)), end="")
