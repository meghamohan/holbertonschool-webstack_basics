#!/usr/bin/python3
"""
checks for lowercase characters
"""
def islower(c):
    """
    checks for lowercase characters
    """
    if ord(c) > 91:
        return(True)
    else:
        return(False)
