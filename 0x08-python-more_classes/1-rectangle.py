#!/usr/bin/python3

"""Module - that defines a rectangle"""


class Rectangle():
    """class Rectangle that defines a rectangle"""
    #  Getter method for width property
    @property
    def width(self):
        return self.__width

    #  Setter method for width property
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    #  property getter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    #  Instantiation of main method with optional: width and height
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
