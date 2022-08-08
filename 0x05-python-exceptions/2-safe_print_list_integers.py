#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    i = 0

    for item in my_list:
        len += 1
    for item in my_list:
        if isinstance(item, int) and i < x:
            print("{:d}".format(item), end="")
            i += 1
    if x > len:
        raise IndexError("list index out of range")
    print("")
    return i

