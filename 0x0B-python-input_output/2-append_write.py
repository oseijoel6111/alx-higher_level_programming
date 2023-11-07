#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
