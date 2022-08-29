#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    result = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return result[0:2]
