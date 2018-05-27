#1/usr/bin/python3
def max_integer(my_list=[]):
    """
    find the biggest integer
    """
    if len(my_list) is 0:
        return None
    maxValue = my_list[0]
    for n in my_list:
        if n >= maxValue:
            maxValue = n
    return maxValue
