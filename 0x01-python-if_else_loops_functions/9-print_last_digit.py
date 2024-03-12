#!/usr/bin/python3
def print_last_digit(number):
    """a function that prints the last digit of a number"""

    if number < 0:
        number = number * -1
    last = number % 10
    print(last, end='')
    return (last)
