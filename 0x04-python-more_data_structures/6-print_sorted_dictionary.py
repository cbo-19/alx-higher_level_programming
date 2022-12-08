#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for value in sorted(a_dictionary.keys()):
        print(f"{value:} {a_dictionary[value]}")
