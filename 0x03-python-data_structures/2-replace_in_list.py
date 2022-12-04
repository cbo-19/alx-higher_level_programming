#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        i = idx
        if i < 0 or i >len(my_list):
            return my_list
        else:
            my_list[i] = element
            a = my_list
            return a

