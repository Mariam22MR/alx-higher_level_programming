#!/usr/bin/python3
"""
Defines inherited class function.
"""


def inherits_from(obj, a_class):
    """checks if obj is inherited instance of class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
