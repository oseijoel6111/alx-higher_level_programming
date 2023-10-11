#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    result = 0
    for num in my_list:
        if num not in unique_integers:
            result += num
            unique_integers.add(num)

    return result
