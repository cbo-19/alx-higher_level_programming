#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    return n
    if number < 0:
        num = number * -1
        rec = num % 10 * 1
        return rec

