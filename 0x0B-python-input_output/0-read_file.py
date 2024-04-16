#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """

    with open(filename, 'r', encoding='utf-8') as f:
        #  declare variable to store data
        read_data = f.read()
        print(read_data, end="")
        f.close()
