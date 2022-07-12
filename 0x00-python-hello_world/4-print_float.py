#!/usr/bin/python3
number = 3.14159
if (isinstance(number, float)):
    print("Float: {:.2f}".format(number))
else:
    print("ValueError: Unknown format code 'd' for object of type 'str'")
