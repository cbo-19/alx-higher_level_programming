#!/usr/bin/python3
def fizzbuzz():
    for i in range (1, 101):
        if i in range(15, 101, 15):
            print("{}".format("FizzBuzz"), end=" ")
        elif i in range(3, 101, 3):
            print("{}".format("Fizz"), end=" ")
        elif i in range(5, 101, 3):
            print("{}".format("Buzz"), end=" ")
        else:
            print(i, end=" ")
    return(i)
