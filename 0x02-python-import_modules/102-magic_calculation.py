#!/usr/bin/python3

def magic_calculation(a, b):
    """
    This function performs a calculation based on the values of 'a' and 'b'.
    If 'a' is less than 'b', it performs a series of additions and returns the result.
    Otherwise, it performs a subtraction and returns the result.
    """
    # Import the 'add' and 'sub' functions from an external module
    from magic_calculation_102 import add, sub

    # Check if 'a' is less than 'b'
    if a < b:
        # If 'a' is less than 'b', perform a series of additions
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c

    else:
        # If 'a' is not less than 'b', perform a subtraction
        return sub(a, b)
