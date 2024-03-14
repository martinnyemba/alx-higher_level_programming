#!/usr/bin/python3

from add_0 import add

if __name__ == "__main__":

    #  Assign: the value 1 to a variable called a
    #  the value 2 to a variable called b
    a = 1
    b = 2

    sum = add(a, b)

    #  print: <a value> + <b value> = <add(a, b) value>
    #  followed with a new line

    print("{} + {} = {}".format(a, b, sum))
