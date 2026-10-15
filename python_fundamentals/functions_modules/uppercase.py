#!/usr/bin/env python3

def uppercase(str):
    for char in "{}".format(str):
        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(chr(ord(char))), end='')
    print()
