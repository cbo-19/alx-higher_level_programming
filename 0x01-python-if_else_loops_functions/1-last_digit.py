#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = number % 10
s = "and is not less than 6 and not 0"
if lastdig > 5:
    print(f"Last digit of {number} is {lastdig} and is greater than 5")
elif number < 0:
    num = number * -1
    rec = num % 10 * -1
    if rec < 6 and rec != 0:
        print(f"Last digit of {number} is {rec} and is less than 6 and not 0")
elif lastdig == 0:
    print(f"Last digit of {number} is {lastdig} and is 0")
