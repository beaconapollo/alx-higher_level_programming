#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    new_list = []
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        finally:
            if i >= l1 or i >= l2:
                new_list.append(0)
            elif my_list_2[i] == 0:
                new_list.append(0)
            elif not isinstance(my_list_1[i], int) and not isinstance(my_list_1[i], float):
                new_list.append(0)
            elif not isinstance(my_list_2[i], int) and not isinstance(my_list_2[i], float):
                new_list.append(0)
            i += 1
    return new_list
