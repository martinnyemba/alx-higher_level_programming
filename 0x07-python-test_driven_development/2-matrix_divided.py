#!/usr/bin/python3
"""Module for dividing matrices"""

def validate_input(matrix, div):
    """
    Validates input parameters.

    Args:
        matrix (list): The matrix to be divided, represented as a list of lists.
        div (int or float): The divisor to divide the matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists, contains elements other than integers or floats,
            or if div is not a number.
        ZeroDivisionError: If div is zero.
        ValueError: If all rows of the matrix do not have the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must contain only integers or floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("all rows of the matrix must have the same size")


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by div.

    Args:
        matrix (list): The matrix to be divided, represented as a list of lists.
        div (int or float): The divisor to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If input parameters are invalid.
        ZeroDivisionError: If div is zero.
        ValueError: If all rows of the matrix do not have the same size.
    """
    validate_input(matrix, div)
    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
