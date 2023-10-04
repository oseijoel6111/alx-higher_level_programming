#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""
for i in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(i)), end='')
