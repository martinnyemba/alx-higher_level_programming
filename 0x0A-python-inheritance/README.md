# 0x0A. Python - Inheritance
___
### Requirements
Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


### General learning objectives
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions


### Prototypes:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

### Tasks :

* **0. Lookup**
  * [0-lookup.py](./0-lookup.py): Python function that returns a list of available attributes and methods of an objects.

* **1. My list**
  * [1-my_list.py](./1-my_list.py): Python class `MyList` that inherits from `list`. Includes:
    * Public instance method `def print_sorted(self):` that prints the list in ascending sorted order (assumes all list elements are `int`s).

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py): Python function that returns `True` if an object is exactly an instance of a specified class; otherwise `False`.

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): Python function that returns `True` if an object is an instance or inherited instance of a specified class; otherwise `False`.

* **4. Only sub class of**
  * [4-inherits_from.py](./4-inherits_from.py): Python function that returns `True` if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise `False`.

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py): An empty Python class `BaseGeometry`.

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py): Python class `BaseGeometry`. Builds on [5-base_geometry.py](./5-base_geometry.py) with:
    * Public instance method `def area(self):` that raises an `Exception` with
    the message `area() is not implemented`.

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry.py): Python class `BaseGeometry`. Builds on [6-base_geometry.py](./6-base_geometry.py) with:
    * Public instance method `def integer_validator(self, name, value):` that validates the parameter `value`.
    * Assumes the parameter `name` is always a string.
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception is raised with the message `<name> must be an integer`.
    * The parameter `value` must be greater than `0`, otherwise, a `ValueError` exception is raised with the message `<value> must be greater than 0`.

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). Includes:
    * Private attributes `width` and `height` - validated with `integer_validator`.
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`

* **9. Full rectangle**
  * [9-rectangle.py](./9-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)). Builds on [8-rectangle.py](./8-rectangle.py) with:
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle] <width>/<height>`.

* **10. Square #1**
  * [10-square.py](./10-square.py): Python class `Square` that inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). Includes:
    * Private attribute `size` - validated with `integer_validator`.
    * Instantiation with `size`: `def __init__(self, size):`.
    * Implementation of the `area()` method.

* **11. Square #2**
  * [11-square.py](./11-square.py): Python class `Square` that inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)). Builds on [10-square.py](./10-square.py) with:
    * Special method `__str__` to print squares in the format `[Square] <width>/<height>`.

* **12. My integer**
  * [100-my_int.py](./100-my_int.py): Python class `MyInt` that inherits from `int`. Includes:
    * Inversion of the `==` and `!=` operators.

* **13. Can I?**
  * [101-add_attribute.py](./101-add_attribute.py): Python function that adds a new attribute to an object if possible.
    * If an attribute cannot be added, a `TypeError` exception is raised with the message `can't add new attribute`.
