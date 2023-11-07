#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, user_first_name, user_last_name, user_age):
        """Initialize a new Student.
        """
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.age = user_age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
