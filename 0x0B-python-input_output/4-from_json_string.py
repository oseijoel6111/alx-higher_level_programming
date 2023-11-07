#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json

def from_json_string(stri):
    """Return the Python object represent"""
    return json.loads(stri)
