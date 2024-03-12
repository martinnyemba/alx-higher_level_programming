#!/usr/bin/python3

#  program that prints the ASCII alphabet, in lowercase
#  not followed by a new line

# use a for loop to iterate from 97 to 122
for i in range(97, 123):
    if i != 101 and i != 113:

        #  print character using char strinf format
        print("{:c}" .format(i), end="")
