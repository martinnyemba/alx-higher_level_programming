#!/usr/bin/python3
"""Defines the Square (a special Rectangle)"""
from model.rectangle import Rectangle 


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class contructor method

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """ magic method __str__ """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))
