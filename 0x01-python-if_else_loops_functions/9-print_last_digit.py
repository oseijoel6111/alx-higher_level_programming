#!/usr/bin/python3

def print_last_digit(number):
    # Get the last digit using the modulus operator (%)
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit
