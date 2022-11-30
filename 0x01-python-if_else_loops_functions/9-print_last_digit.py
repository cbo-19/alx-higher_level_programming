#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1 % 10
        print("{}".format(number), end="")
    else:
        print(f"{number % 10}", end="")
    return number
