#!/usr/bin/python3
"""Define class rectangle BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """That represents rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """intialization of new rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
