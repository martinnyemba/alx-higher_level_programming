# 0x04. Python - More Data Structures: Set, Dictionary

This project focuses on exploring more advanced data structures in Python, specifically sets and dictionaries. It covers topics such as set methods, set iteration, dictionary methods, dictionary iteration, lambda functions, and the map, reduce, and filter functions.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome
- Understand sets and how to use them
- Use common methods of sets effectively
- Determine when to use sets versus lists
- Iterate over a set
- Understand dictionaries and how to use them
- Determine when to use dictionaries versus lists or sets
- Understand the concept of keys in a dictionary
- Iterate over a dictionary
- Understand lambda functions
- Use the map, reduce, and filter functions effectively

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- The code should use the pycodestyle (version 2.8.*) style guide
- All files must be executable
- The length of your files will be tested using wc

## Tasks

The project includes the following tasks:

1. Squared simple
Square Matrix Simple

This function computes the square value of all integers in a matrix.

Args:
    matrix (list): A 2-dimensional array.

Returns:
    list: A new matrix with the same size as the input matrix, where each value is the square of the corresponding value in the input matrix. The initial matrix is not modified.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

2. Search and replace

3. Unique addition

This function adds all unique integers in a list, considering each integer only once.

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module

Example Usage:
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

4. Present in both

a function that returns a set of common elements in two sets.

Prototype: def common_elements(set_1, set_2):
You are not allowed to import any module

Args:
    set_1 (set): The first set.
    set_2 (set): The second set.

Returns:
    set: A set containing the common elements between set_1 and set_2.

Example:
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))  # Output: ['C']

5. Only differents
This code defines a function called `only_diff_elements` that takes in two sets as input and returns a new set containing only the elements that are present in one set but not in the other.

Parameters:
- set_1: The first set.
- set_2: The second set.

Returns:
- A new set containing the elements that are present in only one of the input sets.

Example usage:
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))  # Output: ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']

6. Number of keys
7. Print sorted dictionary
8. Update dictionary
9. Simple delete by key
10. Multiply by 2

Each task has its own Python file with the corresponding function implementation.

## Usage

To run the code for each task, you can use the provided main files. For example, to run the code for the first task, you can execute the following command:
