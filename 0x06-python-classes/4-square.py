#!/usr/bin/python3

"""Ddefine Sqaure class"""


class Square:
    """  a class Square that represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """

        self.size = size

    @property
    def size(self):
        """ Define a getter method"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """define a setter method"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""

        return (self.__size * self.__size)
