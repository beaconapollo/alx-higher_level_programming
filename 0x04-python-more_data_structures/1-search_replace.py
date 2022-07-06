#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 1
    while i <= len(my_list):
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i - 1])
        i += 1
    return(new_list)
