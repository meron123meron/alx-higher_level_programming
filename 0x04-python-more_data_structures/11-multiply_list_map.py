#!/usr/bin/python
def multiply_list_map(my_list=[], number=0):
    new = list(map(lambda i: i * number, my_list))
    return new
