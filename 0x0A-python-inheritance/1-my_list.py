#!/usr/bin/python3
"""Define child list class MyList."""


class MyList(list):
    """class is child of built-in list class."""
    def print_sorted(self):
        """prints sorted list."""
        print(sorted(self))
