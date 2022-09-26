#!/usr/bin/python3
"""
Defines a class
"""


class MyList(list):
    """a class that inherits list"""

    def print_sorted(self):
        """print the list in sorted order"""
        print(sorted(self))
