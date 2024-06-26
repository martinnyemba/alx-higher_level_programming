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

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Draw a rectangle using '#' characters.

        Returns:
            str: String representation of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        #  Create the rectangle using a list comprehension
        rect = ['#' * self.__width for _ in range(self.__height)]

        # Join the rows with newline characters
        return "\n".join(rect)
