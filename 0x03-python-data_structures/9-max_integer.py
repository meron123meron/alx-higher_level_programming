#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    start = my_list[0]
    for i in range(len(my_list) - 1):
        if start < my_list[i]:
            start = my_list[i]
    return start
