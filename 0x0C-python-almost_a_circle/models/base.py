#!/usr/bin/python3
"""Base class module"""


class Base:
    """This class is the “base” of all other classes in this project"""

    __nb_objects = 0

    #  constructor method
    def __init__(self, id=None):
        """class constructor method"""
        if self.id != None:
            self.id = id
        else:
            __nb_objects += 1
