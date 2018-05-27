#!/usr/bin/python3
"""
program that removes c/C of a string
"""


def no_c(str):
    newStr = ''
    for i in str:
        if i is not 'c' and i is not 'C':
            newStr += i
    return newStr
