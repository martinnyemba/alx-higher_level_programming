# 0x03. Python - Data Structures: Lists, Tuples




```markdown
## 0.  Print List of Integers

This Python script contains a function that prints all integers of a given list, with each integer printed on a separate line using the `str.format()` method.

### Task Details

- Prototype: `def print_list_integer(my_list=[]):`
- Format: One integer per line.
- Restrictions:
  - Do not import any module.
  - Do not cast integers into strings.
  - Use `str.format()` to print integers.

### Example

Assuming the following list:
```python
my_list = [1, 2, 3, 4, 5]
```
Running the script should output:
```
1
2
3
4
5
```


## 1. Retrieve Element from List

This Python function retrieves an element from a list similar to how it's done in C, following specific conditions.

### Function Details

- Prototype: `def element_at(my_list, idx):`
- Conditions:
  - If `idx` is negative, the function returns `None`.
  - If `idx` is out of range (greater than or equal to the number of elements in `my_list`), the function returns `None`.
  - No module imports are allowed.
  - No try/except statements are allowed.

### Example

Assuming the following list:
```python
my_list = [1, 2, 3, 4, 5]
idx = 3




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
```
