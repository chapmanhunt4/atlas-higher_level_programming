#!/isr/bin/python3

"""
A module with the lookup method, that returns a list of all
methodsand attributes.
"""


def lookup(obj):
    """
    The lookup function acceps an object and returns a list
    of all methods and attributes.

    Parameters:
        obj: the object to be searvhed
    """

    return dir(obj)
