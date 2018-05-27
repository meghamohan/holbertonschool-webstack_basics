#!/usr/bin/python3
"""
replaces an element of a list
"""


def replace_in_list(my_list, idx, element):
    """
    replaces element of a list
    """
    l = len(my_list)
    if idx >= l or idx < 0:
        return my_list
    else:
        my_list[idx] = element
    return my_list
