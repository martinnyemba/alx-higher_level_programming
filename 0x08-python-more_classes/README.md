# 0x08. Python - More Classes and Objects

## Resources
Read or watch:

- [Object Oriented Programming](#) (Read everything until the paragraph “Inheritance” (excluded))
- [Object-Oriented Programming](#) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
- [Class and Instance Attributes](#)
- [classmethods and staticmethods](#)
- [Properties vs. Getters and Setters](#) (Mainly the last part “Public instead of Private Attributes”)
- [str vs repr](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

### Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Tasks
1. Simple rectangle
   - Write an empty class Rectangle that defines a rectangle
   - You are not allowed to import any module

2. Real definition of a rectangle
   - Write a class Rectangle that defines a rectangle with private instance attributes and properties
   - Instantiation with optional width and height
   - You are not allowed to import any module

3. Area and Perimeter
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, and public instance methods
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - You are not allowed to import any module

4. String representation
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, and special methods for string representation
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - You are not allowed to import any module

5. Eval is magic
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, special methods for string representation, and eval support
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - Special method __del__ for instance deletion message
   - You are not allowed to import any module

6. Detect instance deletion
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, special methods for string representation, eval support, and instance deletion detection
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - Special method __del__ for instance deletion message
   - You are not allowed to import any module

7. Change representation
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, special methods for string representation, eval support, instance deletion detection, and changeable representation symbol
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - Special method __del__ for instance deletion message
   - Public class attributes for number of instances and print symbol
   - You are not allowed to import any module

8. Compare rectangles
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, special methods for string representation, eval support, instance deletion detection, changeable representation symbol, and comparison method
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - Special method __del__ for instance deletion message
   - Public class attributes for number of instances and print symbol
   - Static method for comparing rectangles based on area
   - You are not allowed to import any module

9. A square is a rectangle
   - Write a class Rectangle that defines a rectangle with private instance attributes, properties, public instance methods, special

methods for string representation, eval support, instance deletion detection, changeable representation symbol, comparison method, and inheritance
   - Instantiation with optional width and height
   - Public instance methods for area and perimeter calculations
   - Special methods __str__ and __repr__ for string representation
   - Special method __del__ for instance deletion message
   - Public class attributes for number of instances and print symbol
   - Static method for comparing rectangles based on area
   - Class method that returns a new instance with width == height
   - You are not allowed to import any module
   - Notes:
     - Why Class Method are made primary as compared to instance methods?
     - Why static method called static?
     - Rectangle: area() returns a number.
     - Square: area() returns a number.

10. N queens
    - The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a class NQueens that solves the N queens problem
    - Usage: `nqueens.py N`
    - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
    - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1
    - The program should print every possible solution to the problem
    - You are only allowed to import the sys module

## Authors
- **Martin Nyemba** - [martinnyemba](https://github.com/martinnyemba)
