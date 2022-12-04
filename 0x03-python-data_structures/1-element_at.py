#!/usr/bin/python3
def element_at(my_list, idx):
    x = my_list
    for i in range(len(x)):
        i = idx
        if i >=0 and i <= len(x):
            return x[i]
            break
        elif i < 0 or i > len(x):
            return None
