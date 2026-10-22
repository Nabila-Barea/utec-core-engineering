#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        code = ord(char)
        if 97 <= code <= 122:
            char = chr(code - 32)
        result += char
    print(result)
