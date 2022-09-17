#!/usr/bin/python3

"""This is 0-add_integer module
which contains one function.

"""

def add_integer(a, b=98):

    """adds two integers
    a and b

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
