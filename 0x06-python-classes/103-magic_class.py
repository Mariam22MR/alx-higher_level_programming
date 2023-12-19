#!/usr/bin/python3
"""Defind MagicClass matching exactly bytecode provided by ALX."""


import math


class MagicClass:
    """Represent circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass.
        Args:
            radius (float or int): the radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """return area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of MagicClass."""
        return (2 * math.pi * self.__radius)
