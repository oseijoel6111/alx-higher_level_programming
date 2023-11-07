#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(name="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    """
    text = ""
    with open(name) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(name, "w") as w:
        w.write(text)
