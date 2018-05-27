#!/usr/bin/python3
"""
checks for lowercase characters
"""
def islower(c):
    if ord(c) > 91:
        return(True)
    else:
        return(False)
