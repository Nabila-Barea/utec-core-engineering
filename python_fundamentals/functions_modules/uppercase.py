#!/usr/bin/env python3

def uppercase(str):
    for char in f"{str}":
        code = ord(char)
        if 97 <= code <= 122:
            print("{}".format(chr(code - 32)), end='')
        else:
            print("{}".format(char), end='')
    print()
