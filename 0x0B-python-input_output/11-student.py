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

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        """
        for k, v in json.items():
            setattr(self, k, v)
