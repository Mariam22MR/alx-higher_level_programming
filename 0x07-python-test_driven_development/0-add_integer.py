#!/usr/bin/python3
"""script that define function for int add."""


def add_integer(a, b=98):
    """adds two integers.

    Args:
        a: first integer.
        b: second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        sum of two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
