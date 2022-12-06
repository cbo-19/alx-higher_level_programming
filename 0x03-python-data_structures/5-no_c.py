#!/usr/bin/python3
def no_c(my_string):
    my_transl = {67: None, 99: None}
    new_string = my_string.translate(my_transl)
    return new_string
