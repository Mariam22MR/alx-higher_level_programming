#!/usr/bin/python3
"""
Defination of text file-reading function.
"""


def read_file(filename=""):
    """reads the whole file then print it to stdout."""
    with open(filename, encoding='utf-8') as the_file:
        print(the_file.read(), end="")
