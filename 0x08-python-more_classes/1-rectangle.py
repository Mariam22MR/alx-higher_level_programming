#!/usr/bin/python3
"""
define class for rectangle
"""


class Rectangle:
    """Represent rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get for private instans width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instans width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get for private instans height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
         """setter for private instans width of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
