#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
