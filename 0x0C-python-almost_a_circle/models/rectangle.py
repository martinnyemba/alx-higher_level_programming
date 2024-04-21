#!/usr/bin/python3
"""This moudle defines the Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get method for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter  method for the width of the Rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get method for the heigt  of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the Rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @height.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle."""
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @height.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle."""
        self.__y = value
