#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return my_list.copy()
    elif idx not in range(len(my_list)):
        return my_list.copy()
    else:
        new_list[idx] = element
        return new_list.copy()
