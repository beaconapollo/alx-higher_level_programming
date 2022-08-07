#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    l = 0
    i = 0

    for item in my_list:
        l += 1
    if idx < 0 or idx >= l:
        return my_list
    while i < l:
        if i == idx:
            del my_list[i]
        i += 1
    return my_list
