# Python - Almost a circle

## Description
The AirBnB project is a big part of the Higher level curriculum, preparing you comprehensively for it. This project encompasses a review of essential Python concepts including import, exceptions, classes, private attributes, getters/setters, class methods, static methods, inheritance, unittest, and file read/write operations. Additionally, you will delve into args/kwargs, serialization/deserialization, and JSON manipulation.

## Learning Objectives
By the end of this project, you should be able to:
- Understand and implement Unit testing in a large project
- Serialize and deserialize a Class
- Read and write a JSON file
- Utilize *args and **kwargs effectively
- Handle named arguments in functions

## Requirements
- Python Scripts
  - Allowed editors: vi, vim, emacs
  - Ubuntu 20.04 LTS with python3 (version 3.8.5)
  - Code should follow PEP 8 guidelines
  - All modules, classes, and functions must be well-documented
- Python Unit Tests
  - Utilize the unittest module
  - Test files should follow a specific naming convention and organization
  - Tests should be executable using `python3 -m unittest discover tests`

## The Python tools:
* Import
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs`
* JSON and CSV serialization/deserialization
* Unittesting

## Tests :

* [tests/test_models](./tests/test_models): Folder containing the following independently-developed test files:
  * [test_base.py](./tests/test_models/test_base.py)
  * [test_rectangle.py](./tests/test_models/test_rectangle.py)
  * [test_square.py](./tests/test_models/test_square.py)

## Classes

### Base
Represents the "base" class for all other classes in the project. Includes:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` that returns the JSON string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` that returns a list of objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` that instantiates an object with provided attributes.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` that returns a list of objects instantiated from a JSON file.
  * Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.csv` (ie. `Rectangle.csv`)
  * Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
* Class method `def load_from_file_csv(cls):` that returns a list of objects instantiated from a CSV file.
  * Reads from the CSV file `<cls name>.csv` (ie. `Rectangle.csv`)
  * If the file does not exist, the function returns an empty list.
* Static method `def draw(list_rectangles, list_squares):` that draws `Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  * The parameter `list_rectangles` is expected to be a list of `Rectangle` objects to print.
  * The parameter `list_squares` is expected to be a list of `Square` objects to print.

### Rectangle

Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is >= 0, raises a `ValueError` exception with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception with the message `<attribute> must be >= 0`.
* Public method `def area(self):` that returns the area of the `Rectangle` instance.
* Public method `def display(self):` that prints the `Rectangle` instance to `stdout` using the `#` character.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
* Overwrite of `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Rectangle` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `width`
    * 3rd: `height`
    * 4th: `x`
    * 5th: `y`
  * `**kwargs` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle` instance.

### Square

Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `size`
    * 3rd: `x`
    * 4th: `y`
  * `**kwargs` is expected to be a double pointer to a dictoinary of new key/value attributes to update the `Square` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.

## Tasks
1. **Base class**
   - Create a base class `Base` with specific functionalities.
2. **First Rectangle**
   - Implement a Rectangle class that inherits from Base.
3. **Validate attributes**
   - Add validation to Rectangle attributes.
4. **Area first**
   - Implement an area calculation method for Rectangle.
5. **Display #0**
   - Add a method to display the Rectangle using '#'.
6. **__str__**
   - Override the __str__ method for Rectangle.
7. **Display #1**
   - Improve the display method to consider x and y.
8. **Update #0**
   - Add an update method to Rectangle using *args.
9. **Update #1**
   - Modify the update method to accept **kwargs as well.
10. **And now, the Square!**
    - Create a Square class inheriting from Rectangle.
11. **Square size**
    - Add size getter and setter methods to Square.
12. **Square update**
    - Implement an update method for Square using *args and **kwargs.
13. **Rectangle instance to dictionary representation**
    - Add a method to convert Rectangle instance to a dictionary.
14. **Square instance to dictionary representation**
    - Implement a method to convert Square instance to a dictionary.
15. **Dictionary to JSON string**
    - Add a static method to Base to convert dictionaries to JSON strings.

## Repository Information
- GitHub Repository: [alx-higher_level_programming](https://github.com/martinnyemba/alx-higher_level_programming)
- Directory: 0x0C-python-almost_a_circle
- Relevant Files: models/base.py, models/rectangle.py, models/square.py, tests/
