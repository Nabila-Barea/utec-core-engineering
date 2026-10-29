#!/usr/bin/env python3
"""Define a square that inherits from Rectangle."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square."""

    def __str__(self):
        """Return the square description."""
        description = super().__str__()
        dimensions = description.split("] ", 1)[1]
        return "[Square] {}".format(dimensions)
