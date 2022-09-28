#!/usr/bin/python3
"""Defines a function that appends.."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
