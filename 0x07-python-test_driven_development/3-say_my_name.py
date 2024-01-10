#!/usr/bin/python3
"""
Module for say_my_name method.
"""


def say_my_name(first_name, last_name=""):
    """method for print first name  and last name.

    Args:
        first_name (str): first name to print.
        last_name (str): last name to print.
    Raises:
        TypeError: if either of first_name or last_name not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
