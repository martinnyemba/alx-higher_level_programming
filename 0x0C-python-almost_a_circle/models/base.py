#!/usr/bin/python3
"""Base class module"""
import json
import csv


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
        """Writes JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """The list of the JSON string representation """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance.
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as json_file:
                json_string = json_file.read()
                if not json_string:
                    return []
                obj_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**obj_dict) for obj_dict in obj_dicts]
                return instances

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to a CSV file.

        Args:
            cls: The class itself (e.g., Rectangle or Square).
            list_objs (list): A list of objects to serialize.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csv_file:
            writer = csv.writer(csv_file)
            for objs in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([objs.id, objs.width, objs.height,
                                     objs.x, objs.y])
                elif cls.__name__ == "Square":
                    writer.writerow([objs.id, objs.size, objs.x, objs.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file.

        Args:
            cls: The class itself (e.g., Rectangle or Square).

        Returns:
            list: A list of deserialized objects.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls.create(id=int(row[0]),
                                         width=int(row[1]),
                                         height=int(row[2]),
                                         x=int(row[3]),
                                         y=int(row[4]))
                    elif cls.__name__ == "Square":
                        obj = cls.create(id=int(row[0]),
                                         size=int(row[1]),
                                         x=int(row[2]),
                                         y=int(row[3]))
                    instances.append(obj)
                return instances
        except FileNotFoundError:
            return []
