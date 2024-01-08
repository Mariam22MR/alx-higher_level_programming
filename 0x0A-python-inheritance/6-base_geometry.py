#!/usr/bin/python3
"""Define baseGeometry class for geometry"""


class BaseGeometry:
    """represent BaseGeometry class."""
    def area(self):
        """raise exception indicate that area() is not implemented"""
        raise Exception("area() is not implemented")
