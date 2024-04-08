#!/usr/bin/python3

"""Module - that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """
    # Getter method for width property
    @property
    def width(self):
        return self.__width
    # Setter method for width property
    @width.setter
    def width(self, value):
        return self.__width = value
    # Instantiation of main method with optional: width and height

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def area(self):
        return (self.width * self.height)
    def perimeter(self):
        

if __name__ == '__main__':
    import doctest
    doctest.testmod('1-rectangle_test.txt')
