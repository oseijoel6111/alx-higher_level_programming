#!/usr/bin/python3
# Author - JOEL OSEI ACQUAH

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    result = ""
    for i in range(len(str)):
        if i != n:
            result += str[i]
    
    return result