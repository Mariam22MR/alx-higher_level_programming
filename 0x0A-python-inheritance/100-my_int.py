#!/usr/bin/python3
"""Define class MyInt inherit from int."""


class MyInt(int):
    """custom int class that invert == , != operators."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
