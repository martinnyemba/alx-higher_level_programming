#!/usr/bin/python3
"""Base class module"""


class Base:
    """This class is the “base” of all other classes in this project

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    #  constructor method
    def __init__(self, id=None):
        """class constructor method

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
