#!/usr/bin/python3
def main():
    for i in range(0, 100):
        if i < 10:
            print("0{:d},".format(i), end=" ")
        else:
            print("{:d},".format(i), end=" ")


main()
