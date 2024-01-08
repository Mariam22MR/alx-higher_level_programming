#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first integer.
        b: second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        sum of the two integers.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
