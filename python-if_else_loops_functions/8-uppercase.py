#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= char <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
