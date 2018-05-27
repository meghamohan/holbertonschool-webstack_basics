#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    """
    prints a dictionary ordered keys
    """
    keys = sorted(my_dict)
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))
