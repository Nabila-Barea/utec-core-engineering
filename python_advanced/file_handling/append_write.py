#!/usr/bin/env python3
"""Append text to files."""


def append_write(filename="", text=""):
    """Append text and return the number of characters written."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
