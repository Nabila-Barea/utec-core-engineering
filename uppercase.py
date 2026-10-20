#!/usr/bin/env python3


def uppercase(str):
    for char in str:
        code = ord(char)
        if 97 <= code <= 122:
            print(chr(code - 32), end="")
        else:
            print(char, end="")
    print()
