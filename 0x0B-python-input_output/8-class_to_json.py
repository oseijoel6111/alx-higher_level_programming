#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(ob):
    """Return the dictionary represntation of a simple data structure."""
    return ob.__dict__
