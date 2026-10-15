#!/usr/bin/env python3

def uppercase(s):
    result = ''
    for char in f"{s}":
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
