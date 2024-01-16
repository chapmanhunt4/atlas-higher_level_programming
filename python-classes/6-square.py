#!/usr/bin/python3

"""
This module defines a class Square with an attribute size.
"""


class Square:
    """
    The Square class with a size attribute.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Parameters:
        size (int): The size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value: the value to set as size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute

        Args:
            value: value to set as position
        """
        error = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(error)
        for i in value:
            if (type(i) is int and i < 0) or type(i) is not int:
                raise TypeError(error)
        else:
            self.__position = value

    def area(self):
        """
        A method of the class that finds area.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the area and position.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print(" " * self.position[0], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
