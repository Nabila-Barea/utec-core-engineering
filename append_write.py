#!/usr/bin/env python3
"""Module for appending strings to a text file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
