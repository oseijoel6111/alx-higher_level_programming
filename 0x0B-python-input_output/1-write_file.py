#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    
    return num_characters_written
