#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv) - 1

    if arg_num == 0:
        print("0 arguments.")
    elif arg_num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_num))
    for i, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(i, arg))
