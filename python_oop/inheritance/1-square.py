#!/usr/bin/env python3
"""Define a square that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
