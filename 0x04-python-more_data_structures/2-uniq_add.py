#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for n in set(my_list):
            add = add + n
    return add
