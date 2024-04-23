#!/usr/bin/python3
"""Defines the Square (a special Rectangle)"""
from models.rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """
        Update the values of the Square attributes.
        This method allows updating multiple attributes of the Square
        object at once.
        It accepts positional arguments (args) or keyword arguments (kwargs).

        Args:
            *args: Positional arguments representing the attributes in the
            order id, size, x, y.
            **kwargs: Keyword arguments representing the attributes with
            their respective names.
        """
        length = len(args)
        if length:  # checks if there are any positional arguments
            # iterates over the positional arguments using enumerate
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg

        #  If there are no positional arguments (length is 0)
        #  checks the keyword arguments (kwargs) using if "key" in kwargs
        else:
            if "id" in kwargs:
                #  retrieve value associated with specified key from kwargs
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.size = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def __str__(self):
        """
        Return a string representation of the Square object.
        This magic method __str__ is automatically called when using
        the str() function or when an object is converted to a string
        (e.g., through print).

        Returns:
            str: A string representing the Square object in the
            format "[Square] (id) x/y - size".
            Here, 'id' is the unique identifier, 'x' and 'y' are the
            coordinates, and 'size' is the size of the square.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def to_dictionary(self):
        """
        Convert the Square object to a dictionary.

        This method creates a dictionary representation of the Square
        object, including its attributes:

        Attributes:
            - id: Unique identifier of the Square.
            - size: Size of the Square.
            - x: x-coordinate of the Square's position.
            - y: y-coordinate of the Square's position.

        Returns:
            dict: A dictionary containing the attributes of the Square
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
