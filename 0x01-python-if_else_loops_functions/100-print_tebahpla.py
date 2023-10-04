#!/usr/bin/python3
# Author -JOEL OSEI ACQUAH

for i in range(ord('z'), ord('A') - 1, -1):
    if i % 2 == 0:
        print("{}".format(chr(i).lower()), end='')
    else:
        print("{}".format(chr(i).upper()), end='')
