#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for m in list(a_dictionary.keys()):
        if a_dictionary[m] is value:
            del a_dictionary[m]
    return a_dictionary
