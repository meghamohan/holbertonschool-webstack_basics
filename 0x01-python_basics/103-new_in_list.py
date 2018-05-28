#!/usr/bin/python3
"""
to replace an element in a list
"""


def new_in_list(my_list, idx, element):
    newList = []
    for i in range(len(my_list)):
        if i == idx:
            newList.append(element)
        else:
            newList.append(my_list[i])
    return newList
