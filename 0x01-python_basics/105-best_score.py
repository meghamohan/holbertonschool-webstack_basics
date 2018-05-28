#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        maxValue = max(my_dict.values())
        for k, v in my_dict.items():
            if v == maxValue:
                return k
    return None
