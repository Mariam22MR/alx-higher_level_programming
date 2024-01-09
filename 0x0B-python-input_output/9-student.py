#!/usr/bin/python3
"""defination of class student."""


class Student:
    """representation of student."""

    def __init__(self, first_name, last_name, age):
        """initialization of new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets dictionary representation of Student."""
        return self.__dict__
