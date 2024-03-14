#!/usr/bin/python3
# program that imports all functions from the file calculator_1.py and
#   handles basic operations
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    argv = sys.argv
    argv_length = len(argv)

    # Check number of arguments
    if (argv_length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get the operands and operator
    operator = sys.argv[2]
    a = int(argv[1])
    b = int(argv[3])

    # Perform operation and print result
    if (operator in "+-*/"):
        if operator == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
