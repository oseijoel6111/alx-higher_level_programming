#!/usr/bin/python3
# Author - JOEL OSEI ACQUAH

def magic_calculation(a, b, c):
    result = 0

    if a < b:
        result = c
    elif c > b:
        result = a + b
    else:
        result = a * b - c

    return result
