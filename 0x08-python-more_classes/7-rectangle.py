#!/usr/bin/python3
"""
module for rectangle class
"""


class Rectangle:
    """Representation of rectangle

    Attributes:
        number_of_instances (int): number of active instances.
        print_symbol (any): can be any type.
    """

    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width=0, height=0):
        """Initialization of new rectangle

         Args:
            width: width of new rectangle.
            height: height of new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for private instancs width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instancs width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

  @property
    def height(self):
        """getter for private instancs height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instancs height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
         if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable string Representaton rectangle"""
        if is not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """Return string representation of Rectangle."""
        return 'Rectangl(' + str(self.width) + ', ' + str( self.heigh) + ')'

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
