#!/usr/bin/python3
def print_reversed_list_integer(list):
    n = len(list)
    i = n - 1
    while i >= 0:
        print("{:d}".format(list[i], end=''))
        i -= 1
