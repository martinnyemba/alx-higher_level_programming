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
        #  validation of width setter methods and instantiation
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get method for the heigt  of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the Rectangle."""
        #  validation of height setter methods and instantiation
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @height.setter
    def x(self, value):
        """Set the x coordinate of the Rectangle."""
        #  validation of x setter methods and instantiation
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        #  validation of y setter methods and instantiation
        return self.__y

    @height.setter
    def y(self, value):
        """Set the y coordinate of the Rectangle."""
        #  validation of y setter methods and instantiation
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    
    def area(self):
        """Defines the area value of the Rectangle instance.

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        Returns:
            Area (int): width * height
        """
        return self.width * self.height

    
    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range (self.height):
            print("" * self.x, end="")
            print("#" * self.width)
    
    def __str__(self):
        """the __str__ method
        returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
