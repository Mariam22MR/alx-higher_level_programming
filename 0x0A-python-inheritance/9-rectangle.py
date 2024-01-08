#!/usr/bin/python3
"""Defines class rectangle BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """intialization of new Rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """string representation method."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
