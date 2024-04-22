#!/usr/bin/python3
"""Base class module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of a list of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(list_dicts))
