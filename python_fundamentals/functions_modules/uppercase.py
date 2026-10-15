#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in f"{str}":
        code = ord(char)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += char
    print(result)
