#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use 0 for each missing integer
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the addition of the first elements and the addition of the second elements
    return (a[0] + b[0], a[1] + b[1])
