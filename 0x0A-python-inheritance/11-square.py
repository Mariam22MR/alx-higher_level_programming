#!/usr/bin/python3
"""Define rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents square."""

    def __init__(self, size):
        """initialization of new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
