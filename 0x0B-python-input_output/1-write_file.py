#!/usr/bin/python3
"""Defination of file-writing function."""


def write_file(filename="", text=""):
    """
    Args:
        filename(str) : name of the file
        text(str) : text to write
    Return:
        number of characters that are written
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
