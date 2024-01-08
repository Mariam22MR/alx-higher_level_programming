#!/usr/bin/python3
"""
Define class and inherited class function.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is inherited instance of class."""
    if isinstance(obj, a_class):
        return True
    return False
