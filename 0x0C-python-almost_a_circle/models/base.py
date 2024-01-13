#!/usr/bin/python3
"""Module for Base class."""
from json import dumps, loads
import csv


class Base:
    """representation of the base of our OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """This initialize new Base.

        Args:
            id (int): the identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

