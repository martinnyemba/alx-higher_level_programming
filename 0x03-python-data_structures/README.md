0x03. Python - Data Structures: Lists, Tuples

## Python

### Resources
Read or watch:

- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures (until 5.3. Tuples and Sequences included)](https://docs.python.org/3/tutorial/datastructures.html)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=1yUn-ydsgKk)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it

### Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### C
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded

## Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)

## Tasks

### 0. Print a list of integers
Write a function that prints all integers of a list.

- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.

- Prototype: `def element_at(my_list, idx):`
- If idx is negative, the function should return None
- If idx is out of range (> of number of element in my_list), the function should return None
- You are not allowed to import any module
- You are not allowed to use try/except

### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

- Prototype: `def replace_in_list(my_list, idx, element):`
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except

### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

- Prototype: `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

- Prototype: `def new_in_list(my_list, idx, element):`
- If idx is negative, the function should return a copy of the original list
- If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
- You are not allowed to import any module
- You are not allowed to use try/except

### 5. Can you C me now?
Write a function that removes all characters c and C from a string.

- Prototype: `def no_c(my_string):`
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`

### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

- Prototype: `def print_matrix_integer(matrix=[[]]):`
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### 7. Tuples addition
Write a function that adds 2 tuples.

- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
    - The first element should be the addition of the first element of each argument
    - The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

- Prototype: `def multiple_returns(sentence):`
0x03. Python - Data Structures: Lists, Tuples



## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/martinnyemba/alx-higher_level_programming.git
   ```
2. Navigate to the directory:
   ```
   cd alx-higher_level_programming/0x03-python-data_structures
   ```
3. Execute the script with your list:
   ```
   ./0-print_list_integer.py
   ```
   Replace `my_list` in the script with your desired list of integers.

## Author

- Author: Martin Nyemba
- GitHub: [Your GitHub Profile](https://github.com/martinnyemba)
