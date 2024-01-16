#!/usr/bin/python3
"""
A module that prints text with newlines as called.
"""


def text_indentation(text):
    """
    A function that prints two new lines after each of the
    '.', '?', and ':' characters.

    Args:
        text: the text to be printed.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    indented = ""

    for c in text:
        if c in [".", "?", ":"]:
            indented += c + "\n\n"
        else:
            indented += c

    print("{}".format(indented), end="")
