#!/usr/bin/python3
def fizzbuzz():
    """function that prints the numbers from 1 to 100 separated by a space"""
    for i in range(1, 101):
        result = ""
        if (i % 3 == 0):
            result += "Fizz"
        if (i % 5 == 0):
            result += "Buzz"
        print("{}".format(result) or "{}".format(i), end='')
        print(" ", end='')
