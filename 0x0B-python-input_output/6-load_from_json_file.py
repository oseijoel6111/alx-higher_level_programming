#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json

def load_from_json_file(name):
    """Create a Python obj from a JSON file."""
    with open(name) as file:
        return json.load(file)
