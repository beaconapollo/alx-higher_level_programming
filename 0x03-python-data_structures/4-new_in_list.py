#!/usr/bin/python3
def new_in_list(list, index, ne):
    new = list
    n = len(new)
    if index >= 0 and index < n:
        new[index] = ne
    return(new)
