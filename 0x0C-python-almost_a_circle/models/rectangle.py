#!/usr/bin/python3
"""Defines rectangle class."""
from models.base import Base


class Rectangle(Base):
    """represents rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            id (int): identity of new Rectangle.
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
            x (int): x coordinate of new Rectangle.
            y (int): y coordinate of new Rectangl.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """Method for validating value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Return area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints string representation of this rectangle."""
        s = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(s, end='')

    def __str__(self):
        """returns print() and str() representation of Rectangle."""
        return "[{}] ({}) {}/{} - {}/{}".
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updates instance attributes via no-keyword & keyword args."""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
