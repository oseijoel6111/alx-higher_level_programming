#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter (ASCII values 97 to 122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert the character to uppercase using the ASCII value difference (32)
            char = chr(ord(char) - 32)
        # Print the character without a newline
        print(char, end='')

    print()
