#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    if number < 0:
        num = number * -1
        rec = num % 10 * 1
        print(f"{rec}")
    else:
        print(f"{n}")

