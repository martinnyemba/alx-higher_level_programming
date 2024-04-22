#!/usr/bin/python3
"""Defines the Square (a special Rectangle)"""


class Square(Rectangke):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class contructor method

        Args:
            size (int):
            x (int):
            y (int)
            width (int)
            height (int):
        """
        super().__init__(id, x, y, width, height)
        self.size = width, height

    def __str__(self):
        """ magic method __str__ """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))
