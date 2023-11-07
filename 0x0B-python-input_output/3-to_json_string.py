#!/usr/bin/python3
"""Defines a string-to-JSON."""
import json

def to_json_string(obj):
    """Return the JSON representation of a string object."""
    return json.dumps(obj)
